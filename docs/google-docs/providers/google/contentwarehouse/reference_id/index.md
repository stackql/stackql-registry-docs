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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>reference_id</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.contentwarehouse.reference_id</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the document. Format: projects/&#123;project_number&#125;/locations/&#123;location&#125;/documents/&#123;document_id&#125;. The name is ignored when creating a document. |
| `rawDocumentPath` | `string` | Raw document file in Cloud Storage path. |
| `textExtractionDisabled` | `boolean` | If true, text extraction will not be performed. |
| `properties` | `array` | List of values that are user supplied metadata. |
| `cloudAiDocument` | `object` | Document represents the canonical document resource in Document AI. It is an interchange format that provides insights into documents and allows for collaboration between users and Document AI to iterate and optimize for quality. |
| `referenceId` | `string` | The reference ID set by customers. Must be unique per project and location. |
| `documentSchemaName` | `string` | The Document schema name. Format: projects/&#123;project_number&#125;/locations/&#123;location&#125;/documentSchemas/&#123;document_schema_id&#125;. |
| `rawDocumentFileType` | `string` | This is used when DocAI was not used to load the document and parsing/ extracting is needed for the inline_raw_document. For example, if inline_raw_document is the byte representation of a PDF file, then this should be set to: RAW_DOCUMENT_FILE_TYPE_PDF. |
| `title` | `string` | Title that describes the document. This can be the top heading or text that describes the document. |
| `inlineRawDocument` | `string` | Raw document content. |
| `createTime` | `string` | Output only. The time when the document is created. |
| `updater` | `string` | The user who lastly updates the document. |
| `contentCategory` | `string` | Indicates the category (image, audio, video etc.) of the original content. |
| `updateTime` | `string` | Output only. The time when the document is last updated. |
| `creator` | `string` | The user who creates the document. |
| `displayName` | `string` | Required. Display name of the document given by the user. This name will be displayed in the UI. Customer can populate this field with the name of the document. This differs from the 'title' field as 'title' is optional and stores the top heading in the document. |
| `textExtractionEnabled` | `boolean` | If true, text extraction will be performed. |
| `plainText` | `string` | Other document format, such as PPTX, XLXS |
| `displayUri` | `string` | Uri to display the document, for example, in the UI. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_documents_referenceId_get` | `SELECT` | `locationsId, projectsId, referenceIdId` | Gets a document. Returns NOT_FOUND if the document does not exist. |
| `projects_locations_documents_referenceId_delete` | `DELETE` | `locationsId, projectsId, referenceIdId` | Deletes a document. Returns NOT_FOUND if the document does not exist. |
| `projects_locations_documents_referenceId_patch` | `EXEC` | `locationsId, projectsId, referenceIdId` | Updates a document. Returns INVALID_ARGUMENT if the name of the document is non-empty and does not equal the existing name. |
