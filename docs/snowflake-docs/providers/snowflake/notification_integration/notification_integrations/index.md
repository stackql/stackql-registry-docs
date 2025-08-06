--- 
title: notification_integrations
hide_title: false
hide_table_of_contents: false
keywords:
  - notification_integrations
  - notification_integration
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

Creates, updates, deletes, gets or lists a <code>notification_integrations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notification_integrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.notification_integration.notification_integrations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_notification_integrations"
    values={[
        { label: 'list_notification_integrations', value: 'list_notification_integrations' },
        { label: 'fetch_notification_integration', value: 'fetch_notification_integration' }
    ]}
>
<TabItem value="list_notification_integrations">

A Snowflake notification

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
    <td>Name of the notification. (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>Comment for the notification integration.</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the notification was created.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether the notification integration is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="notification_hook" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="fetch_notification_integration">

A Snowflake notification

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
    <td>Name of the notification. (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>Comment for the notification integration.</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the notification was created.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether the notification integration is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="notification_hook" /></td>
    <td><code>object</code></td>
    <td></td>
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
    <td><a href="#list_notification_integrations"><CopyableCode code="list_notification_integrations" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-like">like</a></td>
    <td>List notification integrations</td>
</tr>
<tr>
    <td><a href="#fetch_notification_integration"><CopyableCode code="fetch_notification_integration" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td></td>
    <td>Fetch a notification integration</td>
</tr>
<tr>
    <td><a href="#create_notification_integration"><CopyableCode code="create_notification_integration" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-createMode">createMode</a></td>
    <td>Create a notification integration</td>
</tr>
<tr>
    <td><a href="#delete_notification_integration"><CopyableCode code="delete_notification_integration" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-ifExists">ifExists</a></td>
    <td>Delete a notification integration</td>
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
<tr id="parameter-like">
    <td><CopyableCode code="like" /></td>
    <td><code>string</code></td>
    <td>Query parameter to filter the command output by resource name. Uses case-insensitive pattern matching, with support for SQL wildcard characters. (example: test_%)</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_notification_integrations"
    values={[
        { label: 'list_notification_integrations', value: 'list_notification_integrations' },
        { label: 'fetch_notification_integration', value: 'fetch_notification_integration' }
    ]}
>
<TabItem value="list_notification_integrations">

List notification integrations

```sql
SELECT
name,
comment,
created_on,
enabled,
notification_hook
FROM snowflake.notification_integration.notification_integrations
WHERE endpoint = '{{ endpoint }}' -- required
AND like = '{{ like }}';
```
</TabItem>
<TabItem value="fetch_notification_integration">

Fetch a notification integration

```sql
SELECT
name,
comment,
created_on,
enabled,
notification_hook
FROM snowflake.notification_integration.notification_integrations
WHERE name = '{{ name }}' -- required
AND endpoint = '{{ endpoint }}' -- required;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_notification_integration"
    values={[
        { label: 'create_notification_integration', value: 'create_notification_integration' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_notification_integration">

Create a notification integration

```sql
INSERT INTO snowflake.notification_integration.notification_integrations (
data__name,
data__enabled,
data__comment,
data__notification_hook,
endpoint,
createMode
)
SELECT 
'{{ name }}',
{{ enabled }},
'{{ comment }}',
'{{ notification_hook }}',
'{{ endpoint }}',
'{{ createMode }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: notification_integrations
  props:
    - name: endpoint
      value: string
      description: Required parameter for the notification_integrations resource.
    - name: name
      value: string
      description: >
        Name of the notification.
        
    - name: enabled
      value: boolean
      description: >
        Whether the notification integration is enabled.
        
    - name: comment
      value: string
      description: >
        Comment for the notification integration.
        
    - name: notification_hook
      value: object
    - name: createMode
      value: string
      description: Query parameter allowing support for different modes of resource creation. Possible values include: - `errorIfExists`: Throws an error if you try to create a resource that already exists. - `orReplace`: Automatically replaces the existing resource with the current one. - `ifNotExists`: Creates a new resource when an alter is requested for a non-existent resource. (enum: [errorIfExists, orReplace, ifNotExists], example: ifNotExists, default: errorIfExists)
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_notification_integration"
    values={[
        { label: 'delete_notification_integration', value: 'delete_notification_integration' }
    ]}
>
<TabItem value="delete_notification_integration">

Delete a notification integration

```sql
DELETE FROM snowflake.notification_integration.notification_integrations
WHERE name = '{{ name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND ifExists = '{{ ifExists }}';
```
</TabItem>
</Tabs>
