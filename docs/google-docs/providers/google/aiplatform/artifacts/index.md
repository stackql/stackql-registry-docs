---
title: artifacts
hide_title: false
hide_table_of_contents: false
keywords:
  - artifacts
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
<tr><td><b>Name</b></td><td><code>artifacts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.aiplatform.artifacts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the Artifact. |
| `description` | `string` | Description of the Artifact |
| `state` | `string` | The state of this Artifact. This is a property of the Artifact, and does not imply or capture any ongoing process. This property is managed by clients (such as Vertex AI Pipelines), and the system does not prescribe or check the validity of state transitions. |
| `schemaTitle` | `string` | The title of the schema describing the metadata. Schema title and version is expected to be registered in earlier Create Schema calls. And both are used together as unique identifiers to identify schemas within the local metadata store. |
| `schemaVersion` | `string` | The version of the schema in schema_name to use. Schema title and version is expected to be registered in earlier Create Schema calls. And both are used together as unique identifiers to identify schemas within the local metadata store. |
| `metadata` | `object` | Properties of the Artifact. Top level metadata keys' heading and trailing spaces will be trimmed. The size of this field should not exceed 200KB. |
| `createTime` | `string` | Output only. Timestamp when this Artifact was created. |
| `displayName` | `string` | User provided display name of the Artifact. May be up to 128 Unicode characters. |
| `etag` | `string` | An eTag used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens. |
| `updateTime` | `string` | Output only. Timestamp when this Artifact was last updated. |
| `labels` | `object` | The labels with user-defined metadata to organize your Artifacts. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one Artifact (System labels are excluded). |
| `uri` | `string` | The uniform resource identifier of the artifact file. May be empty if there is no actual artifact file. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `artifactsId, locationsId, metadataStoresId, projectsId` | Retrieves a specific Artifact. |
| `list` | `SELECT` | `locationsId, metadataStoresId, projectsId` | Lists Artifacts in the MetadataStore. |
| `create` | `INSERT` | `locationsId, metadataStoresId, projectsId` | Creates an Artifact associated with a MetadataStore. |
| `delete` | `DELETE` | `artifactsId, locationsId, metadataStoresId, projectsId` | Deletes an Artifact. |
| `_list` | `EXEC` | `locationsId, metadataStoresId, projectsId` | Lists Artifacts in the MetadataStore. |
| `patch` | `EXEC` | `artifactsId, locationsId, metadataStoresId, projectsId` | Updates a stored Artifact. |
| `purge` | `EXEC` | `locationsId, metadataStoresId, projectsId` | Purges Artifacts. |
| `query_artifact_lineage_subgraph` | `EXEC` | `artifactsId, locationsId, metadataStoresId, projectsId` | Retrieves lineage of an Artifact represented through Artifacts and Executions connected by Event edges and returned as a LineageSubgraph. |
