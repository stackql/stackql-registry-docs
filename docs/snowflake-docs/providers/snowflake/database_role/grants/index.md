---
title: grants
hide_title: false
hide_table_of_contents: false
keywords:
  - grants
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

Creates, updates, deletes, gets or lists a <code>grants</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>grants</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.database_role.grants" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="containing_scope" /> | `object` |  |
| <CopyableCode code="created_on" /> | `string` | Date and time when the grant was created |
| <CopyableCode code="grant_option" /> | `boolean` | If true, allows the recipient role to grant the privileges to other roles. |
| <CopyableCode code="granted_by" /> | `string` | The role that granted this privilege to this grantee |
| <CopyableCode code="privileges" /> | `array` | List of privileges to be granted. |
| <CopyableCode code="securable" /> | `object` |  |
| <CopyableCode code="securable_type" /> | `string` | Type of the securable to be granted. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_grants" /> | `SELECT` | <CopyableCode code="database, name, endpoint" /> | List all grants to the role |
| <CopyableCode code="grant_privileges" /> | `INSERT` | <CopyableCode code="database, name, data__securable_type, endpoint" /> | Grant privileges to the role |
| <CopyableCode code="revoke_grants" /> | `DELETE` | <CopyableCode code="database, name, data__securable_type, endpoint" /> | Revoke grants from the role |

## `SELECT` examples

List all grants to the role


```sql
SELECT
containing_scope,
created_on,
grant_option,
granted_by,
privileges,
securable,
securable_type
FROM snowflake.database_role.grants
WHERE database = '{{ database }}' AND name = '{{ name }}' AND endpoint = '{{ endpoint }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>grants</code> resource.

<Tabs     defaultValue="all"    values={[        { label: 'All Properties', value: 'all' }, { label: 'Manifest', value: 'manifest' }    ]}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO snowflake.database_role.grants (
name,
data__securable_type,
endpoint,
database
)
SELECT 
'{ database }',
'{ name }',
'{ securable_type }',
'{ endpoint }'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: grants
  props:
  - name: database
    value: string
  - name: name
    value: string
  - name: data__securable_type
    value: string
  - name: endpoint
    value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>grants</code> resource.

```sql
/*+ delete */
DELETE FROM snowflake.database_role.grants
WHERE database = '{ database }' AND name = '{ name }' AND data__securable_type = '{ data__securable_type }' AND endpoint = '{ endpoint }';
```
