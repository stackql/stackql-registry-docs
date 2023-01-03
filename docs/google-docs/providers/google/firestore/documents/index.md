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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `name` | `string` | The resource name of the document, for example `projects/{project_id}/databases/{database_id}/documents/{document_path}`. |
| `updateTime` | `string` | Output only. The time at which the document was last changed. This value is initially set to the `create_time` then increases monotonically with each change to the document. It can also be compared to values from other documents and the `read_time` of a query. |
| `createTime` | `string` | Output only. The time at which the document was created. This value increases monotonically when a document is deleted then recreated. It can also be compared to values from other documents and the `read_time` of a query. |
| `fields` | `object` | The document's fields. The map keys represent field names. A simple field name contains only characters `a` to `z`, `A` to `Z`, `0` to `9`, or `_`, and must not start with `0` to `9`. For example, `foo_bar_17`. Field names matching the regular expression `__.*__` are reserved. Reserved field names are forbidden except in certain documented contexts. The map keys, represented as UTF-8, must not exceed 1,500 bytes and cannot be empty. Field paths may be used in other contexts to refer to structured fields defined here. For `map_value`, the field path is represented by the simple or quoted field names of the containing fields, delimited by `.`. For example, the structured field `"foo" : { map_value: { "x&y" : { string_value: "hello" }}}` would be represented by the field path `foo.x&y`. Within a field path, a quoted field name starts and ends with `` ` `` and may contain any character. Some characters, including `` ` ``, must be escaped using a `\`. For example, `` `x&y` `` represents `x&y` and `` `bak\`tik` `` represents `` bak`tik ``. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_databases_documents_batchGet` | `SELECT` | `databasesId, projectsId` | Gets multiple documents. Documents returned by this method are not guaranteed to be returned in the same order that they were requested. |
| `projects_databases_documents_get` | `SELECT` | `databasesId, documentsId, documentsId1, projectsId` | Gets a single document. |
| `projects_databases_documents_list` | `SELECT` | `collectionId, databasesId, documentsId, documentsId1, projectsId` | Lists documents. |
| `projects_databases_documents_delete` | `DELETE` | `databasesId, documentsId, documentsId1, projectsId` | Deletes a document. |
| `projects_databases_documents_batchWrite` | `EXEC` | `databasesId, projectsId` | Applies a batch of write operations. The BatchWrite method does not apply the write operations atomically and can apply them out of order. Method does not allow more than one write per document. Each write succeeds or fails independently. See the BatchWriteResponse for the success status of each write. If you require an atomically applied set of writes, use Commit instead. |
| `projects_databases_documents_beginTransaction` | `EXEC` | `databasesId, projectsId` | Starts a new transaction. |
| `projects_databases_documents_commit` | `EXEC` | `databasesId, projectsId` | Commits a transaction, while optionally updating documents. |
| `projects_databases_documents_partitionQuery` | `EXEC` | `databasesId, documentsId, documentsId1, projectsId` | Partitions a query by returning partition cursors that can be used to run the query in parallel. The returned partition cursors are split points that can be used by RunQuery as starting/end points for the query results. |
| `projects_databases_documents_patch` | `EXEC` | `databasesId, documentsId, documentsId1, projectsId` | Updates or inserts a document. |
| `projects_databases_documents_rollback` | `EXEC` | `databasesId, projectsId` | Rolls back a transaction. |
| `projects_databases_documents_runQuery` | `EXEC` | `databasesId, documentsId, documentsId1, projectsId` | Runs a query. |
| `projects_databases_documents_write` | `EXEC` | `databasesId, projectsId` | Streams batches of document updates and deletes, in order. |
