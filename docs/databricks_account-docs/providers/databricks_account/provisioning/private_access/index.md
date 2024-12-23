---
title: private_access
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - private_access
  - provisioning
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

Operations on a <code>private_access</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_access</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.provisioning.private_access" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="account_id" /> | `string` |
| <CopyableCode code="allowed_vpc_endpoint_ids" /> | `array` |
| <CopyableCode code="private_access_level" /> | `string` |
| <CopyableCode code="private_access_settings_id" /> | `string` |
| <CopyableCode code="private_access_settings_name" /> | `string` |
| <CopyableCode code="public_access_enabled" /> | `boolean` |
| <CopyableCode code="region" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="account_id, private_access_settings_id" /> | Gets a private access settings object, which specifies how your workspace is accessed over |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="account_id" /> | Gets a list of all private access settings objects for an account, specified by ID. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="account_id" /> | Creates a private access settings object, which specifies how your workspace is accessed over |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="account_id, private_access_settings_id" /> | Deletes a private access settings object, which determines how your workspace is accessed over |
| <CopyableCode code="replace" /> | `REPLACE` | <CopyableCode code="account_id, private_access_settings_id" /> | Updates an existing private access settings object, which specifies how your workspace is accessed over |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'private_access (list)', value: 'list' },
        { label: 'private_access (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
account_id,
allowed_vpc_endpoint_ids,
private_access_level,
private_access_settings_id,
private_access_settings_name,
public_access_enabled,
region
FROM databricks_account.provisioning.private_access
WHERE account_id = '{{ account_id }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
account_id,
allowed_vpc_endpoint_ids,
private_access_level,
private_access_settings_id,
private_access_settings_name,
public_access_enabled,
region
FROM databricks_account.provisioning.private_access
WHERE account_id = '{{ account_id }}' AND
private_access_settings_id = '{{ private_access_settings_id }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>private_access</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'private_access', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_account.provisioning.private_access (
account_id,
data__private_access_settings_name,
data__region,
data__public_access_enabled,
data__private_access_level,
data__allowed_vpc_endpoint_ids
)
SELECT 
'{{ account_id }}',
'{{ private_access_settings_name }}',
'{{ region }}',
'{{ public_access_enabled }}',
'{{ private_access_level }}',
'{{ allowed_vpc_endpoint_ids }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: private_access_settings_name
    value: string
  - name: region
    value: string
  - name: public_access_enabled
    value: false
  - name: private_access_level
    value: ENDPOINT
  - name: allowed_vpc_endpoint_ids
    value:
    - 497f6eca-6276-4993-bfeb-53cbbbba6f08

```

</TabItem>
</Tabs>

## `REPLACE` example

Replaces a <code>private_access</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update
REPLACE databricks_account.provisioning.private_access
SET field1 = '{ value1 }',
field2 = '{ value2 }', ...
WHERE account_id = '{{ account_id }}' AND
private_access_settings_id = '{{ private_access_settings_id }}';
```

## `DELETE` example

Deletes a <code>private_access</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_account.provisioning.private_access
WHERE account_id = '{{ account_id }}' AND
private_access_settings_id = '{{ private_access_settings_id }}';
```
