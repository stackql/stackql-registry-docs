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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>contexts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.contexts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The resource name of the Context. |
| <CopyableCode code="description" /> | `string` | Description of the Context |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when this Context was created. |
| <CopyableCode code="displayName" /> | `string` | User provided display name of the Context. May be up to 128 Unicode characters. |
| <CopyableCode code="etag" /> | `string` | An eTag used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens. |
| <CopyableCode code="labels" /> | `object` | The labels with user-defined metadata to organize your Contexts. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one Context (System labels are excluded). |
| <CopyableCode code="metadata" /> | `object` | Properties of the Context. Top level metadata keys' heading and trailing spaces will be trimmed. The size of this field should not exceed 200KB. |
| <CopyableCode code="parentContexts" /> | `array` | Output only. A list of resource names of Contexts that are parents of this Context. A Context may have at most 10 parent_contexts. |
| <CopyableCode code="schemaTitle" /> | `string` | The title of the schema describing the metadata. Schema title and version is expected to be registered in earlier Create Schema calls. And both are used together as unique identifiers to identify schemas within the local metadata store. |
| <CopyableCode code="schemaVersion" /> | `string` | The version of the schema in schema_name to use. Schema title and version is expected to be registered in earlier Create Schema calls. And both are used together as unique identifiers to identify schemas within the local metadata store. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp when this Context was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="contextsId, locationsId, metadataStoresId, projectsId" /> | Retrieves a specific Context. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, metadataStoresId, projectsId" /> | Lists Contexts on the MetadataStore. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, metadataStoresId, projectsId" /> | Creates a Context associated with a MetadataStore. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="contextsId, locationsId, metadataStoresId, projectsId" /> | Deletes a stored Context. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="contextsId, locationsId, metadataStoresId, projectsId" /> | Updates a stored Context. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, metadataStoresId, projectsId" /> | Lists Contexts on the MetadataStore. |
| <CopyableCode code="purge" /> | `EXEC` | <CopyableCode code="locationsId, metadataStoresId, projectsId" /> | Purges Contexts. |
| <CopyableCode code="query_context_lineage_subgraph" /> | `EXEC` | <CopyableCode code="contextsId, locationsId, metadataStoresId, projectsId" /> | Retrieves Artifacts and Executions within the specified Context, connected by Event edges and returned as a LineageSubgraph. |
