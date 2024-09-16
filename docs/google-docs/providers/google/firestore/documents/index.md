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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>documents</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>documents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.firestore.documents" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the document, for example `projects/{project_id}/databases/{database_id}/documents/{document_path}`. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time at which the document was created. This value increases monotonically when a document is deleted then recreated. It can also be compared to values from other documents and the `read_time` of a query. |
| <CopyableCode code="fields" /> | `object` | The document's fields. The map keys represent field names. Field names matching the regular expression `__.*__` are reserved. Reserved field names are forbidden except in certain documented contexts. The field names, represented as UTF-8, must not exceed 1,500 bytes and cannot be empty. Field paths may be used in other contexts to refer to structured fields defined here. For `map_value`, the field path is represented by a dot-delimited (`.`) string of segments. Each segment is either a simple field name (defined below) or a quoted field name. For example, the structured field `"foo" : { map_value: { "x&y" : { string_value: "hello" }}}` would be represented by the field path `` foo.`x&y` ``. A simple field name contains only characters `a` to `z`, `A` to `Z`, `0` to `9`, or `_`, and must not start with `0` to `9`. For example, `foo_bar_17`. A quoted field name starts and ends with `` ` `` and may contain any character. Some characters, including `` ` ``, must be escaped using a `\`. For example, `` `x&y` `` represents `x&y` and `` `bak\`tik` `` represents `` bak`tik ``. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time at which the document was last changed. This value is initially set to the `create_time` then increases monotonically with each change to the document. It can also be compared to values from other documents and the `read_time` of a query. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="databasesId, documentsId, documentsId1, projectsId" /> | Gets a single document. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="collectionId, databasesId, documentsId, documentsId1, projectsId" /> | Lists documents. |
| <CopyableCode code="list_documents" /> | `SELECT` | <CopyableCode code="collectionId, databasesId, projectsId" /> | Lists documents. |
| <CopyableCode code="listen" /> | `SELECT` | <CopyableCode code="databasesId, projectsId" /> | Listens to changes. This method is only available via gRPC or WebChannel (not REST). |
| <CopyableCode code="create_document" /> | `INSERT` | <CopyableCode code="collectionId, databasesId, documentsId, projectsId" /> | Creates a new document. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="databasesId, documentsId, documentsId1, projectsId" /> | Deletes a document. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="databasesId, documentsId, documentsId1, projectsId" /> | Updates or inserts a document. |
| <CopyableCode code="batch_get" /> | `EXEC` | <CopyableCode code="databasesId, projectsId" /> | Gets multiple documents. Documents returned by this method are not guaranteed to be returned in the same order that they were requested. |
| <CopyableCode code="batch_write" /> | `EXEC` | <CopyableCode code="databasesId, projectsId" /> | Applies a batch of write operations. The BatchWrite method does not apply the write operations atomically and can apply them out of order. Method does not allow more than one write per document. Each write succeeds or fails independently. See the BatchWriteResponse for the success status of each write. If you require an atomically applied set of writes, use Commit instead. |
| <CopyableCode code="begin_transaction" /> | `EXEC` | <CopyableCode code="databasesId, projectsId" /> | Starts a new transaction. |
| <CopyableCode code="commit" /> | `EXEC` | <CopyableCode code="databasesId, projectsId" /> | Commits a transaction, while optionally updating documents. |
| <CopyableCode code="partition_query" /> | `EXEC` | <CopyableCode code="databasesId, documentsId, documentsId1, projectsId" /> | Partitions a query by returning partition cursors that can be used to run the query in parallel. The returned partition cursors are split points that can be used by RunQuery as starting/end points for the query results. |
| <CopyableCode code="rollback" /> | `EXEC` | <CopyableCode code="databasesId, projectsId" /> | Rolls back a transaction. |
| <CopyableCode code="run_aggregation_query" /> | `EXEC` | <CopyableCode code="databasesId, documentsId, documentsId1, projectsId" /> | Runs an aggregation query. Rather than producing Document results like Firestore.RunQuery, this API allows running an aggregation to produce a series of AggregationResult server-side. High-Level Example: ``` -- Return the number of documents in table given a filter. SELECT COUNT(*) FROM ( SELECT * FROM k where a = true ); ``` |
| <CopyableCode code="run_query" /> | `EXEC` | <CopyableCode code="databasesId, documentsId, documentsId1, projectsId" /> | Runs a query. |
| <CopyableCode code="write" /> | `EXEC` | <CopyableCode code="databasesId, projectsId" /> | Streams batches of document updates and deletes, in order. This method is only available via gRPC or WebChannel (not REST). |

## `SELECT` examples

Listens to changes. This method is only available via gRPC or WebChannel (not REST).

```sql
SELECT
name,
createTime,
fields,
updateTime
FROM google.firestore.documents
WHERE databasesId = '{{ databasesId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>documents</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.firestore.documents (
collectionId,
databasesId,
documentsId,
projectsId,
name,
fields
)
SELECT 
'{{ collectionId }}',
'{{ databasesId }}',
'{{ documentsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ fields }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: fields
      value: '{{ fields }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>documents</code> resource.

```sql
/*+ update */
UPDATE google.firestore.documents
SET 
name = '{{ name }}',
fields = '{{ fields }}'
WHERE 
databasesId = '{{ databasesId }}'
AND documentsId = '{{ documentsId }}'
AND documentsId1 = '{{ documentsId1 }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>documents</code> resource.

```sql
/*+ delete */
DELETE FROM google.firestore.documents
WHERE databasesId = '{{ databasesId }}'
AND documentsId = '{{ documentsId }}'
AND documentsId1 = '{{ documentsId1 }}'
AND projectsId = '{{ projectsId }}';
```
