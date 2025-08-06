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

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods

The following methods are available for this resource:

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
    <th>Optional Params</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><a href="#grant_privilege"><CopyableCode code="grant_privilege" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-granteeType">granteeType</a>, <a href="#parameter-granteeName">granteeName</a>, <a href="#parameter-securableType">securableType</a>, <a href="#parameter-securableName">securableName</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td></td>
    <td>Endpoint to indicate that the privileges listed in the request body should be granted.</td>
</tr>
<tr>
    <td><a href="#grant_group_privilege"><CopyableCode code="grant_group_privilege" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-granteeType">granteeType</a>, <a href="#parameter-granteeName">granteeName</a>, <a href="#parameter-bulkGrantType">bulkGrantType</a>, <a href="#parameter-securableTypePlural">securableTypePlural</a>, <a href="#parameter-scopeType">scopeType</a>, <a href="#parameter-scopeName">scopeName</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td></td>
    <td>Endpoint to indicate that the privileges listed in the request body should be granted to all securables of this type in the given scope.</td>
</tr>
<tr>
    <td><a href="#revoke_privilege"><CopyableCode code="revoke_privilege" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-granteeType">granteeType</a>, <a href="#parameter-granteeName">granteeName</a>, <a href="#parameter-securableType">securableType</a>, <a href="#parameter-securableName">securableName</a>, <a href="#parameter-privilege">privilege</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-deleteMode">deleteMode</a></td>
    <td>Endpoint to indicate that the privilege listed in the path should be revoked.</td>
</tr>
<tr>
    <td><a href="#revoke_group_privilege"><CopyableCode code="revoke_group_privilege" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-granteeType">granteeType</a>, <a href="#parameter-granteeName">granteeName</a>, <a href="#parameter-bulkGrantType">bulkGrantType</a>, <a href="#parameter-securableTypePlural">securableTypePlural</a>, <a href="#parameter-scopeType">scopeType</a>, <a href="#parameter-scopeName">scopeName</a>, <a href="#parameter-privilege">privilege</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-deleteMode">deleteMode</a></td>
    <td>Endpoint to indicate that the privilege listed on the group securable in the given scope should be revoked.</td>
</tr>
</tbody>
</table>## Parameters

Parameters can be passed in the `WHERE` clause of a query. Check the [Methods](#methods) section to see which parameters are required or optional for each operation.

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr id="parameter-bulkGrantType">
    <td><CopyableCode code="bulkGrantType" /></td>
    <td><code>string</code></td>
    <td>String that species whether this group privilege should be on ALL or FUTURE resources of the specified plural type (example: all, enum: [all, future])</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>Organization and Account Name (default: orgid-acctid)</td>
</tr>
<tr id="parameter-granteeName">
    <td><CopyableCode code="granteeName" /></td>
    <td><code>string</code></td>
    <td>String that specifies the name of the privilege grantee. (example: SYSADMIN)</td>
</tr>
<tr id="parameter-granteeType">
    <td><CopyableCode code="granteeType" /></td>
    <td><code>string</code></td>
    <td>String that specifies the type of resource that is the privilege grantee. (example: role, enum: [user, role, application-role, database-role, share])</td>
</tr>
<tr id="parameter-privilege">
    <td><CopyableCode code="privilege" /></td>
    <td><code>string</code></td>
    <td>String that specifies a privilege to be revoked (example: SELECT)</td>
</tr>
<tr id="parameter-scopeName">
    <td><CopyableCode code="scopeName" /></td>
    <td><code>string</code></td>
    <td>String that specifies the name of resource that is the scope of an ALL/FUTURE privilege (example: MY_DB.MY_SC)</td>
</tr>
<tr id="parameter-scopeType">
    <td><CopyableCode code="scopeType" /></td>
    <td><code>string</code></td>
    <td>String that specifies the type of resource that is the scope of an ALL/FUTURE privilege. Can only be DATABASE or SCHEMA (example: schema, enum: [database, schema])</td>
</tr>
<tr id="parameter-securableName">
    <td><CopyableCode code="securableName" /></td>
    <td><code>string</code></td>
    <td>String that specifies the name of resource that is being secured by a privilege. (example: MY_DB)</td>
</tr>
<tr id="parameter-securableType">
    <td><CopyableCode code="securableType" /></td>
    <td><code>string</code></td>
    <td>String that specifies the type of resource that is being secured by a privilege. (example: DATABASE)</td>
</tr>
<tr id="parameter-securableTypePlural">
    <td><CopyableCode code="securableTypePlural" /></td>
    <td><code>string</code></td>
    <td>String that specifies the plural of the type of resource that is being secured by an ALL/FUTURE privilege. Must be either "schemas" or any plural object type that can nest under a schema such as "tables" (example: tables)</td>
</tr>
<tr id="parameter-deleteMode">
    <td><CopyableCode code="deleteMode" /></td>
    <td><code>string</code></td>
    <td>If "cascade", recursively revoke the grant from sub-grantees to which this privilege was re-granted. Acceptable values are "restrict" or "cascade". (example: restrict)</td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="grant_privilege"
    values={[
        { label: 'grant_privilege', value: 'grant_privilege' },
        { label: 'grant_group_privilege', value: 'grant_group_privilege' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="grant_privilege">

Endpoint to indicate that the privileges listed in the request body should be granted.

```sql
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
granteeType,
granteeName,
securableType,
securableName,
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
'{{ granteeType }}',
'{{ granteeName }}',
'{{ securableType }}',
'{{ securableName }}',
'{{ endpoint }}'
;
```
</TabItem>
<TabItem value="grant_group_privilege">

Endpoint to indicate that the privileges listed in the request body should be granted to all securables of this type in the given scope.

```sql
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
granteeType,
granteeName,
bulkGrantType,
securableTypePlural,
scopeType,
scopeName,
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
'{{ granteeType }}',
'{{ granteeName }}',
'{{ bulkGrantType }}',
'{{ securableTypePlural }}',
'{{ scopeType }}',
'{{ scopeName }}',
'{{ endpoint }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: privileges
  props:
    - name: granteeType
      value: string
      description: Required parameter for the privileges resource.
    - name: granteeName
      value: string
      description: Required parameter for the privileges resource.
    - name: securableType
      value: string
      description: Required parameter for the privileges resource.
    - name: securableName
      value: string
      description: Required parameter for the privileges resource.
    - name: endpoint
      value: string
      description: Required parameter for the privileges resource.
    - name: bulkGrantType
      value: string
      description: Required parameter for the privileges resource.
    - name: securableTypePlural
      value: string
      description: Required parameter for the privileges resource.
    - name: scopeType
      value: string
      description: Required parameter for the privileges resource.
    - name: scopeName
      value: string
      description: Required parameter for the privileges resource.
    - name: privileges
      value: array
      description: >
        Privilege type
        
    - name: grant_option
      value: boolean
      description: >
        Can grantee pass this privilege down?
        
    - name: created_on
      value: string
    - name: grantee_type
      value: string
      description: >
        Entity type being granted to
        
    - name: grantee_name
      value: string
      description: >
        Specific name of object being granted to
        
    - name: securable_type
      value: string
      description: >
        Type of object granted on
        
    - name: securable_name
      value: string
      description: >
        Name of specific object granted on (not name of privilege!)
        
    - name: granted_by_role_type
      value: string
      description: >
        Type of role that granted this privilege to this grantee
        
    - name: granted_by_name
      value: string
      description: >
        The role that granted this privilege to this grantee
        
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="revoke_privilege"
    values={[
        { label: 'revoke_privilege', value: 'revoke_privilege' },
        { label: 'revoke_group_privilege', value: 'revoke_group_privilege' }
    ]}
>
<TabItem value="revoke_privilege">

Endpoint to indicate that the privilege listed in the path should be revoked.

```sql
DELETE FROM snowflake.grant.privileges
WHERE granteeType = '{{ granteeType }}' --required
AND granteeName = '{{ granteeName }}' --required
AND securableType = '{{ securableType }}' --required
AND securableName = '{{ securableName }}' --required
AND privilege = '{{ privilege }}' --required
AND endpoint = '{{ endpoint }}' --required
AND deleteMode = '{{ deleteMode }}';
```
</TabItem>
<TabItem value="revoke_group_privilege">

Endpoint to indicate that the privilege listed on the group securable in the given scope should be revoked.

```sql
DELETE FROM snowflake.grant.privileges
WHERE granteeType = '{{ granteeType }}' --required
AND granteeName = '{{ granteeName }}' --required
AND bulkGrantType = '{{ bulkGrantType }}' --required
AND securableTypePlural = '{{ securableTypePlural }}' --required
AND scopeType = '{{ scopeType }}' --required
AND scopeName = '{{ scopeName }}' --required
AND privilege = '{{ privilege }}' --required
AND endpoint = '{{ endpoint }}' --required
AND deleteMode = '{{ deleteMode }}';
```
</TabItem>
</Tabs>
