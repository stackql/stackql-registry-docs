--- 
title: network_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - network_policies
  - network_policy
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

Creates, updates, deletes, gets or lists a <code>network_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.network_policy.network_policies" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_network_policies"
    values={[
        { label: 'list_network_policies', value: 'list_network_policies' },
        { label: 'fetch_network_policy', value: 'fetch_network_policy' }
    ]}
>
<TabItem value="list_network_policies">

A Snowflake network policy

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the network policy (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr>
    <td><CopyableCode code="allowed_ip_list" /></td>
    <td><code>array</code></td>
    <td>List of allowed IPs in a network policy</td>
</tr>
<tr>
    <td><CopyableCode code="allowed_network_rule_list" /></td>
    <td><code>array</code></td>
    <td>List of names of allowed network rules in a network policy</td>
</tr>
<tr>
    <td><CopyableCode code="blocked_ip_list" /></td>
    <td><code>array</code></td>
    <td>List of blocked IPs in a network policy</td>
</tr>
<tr>
    <td><CopyableCode code="blocked_network_rule_list" /></td>
    <td><code>array</code></td>
    <td>List of names of blocked network rules in a network policy</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>user comment associated to an object in the dictionary</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the network policy was created.</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td>Role that owns the network policy (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr>
    <td><CopyableCode code="owner_role_type" /></td>
    <td><code>string</code></td>
    <td>The type of role that owns the network policy (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="fetch_network_policy">

A Snowflake network policy

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the network policy (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr>
    <td><CopyableCode code="allowed_ip_list" /></td>
    <td><code>array</code></td>
    <td>List of allowed IPs in a network policy</td>
</tr>
<tr>
    <td><CopyableCode code="allowed_network_rule_list" /></td>
    <td><code>array</code></td>
    <td>List of names of allowed network rules in a network policy</td>
</tr>
<tr>
    <td><CopyableCode code="blocked_ip_list" /></td>
    <td><code>array</code></td>
    <td>List of blocked IPs in a network policy</td>
</tr>
<tr>
    <td><CopyableCode code="blocked_network_rule_list" /></td>
    <td><code>array</code></td>
    <td>List of names of blocked network rules in a network policy</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>user comment associated to an object in the dictionary</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the network policy was created.</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td>Role that owns the network policy (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr>
    <td><CopyableCode code="owner_role_type" /></td>
    <td><code>string</code></td>
    <td>The type of role that owns the network policy (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
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
    <td><a href="#list_network_policies"><CopyableCode code="list_network_policies" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint">endpoint</a></td>
    <td></td>
    <td>List network policies</td>
</tr>
<tr>
    <td><a href="#fetch_network_policy"><CopyableCode code="fetch_network_policy" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td></td>
    <td>Fetch a network policy</td>
</tr>
<tr>
    <td><a href="#create_network_policy"><CopyableCode code="create_network_policy" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-createMode">createMode</a></td>
    <td>Create a network policy</td>
</tr>
<tr>
    <td><a href="#delete_network_policy"><CopyableCode code="delete_network_policy" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-ifExists">ifExists</a></td>
    <td>Delete a network policy</td>
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
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>Organization and Account Name (default: orgid-acctid)</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Identifier (i.e. name) for the resource. (pattern: ^"([^"]|"")+"|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
<tr id="parameter-createMode">
    <td><CopyableCode code="createMode" /></td>
    <td><code>string</code></td>
    <td>Query parameter allowing support for different modes of resource creation. Possible values include: - `errorIfExists`: Throws an error if you try to create a resource that already exists. - `orReplace`: Automatically replaces the existing resource with the current one. - `ifNotExists`: Creates a new resource when an alter is requested for a non-existent resource. (enum: [errorIfExists, orReplace, ifNotExists], example: ifNotExists, default: errorIfExists)</td>
</tr>
<tr id="parameter-ifExists">
    <td><CopyableCode code="ifExists" /></td>
    <td><code>boolean</code></td>
    <td>Query parameter that specifies how to handle the request for a resource that does not exist: - `true`: The endpoint does not throw an error if the resource does not exist. It returns a 200 success response, but does not take any action on the resource. - `false`: The endpoint throws an error if the resource doesn't exist. (example: true, default: false)</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_network_policies"
    values={[
        { label: 'list_network_policies', value: 'list_network_policies' },
        { label: 'fetch_network_policy', value: 'fetch_network_policy' }
    ]}
>
<TabItem value="list_network_policies">

List network policies

```sql
SELECT
name,
allowed_ip_list,
allowed_network_rule_list,
blocked_ip_list,
blocked_network_rule_list,
comment,
created_on,
owner,
owner_role_type
FROM snowflake.network_policy.network_policies
WHERE endpoint = '{{ endpoint }}' -- required;
```
</TabItem>
<TabItem value="fetch_network_policy">

Fetch a network policy

```sql
SELECT
name,
allowed_ip_list,
allowed_network_rule_list,
blocked_ip_list,
blocked_network_rule_list,
comment,
created_on,
owner,
owner_role_type
FROM snowflake.network_policy.network_policies
WHERE name = '{{ name }}' -- required
AND endpoint = '{{ endpoint }}' -- required;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_network_policy"
    values={[
        { label: 'create_network_policy', value: 'create_network_policy' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_network_policy">

Create a network policy

```sql
INSERT INTO snowflake.network_policy.network_policies (
data__name,
data__allowed_network_rule_list,
data__blocked_network_rule_list,
data__allowed_ip_list,
data__blocked_ip_list,
data__comment,
endpoint,
createMode
)
SELECT 
'{{ name }}',
'{{ allowed_network_rule_list }}',
'{{ blocked_network_rule_list }}',
'{{ allowed_ip_list }}',
'{{ blocked_ip_list }}',
'{{ comment }}',
'{{ endpoint }}',
'{{ createMode }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: network_policies
  props:
    - name: endpoint
      value: string
      description: Required parameter for the network_policies resource.
    - name: name
      value: string
      description: >
        Name of the network policy
        
    - name: allowed_network_rule_list
      value: array
      description: >
        List of names of allowed network rules in a network policy
        
    - name: blocked_network_rule_list
      value: array
      description: >
        List of names of blocked network rules in a network policy
        
    - name: allowed_ip_list
      value: array
      description: >
        List of allowed IPs in a network policy
        
    - name: blocked_ip_list
      value: array
      description: >
        List of blocked IPs in a network policy
        
    - name: comment
      value: string
      description: >
        user comment associated to an object in the dictionary
        
    - name: createMode
      value: string
      description: Query parameter allowing support for different modes of resource creation. Possible values include: - `errorIfExists`: Throws an error if you try to create a resource that already exists. - `orReplace`: Automatically replaces the existing resource with the current one. - `ifNotExists`: Creates a new resource when an alter is requested for a non-existent resource. (enum: [errorIfExists, orReplace, ifNotExists], example: ifNotExists, default: errorIfExists)
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_network_policy"
    values={[
        { label: 'delete_network_policy', value: 'delete_network_policy' }
    ]}
>
<TabItem value="delete_network_policy">

Delete a network policy

```sql
DELETE FROM snowflake.network_policy.network_policies
WHERE name = '{{ name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND ifExists = '{{ ifExists }}';
```
</TabItem>
</Tabs>
