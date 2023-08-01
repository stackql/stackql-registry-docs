---
title: document_schemas
hide_title: false
hide_table_of_contents: false
keywords:
  - document_schemas
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
<tr><td><b>Name</b></td><td><code>document_schemas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.contentwarehouse.document_schemas</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the document schema. Format: projects/&#123;project_number&#125;/locations/&#123;location&#125;/documentSchemas/&#123;document_schema_id&#125;. The name is ignored when creating a document schema. |
| `description` | `string` | Schema description. |
| `createTime` | `string` | Output only. The time when the document schema is created. |
| `displayName` | `string` | Required. Name of the schema given by the user. Must be unique per project. |
| `documentIsFolder` | `boolean` | Document Type, true refers the document is a folder, otherwise it is a typical document. |
| `propertyDefinitions` | `array` | Document details. |
| `updateTime` | `string` | Output only. The time when the document schema is last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `documentSchemasId, locationsId, projectsId` | Gets a document schema. Returns NOT_FOUND if the document schema does not exist. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists document schemas. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a document schema. |
| `delete` | `DELETE` | `documentSchemasId, locationsId, projectsId` | Deletes a document schema. Returns NOT_FOUND if the document schema does not exist. Returns BAD_REQUEST if the document schema has documents depending on it. |
| `patch` | `EXEC` | `documentSchemasId, locationsId, projectsId` | Updates a Document Schema. Returns INVALID_ARGUMENT if the name of the Document Schema is non-empty and does not equal the existing name. Supports only appending new properties, adding new ENUM possible values, and updating the EnumTypeOptions.validation_check_disabled flag for ENUM possible values. Updating existing properties will result into INVALID_ARGUMENT. |
