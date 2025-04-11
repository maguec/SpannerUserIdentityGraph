#!/usr/bin/env python

from google.cloud import spanner
from alive_progress import alive_bar
import uuid, time
import numpy as np

NUMBER_OF_USERS = 1000

if __name__ == "__main__":

    query_times = []
    bad_actors = set()
    s = spanner.Client()
    instance = s.instance("useridentity")
    database = instance.database("useridentitydb")

    with alive_bar(NUMBER_OF_USERS, title="Finding bad actors") as bar:

        with database.snapshot(multi_use=True) as snapshot:
            for i in range(NUMBER_OF_USERS):
                start = time.time_ns()
                results = snapshot.execute_sql(
                    """
                    GRAPH UserIdentity
                    MATCH (e:Email{id: @id})-[h:HAS_DEVICE]->(d:Device)<-[h2:HAS_DEVICE]-(e2:Email)
                    WHERE e.id != e2.id AND e2.sus = 1
                    RETURN COUNT( DISTINCT e2.id) AS SUS_LINKS
                    """,
                    params={"id": str(uuid.UUID(int=i))},
                    param_types={"id": spanner.param_types.STRING},
                )
                for row in results:
                    if row[0] > 0:
                        bad_actors.add(i)
                query_times.append((time.time_ns() - start)/ 1_000_000)
                bar()

    query_times_np = np.array(query_times)
    print(f"\nDatabase Query Time Statistics:")
    print(f"Mean: {query_times_np.mean():.6f} ms")
    print(f"p95 : {np.percentile(query_times_np, 0.95):.6f} ms")
    print(f"p99 : {np.percentile(query_times_np, 0.99):.6f} ms")
    print(f"\nFound {len(bad_actors)} bad actors")
