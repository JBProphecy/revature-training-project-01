
---
# Commands

**start the shell**

``` shell
mongosh
```

---

**exit the shell**

``` shell
exit
```

---

**show all databases**

``` shell
show dbs
```

---

**switch to a database (even if it doesn't exist yet)**

``` shell
use <database_name>
```

---

**show all collections in the current database**

``` shell
show collections
```

---

**reference to the current database**

``` shell
db
```

---

**reference to a collection in the current database (even if it doesn't exist yet)**

``` shell
db.<collection_name>
```

---

**insert a single document into a collection**

``` shell
db.<collection_name>.insertOne(<json_object>)
```

---

**insert many documents into a collection**

``` shell
db.<collection_name>.insertMany([<json_object>, <json_object>, <...>])
```

---

**find documents in a collection**

``` shell
db.<collection_name>.find()
```

``` shell
db.<collection_name>.find(<json_object>)
```

``` shell
db.<collection_name>.find(<json_object>, <json_object>)
```

- This last example has a `json_object` for filters and a `json_object` for fields.

- The first `json_object` is used to filter the documents being searched. To do so, you enter the name of a field as the key and then whatever value should match.

- The second `json_object` is used to determine which fields will be returned from each document. To do so, you enter the name of a field as the key and then a `0` or `1` depending on whether or not you want that field to be returned.

- This method will return the first 20 documents that are found. To continue the search / iterate through more documents and get the next 20, you can use the following command...

``` shell
it
```

---

**find a single document in a collection**

``` shell
db.<collection_name>.findOne()
```

``` shell
db.<collection_name>.findOne(<json_object>)
```

``` shell
db.<collection_name>.findOne(<json_object>, <json_object>)
```

---

**get the number of documents found**

``` shell
db.<collection_name>.find().count()
```

---

**limit the number of documents returned**

``` shell
db.<collection_name>.find().limit(<number>)
```

---

**sort found documents**

``` shell
db.<collection_name>.find().sort(<json_object>)
```

- The `json_object` is used to sort the documents returned. To do so, you enter the name of a field as the key and then a `1` or `-1` depending on whether you want to sort the results in ascending order or descending order respectively.

---
# Operators

| Operator | Meaning                    |
| -------- | -------------------------- |
| `$gt`    | "greater than"             |
| `$gte`   | "greater than or equal to" |
| `$lt`    | "less than"                |
| `$lte`   | "less than or equal to"    |

| Operator | Meaning                                       |
| -------- | --------------------------------------------- |
| `$or`    | duh                                           |
| `$in`    | basically `$or` but iterates through an array |
| `$nin`   | negation of `$in`                             |
| `$all`   |                                               |

---
