---
title: reference_id
hide_title: false
hide_table_of_contents: false
keywords:
  - reference_id
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

Creates, updates, deletes, gets or lists a <code>reference_id</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>reference_id</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.contentwarehouse.reference_id" /></td></tr>
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, referenceIdId" /> | Gets a document. Returns NOT_FOUND if the document does not exist. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, referenceIdId" /> | Deletes a document. Returns NOT_FOUND if the document does not exist. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, referenceIdId" /> | Updates a document. Returns INVALID_ARGUMENT if the name of the document is non-empty and does not equal the existing name. |

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
FROM google.contentwarehouse.reference_id
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND referenceIdId = '{{ referenceIdId }}';
```

## `UPDATE` example

Updates a <code>reference_id</code> resource.

```sql
/*+ update */
UPDATE google.contentwarehouse.reference_id
SET 
cloudAiDocumentOption = '{{ cloudAiDocumentOption }}',
requestMetadata = '{{ requestMetadata }}',
document = '{{ document }}',
updateOptions = '{{ updateOptions }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND referenceIdId = '{{ referenceIdId }}';
```

## `DELETE` example

Deletes the specified <code>reference_id</code> resource.

```sql
/*+ delete */
DELETE FROM google.contentwarehouse.reference_id
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND referenceIdId = '{{ referenceIdId }}';
```
