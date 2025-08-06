--- 
title: grants_on
hide_title: false
hide_table_of_contents: false
keywords:
  - grants_on
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

Creates, updates, deletes, gets or lists a <code>grants_on</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>grants_on</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.role.grants_on" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_grants_on"
    values={[
        { label: 'list_grants_on', value: 'list_grants_on' }
    ]}
>
<TabItem value="list_grants_on">

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the role</td>
</tr>
<tr>
    <td><CopyableCode code="grantee_name" /></td>
    <td><code>string</code></td>
    <td>The name of the grantee</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the grant was created</td>
</tr>
<tr>
    <td><CopyableCode code="grant_option" /></td>
    <td><code>string</code></td>
    <td>If true, allows the recipient role to grant the privileges to other roles.</td>
</tr>
<tr>
    <td><CopyableCode code="granted_by" /></td>
    <td><code>string</code></td>
    <td>The role that granted this privilege to this grantee</td>
</tr>
<tr>
    <td><CopyableCode code="granted_by_role_type" /></td>
    <td><code>string</code></td>
    <td>Type of the role that granted this privilege to this grantee</td>
</tr>
<tr>
    <td><CopyableCode code="granted_on" /></td>
    <td><code>string</code></td>
    <td>The type of of the role</td>
</tr>
<tr>
    <td><CopyableCode code="granted_to" /></td>
    <td><code>string</code></td>
    <td>The type of the grantee</td>
</tr>
<tr>
    <td><CopyableCode code="privilege" /></td>
    <td><code>string</code></td>
    <td>The name of the privilege</td>
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
    <td><a href="#list_grants_on"><CopyableCode code="list_grants_on" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-showLimit">showLimit</a></td>
    <td>List all grants on the role</td>
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
<tr id="parameter-showLimit">
    <td><CopyableCode code="showLimit" /></td>
    <td><code>integer</code></td>
    <td>Query parameter to limit the maximum number of rows returned by a command. (example: 10, minimum: 1, maximum: 10000)</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_grants_on"
    values={[
        { label: 'list_grants_on', value: 'list_grants_on' }
    ]}
>
<TabItem value="list_grants_on">

List all grants on the role

```sql
SELECT
name,
grantee_name,
created_on,
grant_option,
granted_by,
granted_by_role_type,
granted_on,
granted_to,
privilege
FROM snowflake.role.grants_on
WHERE name = '{{ name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND showLimit = '{{ showLimit }}';
```
</TabItem>
</Tabs>
