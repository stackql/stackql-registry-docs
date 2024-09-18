---
title: groups
hide_title: false
hide_table_of_contents: false
keywords:
  - groups
  - monitoring
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

Creates, updates, deletes, gets or lists a <code>groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.monitoring.groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The name of this group. The format is: projects/[PROJECT_ID_OR_NUMBER]/groups/[GROUP_ID] When creating a group, this field is ignored and a new name is created consisting of the project specified in the call to CreateGroup and a unique [GROUP_ID] that is generated automatically. |
| <CopyableCode code="displayName" /> | `string` | A user-assigned name for this group, used only for display purposes. |
| <CopyableCode code="filter" /> | `string` | The filter used to determine which monitored resources belong to this group. |
| <CopyableCode code="isCluster" /> | `boolean` | If true, the members of this group are considered to be a cluster. The system can perform additional analysis on groups that are clusters. |
| <CopyableCode code="parentName" /> | `string` | The name of the group's parent, if it has one. The format is: projects/[PROJECT_ID_OR_NUMBER]/groups/[GROUP_ID] For groups with no parent, parent_name is the empty string, "". |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_groups_get" /> | `SELECT` | <CopyableCode code="groupsId, projectsId" /> | Gets a single group. |
| <CopyableCode code="projects_groups_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists the existing groups. |
| <CopyableCode code="projects_groups_create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates a new group. |
| <CopyableCode code="projects_groups_delete" /> | `DELETE` | <CopyableCode code="groupsId, projectsId" /> | Deletes an existing group. |
| <CopyableCode code="projects_groups_update" /> | `REPLACE` | <CopyableCode code="groupsId, projectsId" /> | Updates an existing group. You can change any group attributes except name. |

## `SELECT` examples

Lists the existing groups.

```sql
SELECT
name,
displayName,
filter,
isCluster,
parentName
FROM google.monitoring.groups
WHERE projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>groups</code> resource.

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
INSERT INTO google.monitoring.groups (
projectsId,
name,
displayName,
parentName,
filter,
isCluster
)
SELECT 
'{{ projectsId }}',
'{{ name }}',
'{{ displayName }}',
'{{ parentName }}',
'{{ filter }}',
true|false
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
displayName: string
parentName: string
filter: string
isCluster: boolean

```
</TabItem>
</Tabs>

## `REPLACE` example

Replaces all fields in the specified <code>groups</code> resource.

```sql
/*+ update */
REPLACE google.monitoring.groups
SET 
name = '{{ name }}',
displayName = '{{ displayName }}',
parentName = '{{ parentName }}',
filter = '{{ filter }}',
isCluster = true|false
WHERE 
groupsId = '{{ groupsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>groups</code> resource.

```sql
/*+ delete */
DELETE FROM google.monitoring.groups
WHERE groupsId = '{{ groupsId }}'
AND projectsId = '{{ projectsId }}';
```
