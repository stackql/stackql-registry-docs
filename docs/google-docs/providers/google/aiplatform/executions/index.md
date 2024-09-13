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

Creates, updates, deletes or gets an <code>execution</code> resource or lists <code>executions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>executions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.executions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="artifacts" /> | `array` | The Artifact nodes in the subgraph. |
| <CopyableCode code="events" /> | `array` | The Event edges between Artifacts and Executions in the subgraph. |
| <CopyableCode code="executions" /> | `array` | The Execution nodes in the subgraph. |

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
artifacts,
events,
executions
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
name,
description,
state,
labels,
createTime,
displayName,
schemaVersion,
schemaTitle,
etag,
updateTime,
metadata
)
SELECT 
'{{ locationsId }}',
'{{ metadataStoresId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ description }}',
'{{ state }}',
'{{ labels }}',
'{{ createTime }}',
'{{ displayName }}',
'{{ schemaVersion }}',
'{{ schemaTitle }}',
'{{ etag }}',
'{{ updateTime }}',
'{{ metadata }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: description
        value: '{{ description }}'
      - name: state
        value: '{{ state }}'
      - name: labels
        value: '{{ labels }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: displayName
        value: '{{ displayName }}'
      - name: schemaVersion
        value: '{{ schemaVersion }}'
      - name: schemaTitle
        value: '{{ schemaTitle }}'
      - name: etag
        value: '{{ etag }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: metadata
        value: '{{ metadata }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a execution only if the necessary resources are available.

```sql
UPDATE google.aiplatform.executions
SET 
name = '{{ name }}',
description = '{{ description }}',
state = '{{ state }}',
labels = '{{ labels }}',
createTime = '{{ createTime }}',
displayName = '{{ displayName }}',
schemaVersion = '{{ schemaVersion }}',
schemaTitle = '{{ schemaTitle }}',
etag = '{{ etag }}',
updateTime = '{{ updateTime }}',
metadata = '{{ metadata }}'
WHERE 
executionsId = '{{ executionsId }}'
AND locationsId = '{{ locationsId }}'
AND metadataStoresId = '{{ metadataStoresId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified execution resource.

```sql
DELETE FROM google.aiplatform.executions
WHERE executionsId = '{{ executionsId }}'
AND locationsId = '{{ locationsId }}'
AND metadataStoresId = '{{ metadataStoresId }}'
AND projectsId = '{{ projectsId }}';
```
