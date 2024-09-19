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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>artifacts</code> resource.

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
| <CopyableCode code="query_artifact_lineage_subgraph" /> | `SELECT` | <CopyableCode code="artifactsId, locationsId, metadataStoresId, projectsId" /> | Retrieves lineage of an Artifact represented through Artifacts and Executions connected by Event edges and returned as a LineageSubgraph. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, metadataStoresId, projectsId" /> | Creates an Artifact associated with a MetadataStore. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="artifactsId, locationsId, metadataStoresId, projectsId" /> | Deletes an Artifact. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="artifactsId, locationsId, metadataStoresId, projectsId" /> | Updates a stored Artifact. |
| <CopyableCode code="purge" /> | `EXEC` | <CopyableCode code="locationsId, metadataStoresId, projectsId" /> | Purges Artifacts. |

## `SELECT` examples

Lists Artifacts in the MetadataStore.

```sql
SELECT
name,
description,
createTime,
displayName,
etag,
labels,
metadata,
schemaTitle,
schemaVersion,
state,
updateTime,
uri
FROM google.aiplatform.artifacts
WHERE locationsId = '{{ locationsId }}'
AND metadataStoresId = '{{ metadataStoresId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>artifacts</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.aiplatform.artifacts (
locationsId,
metadataStoresId,
projectsId,
uri,
labels,
metadata,
schemaVersion,
schemaTitle,
displayName,
state,
etag,
description
)
SELECT 
'{{ locationsId }}',
'{{ metadataStoresId }}',
'{{ projectsId }}',
'{{ uri }}',
'{{ labels }}',
'{{ metadata }}',
'{{ schemaVersion }}',
'{{ schemaTitle }}',
'{{ displayName }}',
'{{ state }}',
'{{ etag }}',
'{{ description }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: createTime
      value: string
    - name: uri
      value: string
    - name: labels
      value: object
    - name: metadata
      value: object
    - name: schemaVersion
      value: string
    - name: schemaTitle
      value: string
    - name: displayName
      value: string
    - name: state
      value: string
    - name: name
      value: string
    - name: updateTime
      value: string
    - name: etag
      value: string
    - name: description
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>artifacts</code> resource.

```sql
/*+ update */
UPDATE google.aiplatform.artifacts
SET 
uri = '{{ uri }}',
labels = '{{ labels }}',
metadata = '{{ metadata }}',
schemaVersion = '{{ schemaVersion }}',
schemaTitle = '{{ schemaTitle }}',
displayName = '{{ displayName }}',
state = '{{ state }}',
etag = '{{ etag }}',
description = '{{ description }}'
WHERE 
artifactsId = '{{ artifactsId }}'
AND locationsId = '{{ locationsId }}'
AND metadataStoresId = '{{ metadataStoresId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>artifacts</code> resource.

```sql
/*+ delete */
DELETE FROM google.aiplatform.artifacts
WHERE artifactsId = '{{ artifactsId }}'
AND locationsId = '{{ locationsId }}'
AND metadataStoresId = '{{ metadataStoresId }}'
AND projectsId = '{{ projectsId }}';
```
