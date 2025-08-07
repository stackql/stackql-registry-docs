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

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_grants"
    values={[
        { label: 'list_grants', value: 'list_grants' }
    ]}
>
<TabItem value="list_grants">

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
    <td>Type of the securable to be granted. Only ROLE is supported</td>
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
    <td><a href="#list_grants"><CopyableCode code="list_grants" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-showLimit"><code>showLimit</code></a></td>
    <td>List all grants to the user</td>
</tr>
<tr>
    <td><a href="#grant"><CopyableCode code="grant" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Grant a role to the user</td>
</tr>
<tr>
    <td><a href="#revoke_grants"><CopyableCode code="revoke_grants" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Revoke grants from the user</td>
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
<tr id="parameter-showLimit">
    <td><CopyableCode code="showLimit" /></td>
    <td><code>integer</code></td>
    <td>Query parameter to limit the maximum number of rows returned by a command.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_grants"
    values={[
        { label: 'list_grants', value: 'list_grants' }
    ]}
>
<TabItem value="list_grants">

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
WHERE name = '{{ name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND showLimit = '{{ showLimit }}';
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="grant"
    values={[
        { label: 'grant', value: 'grant' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="grant">

Grant a role to the user

```sql
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
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: grants
  props:
    - name: name
      value: string
      description: Required parameter for the grants resource.
    - name: endpoint
      value: string
      description: Required parameter for the grants resource.
    - name: securable
      value: object
    - name: containing_scope
      value: object
    - name: securable_type
      value: string
      description: >
        Type of the securable to be granted. Only ROLE is supported
        
    - name: privileges
      value: array
      description: >
        List of privileges to be granted.
        
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="revoke_grants"
    values={[
        { label: 'revoke_grants', value: 'revoke_grants' }
    ]}
>
<TabItem value="revoke_grants">

Revoke grants from the user

```sql
DELETE FROM snowflake.user.grants
WHERE name = '{{ name }}' --required
AND endpoint = '{{ endpoint }}' --required;
```
</TabItem>
</Tabs>
