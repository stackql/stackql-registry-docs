---
title: ip_access_lists
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - ip_access_lists
  - settings
  - databricks_account
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Databricks resources using SQL
custom_edit_url: null
image: /img/providers/databricks_account/stackql-databricks-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Operations on a <code>ip_access_lists</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ip_access_lists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.settings.ip_access_lists" /></td></tr>
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="account_id, ip_access_list_id" /> | Gets an IP access list, specified by its list ID. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="account_id" /> | Gets all IP access lists for the specified account. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="account_id" /> | Creates an IP access list for the account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="account_id, ip_access_list_id" /> | Deletes an IP access list, specified by its list ID. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="account_id, ip_access_list_id" /> | Updates an existing IP access list, specified by its ID. |
| <CopyableCode code="replace" /> | `REPLACE` | <CopyableCode code="account_id, ip_access_list_id" /> | Replaces an IP access list, specified by its ID. |

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
FROM databricks_account.settings.ip_access_lists
WHERE account_id = '{{ account_id }}';
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
FROM databricks_account.settings.ip_access_lists
WHERE account_id = '{{ account_id }}' AND
ip_access_list_id = '{{ ip_access_list_id }}';
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
INSERT INTO databricks_account.settings.ip_access_lists (
account_id,
data__label,
data__list_type,
data__ip_addresses
)
SELECT 
'{{ account_id }}',
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
-- replace field1, field2, etc. with the fields you want to update        
UPDATE databricks_account.settings.ip_access_lists
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE account_id = '{{ account_id }}' AND
ip_access_list_id = '{{ ip_access_list_id }}';
```

## `REPLACE` example

Replaces a <code>ip_access_lists</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update
REPLACE databricks_account.settings.ip_access_lists
SET field1 = '{ value1 }',
field2 = '{ value2 }', ...
WHERE account_id = '{{ account_id }}' AND
ip_access_list_id = '{{ ip_access_list_id }}';
```

## `DELETE` example

Deletes a <code>ip_access_lists</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_account.settings.ip_access_lists
WHERE account_id = '{{ account_id }}' AND
ip_access_list_id = '{{ ip_access_list_id }}';
```
