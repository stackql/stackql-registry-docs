---
title: contexts
hide_title: false
hide_table_of_contents: false
keywords:
  - contexts
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
<tr><td><b>Name</b></td><td><code>contexts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.aiplatform.contexts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. The resource name of the Context. |
| `description` | `string` | Description of the Context |
| `parentContexts` | `array` | Output only. A list of resource names of Contexts that are parents of this Context. A Context may have at most 10 parent_contexts. |
| `createTime` | `string` | Output only. Timestamp when this Context was created. |
| `displayName` | `string` | User provided display name of the Context. May be up to 128 Unicode characters. |
| `etag` | `string` | An eTag used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens. |
| `schemaVersion` | `string` | The version of the schema in schema_name to use. Schema title and version is expected to be registered in earlier Create Schema calls. And both are used together as unique identifiers to identify schemas within the local metadata store. |
| `schemaTitle` | `string` | The title of the schema describing the metadata. Schema title and version is expected to be registered in earlier Create Schema calls. And both are used together as unique identifiers to identify schemas within the local metadata store. |
| `metadata` | `object` | Properties of the Context. Top level metadata keys' heading and trailing spaces will be trimmed. The size of this field should not exceed 200KB. |
| `updateTime` | `string` | Output only. Timestamp when this Context was last updated. |
| `labels` | `object` | The labels with user-defined metadata to organize your Contexts. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one Context (System labels are excluded). |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `contextsId, locationsId, metadataStoresId, projectsId` | Retrieves a specific Context. |
| `list` | `SELECT` | `locationsId, metadataStoresId, projectsId` | Lists Contexts on the MetadataStore. |
| `create` | `INSERT` | `locationsId, metadataStoresId, projectsId` | Creates a Context associated with a MetadataStore. |
| `delete` | `DELETE` | `contextsId, locationsId, metadataStoresId, projectsId` | Deletes a stored Context. |
| `_list` | `EXEC` | `locationsId, metadataStoresId, projectsId` | Lists Contexts on the MetadataStore. |
| `patch` | `EXEC` | `contextsId, locationsId, metadataStoresId, projectsId` | Updates a stored Context. |
| `purge` | `EXEC` | `locationsId, metadataStoresId, projectsId` | Purges Contexts. |
| `query_context_lineage_subgraph` | `EXEC` | `contextsId, locationsId, metadataStoresId, projectsId` | Retrieves Artifacts and Executions within the specified Context, connected by Event edges and returned as a LineageSubgraph. |
