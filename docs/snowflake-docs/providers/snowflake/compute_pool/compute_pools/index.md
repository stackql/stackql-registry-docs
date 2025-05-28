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
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | A Snowflake object identifier. If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive. |
| <CopyableCode code="active_nodes" /> | `integer` | Number of currently active nodes on the compute pool. |
| <CopyableCode code="application" /> | `string` | Name of the Snowflake Native App if the compute pool is created exclusively for the app. |
| <CopyableCode code="auto_resume" /> | `boolean` | Whether Snowflake automatically resumes the compute pool when any statement that requires the compute pool is submitted. |
| <CopyableCode code="auto_suspend_secs" /> | `integer` | Number of seconds until the compute pool automatically suspends. |
| <CopyableCode code="budget" /> | `string` | The name of the budget monitoring the credit usage of the compute pool. |
| <CopyableCode code="comment" /> | `string` | Comment describing the compute pool. |
| <CopyableCode code="created_on" /> | `string` | Time the compute pool was created. |
| <CopyableCode code="error_code" /> | `string` | Current error the compute pool hit if any. |
| <CopyableCode code="idle_nodes" /> | `integer` | Number of currently idle nodes on the compute pool. |
| <CopyableCode code="instance_family" /> | `string` | Instance family for the compute pool. |
| <CopyableCode code="is_exclusive" /> | `boolean` | Whether a compute pool is created exclusively for a Snowflake Native App. |
| <CopyableCode code="max_nodes" /> | `integer` | Maximum number of nodes for the compute pool. |
| <CopyableCode code="min_nodes" /> | `integer` | Minimum number of nodes for the compute pool. |
| <CopyableCode code="num_jobs" /> | `integer` | Number of jobs on the compute pool. |
| <CopyableCode code="num_services" /> | `integer` | Number of services on the compute pool. |
| <CopyableCode code="owner" /> | `string` | Identifier for the current owner of the compute pool. |
| <CopyableCode code="resumed_on" /> | `string` | Time the compute pool was last resumed. |
| <CopyableCode code="state" /> | `string` | Current state of the compute pool. Possible values include UNKNOWN, STARTING, IDLE, ACTIVE, STOPPING, SUSPENDED, and RESIZING. |
| <CopyableCode code="status_message" /> | `string` | Current status of the compute pool if any. |
| <CopyableCode code="target_nodes" /> | `integer` | Number of target nodes on the compute pool. |
| <CopyableCode code="updated_on" /> | `string` | Time the compute pool was last updated. |

## Methods
| Name | Accessible by | Required Params | Optional Params | Description |
|:-----|:--------------|:----------------|:----------------|:------------|
| <CopyableCode code="fetch_compute_pool" /> | `SELECT` | <CopyableCode code="name, endpoint" /> | - | Fetches a named compute pool. You can get the name of the compute pool from the `/api/v2/compute-pools` GET request. |
| <CopyableCode code="list_compute_pools" /> | `SELECT` | <CopyableCode code="endpoint" /> | <CopyableCode code="like" />, <CopyableCode code="startsWith" />, <CopyableCode code="showLimit" /> | Lists the compute pools under the account. |
| <CopyableCode code="create_compute_pool" /> | `INSERT` | <CopyableCode code="data__instance_family, data__max_nodes, data__min_nodes, data__name, endpoint" /> | <CopyableCode code="createMode" />, <CopyableCode code="initiallySuspended" /> | Creates a compute pool, with standard create modifiers as query parameters. See the Compute Pool component definition for what is required to be provided in the request body. |
| <CopyableCode code="delete_compute_pool" /> | `DELETE` | <CopyableCode code="name, endpoint" /> | <CopyableCode code="ifExists" /> | Deletes a compute pool with the given name. If you enable the `ifExists` parameter, the operation succeeds even if the object does not exist. Otherwise, a 404 failure is returned if the object does not exist. |
| <CopyableCode code="create_or_alter_compute_pool" /> | `REPLACE` | <CopyableCode code="name, data__instance_family, data__max_nodes, data__min_nodes, data__name, endpoint" /> | - | Create a (or alter an existing) compute pool. Even if the operation is just an alter, the full property set must be provided. |
| <CopyableCode code="resume_compute_pool" /> | `EXEC` | <CopyableCode code="name, endpoint" /> | - | Resume a compute pool, if suspended. If the specified compute pool is already running, no action is taken. |
| <CopyableCode code="stop_all_services_in_compute_pool" /> | `EXEC` | <CopyableCode code="name, endpoint" /> | - | Stops all services in the compute pool. |
| <CopyableCode code="stop_all_services_in_compute_pool_deprecated" /> | `EXEC` | <CopyableCode code="name, endpoint" /> | - | Stops all services in the compute pool. Deprecated - use :stop-all-services instead. |
| <CopyableCode code="suspend_compute_pool" /> | `EXEC` | <CopyableCode code="name, endpoint" /> | - | Suspend a compute pool, if active. If the specified compute pool is already suspended, no action is taken. |

<br />


<details>
<summary>Optional Parameter Details</summary>

| Name | Description | Type | Default |
|------|-------------|------|---------|
| <CopyableCode code="createMode" /> | Query parameter allowing support for different modes of resource creation. Possible values include: - `errorIfExists`: Throws an error if you try to create a resource that already exists. - `orReplace`: Automatically replaces the existing resource with the current one. - `ifNotExists`: Creates a new resource when an alter is requested for a non-existent resource. | `string` | `errorIfExists` |
| <CopyableCode code="ifExists" /> | Query parameter that specifies how to handle the request for a resource that does not exist: - `true`: The endpoint does not throw an error if the resource does not exist. It returns a 200 success response, but does not take any action on the resource. - `false`: The endpoint throws an error if the resource doesn't exist. | `boolean` | `false` |
| <CopyableCode code="initiallySuspended" /> | Specifies whether the compute pool is created initially in the suspended state. | `boolean` | `-` |
| <CopyableCode code="like" /> | Query parameter to filter the command output by resource name. Uses case-insensitive pattern matching, with support for SQL wildcard characters. | `string` | `-` |
| <CopyableCode code="showLimit" /> | Query parameter to limit the maximum number of rows returned by a command. | `integer` | `-` |
| <CopyableCode code="startsWith" /> | Query parameter to filter the command output based on the string of characters that appear at the beginning of the object name. Uses case-sensitive pattern matching. | `string` | `-` |

</details>

## `SELECT` examples

<Tabs
    defaultValue="list_compute_pools"
    values={[
        { label: 'list_compute_pools', value: 'list_compute_pools' },
        { label: 'fetch_compute_pool', value: 'fetch_compute_pool' }
    ]
}>
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
WHERE endpoint = '{{ endpoint }}';
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
WHERE name = '{{ name }}'
AND endpoint = '{{ endpoint }}';
```
</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>compute_pools</code> resource.

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
INSERT INTO snowflake.compute_pool.compute_pools (
data__name,
data__min_nodes,
data__max_nodes,
data__instance_family,
data__auto_resume,
data__comment,
data__auto_suspend_secs,
endpoint
)
SELECT 
'{{ name }}',
{{ min_nodes }},
{{ max_nodes }},
'{{ instance_family }}',
{{ auto_resume }},
'{{ comment }}',
{{ auto_suspend_secs }},
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO snowflake.compute_pool.compute_pools (
data__name,
data__instance_family,
data__min_nodes,
data__max_nodes,
endpoint
)
SELECT 
'{{ name }}',
'{{ instance_family }}',
{{ min_nodes }},
{{ max_nodes }},
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
# Description fields below are for documentation purposes only and are not required in the manifest
- name: compute_pools
  props:
    - name: data__instance_family
      value: string
    - name: data__max_nodes
      value: string
    - name: data__min_nodes
      value: string
    - name: data__name
      value: string
    - name: endpoint
      value: string
    - name: name
      value: string
      description: >-
        A Snowflake object identifier. If the identifier contains spaces or
        special characters, the entire string must be enclosed in double quotes.
        Identifiers enclosed in double quotes are also case-sensitive.
    - name: min_nodes
      value: integer
      description: Minimum number of nodes for the compute pool.
    - name: max_nodes
      value: integer
      description: Maximum number of nodes for the compute pool.
    - name: instance_family
      value: string
      description: Instance family for the compute pool.
    - name: auto_resume
      value: boolean
      description: >-
        Whether Snowflake automatically resumes the compute pool when any
        statement that requires the compute pool is submitted.
    - name: comment
      value: string
      description: Comment describing the compute pool.
    - name: auto_suspend_secs
      value: integer
      description: Number of seconds until the compute pool automatically suspends.
```
</TabItem>
</Tabs>

## `REPLACE` example

Replaces all fields in the specified <code>compute_pools</code> resource.

```sql
/*+ update */
REPLACE snowflake.compute_pool.compute_pools
SET 
name = '{{ name }}',
min_nodes = {{ min_nodes }},
max_nodes = {{ max_nodes }},
instance_family = '{{ instance_family }}',
auto_resume = {{ auto_resume }},
comment = '{{ comment }}',
auto_suspend_secs = {{ auto_suspend_secs }}
WHERE 
name = '{{ name }}'
AND data__instance_family = '{{ data__instance_family }}'
AND data__max_nodes = '{{ data__max_nodes }}'
AND data__min_nodes = '{{ data__min_nodes }}'
AND data__name = '{{ data__name }}'
AND endpoint = '{{ endpoint }}';
```

## `DELETE` example

Deletes the specified <code>compute_pools</code> resource.

```sql
/*+ delete */
DELETE FROM snowflake.compute_pool.compute_pools
WHERE name = '{{ name }}'
AND endpoint = '{{ endpoint }}';
```
