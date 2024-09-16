---
title: documents
hide_title: false
hide_table_of_contents: false
keywords:
  - documents
  - contentwarehouse
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
<tr><td><b>Id</b></td><td><CopyableCode code="google.contentwarehouse.documents" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the document. Format: projects/{project_number}/locations/{location}/documents/{document_id}. The name is ignored when creating a document. |
| <CopyableCode code="cloudAiDocument" /> | `object` | Document represents the canonical document resource in Document AI. It is an interchange format that provides insights into documents and allows for collaboration between users and Document AI to iterate and optimize for quality. |
| <CopyableCode code="contentCategory" /> | `string` | Indicates the category (image, audio, video etc.) of the original content. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the document is created. |
| <CopyableCode code="creator" /> | `string` | The user who creates the document. |
| <CopyableCode code="displayName" /> | `string` | Required. Display name of the document given by the user. This name will be displayed in the UI. Customer can populate this field with the name of the document. This differs from the 'title' field as 'title' is optional and stores the top heading in the document. |
| <CopyableCode code="displayUri" /> | `string` | Uri to display the document, for example, in the UI. |
| <CopyableCode code="dispositionTime" /> | `string` | Output only. If linked to a Collection with RetentionPolicy, the date when the document becomes mutable. |
| <CopyableCode code="documentSchemaName" /> | `string` | The Document schema name. Format: projects/{project_number}/locations/{location}/documentSchemas/{document_schema_id}. |
| <CopyableCode code="inlineRawDocument" /> | `string` | Raw document content. |
| <CopyableCode code="legalHold" /> | `boolean` | Output only. Indicates if the document has a legal hold on it. |
| <CopyableCode code="plainText" /> | `string` | Other document format, such as PPTX, XLXS |
| <CopyableCode code="properties" /> | `array` | List of values that are user supplied metadata. |
| <CopyableCode code="rawDocumentFileType" /> | `string` | This is used when DocAI was not used to load the document and parsing/ extracting is needed for the inline_raw_document. For example, if inline_raw_document is the byte representation of a PDF file, then this should be set to: RAW_DOCUMENT_FILE_TYPE_PDF. |
| <CopyableCode code="rawDocumentPath" /> | `string` | Raw document file in Cloud Storage path. |
| <CopyableCode code="referenceId" /> | `string` | The reference ID set by customers. Must be unique per project and location. |
| <CopyableCode code="textExtractionDisabled" /> | `boolean` | If true, text extraction will not be performed. |
| <CopyableCode code="textExtractionEnabled" /> | `boolean` | If true, text extraction will be performed. |
| <CopyableCode code="title" /> | `string` | Title that describes the document. This can be the top heading or text that describes the document. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time when the document is last updated. |
| <CopyableCode code="updater" /> | `string` | The user who lastly updates the document. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="documentsId, locationsId, projectsId" /> | Gets a document. Returns NOT_FOUND if the document does not exist. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a document. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="documentsId, locationsId, projectsId" /> | Deletes a document. Returns NOT_FOUND if the document does not exist. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="documentsId, locationsId, projectsId" /> | Updates a document. Returns INVALID_ARGUMENT if the name of the document is non-empty and does not equal the existing name. |
| <CopyableCode code="linked_sources" /> | `EXEC` | <CopyableCode code="documentsId, locationsId, projectsId" /> | Return all source document-links from the document. |
| <CopyableCode code="linked_targets" /> | `EXEC` | <CopyableCode code="documentsId, locationsId, projectsId" /> | Return all target document-links from the document. |
| <CopyableCode code="lock" /> | `EXEC` | <CopyableCode code="documentsId, locationsId, projectsId" /> | Lock the document so the document cannot be updated by other users. |
| <CopyableCode code="search" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Searches for documents using provided SearchDocumentsRequest. This call only returns documents that the caller has permission to search against. |
| <CopyableCode code="set_acl" /> | `EXEC` | <CopyableCode code="documentsId, locationsId, projectsId" /> | Sets the access control policy for a resource. Replaces any existing policy. |

## `SELECT` examples

Gets a document. Returns NOT_FOUND if the document does not exist.

```sql
SELECT
name,
cloudAiDocument,
contentCategory,
createTime,
creator,
displayName,
displayUri,
dispositionTime,
documentSchemaName,
inlineRawDocument,
legalHold,
plainText,
properties,
rawDocumentFileType,
rawDocumentPath,
referenceId,
textExtractionDisabled,
textExtractionEnabled,
title,
updateTime,
updater
FROM google.contentwarehouse.documents
WHERE documentsId = '{{ documentsId }}'
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
INSERT INTO google.contentwarehouse.documents (
locationsId,
projectsId,
cloudAiDocumentOption,
policy,
document,
requestMetadata,
createMask
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ cloudAiDocumentOption }}',
'{{ policy }}',
'{{ document }}',
'{{ requestMetadata }}',
'{{ createMask }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: cloudAiDocumentOption
      value: '{{ cloudAiDocumentOption }}'
    - name: policy
      value: '{{ policy }}'
    - name: document
      value: '{{ document }}'
    - name: requestMetadata
      value: '{{ requestMetadata }}'
    - name: createMask
      value: '{{ createMask }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>documents</code> resource.

```sql
/*+ update */
UPDATE google.contentwarehouse.documents
SET 
updateOptions = '{{ updateOptions }}',
cloudAiDocumentOption = '{{ cloudAiDocumentOption }}',
requestMetadata = '{{ requestMetadata }}',
document = '{{ document }}'
WHERE 
documentsId = '{{ documentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>documents</code> resource.

```sql
/*+ delete */
DELETE FROM google.contentwarehouse.documents
WHERE documentsId = '{{ documentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
