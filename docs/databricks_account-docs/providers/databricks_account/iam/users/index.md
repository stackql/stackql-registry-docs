---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - users
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

Operations on a <code>users</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.iam.users" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="name" /> | `object` |
| <CopyableCode code="active" /> | `boolean` |
| <CopyableCode code="displayName" /> | `string` |
| <CopyableCode code="emails" /> | `array` |
| <CopyableCode code="externalId" /> | `string` |
| <CopyableCode code="roles" /> | `array` |
| <CopyableCode code="userName" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="account_id, id" /> | Gets information for a specific user in Databricks account. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="account_id" /> | Gets details for all the users associated with a Databricks account. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="account_id" /> | Creates a new user in the Databricks account. This new user will also be added to the Databricks account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="account_id, id" /> | Deletes a user. Deleting a user from a Databricks account also removes objects associated with the user. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="account_id, id" /> | Partially updates a user resource by applying the supplied operations on specific user attributes. |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="account_id, id" /> | Replaces a user's information with the data supplied in request. |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'users (list)', value: 'list' },
        { label: 'users (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
id,
name,
active,
displayName,
emails,
externalId,
roles,
userName
FROM databricks_account.iam.users
WHERE account_id = '{{ account_id }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
id,
name,
active,
displayName,
emails,
externalId,
roles,
userName
FROM databricks_account.iam.users
WHERE account_id = '{{ account_id }}' AND
id = '{{ id }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>users</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'users', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_account.iam.users (
account_id,
data__userName,
data__emails,
data__name,
data__displayName,
data__roles,
data__externalId,
data__active
)
SELECT 
'{{ account_id }}',
'{{ userName }}',
'{{ emails }}',
'{{ name }}',
'{{ displayName }}',
'{{ roles }}',
'{{ externalId }}',
'{{ active }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: userName
    value: user@example.com
  - name: emails
    value:
    - $ref: string
      value: string
      display: string
      primary: true
      type: string
  - name: name
    value:
      givenName: string
      familyName: string
  - name: displayName
    value: string
  - name: roles
    value:
    - $ref: string
      value: string
      display: string
      primary: true
      type: string
  - name: externalId
    value: string
  - name: active
    value: true

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>users</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update        
UPDATE databricks_account.iam.users
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE account_id = '{{ account_id }}' AND
id = '{{ id }}';
```

## `REPLACE` example

Replaces a <code>users</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update
REPLACE databricks_account.iam.users
SET field1 = '{ value1 }',
field2 = '{ value2 }', ...
WHERE account_id = '{{ account_id }}' AND
id = '{{ id }}';
```

## `DELETE` example

Deletes a <code>users</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_account.iam.users
WHERE account_id = '{{ account_id }}' AND
id = '{{ id }}';
```
