#!/usr/bin/env python

from google.cloud import spanner
from alive_progress import alive_bar
import uuid, time
import numpy as np


if __name__ == "__main__":

    good_order_shapes = []
    query_times = []
    s = spanner.Client()
    instance = s.instance("useridentity")
    database = instance.database("useridentitydb")
    print("Getting a list of shapes")
    with database.snapshot() as snapshot:
        results = snapshot.execute_sql("""
        GRAPH UserIdentity
        MATCH (cc:CC)<-[EMAIL_HAS_CC]-(e:Email{sus:0})<-[HAS_EMAIL]-(o:SalesOrder{sus: 0})-[hs:HAS_ADDRESS]->(sa:ShippingAddress{sus: 0})
        RETURN o.id AS SO_ID, hs.ts AS SO_DATE, sa.id as SA_ID, e.id as EMAIL_ID, cc.id as CC_ID
        LIMIT 1000
        """)
        for row in results:
            good_order_shapes.append(
                {
                    "sa_id": row[2],
                    "email_id": row[3],
                    "cc_id": row[4],
                }
            )
    print(good_order_shapes[0])

    with alive_bar(len(good_order_shapes), title="Finding similar shapes") as bar:

        with database.snapshot(multi_use=True) as snapshot:
            for i in good_order_shapes:
                start = time.time_ns()
                results = snapshot.execute_sql(
                    """
                    GRAPH UserIdentity
                    MATCH (cc:CC{id: @cc_id})<-[EMAIL_HAS_CC]-(e:Email{id:@email_id})<-[HAS_EMAIL]-(o:SalesOrder{sus: 0})-[hs:HAS_ADDRESS]->(sa:ShippingAddress{id: @sa_id})
                    RETURN hs.ts as TS
                    """,
                    params=i,
                    param_types={
                        "sa_id": spanner.param_types.STRING,
                        "email_id": spanner.param_types.STRING,
                        "cc_id": spanner.param_types.STRING,
                    },
                )
                for row in results:
                    k = 1
                query_times.append((time.time_ns() - start)/ 1_000_000)
                bar()

    query_times_np = np.array(query_times)
    print(f"\nDatabase Query Time Statistics:")
    print(f"Mean: {query_times_np.mean():.6f} ms")
    print(f"p95 : {np.percentile(query_times_np, 0.95):.6f} ms")
    print(f"p99 : {np.percentile(query_times_np, 0.99):.6f} ms")
