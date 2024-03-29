---
title: documents
hide_title: false
hide_table_of_contents: false
keywords:
  - documents
  - firestore
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>documents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.firestore.documents</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the document, for example `projects/&#123;project_id&#125;/databases/&#123;database_id&#125;/documents/&#123;document_path&#125;`. |
| `fields` | `object` | The document's fields. The map keys represent field names. A simple field name contains only characters `a` to `z`, `A` to `Z`, `0` to `9`, or `_`, and must not start with `0` to `9`. For example, `foo_bar_17`. Field names matching the regular expression `__.*__` are reserved. Reserved field names are forbidden except in certain documented contexts. The map keys, represented as UTF-8, must not exceed 1,500 bytes and cannot be empty. Field paths may be used in other contexts to refer to structured fields defined here. For `map_value`, the field path is represented by the simple or quoted field names of the containing fields, delimited by `.`. For example, the structured field `"foo" : &#123; map_value: &#123; "x&y" : &#123; string_value: "hello" &#125;&#125;&#125;` would be represented by the field path `foo.x&y`. Within a field path, a quoted field name starts and ends with `` ` `` and may contain any character. Some characters, including `` ` ``, must be escaped using a `\`. For example, `` `x&y` `` represents `x&y` and `` `bak\`tik` `` represents `` bak`tik ``. |
| `updateTime` | `string` | Output only. The time at which the document was last changed. This value is initially set to the `create_time` then increases monotonically with each change to the document. It can also be compared to values from other documents and the `read_time` of a query. |
| `createTime` | `string` | Output only. The time at which the document was created. This value increases monotonically when a document is deleted then recreated. It can also be compared to values from other documents and the `read_time` of a query. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `databasesId, documentsId, documentsId1, projectsId` | Gets a single document. |
| `list` | `SELECT` | `collectionId, databasesId, documentsId, documentsId1, projectsId` | Lists documents. |
| `list_documents` | `SELECT` | `collectionId, databasesId, projectsId` | Lists documents. |
| `create_document` | `INSERT` | `collectionId, databasesId, documentsId, projectsId` | Creates a new document. |
| `delete` | `DELETE` | `databasesId, documentsId, documentsId1, projectsId` | Deletes a document. |
| `_list` | `EXEC` | `collectionId, databasesId, documentsId, documentsId1, projectsId` | Lists documents. |
| `_list_documents` | `EXEC` | `collectionId, databasesId, projectsId` | Lists documents. |
| `batch_get` | `EXEC` | `databasesId, projectsId` | Gets multiple documents. Documents returned by this method are not guaranteed to be returned in the same order that they were requested. |
| `batch_write` | `EXEC` | `databasesId, projectsId` | Applies a batch of write operations. The BatchWrite method does not apply the write operations atomically and can apply them out of order. Method does not allow more than one write per document. Each write succeeds or fails independently. See the BatchWriteResponse for the success status of each write. If you require an atomically applied set of writes, use Commit instead. |
| `begin_transaction` | `EXEC` | `databasesId, projectsId` | Starts a new transaction. |
| `commit` | `EXEC` | `databasesId, projectsId` | Commits a transaction, while optionally updating documents. |
| `listen` | `EXEC` | `databasesId, projectsId` | Listens to changes. This method is only available via gRPC or WebChannel (not REST). |
| `partition_query` | `EXEC` | `databasesId, documentsId, documentsId1, projectsId` | Partitions a query by returning partition cursors that can be used to run the query in parallel. The returned partition cursors are split points that can be used by RunQuery as starting/end points for the query results. |
| `patch` | `EXEC` | `databasesId, documentsId, documentsId1, projectsId` | Updates or inserts a document. |
| `rollback` | `EXEC` | `databasesId, projectsId` | Rolls back a transaction. |
| `run_aggregation_query` | `EXEC` | `databasesId, documentsId, documentsId1, projectsId` | Runs an aggregation query. Rather than producing Document results like Firestore.RunQuery, this API allows running an aggregation to produce a series of AggregationResult server-side. High-Level Example: ``` -- Return the number of documents in table given a filter. SELECT COUNT(*) FROM ( SELECT * FROM k where a = true ); ``` |
| `run_query` | `EXEC` | `databasesId, documentsId, documentsId1, projectsId` | Runs a query. |
| `write` | `EXEC` | `databasesId, projectsId` | Streams batches of document updates and deletes, in order. This method is only available via gRPC or WebChannel (not REST). |
