---
title: groups
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - groups
  - iam
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

Operations on a <code>groups</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.iam.groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="displayName" /> | `string` |
| <CopyableCode code="externalId" /> | `string` |
| <CopyableCode code="members" /> | `array` |
| <CopyableCode code="roles" /> | `array` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="account_id, id" /> | Gets the information for a specific group in the Databricks account. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="account_id" /> | Gets all details of the groups associated with the Databricks account. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="account_id" /> | Creates a group in the Databricks account with a unique name, using the supplied group details. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="account_id, id" /> | Deletes a group from the Databricks account. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="account_id, id" /> | Partially updates the details of a group. |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="account_id, id" /> | Updates the details of a group by replacing the entire group entity. |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'groups (list)', value: 'list' },
        { label: 'groups (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
id,
displayName,
externalId,
members,
roles
FROM databricks_account.iam.groups
WHERE account_id = '{{ account_id }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
id,
displayName,
externalId,
members,
roles
FROM databricks_account.iam.groups
WHERE account_id = '{{ account_id }}' AND
id = '{{ id }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>groups</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'groups', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_account.iam.groups (
account_id,
data__displayName,
data__members,
data__roles,
data__externalId
)
SELECT 
'{{ account_id }}',
'{{ displayName }}',
'{{ members }}',
'{{ roles }}',
'{{ externalId }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: displayName
    value: string
  - name: members
    value:
    - $ref: string
      value: string
      display: string
      primary: true
      type: string
  - name: roles
    value:
    - $ref: string
      value: string
      display: string
      primary: true
      type: string
  - name: externalId
    value: string

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>groups</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update        
UPDATE databricks_account.iam.groups
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE account_id = '{{ account_id }}' AND
id = '{{ id }}';
```

## `REPLACE` example

Replaces a <code>groups</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update
REPLACE databricks_account.iam.groups
SET field1 = '{ value1 }',
field2 = '{ value2 }', ...
WHERE account_id = '{{ account_id }}' AND
id = '{{ id }}';
```

## `DELETE` example

Deletes a <code>groups</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_account.iam.groups
WHERE account_id = '{{ account_id }}' AND
id = '{{ id }}';
```
