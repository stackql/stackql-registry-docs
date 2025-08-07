--- 
title: future_grants
hide_title: false
hide_table_of_contents: false
keywords:
  - future_grants
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

Creates, updates, deletes, gets or lists a <code>future_grants</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>future_grants</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.database_role.future_grants" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_future_grants"
    values={[
        { label: 'list_future_grants', value: 'list_future_grants' }
    ]}
>
<TabItem value="list_future_grants">

successful

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="containing_scope" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the grant was created</td>
</tr>
<tr>
    <td><CopyableCode code="grant_option" /></td>
    <td><code>boolean</code></td>
    <td>If true, allows the recipient role to grant the privileges to other roles.</td>
</tr>
<tr>
    <td><CopyableCode code="granted_by" /></td>
    <td><code>string</code></td>
    <td>The role that granted this privilege to this grantee</td>
</tr>
<tr>
    <td><CopyableCode code="privileges" /></td>
    <td><code>array</code></td>
    <td>List of privileges to be granted.</td>
</tr>
<tr>
    <td><CopyableCode code="securable" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="securable_type" /></td>
    <td><code>string</code></td>
    <td>Type of the securable to be granted.</td>
</tr>
</tbody>
</table>
</TabItem>
</Tabs>

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
    <td><a href="#list_future_grants"><CopyableCode code="list_future_grants" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-showLimit"><code>showLimit</code></a></td>
    <td>List all future grants to the role</td>
</tr>
<tr>
    <td><a href="#grant_future_privileges"><CopyableCode code="grant_future_privileges" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Grant future privileges to the role</td>
</tr>
<tr>
    <td><a href="#revoke_future_grants"><CopyableCode code="revoke_future_grants" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-mode"><code>mode</code></a></td>
    <td>Revoke future grants from the role</td>
</tr>
</tbody>
</table>

## Parameters

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
<tr id="parameter-database_name">
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>Identifier (i.e. name) for the database to which the resource belongs. You can use the <code>/api/v2/databases</code> GET request to get a list of available databases.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>Organization and Account Name (default: orgid-acctid)</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Identifier (i.e. name) for the resource.</td>
</tr>
<tr id="parameter-mode">
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>Query parameter determines whether the revoke operation succeeds or fails for the privileges, based on the whether the privileges had been re-granted to another role. - restrict: If the privilege being revoked has been re-granted to another role, the REVOKE command fails. - cascade: If the privilege being revoked has been re-granted, the REVOKE command recursively revokes these dependent grants. If the same privilege on an object has been granted to the target role by a different grantor (parallel grant), that grant is not affected and the target role retains the privilege.</td>
</tr>
<tr id="parameter-showLimit">
    <td><CopyableCode code="showLimit" /></td>
    <td><code>integer</code></td>
    <td>Query parameter to limit the maximum number of rows returned by a command.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_future_grants"
    values={[
        { label: 'list_future_grants', value: 'list_future_grants' }
    ]}
>
<TabItem value="list_future_grants">

List all future grants to the role

```sql
SELECT
containing_scope,
created_on,
grant_option,
granted_by,
privileges,
securable,
securable_type
FROM snowflake.database_role.future_grants
WHERE database_name = '{{ database_name }}' -- required
AND name = '{{ name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND showLimit = '{{ showLimit }}';
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="grant_future_privileges"
    values={[
        { label: 'grant_future_privileges', value: 'grant_future_privileges' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="grant_future_privileges">

Grant future privileges to the role

```sql
INSERT INTO snowflake.database_role.future_grants (
data__securable,
data__containing_scope,
data__securable_type,
data__grant_option,
data__privileges,
database_name,
name,
endpoint
)
SELECT 
'{{ securable }}',
'{{ containing_scope }}',
'{{ securable_type }}',
{{ grant_option }},
'{{ privileges }}',
'{{ database_name }}',
'{{ name }}',
'{{ endpoint }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: future_grants
  props:
    - name: database_name
      value: string
      description: Required parameter for the future_grants resource.
    - name: name
      value: string
      description: Required parameter for the future_grants resource.
    - name: endpoint
      value: string
      description: Required parameter for the future_grants resource.
    - name: securable
      value: object
    - name: containing_scope
      value: object
    - name: securable_type
      value: string
      description: >
        Type of the securable to be granted.
        
    - name: grant_option
      value: boolean
      description: >
        If true, allows the recipient role to grant the privileges to other roles.
        
    - name: privileges
      value: array
      description: >
        List of privileges to be granted.
        
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="revoke_future_grants"
    values={[
        { label: 'revoke_future_grants', value: 'revoke_future_grants' }
    ]}
>
<TabItem value="revoke_future_grants">

Revoke future grants from the role

```sql
DELETE FROM snowflake.database_role.future_grants
WHERE database_name = '{{ database_name }}' --required
AND name = '{{ name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND mode = '{{ mode }}';
```
</TabItem>
</Tabs>
