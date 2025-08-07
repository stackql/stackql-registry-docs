--- 
title: grants_to
hide_title: false
hide_table_of_contents: false
keywords:
  - grants_to
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

Creates, updates, deletes, gets or lists a <code>grants_to</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>grants_to</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.grant.grants_to" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_grants_to"
    values={[
        { label: 'list_grants_to', value: 'list_grants_to' }
    ]}
>
<TabItem value="list_grants_to">

Properties of a grant that can be granted to a role or user.

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
    <td><CopyableCode code="granted_by_name" /></td>
    <td><code>string</code></td>
    <td>The role that granted this privilege to this grantee (example: SUBADMIN)</td>
</tr>
<tr>
    <td><CopyableCode code="grantee_name" /></td>
    <td><code>string</code></td>
    <td>Specific name of object being granted to (example: ACCOUNTADMIN)</td>
</tr>
<tr>
    <td><CopyableCode code="securable_name" /></td>
    <td><code>string</code></td>
    <td>Name of specific object granted on (not name of privilege!)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="grant_option" /></td>
    <td><code>boolean</code></td>
    <td>Can grantee pass this privilege down?</td>
</tr>
<tr>
    <td><CopyableCode code="granted_by_role_type" /></td>
    <td><code>string</code></td>
    <td>Type of role that granted this privilege to this grantee (example: ROLE)</td>
</tr>
<tr>
    <td><CopyableCode code="grantee_type" /></td>
    <td><code>string</code></td>
    <td>Entity type being granted to (example: ROLE)</td>
</tr>
<tr>
    <td><CopyableCode code="privileges" /></td>
    <td><code>array</code></td>
    <td>Privilege type</td>
</tr>
<tr>
    <td><CopyableCode code="securable_type" /></td>
    <td><code>string</code></td>
    <td>Type of object granted on (example: ACCOUNT)</td>
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
    <td><a href="#list_grants_to"><CopyableCode code="list_grants_to" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-granteeType"><code>granteeType</code></a>, <a href="#parameter-granteeName"><code>granteeName</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-showLimit"><code>showLimit</code></a></td>
    <td>List the roles and privileges granted to the specified grantee using the output of SHOW GRANTS TO</td>
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
<tr id="parameter-granteeName">
    <td><CopyableCode code="granteeName" /></td>
    <td><code>string</code></td>
    <td>String that specifies the name of the privilege grantee.</td>
</tr>
<tr id="parameter-granteeType">
    <td><CopyableCode code="granteeType" /></td>
    <td><code>string</code></td>
    <td>String that specifies the type of resource that is the privilege grantee.</td>
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
    defaultValue="list_grants_to"
    values={[
        { label: 'list_grants_to', value: 'list_grants_to' }
    ]}
>
<TabItem value="list_grants_to">

List the roles and privileges granted to the specified grantee using the output of SHOW GRANTS TO

```sql
SELECT
granted_by_name,
grantee_name,
securable_name,
created_on,
grant_option,
granted_by_role_type,
grantee_type,
privileges,
securable_type
FROM snowflake.grant.grants_to
WHERE granteeType = '{{ granteeType }}' -- required
AND granteeName = '{{ granteeName }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND showLimit = '{{ showLimit }}';
```
</TabItem>
</Tabs>
