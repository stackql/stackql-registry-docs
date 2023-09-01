---
title: metadata_schemas
hide_title: false
hide_table_of_contents: false
keywords:
  - metadata_schemas
  - aiplatform
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
<tr><td><b>Name</b></td><td><code>metadata_schemas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.aiplatform.metadata_schemas</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the MetadataSchema. |
| `description` | `string` | Description of the Metadata Schema |
| `createTime` | `string` | Output only. Timestamp when this MetadataSchema was created. |
| `schema` | `string` | Required. The raw YAML string representation of the MetadataSchema. The combination of [MetadataSchema.version] and the schema name given by `title` in [MetadataSchema.schema] must be unique within a MetadataStore. The schema is defined as an OpenAPI 3.0.2 [MetadataSchema Object](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.2.md#schemaObject) |
| `schemaType` | `string` | The type of the MetadataSchema. This is a property that identifies which metadata types will use the MetadataSchema. |
| `schemaVersion` | `string` | The version of the MetadataSchema. The version's format must match the following regular expression: `^[0-9]+.+.+$`, which would allow to order/compare different versions. Example: 1.0.0, 1.0.1, etc. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, metadataSchemasId, metadataStoresId, projectsId` | Retrieves a specific MetadataSchema. |
| `list` | `SELECT` | `locationsId, metadataStoresId, projectsId` | Lists MetadataSchemas. |
| `create` | `INSERT` | `locationsId, metadataStoresId, projectsId` | Creates a MetadataSchema. |
| `_list` | `EXEC` | `locationsId, metadataStoresId, projectsId` | Lists MetadataSchemas. |
