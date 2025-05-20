---
title: database_roles
hide_title: false
hide_table_of_contents: false
keywords:
  - database_roles
  - database_role
  - snowflake
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage snowflake resources using SQL
custom_edit_url: null
image: /img/providers/snowflake/stackql-snowflake-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>database_roles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>database_roles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.database_role.database_roles" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the database role |
| <CopyableCode code="comment" /> | `string` | User comment associated to an object in the dictionary |
| <CopyableCode code="created_on" /> | `string` | Date and time when the database role was created |
| <CopyableCode code="granted_database_roles" /> | `integer` | How many database roles this database role has been granted |
| <CopyableCode code="granted_to_database_roles" /> | `integer` | How many database roles this database role has been granted to |
| <CopyableCode code="granted_to_roles" /> | `integer` | How many roles this database role has been granted to |
| <CopyableCode code="owner" /> | `string` | Role that owns the database role |
| <CopyableCode code="owner_role_type" /> | `string` | The type of role that owns the database role |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_database_roles" /> | `SELECT` | <CopyableCode code="database, endpoint" /> | List database roles |
| <CopyableCode code="create_database_role" /> | `INSERT` | <CopyableCode code="database, data__name, endpoint" /> | Create a database role |
| <CopyableCode code="delete_database_role" /> | `DELETE` | <CopyableCode code="database, name, endpoint" /> | Delete a database role |
| <CopyableCode code="clone_database_role" /> | `EXEC` | <CopyableCode code="database, name, data__name, endpoint" /> | Create a new database role by cloning from the specified resource |

## `SELECT` examples

List database roles


```sql
SELECT
name,
comment,
created_on,
granted_database_roles,
granted_to_database_roles,
granted_to_roles,
owner,
owner_role_type
FROM snowflake.database_role.database_roles
WHERE database = '{{ database }}' AND endpoint = '{{ endpoint }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>database_roles</code> resource.

<Tabs     defaultValue="all"    values={[        { label: 'All Properties', value: 'all' }, { label: 'Manifest', value: 'manifest' }    ]}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO snowflake.database_role.database_roles (
data__name,
endpoint,
database
)
SELECT 
'{ endpoint }',
'{ name }',
'{ database }'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: database_roles
  props:
  - name: database
    value: string
  - name: data__name
    value: string
  - name: endpoint
    value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>database_roles</code> resource.

```sql
/*+ delete */
DELETE FROM snowflake.database_role.database_roles
WHERE database = '{ database }' AND name = '{ name }' AND endpoint = '{ endpoint }';
```
