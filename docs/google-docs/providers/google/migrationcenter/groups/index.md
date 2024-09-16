---
title: groups
hide_title: false
hide_table_of_contents: false
keywords:
  - groups
  - migrationcenter
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
<tr><td><b>Id</b></td><td><CopyableCode code="google.migrationcenter.groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The name of the group. |
| <CopyableCode code="description" /> | `string` | Optional. The description of the group. |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp when the group was created. |
| <CopyableCode code="displayName" /> | `string` | Optional. User-friendly display name. |
| <CopyableCode code="labels" /> | `object` | Labels as key value pairs. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The timestamp when the group was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="groupsId, locationsId, projectsId" /> | Gets the details of a group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists all groups in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new group in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="groupsId, locationsId, projectsId" /> | Deletes a group. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="groupsId, locationsId, projectsId" /> | Updates the parameters of a group. |

## `SELECT` examples

Lists all groups in a given project and location.

```sql
SELECT
name,
description,
createTime,
displayName,
labels,
updateTime
FROM google.migrationcenter.groups
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
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
INSERT INTO google.migrationcenter.groups (
locationsId,
projectsId,
labels,
displayName,
description
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ labels }}',
'{{ displayName }}',
'{{ description }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: labels
      value: '{{ labels }}'
    - name: displayName
      value: '{{ displayName }}'
    - name: description
      value: '{{ description }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>groups</code> resource.

```sql
/*+ update */
UPDATE google.migrationcenter.groups
SET 
labels = '{{ labels }}',
displayName = '{{ displayName }}',
description = '{{ description }}'
WHERE 
groupsId = '{{ groupsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>groups</code> resource.

```sql
/*+ delete */
DELETE FROM google.migrationcenter.groups
WHERE groupsId = '{{ groupsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
