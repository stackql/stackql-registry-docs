---
title: runs
hide_title: false
hide_table_of_contents: false
keywords:
  - runs
  - datalineage
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

Creates, updates, deletes, gets or lists a <code>runs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.datalineage.runs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The resource name of the run. Format: `projects/{project}/locations/{location}/processes/{process}/runs/{run}`. Can be specified or auto-assigned. {run} must be not longer than 200 characters and only contain characters in a set: `a-zA-Z0-9_-:.` |
| <CopyableCode code="attributes" /> | `object` | Optional. The attributes of the run. Should only be used for the purpose of non-semantic management (classifying, describing or labeling the run). Up to 100 attributes are allowed. |
| <CopyableCode code="displayName" /> | `string` | Optional. A human-readable name you can set to display in a user interface. Must be not longer than 1024 characters and only contain UTF-8 letters or numbers, spaces or characters like `_-:&.` |
| <CopyableCode code="endTime" /> | `string` | Optional. The timestamp of the end of the run. |
| <CopyableCode code="startTime" /> | `string` | Required. The timestamp of the start of the run. |
| <CopyableCode code="state" /> | `string` | Required. The state of the run. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, processesId, projectsId, runsId" /> | Gets the details of the specified run. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, processesId, projectsId" /> | Lists runs in the given project and location. List order is descending by `start_time`. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, processesId, projectsId" /> | Creates a new run. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, processesId, projectsId, runsId" /> | Deletes the run with the specified name. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, processesId, projectsId, runsId" /> | Updates a run. |

## `SELECT` examples

Lists runs in the given project and location. List order is descending by `start_time`.

```sql
SELECT
name,
attributes,
displayName,
endTime,
startTime,
state
FROM google.datalineage.runs
WHERE locationsId = '{{ locationsId }}'
AND processesId = '{{ processesId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>runs</code> resource.

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
INSERT INTO google.datalineage.runs (
locationsId,
processesId,
projectsId,
attributes,
startTime,
endTime,
name,
state,
displayName
)
SELECT 
'{{ locationsId }}',
'{{ processesId }}',
'{{ projectsId }}',
'{{ attributes }}',
'{{ startTime }}',
'{{ endTime }}',
'{{ name }}',
'{{ state }}',
'{{ displayName }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: attributes
      value: '{{ attributes }}'
    - name: startTime
      value: '{{ startTime }}'
    - name: endTime
      value: '{{ endTime }}'
    - name: name
      value: '{{ name }}'
    - name: state
      value: '{{ state }}'
    - name: displayName
      value: '{{ displayName }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>runs</code> resource.

```sql
/*+ update */
UPDATE google.datalineage.runs
SET 
attributes = '{{ attributes }}',
startTime = '{{ startTime }}',
endTime = '{{ endTime }}',
name = '{{ name }}',
state = '{{ state }}',
displayName = '{{ displayName }}'
WHERE 
locationsId = '{{ locationsId }}'
AND processesId = '{{ processesId }}'
AND projectsId = '{{ projectsId }}'
AND runsId = '{{ runsId }}';
```

## `DELETE` example

Deletes the specified <code>runs</code> resource.

```sql
/*+ delete */
DELETE FROM google.datalineage.runs
WHERE locationsId = '{{ locationsId }}'
AND processesId = '{{ processesId }}'
AND projectsId = '{{ projectsId }}'
AND runsId = '{{ runsId }}';
```
