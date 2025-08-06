--- 
title: api_integrations
hide_title: false
hide_table_of_contents: false
keywords:
  - api_integrations
  - api_integration
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

Creates, updates, deletes, gets or lists an <code>api_integrations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>api_integrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.api_integration.api_integrations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_api_integrations"
    values={[
        { label: 'list_api_integrations', value: 'list_api_integrations' },
        { label: 'fetch_api_integration', value: 'fetch_api_integration' }
    ]}
>
<TabItem value="list_api_integrations">

A Snowflake API integration object.

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
    <td>Name of the API integration. (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr>
    <td><CopyableCode code="api_allowed_prefixes" /></td>
    <td><code>array</code></td>
    <td>A comma-separated list of endpoints and resources that Snowflake can access.</td>
</tr>
<tr>
    <td><CopyableCode code="api_blocked_prefixes" /></td>
    <td><code>array</code></td>
    <td>A comma-separated list of endpoints and resources that are not allowed to be called from Snowflake.</td>
</tr>
<tr>
    <td><CopyableCode code="api_hook" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>Comment for the API integration.</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the API integration was created.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether the API integration is enabled.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="fetch_api_integration">

A Snowflake API integration object.

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
    <td>Name of the API integration. (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr>
    <td><CopyableCode code="api_allowed_prefixes" /></td>
    <td><code>array</code></td>
    <td>A comma-separated list of endpoints and resources that Snowflake can access.</td>
</tr>
<tr>
    <td><CopyableCode code="api_blocked_prefixes" /></td>
    <td><code>array</code></td>
    <td>A comma-separated list of endpoints and resources that are not allowed to be called from Snowflake.</td>
</tr>
<tr>
    <td><CopyableCode code="api_hook" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>Comment for the API integration.</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the API integration was created.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether the API integration is enabled.</td>
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
    <td><a href="#list_api_integrations"><CopyableCode code="list_api_integrations" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-like">like</a></td>
    <td>List API integrations</td>
</tr>
<tr>
    <td><a href="#fetch_api_integration"><CopyableCode code="fetch_api_integration" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td></td>
    <td>Fetch an API integration</td>
</tr>
<tr>
    <td><a href="#create_api_integration"><CopyableCode code="create_api_integration" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-createMode">createMode</a></td>
    <td>Create an API integration</td>
</tr>
<tr>
    <td><a href="#create_or_alter_api_integration"><CopyableCode code="create_or_alter_api_integration" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td></td>
    <td>Create an (or alter an existing) API integration. Note that API_KEY is not currently altered by this operation and is supported for a newly-created object only. Unsetting API_BLOCKED_PREFIXES is also unsupported.</td>
</tr>
<tr>
    <td><a href="#delete_api_integration"><CopyableCode code="delete_api_integration" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-ifExists">ifExists</a></td>
    <td>Delete an API integration</td>
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
    <td>Identifier (i.e. name) for the resource. (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
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
<tr id="parameter-like">
    <td><CopyableCode code="like" /></td>
    <td><code>string</code></td>
    <td>Query parameter to filter the command output by resource name. Uses case-insensitive pattern matching, with support for SQL wildcard characters. (example: test_%)</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_api_integrations"
    values={[
        { label: 'list_api_integrations', value: 'list_api_integrations' },
        { label: 'fetch_api_integration', value: 'fetch_api_integration' }
    ]}
>
<TabItem value="list_api_integrations">

List API integrations

```sql
SELECT
name,
api_allowed_prefixes,
api_blocked_prefixes,
api_hook,
comment,
created_on,
enabled
FROM snowflake.api_integration.api_integrations
WHERE endpoint = '{{ endpoint }}' -- required
AND like = '{{ like }}';
```
</TabItem>
<TabItem value="fetch_api_integration">

Fetch an API integration

```sql
SELECT
name,
api_allowed_prefixes,
api_blocked_prefixes,
api_hook,
comment,
created_on,
enabled
FROM snowflake.api_integration.api_integrations
WHERE name = '{{ name }}' -- required
AND endpoint = '{{ endpoint }}' -- required;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_api_integration"
    values={[
        { label: 'create_api_integration', value: 'create_api_integration' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_api_integration">

Create an API integration

```sql
INSERT INTO snowflake.api_integration.api_integrations (
data__name,
data__api_hook,
data__api_allowed_prefixes,
data__api_blocked_prefixes,
data__enabled,
data__comment,
endpoint,
createMode
)
SELECT 
'{{ name }}',
'{{ api_hook }}',
'{{ api_allowed_prefixes }}',
'{{ api_blocked_prefixes }}',
{{ enabled }},
'{{ comment }}',
'{{ endpoint }}',
'{{ createMode }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: api_integrations
  props:
    - name: endpoint
      value: string
      description: Required parameter for the api_integrations resource.
    - name: name
      value: string
      description: >
        Name of the API integration.
        
    - name: api_hook
      value: object
    - name: api_allowed_prefixes
      value: array
      description: >
        A comma-separated list of endpoints and resources that Snowflake can access.
        
    - name: api_blocked_prefixes
      value: array
      description: >
        A comma-separated list of endpoints and resources that are not allowed to be called from Snowflake.
        
    - name: enabled
      value: boolean
      description: >
        Whether the API integration is enabled.
        
    - name: comment
      value: string
      description: >
        Comment for the API integration.
        
    - name: createMode
      value: string
      description: Query parameter allowing support for different modes of resource creation. Possible values include: - `errorIfExists`: Throws an error if you try to create a resource that already exists. - `orReplace`: Automatically replaces the existing resource with the current one. - `ifNotExists`: Creates a new resource when an alter is requested for a non-existent resource. (enum: [errorIfExists, orReplace, ifNotExists], example: ifNotExists, default: errorIfExists)
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_alter_api_integration"
    values={[
        { label: 'create_or_alter_api_integration', value: 'create_or_alter_api_integration' }
    ]}
>
<TabItem value="create_or_alter_api_integration">

Create an (or alter an existing) API integration. Note that API_KEY is not currently altered by this operation and is supported for a newly-created object only. Unsetting API_BLOCKED_PREFIXES is also unsupported.

```sql
REPLACE snowflake.api_integration.api_integrations
SET 
data__name = '{{ name }}',
data__api_hook = '{{ api_hook }}',
data__api_allowed_prefixes = '{{ api_allowed_prefixes }}',
data__api_blocked_prefixes = '{{ api_blocked_prefixes }}',
data__enabled = {{ enabled }},
data__comment = '{{ comment }}'
WHERE 
name = '{{ name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND data__name = '{{ name }}' --required
AND data__api_hook = '{{ api_hook }}' --required
AND data__api_allowed_prefixes = '{{ api_allowed_prefixes }}' --required
AND data__enabled = {{ enabled }} --required;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_api_integration"
    values={[
        { label: 'delete_api_integration', value: 'delete_api_integration' }
    ]}
>
<TabItem value="delete_api_integration">

Delete an API integration

```sql
DELETE FROM snowflake.api_integration.api_integrations
WHERE name = '{{ name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND ifExists = '{{ ifExists }}';
```
</TabItem>
</Tabs>
