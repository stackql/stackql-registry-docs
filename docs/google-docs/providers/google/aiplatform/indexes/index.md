---
title: indexes
hide_title: false
hide_table_of_contents: false
keywords:
  - indexes
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
<tr><td><b>Name</b></td><td><code>indexes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.aiplatform.indexes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the Index. |
| `description` | `string` | The description of the Index. |
| `metadataSchemaUri` | `string` | Immutable. Points to a YAML file stored on Google Cloud Storage describing additional information about the Index, that is specific to it. Unset if the Index does not have any additional information. The schema is defined as an OpenAPI 3.0.2 [Schema Object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.2.md#schemaObject). Note: The URI given on output will be immutable and probably different, including the URI scheme, than the one given on input. The output URI will point to a location where the user only has a read access. |
| `deployedIndexes` | `array` | Output only. The pointers to DeployedIndexes created from this Index. An Index can be only deleted if all its DeployedIndexes had been undeployed first. |
| `indexUpdateMethod` | `string` | Immutable. The update method to use with this Index. If not set, BATCH_UPDATE will be used by default. |
| `indexStats` | `object` | Stats of the Index. |
| `createTime` | `string` | Output only. Timestamp when this Index was created. |
| `updateTime` | `string` | Output only. Timestamp when this Index was most recently updated. This also includes any update to the contents of the Index. Note that Operations working on this Index may have their Operations.metadata.generic_metadata.update_time a little after the value of this timestamp, yet that does not mean their results are not already reflected in the Index. Result of any successfully completed Operation on the Index is reflected in it. |
| `metadata` | `any` | An additional information about the Index; the schema of the metadata can be found in metadata_schema. |
| `etag` | `string` | Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens. |
| `displayName` | `string` | Required. The display name of the Index. The name can be up to 128 characters long and can consist of any UTF-8 characters. |
| `labels` | `object` | The labels with user-defined metadata to organize your Indexes. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `indexesId, locationsId, projectsId` | Gets an Index. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists Indexes in a Location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates an Index. |
| `delete` | `DELETE` | `indexesId, locationsId, projectsId` | Deletes an Index. An Index can only be deleted when all its DeployedIndexes had been undeployed. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists Indexes in a Location. |
| `patch` | `EXEC` | `indexesId, locationsId, projectsId` | Updates an Index. |
| `upsert_datapoints` | `EXEC` | `indexesId, locationsId, projectsId` | Add/update Datapoints into an Index. |
