---
title: groups
hide_title: false
hide_table_of_contents: false
keywords:
  - groups
  - vmmigration
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
<tr><td><b>Id</b></td><td><CopyableCode code="google.vmmigration.groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The Group name. |
| <CopyableCode code="description" /> | `string` | User-provided description of the group. |
| <CopyableCode code="createTime" /> | `string` | Output only. The create time timestamp. |
| <CopyableCode code="displayName" /> | `string` | Display name is a user defined name for this group which can be updated. |
| <CopyableCode code="migrationTargetType" /> | `string` | Immutable. The target type of this group. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The update time timestamp. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="groupsId, locationsId, projectsId" /> | Gets details of a single Group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists Groups in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new Group in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="groupsId, locationsId, projectsId" /> | Deletes a single Group. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="groupsId, locationsId, projectsId" /> | Updates the parameters of a single Group. |

## `SELECT` examples

Lists Groups in a given project and location.

```sql
SELECT
name,
description,
createTime,
displayName,
migrationTargetType,
updateTime
FROM google.vmmigration.groups
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
INSERT INTO google.vmmigration.groups (
locationsId,
projectsId,
name,
createTime,
updateTime,
description,
displayName,
migrationTargetType
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ description }}',
'{{ displayName }}',
'{{ migrationTargetType }}'
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
      - name: createTime
        value: '{{ createTime }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: description
        value: '{{ description }}'
      - name: displayName
        value: '{{ displayName }}'
      - name: migrationTargetType
        value: '{{ migrationTargetType }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>groups</code> resource.

```sql
/*+ update */
UPDATE google.vmmigration.groups
SET 
name = '{{ name }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
description = '{{ description }}',
displayName = '{{ displayName }}',
migrationTargetType = '{{ migrationTargetType }}'
WHERE 
groupsId = '{{ groupsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>groups</code> resource.

```sql
/*+ delete */
DELETE FROM google.vmmigration.groups
WHERE groupsId = '{{ groupsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
