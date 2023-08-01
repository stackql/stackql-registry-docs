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
| `documents` | `array` | The Documents found. |
| `nextPageToken` | `string` | A token to retrieve the next page of documents. If this field is omitted, there are no subsequent pages. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `databasesId, documentsId, documentsId1, projectsId` | Gets a single document. |
| `list` | `SELECT` | `collectionId, databasesId, documentsId, documentsId1, projectsId` | Lists documents. |
| `delete` | `DELETE` | `databasesId, documentsId, documentsId1, projectsId` | Deletes a document. |
| `batch_get` | `EXEC` | `databasesId, projectsId` | Gets multiple documents. Documents returned by this method are not guaranteed to be returned in the same order that they were requested. |
| `batch_write` | `EXEC` | `databasesId, projectsId` | Applies a batch of write operations. The BatchWrite method does not apply the write operations atomically and can apply them out of order. Method does not allow more than one write per document. Each write succeeds or fails independently. See the BatchWriteResponse for the success status of each write. If you require an atomically applied set of writes, use Commit instead. |
| `begin_transaction` | `EXEC` | `databasesId, projectsId` | Starts a new transaction. |
| `commit` | `EXEC` | `databasesId, projectsId` | Commits a transaction, while optionally updating documents. |
| `partition_query` | `EXEC` | `databasesId, documentsId, documentsId1, projectsId` | Partitions a query by returning partition cursors that can be used to run the query in parallel. The returned partition cursors are split points that can be used by RunQuery as starting/end points for the query results. |
| `patch` | `EXEC` | `databasesId, documentsId, documentsId1, projectsId` | Updates or inserts a document. |
| `rollback` | `EXEC` | `databasesId, projectsId` | Rolls back a transaction. |
| `run_aggregation_query` | `EXEC` | `databasesId, documentsId, documentsId1, projectsId` | Runs an aggregation query. Rather than producing Document results like Firestore.RunQuery, this API allows running an aggregation to produce a series of AggregationResult server-side. High-Level Example: ``` -- Return the number of documents in table given a filter. SELECT COUNT(*) FROM ( SELECT * FROM k where a = true ); ``` |
| `run_query` | `EXEC` | `databasesId, documentsId, documentsId1, projectsId` | Runs a query. |
| `write` | `EXEC` | `databasesId, projectsId` | Streams batches of document updates and deletes, in order. This method is only available via gRPC or WebChannel (not REST). |
