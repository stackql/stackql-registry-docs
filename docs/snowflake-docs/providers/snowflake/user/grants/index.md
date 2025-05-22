---
title: grants
hide_title: false
hide_table_of_contents: false
keywords:
  - grants
  - user
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
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.user.grants" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="containing_scope" /> | `object` |  |
| <CopyableCode code="created_on" /> | `string` | Date and time when the grant was created |
| <CopyableCode code="granted_by" /> | `string` | The role that granted this privilege to this grantee |
| <CopyableCode code="privileges" /> | `array` | List of privileges to be granted. |
| <CopyableCode code="securable" /> | `object` |  |
| <CopyableCode code="securable_type" /> | `string` | Type of the securable to be granted. Only ROLE is supported |

## Methods
| Name | Accessible by | Required Params | Optional Params | Description |
|:-----|:--------------|:----------------|:----------------|:------------|
| <CopyableCode code="list_grants" /> | `SELECT` | <CopyableCode code="name, endpoint" /> | <CopyableCode code="showLimit" /> | List all grants to the user |
| <CopyableCode code="grant" /> | `INSERT` | <CopyableCode code="name, data__securable_type, endpoint" /> | - | Grant a role to the user |
| <CopyableCode code="revoke_grants" /> | `DELETE` | <CopyableCode code="name, data__securable_type, endpoint" /> | - | Revoke grants from the user |
<br />

<details>
<summary>Optional Parameter Details</summary>

| Name | Description | Type | Default |
|------|-------------|------|---------|
| <CopyableCode code="showLimit" /> | Query parameter to limit the maximum number of rows returned by a command. | `integer` | `-` |

</details>

## `SELECT` examples

List all grants to the user


```sql
SELECT
containing_scope,
created_on,
granted_by,
privileges,
securable,
securable_type
FROM snowflake.user.grants
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
INSERT INTO snowflake.user.grants (
data__securable,
data__containing_scope,
data__securable_type,
data__privileges,
name,
endpoint
)
SELECT 
'{{ securable }}',
'{{ containing_scope }}',
'{{ securable_type }}',
'{{ privileges }}',
'{{ name }}',
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO snowflake.user.grants (
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
      props:
        - name: database
          value: string
        - name: schema
          value: string
        - name: name
          value: string
    - name: containing_scope
      props:
        - name: database
          value: string
        - name: schema
          value: string
    - name: securable_type
      value: string
    - name: privileges
      value: array

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>grants</code> resource.

```sql
/*+ delete */
DELETE FROM snowflake.user.grants
WHERE name = '{{ name }}'
AND data__securable_type = '{{ data__securable_type }}'
AND endpoint = '{{ endpoint }}';
```
