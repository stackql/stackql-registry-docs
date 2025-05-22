---
title: warehouses
hide_title: false
hide_table_of_contents: false
keywords:
  - warehouses
  - warehouse
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

Creates, updates, deletes, gets or lists a <code>warehouses</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>warehouses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.warehouse.warehouses" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | A Snowflake object identifier. If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive. |
| <CopyableCode code="auto_resume" /> | `string` | Specifies whether to automatically resume a warehouse when a SQL statement is submitted to it |
| <CopyableCode code="auto_suspend" /> | `integer` | time in seconds before auto suspend |
| <CopyableCode code="available" /> | `string` | Percentage of the warehouse compute resources that are provisioned and available. |
| <CopyableCode code="budget" /> | `string` | Comment representing budget for warehouse. |
| <CopyableCode code="comment" /> | `string` | Specifies a comment for the warehouse |
| <CopyableCode code="created_on" /> | `string` | Date and time when the warehouse was created. |
| <CopyableCode code="enable_query_acceleration" /> | `string` | Specifies whether to enable the query acceleration service for queries that rely on this warehouse for compute resources |
| <CopyableCode code="initially_suspended" /> | `string` | Specifies whether the warehouse is created initially in the Suspended state |
| <CopyableCode code="is_current" /> | `boolean` | Whether the warehouse is in use for the session. Only one warehouse can be in use at a time for a session. To specify or change the warehouse for a session, use the USE WAREHOUSE command. |
| <CopyableCode code="is_default" /> | `boolean` | Whether the warehouse is the default for the current user. |
| <CopyableCode code="kind" /> | `string` |  |
| <CopyableCode code="max_cluster_count" /> | `integer` | Specifies the maximum number of clusters for a multi-cluster warehouse |
| <CopyableCode code="max_concurrency_level" /> | `integer` | Object parameter that specifies the concurrency level for SQL statements executed by a warehouse cluster |
| <CopyableCode code="min_cluster_count" /> | `integer` | Specifies the minimum number of clusters for a multi-cluster warehouse |
| <CopyableCode code="other" /> | `string` | Percentage of the warehouse compute resources that are in a state other than available, provisioning, or quiescing. |
| <CopyableCode code="owner" /> | `string` | Role that owns the warehouse. |
| <CopyableCode code="owner_role_type" /> | `string` | The type of role that owns the object. |
| <CopyableCode code="provisioning" /> | `string` | Percentage of the warehouse compute resources that are in the process of provisioning. |
| <CopyableCode code="query_acceleration_max_scale_factor" /> | `integer` | Specifies the maximum scale factor for leasing compute resources for query acceleration. The scale factor is used as a multiplier based on warehouse size |
| <CopyableCode code="queued" /> | `integer` | Number of SQL statements that are queued for the warehouse. |
| <CopyableCode code="quiescing" /> | `string` | Percentage of the warehouse compute resources that are executing SQL statements, but will be shut down once the queries complete. |
| <CopyableCode code="resource_monitor" /> | `string` | A Snowflake object identifier. If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive. |
| <CopyableCode code="resumed_on" /> | `string` | Date and time when the warehouse was last started or restarted. |
| <CopyableCode code="running" /> | `integer` | Number of SQL statements that are being executed by the warehouse. |
| <CopyableCode code="scaling_policy" /> | `string` | Scaling policy of warehouse, possible scaling policies: STANDARD, ECONOMY |
| <CopyableCode code="size" /> | `string` | [Deprecated] names of size: X-Small, Small, Medium, Large, X-Large, 2X-Large, 3X-Large, 4X-Large, 5X-Large, 6X-Large |
| <CopyableCode code="started_clusters" /> | `integer` | Number of clusters currently started. |
| <CopyableCode code="state" /> | `string` | The state of warehouse, possible states: STARTED, STARTING, DYNAMIC, SUSPENDED, RESIZING, RESUMING, SUSPENDING |
| <CopyableCode code="statement_queued_timeout_in_seconds" /> | `integer` | Object parameter that specifies the time, in seconds, a SQL statement can be queued on a warehouse before it is canceled by the system |
| <CopyableCode code="statement_timeout_in_seconds" /> | `integer` | Object parameter that specifies the time, in seconds, after which a running SQL statement is canceled by the system |
| <CopyableCode code="target_statement_size" /> | `string` | Names of size: X-Small, Small, Medium, Large, X-Large, 2X-Large, 3X-Large, 4X-Large, 5X-Large, 6X-Large |
| <CopyableCode code="type" /> | `string` | [Deprecated] Type of warehouse, possible types: STANDARD, SNOWPARK-OPTIMIZED |
| <CopyableCode code="updated_on" /> | `string` | Date and time when the warehouse was last updated, which includes changing any of the properties of the warehouse or changing the state (STARTED, SUSPENDED, RESIZING) of the warehouse. |
| <CopyableCode code="wait_for_completion" /> | `string` | When resizing a warehouse, you can use this parameter to block the return of the ALTER WAREHOUSE command until the resize has finished provisioning all its compute resources |
| <CopyableCode code="warehouse_credit_limit" /> | `integer` | Credit limit that are can be executed by the warehouse. |
| <CopyableCode code="warehouse_size" /> | `string` | Size of warehouse, possible sizes: XSMALL, SMALL, MEDIUM, LARGE, XLARGE, XXLARGE, XXXLARGE, X4LARGE, X5LARGE, X6LARGE |
| <CopyableCode code="warehouse_type" /> | `string` | Type of warehouse, possible types: STANDARD, SNOWPARK-OPTIMIZED |

## Methods
| Name | Accessible by | Required Params | Optional Params | Description |
|:-----|:--------------|:----------------|:----------------|:------------|
| <CopyableCode code="fetch_warehouse" /> | `SELECT` | <CopyableCode code="name, endpoint" /> | - | Describes the warehouse, show information of the chosen warehouse. Equivalent to DESCRIBE WAREHOUSE in SQL. |
| <CopyableCode code="list_warehouses" /> | `SELECT` | <CopyableCode code="endpoint" /> | <CopyableCode code="like" /> | Show a list of warehouse filtered by pattern. Equivalent to SHOW WAREHOUSE in SQL. |
| <CopyableCode code="create_warehouse" /> | `INSERT` | <CopyableCode code="data__name, endpoint" /> | <CopyableCode code="createMode" /> | Create a virtual warehouse. Equivalent to CREATE WAREHOUSE in SQL. |
| <CopyableCode code="delete_warehouse" /> | `DELETE` | <CopyableCode code="name, endpoint" /> | <CopyableCode code="ifExists" /> | Removes the specified virtual warehouse from the system. Equivalent to DROP WAREHOUSE in SQL. |
| <CopyableCode code="create_or_alter_warehouse" /> | `REPLACE` | <CopyableCode code="name, data__name, endpoint" /> | - | Create a (or alter an existing) warehouse. Even if the operation is just an alter, the full property set must be provided. |
| <CopyableCode code="abort_all_queries_on_warehouse" /> | `EXEC` | <CopyableCode code="name, endpoint" /> | <CopyableCode code="ifExists" /> | Aborts all the queries currently running or queued on the warehouse. |
| <CopyableCode code="disable_warehouse" /> | `EXEC` | <CopyableCode code="name, endpoint" /> | <CopyableCode code="ifExists" /> | Disable an adaptive warehouse and put the warehouse into a ‘disabled’ state, if the warehouse is not disabled. |
| <CopyableCode code="enable_warehouse" /> | `EXEC` | <CopyableCode code="name, endpoint" /> | <CopyableCode code="ifExists" /> | Enable an adaptive warehouse and put the warehouse into a ‘enabled’ state, if the warehouse is not enabled. |
| <CopyableCode code="rename_warehouse" /> | `EXEC` | <CopyableCode code="name, data__name, endpoint" /> | <CopyableCode code="ifExists" /> | Specifies a new identifier for the warehouse; must be unique for current account. |
| <CopyableCode code="resume_warehouse" /> | `EXEC` | <CopyableCode code="name, endpoint" /> | <CopyableCode code="ifExists" /> | Bring current warehouse to a usable ‘Running’ state by provisioning compute resources if current warehouse is suspended. |
| <CopyableCode code="suspend_warehouse" /> | `EXEC` | <CopyableCode code="name, endpoint" /> | <CopyableCode code="ifExists" /> | Remove all compute nodes from a warehouse and put the warehouse into a ‘Suspended’ state if current warehouse is not suspended. |
| <CopyableCode code="use_warehouse" /> | `EXEC` | <CopyableCode code="name, endpoint" /> | - | [Deprecated] Specifies the active/current warehouse for the session. |

  

<details>
<summary>Optional Parameter Details</summary>

| Name | Description | Type | Default |
|------|-------------|------|---------|
| <CopyableCode code="createMode" /> | Query parameter allowing support for different modes of resource creation. Possible values include: - `errorIfExists`: Throws an error if you try to create a resource that already exists. - `orReplace`: Automatically replaces the existing resource with the current one. - `ifNotExists`: Creates a new resource when an alter is requested for a non-existent resource. | `string` | `errorIfExists` |
| <CopyableCode code="ifExists" /> | Query parameter that specifies how to handle the request for a resource that does not exist: - `true`: The endpoint does not throw an error if the resource does not exist. It returns a 200 success response, but does not take any action on the resource. - `false`: The endpoint throws an error if the resource doesn't exist. | `boolean` | `false` |
| <CopyableCode code="like" /> | Query parameter to filter the command output by resource name. Uses case-insensitive pattern matching, with support for SQL wildcard characters. | `string` | `-` |

</details>

## `SELECT` examples

Show a list of warehouse filtered by pattern. Equivalent to SHOW WAREHOUSE in SQL.


```sql
SELECT
name,
auto_resume,
auto_suspend,
available,
budget,
comment,
created_on,
enable_query_acceleration,
initially_suspended,
is_current,
is_default,
kind,
max_cluster_count,
max_concurrency_level,
min_cluster_count,
other,
owner,
owner_role_type,
provisioning,
query_acceleration_max_scale_factor,
queued,
quiescing,
resource_monitor,
resumed_on,
running,
scaling_policy,
size,
started_clusters,
state,
statement_queued_timeout_in_seconds,
statement_timeout_in_seconds,
target_statement_size,
type,
updated_on,
wait_for_completion,
warehouse_credit_limit,
warehouse_size,
warehouse_type
FROM snowflake.warehouse.warehouses
WHERE endpoint = '{{ endpoint }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>warehouses</code> resource.

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
INSERT INTO snowflake.warehouse.warehouses (
data__name,
data__warehouse_type,
data__warehouse_size,
data__wait_for_completion,
data__max_cluster_count,
data__min_cluster_count,
data__scaling_policy,
data__auto_suspend,
data__auto_resume,
data__initially_suspended,
data__resource_monitor,
data__comment,
data__enable_query_acceleration,
data__query_acceleration_max_scale_factor,
data__max_concurrency_level,
data__statement_queued_timeout_in_seconds,
data__statement_timeout_in_seconds,
data__type,
data__size,
data__warehouse_credit_limit,
data__target_statement_size,
endpoint
)
SELECT 
'{{ name }}',
'{{ warehouse_type }}',
'{{ warehouse_size }}',
'{{ wait_for_completion }}',
'{{ max_cluster_count }}',
'{{ min_cluster_count }}',
'{{ scaling_policy }}',
'{{ auto_suspend }}',
'{{ auto_resume }}',
'{{ initially_suspended }}',
'{{ resource_monitor }}',
'{{ comment }}',
'{{ enable_query_acceleration }}',
'{{ query_acceleration_max_scale_factor }}',
'{{ max_concurrency_level }}',
'{{ statement_queued_timeout_in_seconds }}',
'{{ statement_timeout_in_seconds }}',
'{{ type }}',
'{{ size }}',
'{{ warehouse_credit_limit }}',
'{{ target_statement_size }}',
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO snowflake.warehouse.warehouses (
data__name,
endpoint
)
SELECT 
'{{ name }}',
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: warehouses
  props:
    - name: data__name
      value: string
    - name: endpoint
      value: string
    - name: name
      value: string
    - name: warehouse_type
      value: string
    - name: warehouse_size
      value: string
    - name: wait_for_completion
      value: string
    - name: max_cluster_count
      value: integer
    - name: min_cluster_count
      value: integer
    - name: scaling_policy
      value: string
    - name: auto_suspend
      value: integer
    - name: auto_resume
      value: string
    - name: initially_suspended
      value: string
    - name: resource_monitor
      value: string
    - name: comment
      value: string
    - name: enable_query_acceleration
      value: string
    - name: query_acceleration_max_scale_factor
      value: integer
    - name: max_concurrency_level
      value: integer
    - name: statement_queued_timeout_in_seconds
      value: integer
    - name: statement_timeout_in_seconds
      value: integer
    - name: type
      value: string
    - name: size
      value: string
    - name: warehouse_credit_limit
      value: integer
    - name: target_statement_size
      value: string

```
</TabItem>
</Tabs>

## `REPLACE` example

Replaces all fields in the specified <code>warehouses</code> resource.

```sql
/*+ update */
REPLACE snowflake.warehouse.warehouses
SET 
name = '{{ name }}',
warehouse_type = '{{ warehouse_type }}',
warehouse_size = '{{ warehouse_size }}',
wait_for_completion = '{{ wait_for_completion }}',
max_cluster_count = '{{ max_cluster_count }}',
min_cluster_count = '{{ min_cluster_count }}',
scaling_policy = '{{ scaling_policy }}',
auto_suspend = '{{ auto_suspend }}',
auto_resume = '{{ auto_resume }}',
initially_suspended = '{{ initially_suspended }}',
resource_monitor = '{{ resource_monitor }}',
comment = '{{ comment }}',
enable_query_acceleration = '{{ enable_query_acceleration }}',
query_acceleration_max_scale_factor = '{{ query_acceleration_max_scale_factor }}',
max_concurrency_level = '{{ max_concurrency_level }}',
statement_queued_timeout_in_seconds = '{{ statement_queued_timeout_in_seconds }}',
statement_timeout_in_seconds = '{{ statement_timeout_in_seconds }}',
type = '{{ type }}',
size = '{{ size }}',
warehouse_credit_limit = '{{ warehouse_credit_limit }}',
target_statement_size = '{{ target_statement_size }}'
WHERE 
name = '{{ name }}'
AND data__name = '{{ data__name }}'
AND endpoint = '{{ endpoint }}';
```

## `DELETE` example

Deletes the specified <code>warehouses</code> resource.

```sql
/*+ delete */
DELETE FROM snowflake.warehouse.warehouses
WHERE name = '{{ name }}'
AND endpoint = '{{ endpoint }}';
```
