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

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_warehouses"
    values={[
        { label: 'list_warehouses', value: 'list_warehouses' },
        { label: 'fetch_warehouse', value: 'fetch_warehouse' }
    ]}
>
<TabItem value="list_warehouses">

A Snowflake virtual warehouse

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
    <td><CopyableCode code="auto_resume" /></td>
    <td><code>string</code></td>
    <td>Specifies whether to automatically resume a warehouse when a SQL statement is submitted to it</td>
</tr>
<tr>
    <td><CopyableCode code="auto_suspend" /></td>
    <td><code>integer (int32)</code></td>
    <td>time in seconds before auto suspend</td>
</tr>
<tr>
    <td><CopyableCode code="available" /></td>
    <td><code>string (Percentage)</code></td>
    <td>Percentage of the warehouse compute resources that are provisioned and available.</td>
</tr>
<tr>
    <td><CopyableCode code="budget" /></td>
    <td><code>string</code></td>
    <td>Comment representing budget for warehouse.</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string (comment)</code></td>
    <td>Specifies a comment for the warehouse</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the warehouse was created.</td>
</tr>
<tr>
    <td><CopyableCode code="enable_query_acceleration" /></td>
    <td><code>string</code></td>
    <td>Specifies whether to enable the query acceleration service for queries that rely on this warehouse for compute resources</td>
</tr>
<tr>
    <td><CopyableCode code="initially_suspended" /></td>
    <td><code>string</code></td>
    <td>Specifies whether the warehouse is created initially in the Suspended state</td>
</tr>
<tr>
    <td><CopyableCode code="is_current" /></td>
    <td><code>boolean</code></td>
    <td>Whether the warehouse is in use for the session. Only one warehouse can be in use at a time for a session.  To specify or change the warehouse for a session, use the USE WAREHOUSE command.</td>
</tr>
<tr>
    <td><CopyableCode code="is_default" /></td>
    <td><code>boolean</code></td>
    <td>Whether the warehouse is the default for the current user.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string (warehouse)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="max_cluster_count" /></td>
    <td><code>integer (int32)</code></td>
    <td>Specifies the maximum number of clusters for a multi-cluster warehouse</td>
</tr>
<tr>
    <td><CopyableCode code="max_concurrency_level" /></td>
    <td><code>integer (int32)</code></td>
    <td>Object parameter that specifies the concurrency level for SQL statements executed by a warehouse cluster</td>
</tr>
<tr>
    <td><CopyableCode code="min_cluster_count" /></td>
    <td><code>integer (int32)</code></td>
    <td>Specifies the minimum number of clusters for a multi-cluster warehouse</td>
</tr>
<tr>
    <td><CopyableCode code="other" /></td>
    <td><code>string (Percentage)</code></td>
    <td>Percentage of the warehouse compute resources that are in a state other than available,  provisioning, or quiescing.</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string (role name)</code></td>
    <td>Role that owns the warehouse.</td>
</tr>
<tr>
    <td><CopyableCode code="owner_role_type" /></td>
    <td><code>string</code></td>
    <td>The type of role that owns the object.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioning" /></td>
    <td><code>string (Percentage)</code></td>
    <td>Percentage of the warehouse compute resources that are in the process of provisioning.</td>
</tr>
<tr>
    <td><CopyableCode code="query_acceleration_max_scale_factor" /></td>
    <td><code>integer (int32)</code></td>
    <td>Specifies the maximum scale factor for leasing compute resources for query acceleration. The scale factor is used as a multiplier based on warehouse size</td>
</tr>
<tr>
    <td><CopyableCode code="queued" /></td>
    <td><code>integer (int32)</code></td>
    <td>Number of SQL statements that are queued for the warehouse.</td>
</tr>
<tr>
    <td><CopyableCode code="quiescing" /></td>
    <td><code>string (Percentage)</code></td>
    <td>Percentage of the warehouse compute resources that are executing SQL statements,  but will be shut down once the queries complete.</td>
</tr>
<tr>
    <td><CopyableCode code="resource_monitor" /></td>
    <td><code>string</code></td>
    <td>A Snowflake object identifier. If the identifier contains spaces or special characters,  the entire string must be enclosed in double quotes.  Identifiers enclosed in double quotes are also case-sensitive.  (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
<tr>
    <td><CopyableCode code="resumed_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the warehouse was last started or restarted.</td>
</tr>
<tr>
    <td><CopyableCode code="running" /></td>
    <td><code>integer (int32)</code></td>
    <td>Number of SQL statements that are being executed by the warehouse.</td>
</tr>
<tr>
    <td><CopyableCode code="scaling_policy" /></td>
    <td><code>string</code></td>
    <td>Scaling policy of warehouse, possible scaling policies: STANDARD, ECONOMY</td>
</tr>
<tr>
    <td><CopyableCode code="size" /></td>
    <td><code>string</code></td>
    <td>[Deprecated] names of size: X-Small, Small, Medium, Large, X-Large, 2X-Large, 3X-Large, 4X-Large, 5X-Large, 6X-Large</td>
</tr>
<tr>
    <td><CopyableCode code="started_clusters" /></td>
    <td><code>integer (int32)</code></td>
    <td>Number of clusters currently started.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The state of warehouse, possible states: STARTED, STARTING, DYNAMIC, SUSPENDED, RESIZING, RESUMING, SUSPENDING</td>
</tr>
<tr>
    <td><CopyableCode code="statement_queued_timeout_in_seconds" /></td>
    <td><code>integer (int32)</code></td>
    <td>Object parameter that specifies the time, in seconds, a SQL statement can be queued on a warehouse before it is canceled by the system</td>
</tr>
<tr>
    <td><CopyableCode code="statement_timeout_in_seconds" /></td>
    <td><code>integer (int32)</code></td>
    <td>Object parameter that specifies the time, in seconds, after which a running SQL statement  is canceled by the system</td>
</tr>
<tr>
    <td><CopyableCode code="target_statement_size" /></td>
    <td><code>string</code></td>
    <td>Names of size: X-Small, Small, Medium, Large, X-Large, 2X-Large, 3X-Large, 4X-Large, 5X-Large, 6X-Large</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>[Deprecated] Type of warehouse, possible types: STANDARD, SNOWPARK-OPTIMIZED</td>
</tr>
<tr>
    <td><CopyableCode code="updated_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the warehouse was last updated,  which includes changing any of the properties of the warehouse or changing the state (STARTED, SUSPENDED, RESIZING) of the warehouse.</td>
</tr>
<tr>
    <td><CopyableCode code="wait_for_completion" /></td>
    <td><code>string</code></td>
    <td>When resizing a warehouse, you can use this parameter to block the return of the ALTER WAREHOUSE command until the resize has finished provisioning all its compute resources</td>
</tr>
<tr>
    <td><CopyableCode code="warehouse_credit_limit" /></td>
    <td><code>integer (int64)</code></td>
    <td>Credit limit that are can be executed by the warehouse.</td>
</tr>
<tr>
    <td><CopyableCode code="warehouse_size" /></td>
    <td><code>string</code></td>
    <td>Size of warehouse, possible sizes: XSMALL, SMALL, MEDIUM, LARGE, XLARGE, XXLARGE, XXXLARGE, X4LARGE, X5LARGE, X6LARGE</td>
</tr>
<tr>
    <td><CopyableCode code="warehouse_type" /></td>
    <td><code>string</code></td>
    <td>Type of warehouse, possible types: STANDARD, SNOWPARK-OPTIMIZED</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="fetch_warehouse">

A Snowflake virtual warehouse

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
    <td><CopyableCode code="auto_resume" /></td>
    <td><code>string</code></td>
    <td>Specifies whether to automatically resume a warehouse when a SQL statement is submitted to it</td>
</tr>
<tr>
    <td><CopyableCode code="auto_suspend" /></td>
    <td><code>integer (int32)</code></td>
    <td>time in seconds before auto suspend</td>
</tr>
<tr>
    <td><CopyableCode code="available" /></td>
    <td><code>string (Percentage)</code></td>
    <td>Percentage of the warehouse compute resources that are provisioned and available.</td>
</tr>
<tr>
    <td><CopyableCode code="budget" /></td>
    <td><code>string</code></td>
    <td>Comment representing budget for warehouse.</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string (comment)</code></td>
    <td>Specifies a comment for the warehouse</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the warehouse was created.</td>
</tr>
<tr>
    <td><CopyableCode code="enable_query_acceleration" /></td>
    <td><code>string</code></td>
    <td>Specifies whether to enable the query acceleration service for queries that rely on this warehouse for compute resources</td>
</tr>
<tr>
    <td><CopyableCode code="initially_suspended" /></td>
    <td><code>string</code></td>
    <td>Specifies whether the warehouse is created initially in the Suspended state</td>
</tr>
<tr>
    <td><CopyableCode code="is_current" /></td>
    <td><code>boolean</code></td>
    <td>Whether the warehouse is in use for the session. Only one warehouse can be in use at a time for a session.  To specify or change the warehouse for a session, use the USE WAREHOUSE command.</td>
</tr>
<tr>
    <td><CopyableCode code="is_default" /></td>
    <td><code>boolean</code></td>
    <td>Whether the warehouse is the default for the current user.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string (warehouse)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="max_cluster_count" /></td>
    <td><code>integer (int32)</code></td>
    <td>Specifies the maximum number of clusters for a multi-cluster warehouse</td>
</tr>
<tr>
    <td><CopyableCode code="max_concurrency_level" /></td>
    <td><code>integer (int32)</code></td>
    <td>Object parameter that specifies the concurrency level for SQL statements executed by a warehouse cluster</td>
</tr>
<tr>
    <td><CopyableCode code="min_cluster_count" /></td>
    <td><code>integer (int32)</code></td>
    <td>Specifies the minimum number of clusters for a multi-cluster warehouse</td>
</tr>
<tr>
    <td><CopyableCode code="other" /></td>
    <td><code>string (Percentage)</code></td>
    <td>Percentage of the warehouse compute resources that are in a state other than available,  provisioning, or quiescing.</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string (role name)</code></td>
    <td>Role that owns the warehouse.</td>
</tr>
<tr>
    <td><CopyableCode code="owner_role_type" /></td>
    <td><code>string</code></td>
    <td>The type of role that owns the object.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioning" /></td>
    <td><code>string (Percentage)</code></td>
    <td>Percentage of the warehouse compute resources that are in the process of provisioning.</td>
</tr>
<tr>
    <td><CopyableCode code="query_acceleration_max_scale_factor" /></td>
    <td><code>integer (int32)</code></td>
    <td>Specifies the maximum scale factor for leasing compute resources for query acceleration. The scale factor is used as a multiplier based on warehouse size</td>
</tr>
<tr>
    <td><CopyableCode code="queued" /></td>
    <td><code>integer (int32)</code></td>
    <td>Number of SQL statements that are queued for the warehouse.</td>
</tr>
<tr>
    <td><CopyableCode code="quiescing" /></td>
    <td><code>string (Percentage)</code></td>
    <td>Percentage of the warehouse compute resources that are executing SQL statements,  but will be shut down once the queries complete.</td>
</tr>
<tr>
    <td><CopyableCode code="resource_monitor" /></td>
    <td><code>string</code></td>
    <td>A Snowflake object identifier. If the identifier contains spaces or special characters,  the entire string must be enclosed in double quotes.  Identifiers enclosed in double quotes are also case-sensitive.  (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
<tr>
    <td><CopyableCode code="resumed_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the warehouse was last started or restarted.</td>
</tr>
<tr>
    <td><CopyableCode code="running" /></td>
    <td><code>integer (int32)</code></td>
    <td>Number of SQL statements that are being executed by the warehouse.</td>
</tr>
<tr>
    <td><CopyableCode code="scaling_policy" /></td>
    <td><code>string</code></td>
    <td>Scaling policy of warehouse, possible scaling policies: STANDARD, ECONOMY</td>
</tr>
<tr>
    <td><CopyableCode code="size" /></td>
    <td><code>string</code></td>
    <td>[Deprecated] names of size: X-Small, Small, Medium, Large, X-Large, 2X-Large, 3X-Large, 4X-Large, 5X-Large, 6X-Large</td>
</tr>
<tr>
    <td><CopyableCode code="started_clusters" /></td>
    <td><code>integer (int32)</code></td>
    <td>Number of clusters currently started.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The state of warehouse, possible states: STARTED, STARTING, DYNAMIC, SUSPENDED, RESIZING, RESUMING, SUSPENDING</td>
</tr>
<tr>
    <td><CopyableCode code="statement_queued_timeout_in_seconds" /></td>
    <td><code>integer (int32)</code></td>
    <td>Object parameter that specifies the time, in seconds, a SQL statement can be queued on a warehouse before it is canceled by the system</td>
</tr>
<tr>
    <td><CopyableCode code="statement_timeout_in_seconds" /></td>
    <td><code>integer (int32)</code></td>
    <td>Object parameter that specifies the time, in seconds, after which a running SQL statement  is canceled by the system</td>
</tr>
<tr>
    <td><CopyableCode code="target_statement_size" /></td>
    <td><code>string</code></td>
    <td>Names of size: X-Small, Small, Medium, Large, X-Large, 2X-Large, 3X-Large, 4X-Large, 5X-Large, 6X-Large</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>[Deprecated] Type of warehouse, possible types: STANDARD, SNOWPARK-OPTIMIZED</td>
</tr>
<tr>
    <td><CopyableCode code="updated_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the warehouse was last updated,  which includes changing any of the properties of the warehouse or changing the state (STARTED, SUSPENDED, RESIZING) of the warehouse.</td>
</tr>
<tr>
    <td><CopyableCode code="wait_for_completion" /></td>
    <td><code>string</code></td>
    <td>When resizing a warehouse, you can use this parameter to block the return of the ALTER WAREHOUSE command until the resize has finished provisioning all its compute resources</td>
</tr>
<tr>
    <td><CopyableCode code="warehouse_credit_limit" /></td>
    <td><code>integer (int64)</code></td>
    <td>Credit limit that are can be executed by the warehouse.</td>
</tr>
<tr>
    <td><CopyableCode code="warehouse_size" /></td>
    <td><code>string</code></td>
    <td>Size of warehouse, possible sizes: XSMALL, SMALL, MEDIUM, LARGE, XLARGE, XXLARGE, XXXLARGE, X4LARGE, X5LARGE, X6LARGE</td>
</tr>
<tr>
    <td><CopyableCode code="warehouse_type" /></td>
    <td><code>string</code></td>
    <td>Type of warehouse, possible types: STANDARD, SNOWPARK-OPTIMIZED</td>
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
    <td><a href="#list_warehouses"><CopyableCode code="list_warehouses" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-like">like</a></td>
    <td>Show a list of warehouse filtered by pattern. Equivalent to SHOW WAREHOUSE in SQL.</td>
</tr>
<tr>
    <td><a href="#fetch_warehouse"><CopyableCode code="fetch_warehouse" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td></td>
    <td>Describes the warehouse, show information of the chosen warehouse. Equivalent to DESCRIBE WAREHOUSE in SQL.</td>
</tr>
<tr>
    <td><a href="#create_warehouse"><CopyableCode code="create_warehouse" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-createMode">createMode</a></td>
    <td>Create a virtual warehouse. Equivalent to CREATE WAREHOUSE in SQL.</td>
</tr>
<tr>
    <td><a href="#create_or_alter_warehouse"><CopyableCode code="create_or_alter_warehouse" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td></td>
    <td>Create a (or alter an existing) warehouse. Even if the operation is just an alter, the full property set must be provided.</td>
</tr>
<tr>
    <td><a href="#delete_warehouse"><CopyableCode code="delete_warehouse" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-ifExists">ifExists</a></td>
    <td>Removes the specified virtual warehouse from the system. Equivalent to DROP WAREHOUSE in SQL.</td>
</tr>
<tr>
    <td><a href="#resume_warehouse"><CopyableCode code="resume_warehouse" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-ifExists">ifExists</a></td>
    <td>Bring current warehouse to a usable ‘Running’ state by provisioning compute resources if current warehouse is suspended.</td>
</tr>
<tr>
    <td><a href="#suspend_warehouse"><CopyableCode code="suspend_warehouse" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-ifExists">ifExists</a></td>
    <td>Remove all compute nodes from a warehouse and put the warehouse into a ‘Suspended’ state if current warehouse is not suspended.</td>
</tr>
<tr>
    <td><a href="#rename_warehouse"><CopyableCode code="rename_warehouse" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-ifExists">ifExists</a></td>
    <td>Specifies a new identifier for the warehouse; must be unique for current account.</td>
</tr>
<tr>
    <td><a href="#abort_all_queries_on_warehouse"><CopyableCode code="abort_all_queries_on_warehouse" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-ifExists">ifExists</a></td>
    <td>Aborts all the queries currently running or queued on the warehouse.</td>
</tr>
<tr>
    <td><a href="#use_warehouse"><CopyableCode code="use_warehouse" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td></td>
    <td>[Deprecated] Specifies the active/current warehouse for the session.</td>
</tr>
<tr>
    <td><a href="#enable_warehouse"><CopyableCode code="enable_warehouse" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-ifExists">ifExists</a></td>
    <td>Enable an adaptive warehouse and put the warehouse into a ‘enabled’ state, if the warehouse is not enabled.</td>
</tr>
<tr>
    <td><a href="#disable_warehouse"><CopyableCode code="disable_warehouse" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-ifExists">ifExists</a></td>
    <td>Disable an adaptive warehouse and put the warehouse into a ‘disabled’ state, if the warehouse is not disabled.</td>
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
    defaultValue="list_warehouses"
    values={[
        { label: 'list_warehouses', value: 'list_warehouses' },
        { label: 'fetch_warehouse', value: 'fetch_warehouse' }
    ]}
>
<TabItem value="list_warehouses">

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
WHERE endpoint = '{{ endpoint }}' -- required
AND like = '{{ like }}';
```
</TabItem>
<TabItem value="fetch_warehouse">

Describes the warehouse, show information of the chosen warehouse. Equivalent to DESCRIBE WAREHOUSE in SQL.

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
WHERE name = '{{ name }}' -- required
AND endpoint = '{{ endpoint }}' -- required;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_warehouse"
    values={[
        { label: 'create_warehouse', value: 'create_warehouse' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_warehouse">

Create a virtual warehouse. Equivalent to CREATE WAREHOUSE in SQL.

```sql
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
endpoint,
createMode
)
SELECT 
'{{ name }}',
'{{ warehouse_type }}',
'{{ warehouse_size }}',
'{{ wait_for_completion }}',
{{ max_cluster_count }},
{{ min_cluster_count }},
'{{ scaling_policy }}',
{{ auto_suspend }},
'{{ auto_resume }}',
'{{ initially_suspended }}',
'{{ resource_monitor }}',
'{{ comment }}',
'{{ enable_query_acceleration }}',
{{ query_acceleration_max_scale_factor }},
{{ max_concurrency_level }},
{{ statement_queued_timeout_in_seconds }},
{{ statement_timeout_in_seconds }},
'{{ type }}',
'{{ size }}',
{{ warehouse_credit_limit }},
'{{ target_statement_size }}',
'{{ endpoint }}',
'{{ createMode }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: warehouses
  props:
    - name: endpoint
      value: string
      description: Required parameter for the warehouses resource.
    - name: name
      value: string
      description: >
        A Snowflake object identifier. If the identifier contains spaces or special characters,  the entire string must be enclosed in double quotes.  Identifiers enclosed in double quotes are also case-sensitive.

    - name: warehouse_type
      value: string
      description: >
        Type of warehouse, possible types: STANDARD, SNOWPARK-OPTIMIZED
        
    - name: warehouse_size
      value: string
      description: >
        Size of warehouse, possible sizes: XSMALL, SMALL, MEDIUM, LARGE, XLARGE, XXLARGE, XXXLARGE, X4LARGE, X5LARGE, X6LARGE
        
    - name: wait_for_completion
      value: string
      description: >
        When resizing a warehouse, you can use this parameter to block the return of the ALTER WAREHOUSE command until the resize has finished provisioning all its compute resources
        
      valid_values: ['true', 'false']
    - name: max_cluster_count
      value: integer
      description: >
        Specifies the maximum number of clusters for a multi-cluster warehouse
        
    - name: min_cluster_count
      value: integer
      description: >
        Specifies the minimum number of clusters for a multi-cluster warehouse
        
    - name: scaling_policy
      value: string
      description: >
        Scaling policy of warehouse, possible scaling policies: STANDARD, ECONOMY
        
    - name: auto_suspend
      value: integer
      description: >
        time in seconds before auto suspend
        
    - name: auto_resume
      value: string
      description: >
        Specifies whether to automatically resume a warehouse when a SQL statement is submitted to it
        
      valid_values: ['true', 'false']
    - name: initially_suspended
      value: string
      description: >
        Specifies whether the warehouse is created initially in the Suspended state
        
      valid_values: ['true', 'false']
    - name: resource_monitor
      value: string
      description: >
        A Snowflake object identifier. If the identifier contains spaces or special characters,  the entire string must be enclosed in double quotes.  Identifiers enclosed in double quotes are also case-sensitive.

    - name: comment
      value: string
      description: >
        Specifies a comment for the warehouse
        
    - name: enable_query_acceleration
      value: string
      description: >
        Specifies whether to enable the query acceleration service for queries that rely on this warehouse for compute resources
        
      valid_values: ['true', 'false']
    - name: query_acceleration_max_scale_factor
      value: integer
      description: >
        Specifies the maximum scale factor for leasing compute resources for query acceleration. The scale factor is used as a multiplier based on warehouse size
        
    - name: max_concurrency_level
      value: integer
      description: >
        Object parameter that specifies the concurrency level for SQL statements executed by a warehouse cluster
        
    - name: statement_queued_timeout_in_seconds
      value: integer
      description: >
        Object parameter that specifies the time, in seconds, a SQL statement can be queued on a warehouse before it is canceled by the system
        
    - name: statement_timeout_in_seconds
      value: integer
      description: >
        Object parameter that specifies the time, in seconds, after which a running SQL statement  is canceled by the system
        
    - name: type
      value: string
      description: >
        [Deprecated] Type of warehouse, possible types: STANDARD, SNOWPARK-OPTIMIZED
        
    - name: size
      value: string
      description: >
        [Deprecated] names of size: X-Small, Small, Medium, Large, X-Large, 2X-Large, 3X-Large, 4X-Large, 5X-Large, 6X-Large
        
    - name: warehouse_credit_limit
      value: integer
      description: >
        Credit limit that are can be executed by the warehouse.
        
    - name: target_statement_size
      value: string
      description: >
        Names of size: X-Small, Small, Medium, Large, X-Large, 2X-Large, 3X-Large, 4X-Large, 5X-Large, 6X-Large
        
    - name: createMode
      value: string
      description: Query parameter allowing support for different modes of resource creation. Possible values include: - `errorIfExists`: Throws an error if you try to create a resource that already exists. - `orReplace`: Automatically replaces the existing resource with the current one. - `ifNotExists`: Creates a new resource when an alter is requested for a non-existent resource. (enum: [errorIfExists, orReplace, ifNotExists], example: ifNotExists, default: errorIfExists)
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_alter_warehouse"
    values={[
        { label: 'create_or_alter_warehouse', value: 'create_or_alter_warehouse' }
    ]}
>
<TabItem value="create_or_alter_warehouse">

Create a (or alter an existing) warehouse. Even if the operation is just an alter, the full property set must be provided.

```sql
REPLACE snowflake.warehouse.warehouses
SET 
data__name = '{{ name }}',
data__warehouse_type = '{{ warehouse_type }}',
data__warehouse_size = '{{ warehouse_size }}',
data__wait_for_completion = '{{ wait_for_completion }}',
data__max_cluster_count = {{ max_cluster_count }},
data__min_cluster_count = {{ min_cluster_count }},
data__scaling_policy = '{{ scaling_policy }}',
data__auto_suspend = {{ auto_suspend }},
data__auto_resume = '{{ auto_resume }}',
data__initially_suspended = '{{ initially_suspended }}',
data__resource_monitor = '{{ resource_monitor }}',
data__comment = '{{ comment }}',
data__enable_query_acceleration = '{{ enable_query_acceleration }}',
data__query_acceleration_max_scale_factor = {{ query_acceleration_max_scale_factor }},
data__max_concurrency_level = {{ max_concurrency_level }},
data__statement_queued_timeout_in_seconds = {{ statement_queued_timeout_in_seconds }},
data__statement_timeout_in_seconds = {{ statement_timeout_in_seconds }},
data__type = '{{ type }}',
data__size = '{{ size }}',
data__warehouse_credit_limit = {{ warehouse_credit_limit }},
data__target_statement_size = '{{ target_statement_size }}'
WHERE 
name = '{{ name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND data__name = '{{ name }}' --required;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_warehouse"
    values={[
        { label: 'delete_warehouse', value: 'delete_warehouse' }
    ]}
>
<TabItem value="delete_warehouse">

Removes the specified virtual warehouse from the system. Equivalent to DROP WAREHOUSE in SQL.

```sql
DELETE FROM snowflake.warehouse.warehouses
WHERE name = '{{ name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND ifExists = '{{ ifExists }}';
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="resume_warehouse"
    values={[
        { label: 'resume_warehouse', value: 'resume_warehouse' },
        { label: 'suspend_warehouse', value: 'suspend_warehouse' },
        { label: 'rename_warehouse', value: 'rename_warehouse' },
        { label: 'abort_all_queries_on_warehouse', value: 'abort_all_queries_on_warehouse' },
        { label: 'use_warehouse', value: 'use_warehouse' },
        { label: 'enable_warehouse', value: 'enable_warehouse' },
        { label: 'disable_warehouse', value: 'disable_warehouse' }
    ]}
>
<TabItem value="resume_warehouse">

Bring current warehouse to a usable ‘Running’ state by provisioning compute resources if current warehouse is suspended.

```sql
EXEC snowflake.warehouse.warehouses.resume_warehouse 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@ifExists={{ ifExists }};
```
</TabItem>
<TabItem value="suspend_warehouse">

Remove all compute nodes from a warehouse and put the warehouse into a ‘Suspended’ state if current warehouse is not suspended.

```sql
EXEC snowflake.warehouse.warehouses.suspend_warehouse 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@ifExists={{ ifExists }};
```
</TabItem>
<TabItem value="rename_warehouse">

Specifies a new identifier for the warehouse; must be unique for current account.

```sql
EXEC snowflake.warehouse.warehouses.rename_warehouse 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@ifExists={{ ifExists }} 
@@json=
'{
"name": "{{ name }}", 
"warehouse_type": "{{ warehouse_type }}", 
"warehouse_size": "{{ warehouse_size }}", 
"wait_for_completion": "{{ wait_for_completion }}", 
"max_cluster_count": {{ max_cluster_count }}, 
"min_cluster_count": {{ min_cluster_count }}, 
"scaling_policy": "{{ scaling_policy }}", 
"auto_suspend": {{ auto_suspend }}, 
"auto_resume": "{{ auto_resume }}", 
"initially_suspended": "{{ initially_suspended }}", 
"resource_monitor": "{{ resource_monitor }}", 
"comment": "{{ comment }}", 
"enable_query_acceleration": "{{ enable_query_acceleration }}", 
"query_acceleration_max_scale_factor": {{ query_acceleration_max_scale_factor }}, 
"max_concurrency_level": {{ max_concurrency_level }}, 
"statement_queued_timeout_in_seconds": {{ statement_queued_timeout_in_seconds }}, 
"statement_timeout_in_seconds": {{ statement_timeout_in_seconds }}, 
"type": "{{ type }}", 
"size": "{{ size }}", 
"warehouse_credit_limit": {{ warehouse_credit_limit }}, 
"target_statement_size": "{{ target_statement_size }}"
}';
```
</TabItem>
<TabItem value="abort_all_queries_on_warehouse">

Aborts all the queries currently running or queued on the warehouse.

```sql
EXEC snowflake.warehouse.warehouses.abort_all_queries_on_warehouse 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@ifExists={{ ifExists }};
```
</TabItem>
<TabItem value="use_warehouse">

[Deprecated] Specifies the active/current warehouse for the session.

```sql
EXEC snowflake.warehouse.warehouses.use_warehouse 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required;
```
</TabItem>
<TabItem value="enable_warehouse">

Enable an adaptive warehouse and put the warehouse into a ‘enabled’ state, if the warehouse is not enabled.

```sql
EXEC snowflake.warehouse.warehouses.enable_warehouse 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@ifExists={{ ifExists }};
```
</TabItem>
<TabItem value="disable_warehouse">

Disable an adaptive warehouse and put the warehouse into a ‘disabled’ state, if the warehouse is not disabled.

```sql
EXEC snowflake.warehouse.warehouses.disable_warehouse 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@ifExists={{ ifExists }};
```
</TabItem>
</Tabs>
