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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>artifacts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.artifacts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the Artifact. |
| <CopyableCode code="description" /> | `string` | Description of the Artifact |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when this Artifact was created. |
| <CopyableCode code="displayName" /> | `string` | User provided display name of the Artifact. May be up to 128 Unicode characters. |
| <CopyableCode code="etag" /> | `string` | An eTag used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens. |
| <CopyableCode code="labels" /> | `object` | The labels with user-defined metadata to organize your Artifacts. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one Artifact (System labels are excluded). |
| <CopyableCode code="metadata" /> | `object` | Properties of the Artifact. Top level metadata keys' heading and trailing spaces will be trimmed. The size of this field should not exceed 200KB. |
| <CopyableCode code="schemaTitle" /> | `string` | The title of the schema describing the metadata. Schema title and version is expected to be registered in earlier Create Schema calls. And both are used together as unique identifiers to identify schemas within the local metadata store. |
| <CopyableCode code="schemaVersion" /> | `string` | The version of the schema in schema_name to use. Schema title and version is expected to be registered in earlier Create Schema calls. And both are used together as unique identifiers to identify schemas within the local metadata store. |
| <CopyableCode code="state" /> | `string` | The state of this Artifact. This is a property of the Artifact, and does not imply or capture any ongoing process. This property is managed by clients (such as Vertex AI Pipelines), and the system does not prescribe or check the validity of state transitions. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp when this Artifact was last updated. |
| <CopyableCode code="uri" /> | `string` | The uniform resource identifier of the artifact file. May be empty if there is no actual artifact file. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="artifactsId, locationsId, metadataStoresId, projectsId" /> | Retrieves a specific Artifact. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, metadataStoresId, projectsId" /> | Lists Artifacts in the MetadataStore. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, metadataStoresId, projectsId" /> | Creates an Artifact associated with a MetadataStore. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="artifactsId, locationsId, metadataStoresId, projectsId" /> | Deletes an Artifact. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="artifactsId, locationsId, metadataStoresId, projectsId" /> | Updates a stored Artifact. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, metadataStoresId, projectsId" /> | Lists Artifacts in the MetadataStore. |
| <CopyableCode code="purge" /> | `EXEC` | <CopyableCode code="locationsId, metadataStoresId, projectsId" /> | Purges Artifacts. |
| <CopyableCode code="query_artifact_lineage_subgraph" /> | `EXEC` | <CopyableCode code="artifactsId, locationsId, metadataStoresId, projectsId" /> | Retrieves lineage of an Artifact represented through Artifacts and Executions connected by Event edges and returned as a LineageSubgraph. |
