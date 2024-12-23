---
title: ip_access_lists
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - ip_access_lists
  - workspace
  - databricks_workspace
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Databricks resources using SQL
custom_edit_url: null
image: /img/providers/databricks_workspace/stackql-databricks-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Operations on a <code>ip_access_lists</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ip_access_lists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.workspace.ip_access_lists" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="address_count" /> | `integer` |
| <CopyableCode code="created_at" /> | `integer` |
| <CopyableCode code="created_by" /> | `integer` |
| <CopyableCode code="enabled" /> | `boolean` |
| <CopyableCode code="ip_addresses" /> | `array` |
| <CopyableCode code="label" /> | `string` |
| <CopyableCode code="list_id" /> | `string` |
| <CopyableCode code="list_type" /> | `string` |
| <CopyableCode code="updated_at" /> | `integer` |
| <CopyableCode code="updated_by" /> | `integer` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="ip_access_list_id, deployment_name" /> | Gets an IP access list, specified by its list ID. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Gets all IP access lists for the specified workspace. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Creates an IP access list for this workspace. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="ip_access_list_id, deployment_name" /> | Deletes an IP access list, specified by its list ID. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="ip_access_list_id, deployment_name" /> | Updates an existing IP access list, specified by its ID. |
| <CopyableCode code="replace" /> | `REPLACE` | <CopyableCode code="ip_access_list_id, deployment_name" /> | Replaces an IP access list, specified by its ID. |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'ip_access_lists (list)', value: 'list' },
        { label: 'ip_access_lists (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
address_count,
created_at,
created_by,
enabled,
ip_addresses,
label,
list_id,
list_type,
updated_at,
updated_by
FROM databricks_workspace.workspace.ip_access_lists
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
address_count,
created_at,
created_by,
enabled,
ip_addresses,
label,
list_id,
list_type,
updated_at,
updated_by
FROM databricks_workspace.workspace.ip_access_lists
WHERE ip_access_list_id = '{{ ip_access_list_id }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>ip_access_lists</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'ip_access_lists', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.workspace.ip_access_lists (
deployment_name,
data__label,
data__list_type,
data__ip_addresses
)
SELECT 
'{{ deployment_name }}',
'{{ label }}',
'{{ list_type }}',
'{{ ip_addresses }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: label
    value: Office VPN
  - name: list_type
    value: ALLOW
  - name: ip_addresses
    value:
    - 192.168.100.0/22

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>ip_access_lists</code> resource.

```sql
/*+ update */
UPDATE databricks_workspace.workspace.ip_access_lists
SET { field = value }
WHERE ip_access_list_id = '{{ ip_access_list_id }}' AND
deployment_name = '{{ deployment_name }}';
```

## `REPLACE` example

Replaces a <code>ip_access_lists</code> resource.

```sql
/*+ update */
REPLACE databricks_workspace.workspace.ip_access_lists
SET { field = value }
WHERE ip_access_list_id = '{{ ip_access_list_id }}' AND
deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>ip_access_lists</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.workspace.ip_access_lists
WHERE ip_access_list_id = '{{ ip_access_list_id }}' AND
deployment_name = '{{ deployment_name }}';
```
