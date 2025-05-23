---
title: grants
hide_title: false
hide_table_of_contents: false
keywords:
  - grants
  - role
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
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.role.grants" /></td></tr>
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
| Name | Accessible by | Required Params | Optional Params | Description |
|:-----|:--------------|:----------------|:----------------|:------------|
| <CopyableCode code="list_grants" /> | `SELECT` | <CopyableCode code="name, endpoint" /> | <CopyableCode code="showLimit" /> | List all grants to the role |
| <CopyableCode code="grant_privileges" /> | `INSERT` | <CopyableCode code="name, data__securable_type, endpoint" /> | - | Grant privileges to the role |
| <CopyableCode code="revoke_grants" /> | `DELETE` | <CopyableCode code="name, data__securable_type, endpoint" /> | <CopyableCode code="mode" /> | Revoke grants from the role |

<br />


<details>
<summary>Optional Parameter Details</summary>

| Name | Description | Type | Default |
|------|-------------|------|---------|
| <CopyableCode code="mode" /> | Query parameter determines whether the revoke operation succeeds or fails for the privileges, based on the whether the privileges had been re-granted to another role. - restrict: If the privilege being revoked has been re-granted to another role, the REVOKE command fails. - cascade: If the privilege being revoked has been re-granted, the REVOKE command recursively revokes these dependent grants. If the same privilege on an object has been granted to the target role by a different grantor (parallel grant), that grant is not affected and the target role retains the privilege. | `string` | `-` |
| <CopyableCode code="showLimit" /> | Query parameter to limit the maximum number of rows returned by a command. | `integer` | `-` |

</details>

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
FROM snowflake.role.grants
WHERE name = '{{ name }}'
AND endpoint = '{{ endpoint }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>grants</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'Required Properties', value: 'required' },
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO snowflake.role.grants (
data__securable,
data__containing_scope,
data__securable_type,
data__grant_option,
data__privileges,
name,
endpoint
)
SELECT 
'{{ securable }}',
'{{ containing_scope }}',
'{{ securable_type }}',
'{{ grant_option }}',
'{{ privileges }}',
'{{ name }}',
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO snowflake.role.grants (
data__securable_type,
name,
endpoint
)
SELECT 
'{{ securable_type }}',
'{{ name }}',
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: grants
  props:
    - name: name
      value: string
    - name: data__securable_type
      value: string
    - name: endpoint
      value: string
    - name: securable
      value:
        - name: database
          value: string
        - name: schema
          value: string
        - name: service
          value: string
        - name: name
          value: string
    - name: containing_scope
      value:
        - name: database
          value: string
        - name: schema
          value: string
    - name: securable_type
      value: string
    - name: grant_option
      value: boolean
    - name: privileges
      value: array

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>grants</code> resource.

```sql
/*+ delete */
DELETE FROM snowflake.role.grants
WHERE name = '{{ name }}'
AND data__securable_type = '{{ data__securable_type }}'
AND endpoint = '{{ endpoint }}';
```
