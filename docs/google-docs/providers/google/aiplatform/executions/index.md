---
title: executions
hide_title: false
hide_table_of_contents: false
keywords:
  - executions
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
<tr><td><b>Name</b></td><td><code>executions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.aiplatform.executions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the Execution. |
| `description` | `string` | Description of the Execution |
| `metadata` | `object` | Properties of the Execution. Top level metadata keys' heading and trailing spaces will be trimmed. The size of this field should not exceed 200KB. |
| `schemaVersion` | `string` | The version of the schema in `schema_title` to use. Schema title and version is expected to be registered in earlier Create Schema calls. And both are used together as unique identifiers to identify schemas within the local metadata store. |
| `schemaTitle` | `string` | The title of the schema describing the metadata. Schema title and version is expected to be registered in earlier Create Schema calls. And both are used together as unique identifiers to identify schemas within the local metadata store. |
| `labels` | `object` | The labels with user-defined metadata to organize your Executions. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one Execution (System labels are excluded). |
| `updateTime` | `string` | Output only. Timestamp when this Execution was last updated. |
| `state` | `string` | The state of this Execution. This is a property of the Execution, and does not imply or capture any ongoing process. This property is managed by clients (such as Vertex AI Pipelines) and the system does not prescribe or check the validity of state transitions. |
| `createTime` | `string` | Output only. Timestamp when this Execution was created. |
| `displayName` | `string` | User provided display name of the Execution. May be up to 128 Unicode characters. |
| `etag` | `string` | An eTag used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `executionsId, locationsId, metadataStoresId, projectsId` | Retrieves a specific Execution. |
| `list` | `SELECT` | `locationsId, metadataStoresId, projectsId` | Lists Executions in the MetadataStore. |
| `create` | `INSERT` | `locationsId, metadataStoresId, projectsId` | Creates an Execution associated with a MetadataStore. |
| `delete` | `DELETE` | `executionsId, locationsId, metadataStoresId, projectsId` | Deletes an Execution. |
| `_list` | `EXEC` | `locationsId, metadataStoresId, projectsId` | Lists Executions in the MetadataStore. |
| `patch` | `EXEC` | `executionsId, locationsId, metadataStoresId, projectsId` | Updates a stored Execution. |
| `purge` | `EXEC` | `locationsId, metadataStoresId, projectsId` | Purges Executions. |
| `query_execution_inputs_and_outputs` | `EXEC` | `executionsId, locationsId, metadataStoresId, projectsId` | Obtains the set of input and output Artifacts for this Execution, in the form of LineageSubgraph that also contains the Execution and connecting Events. |
