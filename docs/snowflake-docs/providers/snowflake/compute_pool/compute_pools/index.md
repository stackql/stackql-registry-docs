--- 
title: compute_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - compute_pools
  - compute_pool
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

Creates, updates, deletes, gets or lists a <code>compute_pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>compute_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.compute_pool.compute_pools" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_compute_pools"
    values={[
        { label: 'list_compute_pools', value: 'list_compute_pools' },
        { label: 'fetch_compute_pool', value: 'fetch_compute_pool' }
    ]}
>
<TabItem value="list_compute_pools">

A Snowflake compute pool definition.

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
    <td>A Snowflake object identifier. If the identifier contains spaces or special characters,  the entire string must be enclosed in double quotes.  Identifiers enclosed in double quotes are also case-sensitive.  (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
<tr>
    <td><CopyableCode code="active_nodes" /></td>
    <td><code>integer</code></td>
    <td>Number of currently active nodes on the compute pool.</td>
</tr>
<tr>
    <td><CopyableCode code="application" /></td>
    <td><code>string</code></td>
    <td>Name of the Snowflake Native App if the compute pool is created exclusively for the app.</td>
</tr>
<tr>
    <td><CopyableCode code="auto_resume" /></td>
    <td><code>boolean</code></td>
    <td>Whether Snowflake automatically resumes the compute pool when any statement that requires the compute pool is submitted.</td>
</tr>
<tr>
    <td><CopyableCode code="auto_suspend_secs" /></td>
    <td><code>integer (int64)</code></td>
    <td>Number of seconds until the compute pool automatically suspends.</td>
</tr>
<tr>
    <td><CopyableCode code="budget" /></td>
    <td><code>string</code></td>
    <td>The name of the budget monitoring the credit usage of the compute pool.</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>Comment describing the compute pool.</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time the compute pool was created.</td>
</tr>
<tr>
    <td><CopyableCode code="error_code" /></td>
    <td><code>string</code></td>
    <td>Current error the compute pool hit if any.</td>
</tr>
<tr>
    <td><CopyableCode code="idle_nodes" /></td>
    <td><code>integer</code></td>
    <td>Number of currently idle nodes on the compute pool.</td>
</tr>
<tr>
    <td><CopyableCode code="instance_family" /></td>
    <td><code>string</code></td>
    <td>Instance family for the compute pool.</td>
</tr>
<tr>
    <td><CopyableCode code="is_exclusive" /></td>
    <td><code>boolean</code></td>
    <td>Whether a compute pool is created exclusively for a Snowflake Native App.</td>
</tr>
<tr>
    <td><CopyableCode code="max_nodes" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of nodes for the compute pool.</td>
</tr>
<tr>
    <td><CopyableCode code="min_nodes" /></td>
    <td><code>integer</code></td>
    <td>Minimum number of nodes for the compute pool.</td>
</tr>
<tr>
    <td><CopyableCode code="num_jobs" /></td>
    <td><code>integer</code></td>
    <td>Number of jobs on the compute pool.</td>
</tr>
<tr>
    <td><CopyableCode code="num_services" /></td>
    <td><code>integer</code></td>
    <td>Number of services on the compute pool.</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td>Identifier for the current owner of the compute pool.</td>
</tr>
<tr>
    <td><CopyableCode code="resumed_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time the compute pool was last resumed.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Current state of the compute pool. Possible values include UNKNOWN, STARTING, IDLE, ACTIVE, STOPPING, SUSPENDED, and RESIZING.</td>
</tr>
<tr>
    <td><CopyableCode code="status_message" /></td>
    <td><code>string</code></td>
    <td>Current status of the compute pool if any.</td>
</tr>
<tr>
    <td><CopyableCode code="target_nodes" /></td>
    <td><code>integer</code></td>
    <td>Number of target nodes on the compute pool.</td>
</tr>
<tr>
    <td><CopyableCode code="updated_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time the compute pool was last updated.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="fetch_compute_pool">

A Snowflake compute pool definition.

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
    <td>A Snowflake object identifier. If the identifier contains spaces or special characters,  the entire string must be enclosed in double quotes.  Identifiers enclosed in double quotes are also case-sensitive.  (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
<tr>
    <td><CopyableCode code="active_nodes" /></td>
    <td><code>integer</code></td>
    <td>Number of currently active nodes on the compute pool.</td>
</tr>
<tr>
    <td><CopyableCode code="application" /></td>
    <td><code>string</code></td>
    <td>Name of the Snowflake Native App if the compute pool is created exclusively for the app.</td>
</tr>
<tr>
    <td><CopyableCode code="auto_resume" /></td>
    <td><code>boolean</code></td>
    <td>Whether Snowflake automatically resumes the compute pool when any statement that requires the compute pool is submitted.</td>
</tr>
<tr>
    <td><CopyableCode code="auto_suspend_secs" /></td>
    <td><code>integer (int64)</code></td>
    <td>Number of seconds until the compute pool automatically suspends.</td>
</tr>
<tr>
    <td><CopyableCode code="budget" /></td>
    <td><code>string</code></td>
    <td>The name of the budget monitoring the credit usage of the compute pool.</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>Comment describing the compute pool.</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time the compute pool was created.</td>
</tr>
<tr>
    <td><CopyableCode code="error_code" /></td>
    <td><code>string</code></td>
    <td>Current error the compute pool hit if any.</td>
</tr>
<tr>
    <td><CopyableCode code="idle_nodes" /></td>
    <td><code>integer</code></td>
    <td>Number of currently idle nodes on the compute pool.</td>
</tr>
<tr>
    <td><CopyableCode code="instance_family" /></td>
    <td><code>string</code></td>
    <td>Instance family for the compute pool.</td>
</tr>
<tr>
    <td><CopyableCode code="is_exclusive" /></td>
    <td><code>boolean</code></td>
    <td>Whether a compute pool is created exclusively for a Snowflake Native App.</td>
</tr>
<tr>
    <td><CopyableCode code="max_nodes" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of nodes for the compute pool.</td>
</tr>
<tr>
    <td><CopyableCode code="min_nodes" /></td>
    <td><code>integer</code></td>
    <td>Minimum number of nodes for the compute pool.</td>
</tr>
<tr>
    <td><CopyableCode code="num_jobs" /></td>
    <td><code>integer</code></td>
    <td>Number of jobs on the compute pool.</td>
</tr>
<tr>
    <td><CopyableCode code="num_services" /></td>
    <td><code>integer</code></td>
    <td>Number of services on the compute pool.</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td>Identifier for the current owner of the compute pool.</td>
</tr>
<tr>
    <td><CopyableCode code="resumed_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time the compute pool was last resumed.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Current state of the compute pool. Possible values include UNKNOWN, STARTING, IDLE, ACTIVE, STOPPING, SUSPENDED, and RESIZING.</td>
</tr>
<tr>
    <td><CopyableCode code="status_message" /></td>
    <td><code>string</code></td>
    <td>Current status of the compute pool if any.</td>
</tr>
<tr>
    <td><CopyableCode code="target_nodes" /></td>
    <td><code>integer</code></td>
    <td>Number of target nodes on the compute pool.</td>
</tr>
<tr>
    <td><CopyableCode code="updated_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time the compute pool was last updated.</td>
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
    <td><a href="#list_compute_pools"><CopyableCode code="list_compute_pools" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-like"><code>like</code></a>, <a href="#parameter-startsWith"><code>startsWith</code></a>, <a href="#parameter-showLimit"><code>showLimit</code></a></td>
    <td>Lists the compute pools under the account.</td>
</tr>
<tr>
    <td><a href="#fetch_compute_pool"><CopyableCode code="fetch_compute_pool" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Fetches a named compute pool. You can get the name of the compute pool from the <code>/api/v2/compute-pools</code> GET request.</td>
</tr>
<tr>
    <td><a href="#create_compute_pool"><CopyableCode code="create_compute_pool" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-createMode"><code>createMode</code></a>, <a href="#parameter-initiallySuspended"><code>initiallySuspended</code></a></td>
    <td>Creates a compute pool, with standard create modifiers as query parameters. See the Compute Pool component definition for what is required to be provided in the request body.</td>
</tr>
<tr>
    <td><a href="#create_or_alter_compute_pool"><CopyableCode code="create_or_alter_compute_pool" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create a (or alter an existing) compute pool. Even if the operation is just an alter, the full property set must be provided.</td>
</tr>
<tr>
    <td><a href="#delete_compute_pool"><CopyableCode code="delete_compute_pool" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-ifExists"><code>ifExists</code></a></td>
    <td>Deletes a compute pool with the given name. If you enable the <code>ifExists</code> parameter, the operation succeeds even if the object does not exist. Otherwise, a 404 failure is returned if the object does not exist.</td>
</tr>
<tr>
    <td><a href="#resume_compute_pool"><CopyableCode code="resume_compute_pool" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Resume a compute pool, if suspended. If the specified compute pool is already running, no action is taken.</td>
</tr>
<tr>
    <td><a href="#suspend_compute_pool"><CopyableCode code="suspend_compute_pool" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Suspend a compute pool, if active. If the specified compute pool is already suspended, no action is taken.</td>
</tr>
<tr>
    <td><a href="#stop_all_services_in_compute_pool_deprecated"><CopyableCode code="stop_all_services_in_compute_pool_deprecated" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Stops all services in the compute pool. Deprecated - use :stop-all-services instead.</td>
</tr>
<tr>
    <td><a href="#stop_all_services_in_compute_pool"><CopyableCode code="stop_all_services_in_compute_pool" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Stops all services in the compute pool.</td>
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
<tr id="parameter-createMode">
    <td><CopyableCode code="createMode" /></td>
    <td><code>string</code></td>
    <td>Query parameter allowing support for different modes of resource creation. Possible values include: - <code>errorIfExists</code>: Throws an error if you try to create a resource that already exists. - <code>orReplace</code>: Automatically replaces the existing resource with the current one. - <code>ifNotExists</code>: Creates a new resource when an alter is requested for a non-existent resource.</td>
</tr>
<tr id="parameter-ifExists">
    <td><CopyableCode code="ifExists" /></td>
    <td><code>boolean</code></td>
    <td>Query parameter that specifies how to handle the request for a resource that does not exist: - <code>true</code>: The endpoint does not throw an error if the resource does not exist. It returns a 200 success response, but does not take any action on the resource. - <code>false</code>: The endpoint throws an error if the resource doesn't exist.</td>
</tr>
<tr id="parameter-initiallySuspended">
    <td><CopyableCode code="initiallySuspended" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether the compute pool is created initially in the suspended state.</td>
</tr>
<tr id="parameter-like">
    <td><CopyableCode code="like" /></td>
    <td><code>string</code></td>
    <td>Query parameter to filter the command output by resource name. Uses case-insensitive pattern matching, with support for SQL wildcard characters.</td>
</tr>
<tr id="parameter-showLimit">
    <td><CopyableCode code="showLimit" /></td>
    <td><code>integer</code></td>
    <td>Query parameter to limit the maximum number of rows returned by a command.</td>
</tr>
<tr id="parameter-startsWith">
    <td><CopyableCode code="startsWith" /></td>
    <td><code>string</code></td>
    <td>Query parameter to filter the command output based on the string of characters that appear at the beginning of the object name. Uses case-sensitive pattern matching.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_compute_pools"
    values={[
        { label: 'list_compute_pools', value: 'list_compute_pools' },
        { label: 'fetch_compute_pool', value: 'fetch_compute_pool' }
    ]}
>
<TabItem value="list_compute_pools">

Lists the compute pools under the account.

```sql
SELECT
name,
active_nodes,
application,
auto_resume,
auto_suspend_secs,
budget,
comment,
created_on,
error_code,
idle_nodes,
instance_family,
is_exclusive,
max_nodes,
min_nodes,
num_jobs,
num_services,
owner,
resumed_on,
state,
status_message,
target_nodes,
updated_on
FROM snowflake.compute_pool.compute_pools
WHERE endpoint = '{{ endpoint }}' -- required
AND like = '{{ like }}'
AND startsWith = '{{ startsWith }}'
AND showLimit = '{{ showLimit }}';
```
</TabItem>
<TabItem value="fetch_compute_pool">

Fetches a named compute pool. You can get the name of the compute pool from the `/api/v2/compute-pools` GET request.

```sql
SELECT
name,
active_nodes,
application,
auto_resume,
auto_suspend_secs,
budget,
comment,
created_on,
error_code,
idle_nodes,
instance_family,
is_exclusive,
max_nodes,
min_nodes,
num_jobs,
num_services,
owner,
resumed_on,
state,
status_message,
target_nodes,
updated_on
FROM snowflake.compute_pool.compute_pools
WHERE name = '{{ name }}' -- required
AND endpoint = '{{ endpoint }}' -- required;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_compute_pool"
    values={[
        { label: 'create_compute_pool', value: 'create_compute_pool' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_compute_pool">

Creates a compute pool, with standard create modifiers as query parameters. See the Compute Pool component definition for what is required to be provided in the request body.

```sql
INSERT INTO snowflake.compute_pool.compute_pools (
data__name,
data__min_nodes,
data__max_nodes,
data__instance_family,
data__auto_resume,
data__comment,
data__auto_suspend_secs,
endpoint,
createMode,
initiallySuspended
)
SELECT 
'{{ name }}',
{{ min_nodes }},
{{ max_nodes }},
'{{ instance_family }}',
{{ auto_resume }},
'{{ comment }}',
{{ auto_suspend_secs }},
'{{ endpoint }}',
'{{ createMode }}',
'{{ initiallySuspended }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: compute_pools
  props:
    - name: endpoint
      value: string
      description: Required parameter for the compute_pools resource.
    - name: name
      value: string
      description: >
        A Snowflake object identifier. If the identifier contains spaces or special characters,  the entire string must be enclosed in double quotes.  Identifiers enclosed in double quotes are also case-sensitive.

    - name: min_nodes
      value: integer
      description: >
        Minimum number of nodes for the compute pool.
        
    - name: max_nodes
      value: integer
      description: >
        Maximum number of nodes for the compute pool.
        
    - name: instance_family
      value: string
      description: >
        Instance family for the compute pool.
        
    - name: auto_resume
      value: boolean
      description: >
        Whether Snowflake automatically resumes the compute pool when any statement that requires the compute pool is submitted.
        
    - name: comment
      value: string
      description: >
        Comment describing the compute pool.
        
    - name: auto_suspend_secs
      value: integer
      description: >
        Number of seconds until the compute pool automatically suspends.
        
    - name: createMode
      value: string
      description: Query parameter allowing support for different modes of resource creation. Possible values include: - `errorIfExists`: Throws an error if you try to create a resource that already exists. - `orReplace`: Automatically replaces the existing resource with the current one. - `ifNotExists`: Creates a new resource when an alter is requested for a non-existent resource.
    - name: initiallySuspended
      value: boolean
      description: Specifies whether the compute pool is created initially in the suspended state.
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_alter_compute_pool"
    values={[
        { label: 'create_or_alter_compute_pool', value: 'create_or_alter_compute_pool' }
    ]}
>
<TabItem value="create_or_alter_compute_pool">

Create a (or alter an existing) compute pool. Even if the operation is just an alter, the full property set must be provided.

```sql
REPLACE snowflake.compute_pool.compute_pools
SET 
data__name = '{{ name }}',
data__min_nodes = {{ min_nodes }},
data__max_nodes = {{ max_nodes }},
data__instance_family = '{{ instance_family }}',
data__auto_resume = {{ auto_resume }},
data__comment = '{{ comment }}',
data__auto_suspend_secs = {{ auto_suspend_secs }}
WHERE 
name = '{{ name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND data__name = '{{ name }}' --required
AND data__instance_family = '{{ instance_family }}' --required
AND data__min_nodes = '{{ min_nodes }}' --required
AND data__max_nodes = '{{ max_nodes }}' --required;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_compute_pool"
    values={[
        { label: 'delete_compute_pool', value: 'delete_compute_pool' }
    ]}
>
<TabItem value="delete_compute_pool">

Deletes a compute pool with the given name. If you enable the `ifExists` parameter, the operation succeeds even if the object does not exist. Otherwise, a 404 failure is returned if the object does not exist.

```sql
DELETE FROM snowflake.compute_pool.compute_pools
WHERE name = '{{ name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND ifExists = '{{ ifExists }}';
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="resume_compute_pool"
    values={[
        { label: 'resume_compute_pool', value: 'resume_compute_pool' },
        { label: 'suspend_compute_pool', value: 'suspend_compute_pool' },
        { label: 'stop_all_services_in_compute_pool_deprecated', value: 'stop_all_services_in_compute_pool_deprecated' },
        { label: 'stop_all_services_in_compute_pool', value: 'stop_all_services_in_compute_pool' }
    ]}
>
<TabItem value="resume_compute_pool">

Resume a compute pool, if suspended. If the specified compute pool is already running, no action is taken.

```sql
EXEC snowflake.compute_pool.compute_pools.resume_compute_pool 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required;
```
</TabItem>
<TabItem value="suspend_compute_pool">

Suspend a compute pool, if active. If the specified compute pool is already suspended, no action is taken.

```sql
EXEC snowflake.compute_pool.compute_pools.suspend_compute_pool 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required;
```
</TabItem>
<TabItem value="stop_all_services_in_compute_pool_deprecated">

Stops all services in the compute pool. Deprecated - use :stop-all-services instead.

```sql
EXEC snowflake.compute_pool.compute_pools.stop_all_services_in_compute_pool_deprecated 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required;
```
</TabItem>
<TabItem value="stop_all_services_in_compute_pool">

Stops all services in the compute pool.

```sql
EXEC snowflake.compute_pool.compute_pools.stop_all_services_in_compute_pool 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required;
```
</TabItem>
</Tabs>
