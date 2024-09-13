---
title: documents
hide_title: false
hide_table_of_contents: false
keywords:
  - documents
  - discoveryengine
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

Creates, updates, deletes or gets an <code>document</code> resource or lists <code>documents</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>documents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.discoveryengine.documents" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Immutable. The identifier of the document. Id should conform to [RFC-1034](https://tools.ietf.org/html/rfc1034) standard with a length limit of 63 characters. |
| <CopyableCode code="name" /> | `string` | Immutable. The full resource name of the document. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}/documents/{document_id}`. This field must be a UTF-8 encoded string with a length limit of 1024 characters. |
| <CopyableCode code="content" /> | `object` | Unstructured data linked to this document. |
| <CopyableCode code="derivedStructData" /> | `object` | Output only. This field is OUTPUT_ONLY. It contains derived data that are not in the original input document. |
| <CopyableCode code="indexStatus" /> | `object` | Index status of the document. |
| <CopyableCode code="indexTime" /> | `string` | Output only. The last time the document was indexed. If this field is set, the document could be returned in search results. This field is OUTPUT_ONLY. If this field is not populated, it means the document has never been indexed. |
| <CopyableCode code="jsonData" /> | `string` | The JSON string representation of the document. It should conform to the registered Schema or an `INVALID_ARGUMENT` error is thrown. |
| <CopyableCode code="parentDocumentId" /> | `string` | The identifier of the parent document. Currently supports at most two level document hierarchy. Id should conform to [RFC-1034](https://tools.ietf.org/html/rfc1034) standard with a length limit of 63 characters. |
| <CopyableCode code="schemaId" /> | `string` | The identifier of the schema located in the same data store. |
| <CopyableCode code="structData" /> | `object` | The structured JSON data for the document. It should conform to the registered Schema or an `INVALID_ARGUMENT` error is thrown. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_collections_data_stores_branches_documents_get" /> | `SELECT` | <CopyableCode code="branchesId, collectionsId, dataStoresId, documentsId, locationsId, projectsId" /> | Gets a Document. |
| <CopyableCode code="projects_locations_collections_data_stores_branches_documents_list" /> | `SELECT` | <CopyableCode code="branchesId, collectionsId, dataStoresId, locationsId, projectsId" /> | Gets a list of Documents. |
| <CopyableCode code="projects_locations_data_stores_branches_documents_get" /> | `SELECT` | <CopyableCode code="branchesId, dataStoresId, documentsId, locationsId, projectsId" /> | Gets a Document. |
| <CopyableCode code="projects_locations_data_stores_branches_documents_list" /> | `SELECT` | <CopyableCode code="branchesId, dataStoresId, locationsId, projectsId" /> | Gets a list of Documents. |
| <CopyableCode code="projects_locations_collections_data_stores_branches_documents_create" /> | `INSERT` | <CopyableCode code="branchesId, collectionsId, dataStoresId, locationsId, projectsId" /> | Creates a Document. |
| <CopyableCode code="projects_locations_data_stores_branches_documents_create" /> | `INSERT` | <CopyableCode code="branchesId, dataStoresId, locationsId, projectsId" /> | Creates a Document. |
| <CopyableCode code="projects_locations_collections_data_stores_branches_documents_delete" /> | `DELETE` | <CopyableCode code="branchesId, collectionsId, dataStoresId, documentsId, locationsId, projectsId" /> | Deletes a Document. |
| <CopyableCode code="projects_locations_data_stores_branches_documents_delete" /> | `DELETE` | <CopyableCode code="branchesId, dataStoresId, documentsId, locationsId, projectsId" /> | Deletes a Document. |
| <CopyableCode code="projects_locations_collections_data_stores_branches_documents_patch" /> | `UPDATE` | <CopyableCode code="branchesId, collectionsId, dataStoresId, documentsId, locationsId, projectsId" /> | Updates a Document. |
| <CopyableCode code="projects_locations_data_stores_branches_documents_patch" /> | `UPDATE` | <CopyableCode code="branchesId, dataStoresId, documentsId, locationsId, projectsId" /> | Updates a Document. |
| <CopyableCode code="projects_locations_collections_data_stores_branches_documents_import" /> | `EXEC` | <CopyableCode code="branchesId, collectionsId, dataStoresId, locationsId, projectsId" /> | Bulk import of multiple Documents. Request processing may be synchronous. Non-existing items are created. Note: It is possible for a subset of the Documents to be successfully updated. |
| <CopyableCode code="projects_locations_collections_data_stores_branches_documents_purge" /> | `EXEC` | <CopyableCode code="branchesId, collectionsId, dataStoresId, locationsId, projectsId" /> | Permanently deletes all selected Documents in a branch. This process is asynchronous. Depending on the number of Documents to be deleted, this operation can take hours to complete. Before the delete operation completes, some Documents might still be returned by DocumentService.GetDocument or DocumentService.ListDocuments. To get a list of the Documents to be deleted, set PurgeDocumentsRequest.force to false. |
| <CopyableCode code="projects_locations_data_stores_branches_documents_import" /> | `EXEC` | <CopyableCode code="branchesId, dataStoresId, locationsId, projectsId" /> | Bulk import of multiple Documents. Request processing may be synchronous. Non-existing items are created. Note: It is possible for a subset of the Documents to be successfully updated. |
| <CopyableCode code="projects_locations_data_stores_branches_documents_purge" /> | `EXEC` | <CopyableCode code="branchesId, dataStoresId, locationsId, projectsId" /> | Permanently deletes all selected Documents in a branch. This process is asynchronous. Depending on the number of Documents to be deleted, this operation can take hours to complete. Before the delete operation completes, some Documents might still be returned by DocumentService.GetDocument or DocumentService.ListDocuments. To get a list of the Documents to be deleted, set PurgeDocumentsRequest.force to false. |

## `SELECT` examples

Gets a list of Documents.

```sql
SELECT
id,
name,
content,
derivedStructData,
indexStatus,
indexTime,
jsonData,
parentDocumentId,
schemaId,
structData
FROM google.discoveryengine.documents
WHERE branchesId = '{{ branchesId }}'
AND dataStoresId = '{{ dataStoresId }}'
AND locationsId = '{{ locationsId }}'
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
INSERT INTO google.discoveryengine.documents (
branchesId,
dataStoresId,
locationsId,
projectsId,
structData,
jsonData,
name,
id,
schemaId,
content,
parentDocumentId,
derivedStructData,
indexTime,
indexStatus
)
SELECT 
'{{ branchesId }}',
'{{ dataStoresId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ structData }}',
'{{ jsonData }}',
'{{ name }}',
'{{ id }}',
'{{ schemaId }}',
'{{ content }}',
'{{ parentDocumentId }}',
'{{ derivedStructData }}',
'{{ indexTime }}',
'{{ indexStatus }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: structData
        value: '{{ structData }}'
      - name: jsonData
        value: '{{ jsonData }}'
      - name: name
        value: '{{ name }}'
      - name: id
        value: '{{ id }}'
      - name: schemaId
        value: '{{ schemaId }}'
      - name: content
        value: '{{ content }}'
      - name: parentDocumentId
        value: '{{ parentDocumentId }}'
      - name: derivedStructData
        value: '{{ derivedStructData }}'
      - name: indexTime
        value: '{{ indexTime }}'
      - name: indexStatus
        value: '{{ indexStatus }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a document only if the necessary resources are available.

```sql
UPDATE google.discoveryengine.documents
SET 
structData = '{{ structData }}',
jsonData = '{{ jsonData }}',
name = '{{ name }}',
id = '{{ id }}',
schemaId = '{{ schemaId }}',
content = '{{ content }}',
parentDocumentId = '{{ parentDocumentId }}',
derivedStructData = '{{ derivedStructData }}',
indexTime = '{{ indexTime }}',
indexStatus = '{{ indexStatus }}'
WHERE 
branchesId = '{{ branchesId }}'
AND dataStoresId = '{{ dataStoresId }}'
AND documentsId = '{{ documentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified document resource.

```sql
DELETE FROM google.discoveryengine.documents
WHERE branchesId = '{{ branchesId }}'
AND dataStoresId = '{{ dataStoresId }}'
AND documentsId = '{{ documentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
