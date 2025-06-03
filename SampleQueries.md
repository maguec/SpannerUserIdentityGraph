# Sample Queries

## Find distinct emails per month

```sql
GRAPH UserIdentity
MATCH (o:SalesOrder)-[h:HAS_EMAIL]->(e:Email) 
RETURN  EXTRACT(YEAR FROM h.ts) AS Year, EXTRACT(MONTH FROM h.ts) AS Month,
COUNT(DISTINCT e.email) as Email ORDER BY Month
```
## Find Innocent looking emails that are linked through devices to suspicious emails

```sql
GRAPH UserIdentity
MATCH (e:Email{sus: 0})-[h:HAS_DEVICE]->(d:Device)<-[h2:HAS_DEVICE]-(e2:Email{sus:1})
WHERE e.id != e2.id
RETURN e.email AS PossiblyBad, e2.email AS KnownBad
```

```sql 
GRAPH UserIdentity
MATCH p=(e:Email{email:'david93@example.com'})-[h:HAS_DEVICE]->(d:Device)<-[h2:HAS_DEVICE]-(e2:Email{email: 'operez@example.org'})
RETURN SAFE_TO_JSON(p) AS JSON
```

## Graphically Find everything Linked to an Email

```sql
GRAPH UserIdentity
MATCH p=(e:Email{email: "jamesparks@example.com" })-[h]->{1,3}(j)
WHERE h[0].ts > "2025-04-01"
RETURN SAFE_TO_JSON(p) AS JSON
```

## Which CCs are linked to the most suspicious transactions

```sql
GRAPH UserIdentity
MATCH (s:SalesOrder{sus: 1})-[w]->{1,2}(cc:CC)
RETURN cc.id as CreditCard, COUNT (cc.id) as CC_COUNT
GROUP BY CreditCard
ORDER BY CC_COUNT DESC LIMIT 10
```

## When was the last time that we saw a transaction of this shape

```sql
GRAPH UserIdentity
 MATCH (
  cc:CC{last4: "8963", zip: "36206"})<-[EMAIL_HAS_CC]-(
    e:Email{email:"kevin04@example.com"})<-[HAS_EMAIL]-(
      o:SalesOrder)-[hs:HAS_ADDRESS]->(sa:ShippingAddress)
  WHERE sa.id IN (
    SELECT id FROM ShippingAddress WHERE
    SEARCH_NGRAMS(address_Tokens, '18041 AND Berg AND Brandyhaven'))
 RETURN hs.ts AS TS, o.sus AS IS_SUSPECT, sa.address as Addr
```

## Find all Suspect Orders with and email and last4

```sql
GRAPH UserIdentity
 MATCH (
  cc:CC{last4: "2218"})<-[EMAIL_HAS_CC]-(
    e:Email{email: "jeremy76@example.com"})<-[h:HAS_EMAIL]-(o:SalesOrder{sus: 1})
    WHERE h.ts > "2025-02-01"
 RETURN e.email AS EMAIL, cc.last4 AS LAST4, h.ts AS TS, o.id AS TRANSACT, o.sus AS IS_SUSPECT
```
