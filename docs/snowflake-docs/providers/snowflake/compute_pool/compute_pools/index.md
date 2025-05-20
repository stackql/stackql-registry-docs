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
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="fetch_compute_pool" /> | `SELECT` | <CopyableCode code="name, endpoint" /> | Fetches a named compute pool. You can get the name of the compute pool from the `/api/v2/compute-pools` GET request. |
| <CopyableCode code="list_compute_pools" /> | `SELECT` | <CopyableCode code="endpoint" /> | Lists the compute pools under the account. |
| <CopyableCode code="create_compute_pool" /> | `INSERT` | <CopyableCode code="data__instance_family, data__max_nodes, data__min_nodes, data__name, endpoint" /> | Creates a compute pool, with standard create modifiers as query parameters. See the Compute Pool component definition for what is required to be provided in the request body. |
| <CopyableCode code="delete_compute_pool" /> | `DELETE` | <CopyableCode code="name, endpoint" /> | Deletes a compute pool with the given name. If you enable the `ifExists` parameter, the operation succeeds even if the object does not exist. Otherwise, a 404 failure is returned if the object does not exist. |
| <CopyableCode code="create_or_alter_compute_pool" /> | `REPLACE` | <CopyableCode code="name, data__instance_family, data__max_nodes, data__min_nodes, data__name, endpoint" /> | Create a (or alter an existing) compute pool. Even if the operation is just an alter, the full property set must be provided. |
| <CopyableCode code="resume_compute_pool" /> | `EXEC` | <CopyableCode code="name, endpoint" /> | Resume a compute pool, if suspended. If the specified compute pool is already running, no action is taken. |
| <CopyableCode code="stop_all_services_in_compute_pool" /> | `EXEC` | <CopyableCode code="name, endpoint" /> | Stops all services in the compute pool. |
| <CopyableCode code="stop_all_services_in_compute_pool_deprecated" /> | `EXEC` | <CopyableCode code="name, endpoint" /> | Stops all services in the compute pool. Deprecated - use :stop-all-services instead. |
| <CopyableCode code="suspend_compute_pool" /> | `EXEC` | <CopyableCode code="name, endpoint" /> | Suspend a compute pool, if active. If the specified compute pool is already suspended, no action is taken. |

## `SELECT` examples

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
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>compute_pools</code> resource.

<Tabs     defaultValue="all"    values={[        { label: 'All Properties', value: 'all' }, { label: 'Manifest', value: 'manifest' }    ]}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO snowflake.compute_pool.compute_pools (
data__name,
endpoint,
data__instance_family,
data__min_nodes,
data__max_nodes
)
SELECT 
'{ instance_family }',
'{ min_nodes }',
'{ name }',
'{ endpoint }',
'{ max_nodes }'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
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

```
</TabItem>
</Tabs>

## `REPLACE` example

Replaces all fields in the specified <code>compute_pools</code> resource.

```sql
/*+ update */
REPLACE snowflake.compute_pool.compute_pools
SET 

WHERE 
name = '{ name }' AND data__instance_family = '{ data__instance_family }' AND data__max_nodes = '{ data__max_nodes }' AND data__min_nodes = '{ data__min_nodes }' AND data__name = '{ data__name }' AND endpoint = '{ endpoint }';
```

## `DELETE` example

Deletes the specified <code>compute_pools</code> resource.

```sql
/*+ delete */
DELETE FROM snowflake.compute_pool.compute_pools
WHERE name = '{ name }' AND endpoint = '{ endpoint }';
```
