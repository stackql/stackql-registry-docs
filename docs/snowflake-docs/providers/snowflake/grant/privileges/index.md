---
title: privileges
hide_title: false
hide_table_of_contents: false
keywords:
  - privileges
  - grant
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

Creates, updates, deletes, gets or lists a <code>privileges</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>privileges</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.grant.privileges" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Optional Params | Description |
|:-----|:--------------|:----------------|:----------------|:------------|
| <CopyableCode code="grant_group_privilege" /> | `INSERT` | <CopyableCode code="bulkGrantType, granteeName, granteeType, scopeName, scopeType, securableTypePlural, endpoint" /> | - | Endpoint to indicate that the privileges listed in the request body should be granted to all securables of this type in the given scope. |
| <CopyableCode code="grant_privilege" /> | `INSERT` | <CopyableCode code="granteeName, granteeType, securableName, securableType, endpoint" /> | - | Endpoint to indicate that the privileges listed in the request body should be granted. |
| <CopyableCode code="revoke_group_privilege" /> | `DELETE` | <CopyableCode code="bulkGrantType, granteeName, granteeType, privilege, scopeName, scopeType, securableTypePlural, endpoint" /> | <CopyableCode code="deleteMode" /> | Endpoint to indicate that the privilege listed on the group securable in the given scope should be revoked. |
| <CopyableCode code="revoke_privilege" /> | `DELETE` | <CopyableCode code="granteeName, granteeType, privilege, securableName, securableType, endpoint" /> | <CopyableCode code="deleteMode" /> | Endpoint to indicate that the privilege listed in the path should be revoked. |

<br />


<details>
<summary>Optional Parameter Details</summary>

| Name | Description | Type | Default |
|------|-------------|------|---------|
| <CopyableCode code="deleteMode" /> | If "cascade", recursively revoke the grant from sub-grantees to which this privilege was re-granted. Acceptable values are "restrict" or "cascade". | `string` | `-` |

</details>

## `INSERT` example

Endpoint to indicate that the privileges listed in the request body should be granted.

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
INSERT INTO snowflake.grant.privileges (
data__privileges,
data__grant_option,
data__created_on,
data__grantee_type,
data__grantee_name,
data__securable_type,
data__securable_name,
data__granted_by_role_type,
data__granted_by_name,
granteeName,
granteeType,
securableName,
securableType,
endpoint
)
SELECT 
'{{ privileges }}',
{{ grant_option }},
'{{ created_on }}',
'{{ grantee_type }}',
'{{ grantee_name }}',
'{{ securable_type }}',
'{{ securable_name }}',
'{{ granted_by_role_type }}',
'{{ granted_by_name }}',
'{{ granteeName }}',
'{{ granteeType }}',
'{{ securableName }}',
'{{ securableType }}',
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO snowflake.grant.privileges (
granteeName,
granteeType,
securableName,
securableType,
endpoint
)
SELECT 
'{{ granteeName }}',
'{{ granteeType }}',
'{{ securableName }}',
'{{ securableType }}',
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
# Description fields below are for documentation purposes only and are not required in the manifest
- name: privileges
  props:
    - name: granteeName
      value: string
      description: Required parameter for the privileges resource.
    - name: granteeType
      value: string
      description: Required parameter for the privileges resource.
    - name: securableName
      value: string
      description: Required parameter for the privileges resource.
    - name: securableType
      value: string
      description: Required parameter for the privileges resource.
    - name: endpoint
      value: string
      description: Required parameter for the privileges resource.
    - name: privileges
      value: array
      description: Privilege type
    - name: grant_option
      value: boolean
      description: Can grantee pass this privilege down?
    - name: created_on
      value: string
    - name: grantee_type
      value: string
      description: Entity type being granted to
    - name: grantee_name
      value: string
      description: Specific name of object being granted to
    - name: securable_type
      value: string
      description: Type of object granted on
    - name: securable_name
      value: string
      description: Name of specific object granted on (not name of privilege!)
    - name: granted_by_role_type
      value: string
      description: Type of role that granted this privilege to this grantee
    - name: granted_by_name
      value: string
      description: The role that granted this privilege to this grantee
```
</TabItem>
</Tabs>

## `DELETE` example

Endpoint to indicate that the privilege listed in the path should be revoked.

```sql
/*+ delete */
DELETE FROM snowflake.grant.privileges
WHERE granteeName = '{{ granteeName }}'
AND granteeType = '{{ granteeType }}'
AND privilege = '{{ privilege }}'
AND securableName = '{{ securableName }}'
AND securableType = '{{ securableType }}'
AND endpoint = '{{ endpoint }}';
```
