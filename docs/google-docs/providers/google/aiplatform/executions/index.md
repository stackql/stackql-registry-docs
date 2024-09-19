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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>executions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>executions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.executions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the Execution. |
| <CopyableCode code="description" /> | `string` | Description of the Execution |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when this Execution was created. |
| <CopyableCode code="displayName" /> | `string` | User provided display name of the Execution. May be up to 128 Unicode characters. |
| <CopyableCode code="etag" /> | `string` | An eTag used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens. |
| <CopyableCode code="labels" /> | `object` | The labels with user-defined metadata to organize your Executions. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one Execution (System labels are excluded). |
| <CopyableCode code="metadata" /> | `object` | Properties of the Execution. Top level metadata keys' heading and trailing spaces will be trimmed. The size of this field should not exceed 200KB. |
| <CopyableCode code="schemaTitle" /> | `string` | The title of the schema describing the metadata. Schema title and version is expected to be registered in earlier Create Schema calls. And both are used together as unique identifiers to identify schemas within the local metadata store. |
| <CopyableCode code="schemaVersion" /> | `string` | The version of the schema in `schema_title` to use. Schema title and version is expected to be registered in earlier Create Schema calls. And both are used together as unique identifiers to identify schemas within the local metadata store. |
| <CopyableCode code="state" /> | `string` | The state of this Execution. This is a property of the Execution, and does not imply or capture any ongoing process. This property is managed by clients (such as Vertex AI Pipelines) and the system does not prescribe or check the validity of state transitions. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp when this Execution was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="executionsId, locationsId, metadataStoresId, projectsId" /> | Retrieves a specific Execution. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, metadataStoresId, projectsId" /> | Lists Executions in the MetadataStore. |
| <CopyableCode code="query_execution_inputs_and_outputs" /> | `SELECT` | <CopyableCode code="executionsId, locationsId, metadataStoresId, projectsId" /> | Obtains the set of input and output Artifacts for this Execution, in the form of LineageSubgraph that also contains the Execution and connecting Events. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, metadataStoresId, projectsId" /> | Creates an Execution associated with a MetadataStore. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="executionsId, locationsId, metadataStoresId, projectsId" /> | Deletes an Execution. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="executionsId, locationsId, metadataStoresId, projectsId" /> | Updates a stored Execution. |
| <CopyableCode code="purge" /> | `EXEC` | <CopyableCode code="locationsId, metadataStoresId, projectsId" /> | Purges Executions. |

## `SELECT` examples

Lists Executions in the MetadataStore.

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
updateTime
FROM google.aiplatform.executions
WHERE locationsId = '{{ locationsId }}'
AND metadataStoresId = '{{ metadataStoresId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>executions</code> resource.

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
INSERT INTO google.aiplatform.executions (
locationsId,
metadataStoresId,
projectsId,
schemaVersion,
metadata,
labels,
displayName,
description,
state,
schemaTitle,
etag
)
SELECT 
'{{ locationsId }}',
'{{ metadataStoresId }}',
'{{ projectsId }}',
'{{ schemaVersion }}',
'{{ metadata }}',
'{{ labels }}',
'{{ displayName }}',
'{{ description }}',
'{{ state }}',
'{{ schemaTitle }}',
'{{ etag }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: schemaVersion
      value: string
    - name: metadata
      value: object
    - name: createTime
      value: string
    - name: labels
      value: object
    - name: name
      value: string
    - name: updateTime
      value: string
    - name: displayName
      value: string
    - name: description
      value: string
    - name: state
      value: string
    - name: schemaTitle
      value: string
    - name: etag
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>executions</code> resource.

```sql
/*+ update */
UPDATE google.aiplatform.executions
SET 
schemaVersion = '{{ schemaVersion }}',
metadata = '{{ metadata }}',
labels = '{{ labels }}',
displayName = '{{ displayName }}',
description = '{{ description }}',
state = '{{ state }}',
schemaTitle = '{{ schemaTitle }}',
etag = '{{ etag }}'
WHERE 
executionsId = '{{ executionsId }}'
AND locationsId = '{{ locationsId }}'
AND metadataStoresId = '{{ metadataStoresId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>executions</code> resource.

```sql
/*+ delete */
DELETE FROM google.aiplatform.executions
WHERE executionsId = '{{ executionsId }}'
AND locationsId = '{{ locationsId }}'
AND metadataStoresId = '{{ metadataStoresId }}'
AND projectsId = '{{ projectsId }}';
```
