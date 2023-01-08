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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>documents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.contentwarehouse.documents</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the document. Format: projects/&#123;project_number&#125;/locations/&#123;location&#125;/documents/&#123;document_id&#125;. The name is ignored when creating a document. |
| `textExtractionDisabled` | `boolean` | If true, text extraction will not be performed. |
| `updateTime` | `string` | Output only. The time when the document is last updated. |
| `documentSchemaName` | `string` | The Document schema name. Format: projects/&#123;project_number&#125;/locations/&#123;location&#125;/documentSchemas/&#123;document_schema_id&#125;. |
| `textExtractionEnabled` | `boolean` | If true, text extraction will be performed. |
| `creator` | `string` | The user who creates the document. |
| `rawDocumentFileType` | `string` | This is used when DocAI was not used to load the document and parsing/ extracting is needed for the inline_raw_document. For example, if inline_raw_document is the byte representation of a PDF file, then this should be set to: RAW_DOCUMENT_FILE_TYPE_PDF. |
| `referenceId` | `string` | The reference ID set by customers. Must be unique per project and location. |
| `createTime` | `string` | Output only. The time when the document is created. |
| `displayUri` | `string` | Uri to display the document, for example, in the UI. |
| `properties` | `array` | List of values that are user supplied metadata. |
| `updater` | `string` | The user who lastly updates the document. |
| `cloudAiDocument` | `object` | Document represents the canonical document resource in Document AI. It is an interchange format that provides insights into documents and allows for collaboration between users and Document AI to iterate and optimize for quality. |
| `inlineRawDocument` | `string` | Raw document content. |
| `rawDocumentPath` | `string` | Raw document file in Cloud Storage path. |
| `title` | `string` | Title that describes the document. This can be the top heading or text that describes the document. |
| `displayName` | `string` | Required. Display name of the document given by the user. This name will be displayed in the UI. Customer can populate this field with the name of the document. This differs from the 'title' field as 'title' is optional and stores the top heading in the document. |
| `contentCategory` | `string` | Indicates the category (image, audio, video etc.) of the original content. |
| `plainText` | `string` | Other document format, such as PPTX, XLXS |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_documents_get` | `SELECT` | `documentsId, locationsId, projectsId` | Gets a document. Returns NOT_FOUND if the document does not exist. |
| `projects_locations_documents_create` | `INSERT` | `locationsId, projectsId` | Creates a document. |
| `projects_locations_documents_delete` | `DELETE` | `documentsId, locationsId, projectsId` | Deletes a document. Returns NOT_FOUND if the document does not exist. |
| `projects_locations_documents_linkedSources` | `EXEC` | `documentsId, locationsId, projectsId` | Return all source document-links from the document. |
| `projects_locations_documents_linkedTargets` | `EXEC` | `documentsId, locationsId, projectsId` | Return all target document-links from the document. |
| `projects_locations_documents_patch` | `EXEC` | `documentsId, locationsId, projectsId` | Updates a document. Returns INVALID_ARGUMENT if the name of the document is non-empty and does not equal the existing name. |
| `projects_locations_documents_search` | `EXEC` | `locationsId, projectsId` | Searches for documents using provided SearchDocumentsRequest. This call only returns documents that the caller has permission to search against. |
| `projects_locations_documents_setAcl` | `EXEC` | `documentsId, locationsId, projectsId` | Sets the access control policy for a resource. Replaces any existing policy. |
