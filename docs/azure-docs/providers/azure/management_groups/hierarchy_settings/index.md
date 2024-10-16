---
title: hierarchy_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - hierarchy_settings
  - management_groups
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

Creates, updates, deletes, gets or lists a <code>hierarchy_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hierarchy_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.management_groups.hierarchy_settings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The fully qualified ID for the settings object.  For example, /providers/Microsoft.Management/managementGroups/0000000-0000-0000-0000-000000000000/settings/default. |
| <CopyableCode code="name" /> | `string` | The name of the object. In this case, default. |
| <CopyableCode code="properties" /> | `object` | The generic properties of hierarchy settings. |
| <CopyableCode code="type" /> | `string` | The type of the resource.  For example, Microsoft.Management/managementGroups/settings. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="groupId" /> | Gets the hierarchy settings defined at the Management Group level. Settings can only be set on the root Management Group of the hierarchy. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="groupId" /> | Gets all the hierarchy settings defined at the Management Group level. Settings can only be set on the root Management Group of the hierarchy. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="groupId" /> | Creates or updates the hierarchy settings defined at the Management Group level. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="groupId" /> | Deletes the hierarchy settings defined at the Management Group level. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="groupId" /> | Updates the hierarchy settings defined at the Management Group level. |

## `SELECT` examples

Gets the hierarchy settings defined at the Management Group level. Settings can only be set on the root Management Group of the hierarchy.


```sql
SELECT
id,
name,
properties,
type
FROM azure.management_groups.hierarchy_settings
WHERE groupId = '{{ groupId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>hierarchy_settings</code> resource.

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
INSERT INTO azure.management_groups.hierarchy_settings (
groupId,
properties
)
SELECT 
'{{ groupId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: requireAuthorizationForGroupCreation
          value: boolean
        - name: defaultManagementGroup
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>hierarchy_settings</code> resource.

```sql
/*+ update */
UPDATE azure.management_groups.hierarchy_settings
SET 
properties = '{{ properties }}'
WHERE 
groupId = '{{ groupId }}';
```

## `DELETE` example

Deletes the specified <code>hierarchy_settings</code> resource.

```sql
/*+ delete */
DELETE FROM azure.management_groups.hierarchy_settings
WHERE groupId = '{{ groupId }}';
```
