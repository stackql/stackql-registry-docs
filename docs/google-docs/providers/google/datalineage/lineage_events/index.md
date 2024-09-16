---
title: lineage_events
hide_title: false
hide_table_of_contents: false
keywords:
  - lineage_events
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

Creates, updates, deletes, gets or lists a <code>lineage_events</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>lineage_events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.datalineage.lineage_events" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The resource name of the lineage event. Format: `projects/{project}/locations/{location}/processes/{process}/runs/{run}/lineageEvents/{lineage_event}`. Can be specified or auto-assigned. {lineage_event} must be not longer than 200 characters and only contain characters in a set: `a-zA-Z0-9_-:.` |
| <CopyableCode code="endTime" /> | `string` | Optional. The end of the transformation which resulted in this lineage event. For streaming scenarios, it should be the end of the period from which the lineage is being reported. |
| <CopyableCode code="links" /> | `array` | Optional. List of source-target pairs. Can't contain more than 100 tuples. |
| <CopyableCode code="startTime" /> | `string` | Required. The beginning of the transformation which resulted in this lineage event. For streaming scenarios, it should be the beginning of the period from which the lineage is being reported. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="lineageEventsId, locationsId, processesId, projectsId, runsId" /> | Gets details of a specified lineage event. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, processesId, projectsId, runsId" /> | Lists lineage events in the given project and location. The list order is not defined. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, processesId, projectsId, runsId" /> | Creates a new lineage event. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="lineageEventsId, locationsId, processesId, projectsId, runsId" /> | Deletes the lineage event with the specified name. |

## `SELECT` examples

Lists lineage events in the given project and location. The list order is not defined.

```sql
SELECT
name,
endTime,
links,
startTime
FROM google.datalineage.lineage_events
WHERE locationsId = '{{ locationsId }}'
AND processesId = '{{ processesId }}'
AND projectsId = '{{ projectsId }}'
AND runsId = '{{ runsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>lineage_events</code> resource.

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
INSERT INTO google.datalineage.lineage_events (
locationsId,
processesId,
projectsId,
runsId,
startTime,
links,
name,
endTime
)
SELECT 
'{{ locationsId }}',
'{{ processesId }}',
'{{ projectsId }}',
'{{ runsId }}',
'{{ startTime }}',
'{{ links }}',
'{{ name }}',
'{{ endTime }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: startTime
      value: '{{ startTime }}'
    - name: links
      value: '{{ links }}'
    - name: name
      value: '{{ name }}'
    - name: endTime
      value: '{{ endTime }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>lineage_events</code> resource.

```sql
/*+ delete */
DELETE FROM google.datalineage.lineage_events
WHERE lineageEventsId = '{{ lineageEventsId }}'
AND locationsId = '{{ locationsId }}'
AND processesId = '{{ processesId }}'
AND projectsId = '{{ projectsId }}'
AND runsId = '{{ runsId }}';
```
