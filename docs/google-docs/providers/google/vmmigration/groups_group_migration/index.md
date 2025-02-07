---
title: groups_group_migration
hide_title: false
hide_table_of_contents: false
keywords:
  - groups_group_migration
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

Creates, updates, deletes, gets or lists a <code>groups_group_migration</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>groups_group_migration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.vmmigration.groups_group_migration" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="add_group_migration" /> | `INSERT` | <CopyableCode code="groupsId, locationsId, projectsId" /> | Adds a MigratingVm to a Group. |
| <CopyableCode code="remove_group_migration" /> | `DELETE` | <CopyableCode code="groupsId, locationsId, projectsId" /> | Removes a MigratingVm from a Group. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>groups_group_migration</code> resource.

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
INSERT INTO google.vmmigration.groups_group_migration (
groupsId,
locationsId,
projectsId,
migratingVm
)
SELECT 
'{{ groupsId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ migratingVm }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: migratingVm
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>groups_group_migration</code> resource.

```sql
/*+ delete */
DELETE FROM google.vmmigration.groups_group_migration
WHERE groupsId = '{{ groupsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
