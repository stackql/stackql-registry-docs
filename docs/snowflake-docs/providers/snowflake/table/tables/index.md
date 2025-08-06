--- 
title: tables
hide_title: false
hide_table_of_contents: false
keywords:
  - tables
  - table
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

Creates, updates, deletes, gets or lists a <code>tables</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.table.tables" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_tables"
    values={[
        { label: 'list_tables', value: 'list_tables' },
        { label: 'fetch_table', value: 'fetch_table' }
    ]}
>
<TabItem value="list_tables">

A Snowflake table

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
    <td>Specifies the name for the table, must be unique for the schema in which the table is created</td>
</tr>
<tr>
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>Database in which the table is stored</td>
</tr>
<tr>
    <td><CopyableCode code="schema_name" /></td>
    <td><code>string</code></td>
    <td>Schema in which the table is stored</td>
</tr>
<tr>
    <td><CopyableCode code="automatic_clustering" /></td>
    <td><code>boolean</code></td>
    <td>If Automatic Clustering is enabled for your account, specifies whether it is explicitly enabled or disabled for the table.</td>
</tr>
<tr>
    <td><CopyableCode code="budget" /></td>
    <td><code>string</code></td>
    <td>Name of the budget if the object is monitored by a budget</td>
</tr>
<tr>
    <td><CopyableCode code="bytes" /></td>
    <td><code>integer (int64)</code></td>
    <td>Number of bytes that will be scanned if the entire table is scanned in a query. Note that this number may be different than the number of actual physical bytes stored on-disk for the table</td>
</tr>
<tr>
    <td><CopyableCode code="change_tracking" /></td>
    <td><code>boolean</code></td>
    <td>Change tracking is enabled or disabled</td>
</tr>
<tr>
    <td><CopyableCode code="cluster_by" /></td>
    <td><code>array</code></td>
    <td>Specifies one or more columns or column expressions in the table as the clustering key</td>
</tr>
<tr>
    <td><CopyableCode code="columns" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>Comment for the table</td>
</tr>
<tr>
    <td><CopyableCode code="constraints" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the table was created.</td>
</tr>
<tr>
    <td><CopyableCode code="data_retention_time_in_days" /></td>
    <td><code>integer</code></td>
    <td>Specifies the retention period for the table so that Time Travel actions SELECT, CLONE, UNDROP can be performed on historical data in the table</td>
</tr>
<tr>
    <td><CopyableCode code="default_ddl_collation" /></td>
    <td><code>string</code></td>
    <td>Specifies a default collation specification for the columns in the table, including columns added to the table in the future</td>
</tr>
<tr>
    <td><CopyableCode code="dropped_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the table was dropped</td>
</tr>
<tr>
    <td><CopyableCode code="enable_schema_evolution" /></td>
    <td><code>boolean</code></td>
    <td>Table has schema evolution enabled or disabled</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Table type - permanent, transient, or temporary (default: PERMANENT)</td>
</tr>
<tr>
    <td><CopyableCode code="max_data_extension_time_in_days" /></td>
    <td><code>integer</code></td>
    <td>Specifies the retention period for the table so that Time Travel actions SELECT, CLONE, UNDROP can be performed on historical data in the table</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td>Role that owns the table</td>
</tr>
<tr>
    <td><CopyableCode code="owner_role_type" /></td>
    <td><code>string</code></td>
    <td>The type of role that owns the object.</td>
</tr>
<tr>
    <td><CopyableCode code="rows" /></td>
    <td><code>integer (int64)</code></td>
    <td>Number of rows in the table. Returns NULL for external tables.</td>
</tr>
<tr>
    <td><CopyableCode code="search_optimization" /></td>
    <td><code>boolean</code></td>
    <td>If ON, the table has the search optimization service enabled</td>
</tr>
<tr>
    <td><CopyableCode code="search_optimization_bytes" /></td>
    <td><code>integer (int64)</code></td>
    <td>Number of additional bytes of storage that the search optimization service consumes for this table</td>
</tr>
<tr>
    <td><CopyableCode code="search_optimization_progress" /></td>
    <td><code>integer (int64)</code></td>
    <td>Percentage of the table that has been optimized for search.</td>
</tr>
<tr>
    <td><CopyableCode code="table_type" /></td>
    <td><code>string</code></td>
    <td>Type of the table</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="fetch_table">

A Snowflake table

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
    <td>Specifies the name for the table, must be unique for the schema in which the table is created</td>
</tr>
<tr>
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>Database in which the table is stored</td>
</tr>
<tr>
    <td><CopyableCode code="schema_name" /></td>
    <td><code>string</code></td>
    <td>Schema in which the table is stored</td>
</tr>
<tr>
    <td><CopyableCode code="automatic_clustering" /></td>
    <td><code>boolean</code></td>
    <td>If Automatic Clustering is enabled for your account, specifies whether it is explicitly enabled or disabled for the table.</td>
</tr>
<tr>
    <td><CopyableCode code="budget" /></td>
    <td><code>string</code></td>
    <td>Name of the budget if the object is monitored by a budget</td>
</tr>
<tr>
    <td><CopyableCode code="bytes" /></td>
    <td><code>integer (int64)</code></td>
    <td>Number of bytes that will be scanned if the entire table is scanned in a query. Note that this number may be different than the number of actual physical bytes stored on-disk for the table</td>
</tr>
<tr>
    <td><CopyableCode code="change_tracking" /></td>
    <td><code>boolean</code></td>
    <td>Change tracking is enabled or disabled</td>
</tr>
<tr>
    <td><CopyableCode code="cluster_by" /></td>
    <td><code>array</code></td>
    <td>Specifies one or more columns or column expressions in the table as the clustering key</td>
</tr>
<tr>
    <td><CopyableCode code="columns" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>Comment for the table</td>
</tr>
<tr>
    <td><CopyableCode code="constraints" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the table was created.</td>
</tr>
<tr>
    <td><CopyableCode code="data_retention_time_in_days" /></td>
    <td><code>integer</code></td>
    <td>Specifies the retention period for the table so that Time Travel actions SELECT, CLONE, UNDROP can be performed on historical data in the table</td>
</tr>
<tr>
    <td><CopyableCode code="default_ddl_collation" /></td>
    <td><code>string</code></td>
    <td>Specifies a default collation specification for the columns in the table, including columns added to the table in the future</td>
</tr>
<tr>
    <td><CopyableCode code="dropped_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the table was dropped</td>
</tr>
<tr>
    <td><CopyableCode code="enable_schema_evolution" /></td>
    <td><code>boolean</code></td>
    <td>Table has schema evolution enabled or disabled</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Table type - permanent, transient, or temporary (default: PERMANENT)</td>
</tr>
<tr>
    <td><CopyableCode code="max_data_extension_time_in_days" /></td>
    <td><code>integer</code></td>
    <td>Specifies the retention period for the table so that Time Travel actions SELECT, CLONE, UNDROP can be performed on historical data in the table</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td>Role that owns the table</td>
</tr>
<tr>
    <td><CopyableCode code="owner_role_type" /></td>
    <td><code>string</code></td>
    <td>The type of role that owns the object.</td>
</tr>
<tr>
    <td><CopyableCode code="rows" /></td>
    <td><code>integer (int64)</code></td>
    <td>Number of rows in the table. Returns NULL for external tables.</td>
</tr>
<tr>
    <td><CopyableCode code="search_optimization" /></td>
    <td><code>boolean</code></td>
    <td>If ON, the table has the search optimization service enabled</td>
</tr>
<tr>
    <td><CopyableCode code="search_optimization_bytes" /></td>
    <td><code>integer (int64)</code></td>
    <td>Number of additional bytes of storage that the search optimization service consumes for this table</td>
</tr>
<tr>
    <td><CopyableCode code="search_optimization_progress" /></td>
    <td><code>integer (int64)</code></td>
    <td>Percentage of the table that has been optimized for search.</td>
</tr>
<tr>
    <td><CopyableCode code="table_type" /></td>
    <td><code>string</code></td>
    <td>Type of the table</td>
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
    <td><a href="#list_tables"><CopyableCode code="list_tables" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-like">like</a>, <a href="#parameter-startsWith">startsWith</a>, <a href="#parameter-showLimit">showLimit</a>, <a href="#parameter-fromName">fromName</a>, <a href="#parameter-history">history</a>, <a href="#parameter-deep">deep</a></td>
    <td>Lists the tables under the database and schema.</td>
</tr>
<tr>
    <td><a href="#fetch_table"><CopyableCode code="fetch_table" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td></td>
    <td>Fetch a Table using the describe command output.</td>
</tr>
<tr>
    <td><a href="#create_table"><CopyableCode code="create_table" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-createMode">createMode</a>, <a href="#parameter-copyGrants">copyGrants</a></td>
    <td>Create a table.</td>
</tr>
<tr>
    <td><a href="#create_or_alter_table"><CopyableCode code="create_or_alter_table" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td></td>
    <td>Create a (or alter an existing) table. Even if the operation is just an alter, the full property set must be provided.</td>
</tr>
<tr>
    <td><a href="#delete_table"><CopyableCode code="delete_table" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-ifExists">ifExists</a></td>
    <td>Delete a table with the given name.</td>
</tr>
<tr>
    <td><a href="#create_table_as_select_deprecated"><CopyableCode code="create_table_as_select_deprecated" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-query">query</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-createMode">createMode</a>, <a href="#parameter-copyGrants">copyGrants</a></td>
    <td>Create a table as select.</td>
</tr>
<tr>
    <td><a href="#create_table_as_select"><CopyableCode code="create_table_as_select" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-query">query</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-createMode">createMode</a>, <a href="#parameter-copyGrants">copyGrants</a></td>
    <td>Create a table as select.</td>
</tr>
<tr>
    <td><a href="#create_table_using_template_deprecated"><CopyableCode code="create_table_using_template_deprecated" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-query">query</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-createMode">createMode</a>, <a href="#parameter-copyGrants">copyGrants</a></td>
    <td>Create a table using template.</td>
</tr>
<tr>
    <td><a href="#create_table_using_template"><CopyableCode code="create_table_using_template" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-query">query</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-createMode">createMode</a>, <a href="#parameter-copyGrants">copyGrants</a></td>
    <td>Create a table using template.</td>
</tr>
<tr>
    <td><a href="#clone_table"><CopyableCode code="clone_table" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-createMode">createMode</a>, <a href="#parameter-copyGrants">copyGrants</a>, <a href="#parameter-targetDatabase">targetDatabase</a>, <a href="#parameter-targetSchema">targetSchema</a></td>
    <td>Create a new table by cloning from the specified resource</td>
</tr>
<tr>
    <td><a href="#create_table_like_deprecated"><CopyableCode code="create_table_like_deprecated" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-newTableName">newTableName</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-createMode">createMode</a>, <a href="#parameter-copyGrants">copyGrants</a></td>
    <td>Create a new table like the specified resource, but empty</td>
</tr>
<tr>
    <td><a href="#create_table_like"><CopyableCode code="create_table_like" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-createMode">createMode</a>, <a href="#parameter-copyGrants">copyGrants</a></td>
    <td>Create a new table like the specified resource, but empty</td>
</tr>
<tr>
    <td><a href="#undrop_table"><CopyableCode code="undrop_table" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td></td>
    <td>Undrop specified table</td>
</tr>
<tr>
    <td><a href="#suspend_recluster_table_deprecated"><CopyableCode code="suspend_recluster_table_deprecated" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-ifExists">ifExists</a></td>
    <td>Suspend recluster of a table</td>
</tr>
<tr>
    <td><a href="#suspend_recluster_table"><CopyableCode code="suspend_recluster_table" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-ifExists">ifExists</a></td>
    <td>Suspend recluster of a table</td>
</tr>
<tr>
    <td><a href="#resume_recluster_table_deprecated"><CopyableCode code="resume_recluster_table_deprecated" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-ifExists">ifExists</a></td>
    <td>Resume recluster of a table</td>
</tr>
<tr>
    <td><a href="#resume_recluster_table"><CopyableCode code="resume_recluster_table" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-ifExists">ifExists</a></td>
    <td>Resume recluster of a table</td>
</tr>
<tr>
    <td><a href="#swap_with_table_deprecated"><CopyableCode code="swap_with_table_deprecated" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-targetTableName">targetTableName</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-ifExists">ifExists</a></td>
    <td>Swap with another table</td>
</tr>
<tr>
    <td><a href="#swap_with_table"><CopyableCode code="swap_with_table" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-targetName">targetName</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-ifExists">ifExists</a>, <a href="#parameter-targetDatabase">targetDatabase</a>, <a href="#parameter-targetSchema">targetSchema</a></td>
    <td>Swap with another table</td>
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
<tr id="parameter-database_name">
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>Identifier (i.e. name) for the database to which the resource belongs. You can use the `/api/v2/databases` GET request to get a list of available databases. (pattern: ^"([^"]|"")+"|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
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
<tr id="parameter-newTableName">
    <td><CopyableCode code="newTableName" /></td>
    <td><code>string</code></td>
    <td>The name of the table to be created.</td>
</tr>
<tr id="parameter-query">
    <td><CopyableCode code="query" /></td>
    <td><code>string</code></td>
    <td>The SQL query that uses INFER_SCHEMA on staged files to set the column definitions for the new table.</td>
</tr>
<tr id="parameter-schema_name">
    <td><CopyableCode code="schema_name" /></td>
    <td><code>string</code></td>
    <td>Identifier (i.e. name) for the schema to which the resource belongs. You can use the `/api/v2/databases/{database}/schemas` GET request to get a list of available schemas for the specified database. (pattern: ^"([^"]|"")+"|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
<tr id="parameter-targetName">
    <td><CopyableCode code="targetName" /></td>
    <td><code>string</code></td>
    <td>The name of the target table to be swapped with. (pattern: ^"([^"]|"")+"|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
<tr id="parameter-targetTableName">
    <td><CopyableCode code="targetTableName" /></td>
    <td><code>string</code></td>
    <td>The fully-specified name of the target table to be swapped with.</td>
</tr>
<tr id="parameter-copyGrants">
    <td><CopyableCode code="copyGrants" /></td>
    <td><code>boolean</code></td>
    <td>Query parameter to enable copy grants when creating the object. (example: false, default: false)</td>
</tr>
<tr id="parameter-createMode">
    <td><CopyableCode code="createMode" /></td>
    <td><code>string</code></td>
    <td>Query parameter allowing support for different modes of resource creation. Possible values include: - `errorIfExists`: Throws an error if you try to create a resource that already exists. - `orReplace`: Automatically replaces the existing resource with the current one. - `ifNotExists`: Creates a new resource when an alter is requested for a non-existent resource. (enum: [errorIfExists, orReplace, ifNotExists], example: ifNotExists, default: errorIfExists)</td>
</tr>
<tr id="parameter-deep">
    <td><CopyableCode code="deep" /></td>
    <td><code>boolean</code></td>
    <td>Optionally includes dependency information of the table.</td>
</tr>
<tr id="parameter-fromName">
    <td><CopyableCode code="fromName" /></td>
    <td><code>string</code></td>
    <td>Query parameter to enable fetching rows only following the first row whose object name matches the specified string. Case-sensitive and does not have to be the full name. (example: from_test)</td>
</tr>
<tr id="parameter-history">
    <td><CopyableCode code="history" /></td>
    <td><code>boolean</code></td>
    <td>Optionally includes dropped tables that have not yet been purged.</td>
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
<tr id="parameter-showLimit">
    <td><CopyableCode code="showLimit" /></td>
    <td><code>integer</code></td>
    <td>Query parameter to limit the maximum number of rows returned by a command. (example: 10, minimum: 1, maximum: 10000)</td>
</tr>
<tr id="parameter-startsWith">
    <td><CopyableCode code="startsWith" /></td>
    <td><code>string</code></td>
    <td>Query parameter to filter the command output based on the string of characters that appear at the beginning of the object name. Uses case-sensitive pattern matching. (example: test)</td>
</tr>
<tr id="parameter-targetDatabase">
    <td><CopyableCode code="targetDatabase" /></td>
    <td><code>string</code></td>
    <td>Database of the target table. Defaults to the source table's database. (pattern: ^"([^"]|"")+"|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
<tr id="parameter-targetSchema">
    <td><CopyableCode code="targetSchema" /></td>
    <td><code>string</code></td>
    <td>Schema of the target table. Defaults to the source table's schema. (pattern: ^"([^"]|"")+"|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_tables"
    values={[
        { label: 'list_tables', value: 'list_tables' },
        { label: 'fetch_table', value: 'fetch_table' }
    ]}
>
<TabItem value="list_tables">

Lists the tables under the database and schema.

```sql
SELECT
name,
database_name,
schema_name,
automatic_clustering,
budget,
bytes,
change_tracking,
cluster_by,
columns,
comment,
constraints,
created_on,
data_retention_time_in_days,
default_ddl_collation,
dropped_on,
enable_schema_evolution,
kind,
max_data_extension_time_in_days,
owner,
owner_role_type,
rows,
search_optimization,
search_optimization_bytes,
search_optimization_progress,
table_type
FROM snowflake.table.tables
WHERE database_name = '{{ database_name }}' -- required
AND schema_name = '{{ schema_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND like = '{{ like }}'
AND startsWith = '{{ startsWith }}'
AND showLimit = '{{ showLimit }}'
AND fromName = '{{ fromName }}'
AND history = '{{ history }}'
AND deep = '{{ deep }}';
```
</TabItem>
<TabItem value="fetch_table">

Fetch a Table using the describe command output.

```sql
SELECT
name,
database_name,
schema_name,
automatic_clustering,
budget,
bytes,
change_tracking,
cluster_by,
columns,
comment,
constraints,
created_on,
data_retention_time_in_days,
default_ddl_collation,
dropped_on,
enable_schema_evolution,
kind,
max_data_extension_time_in_days,
owner,
owner_role_type,
rows,
search_optimization,
search_optimization_bytes,
search_optimization_progress,
table_type
FROM snowflake.table.tables
WHERE database_name = '{{ database_name }}' -- required
AND schema_name = '{{ schema_name }}' -- required
AND name = '{{ name }}' -- required
AND endpoint = '{{ endpoint }}' -- required;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_table"
    values={[
        { label: 'create_table', value: 'create_table' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_table">

Create a table.

```sql
INSERT INTO snowflake.table.tables (
data__name,
data__kind,
data__cluster_by,
data__enable_schema_evolution,
data__change_tracking,
data__data_retention_time_in_days,
data__max_data_extension_time_in_days,
data__default_ddl_collation,
data__columns,
data__constraints,
data__comment,
database_name,
schema_name,
endpoint,
createMode,
copyGrants
)
SELECT 
'{{ name }}',
'{{ kind }}',
'{{ cluster_by }}',
{{ enable_schema_evolution }},
{{ change_tracking }},
{{ data_retention_time_in_days }},
{{ max_data_extension_time_in_days }},
'{{ default_ddl_collation }}',
'{{ columns }}',
'{{ constraints }}',
'{{ comment }}',
'{{ database_name }}',
'{{ schema_name }}',
'{{ endpoint }}',
'{{ createMode }}',
'{{ copyGrants }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: tables
  props:
    - name: database_name
      value: string
      description: Required parameter for the tables resource.
    - name: schema_name
      value: string
      description: Required parameter for the tables resource.
    - name: endpoint
      value: string
      description: Required parameter for the tables resource.
    - name: name
      value: string
      description: >
        Specifies the name for the table, must be unique for the schema in which the table is created
        
    - name: kind
      value: string
      description: >
        Table type - permanent, transient, or temporary
        
      valid_values: ['PERMANENT', 'TRANSIENT', 'TEMPORARY', '', 'transient', 'temporary']
      default: PERMANENT
    - name: cluster_by
      value: array
      description: >
        Specifies one or more columns or column expressions in the table as the clustering key
        
    - name: enable_schema_evolution
      value: boolean
      description: >
        Table has schema evolution enabled or disabled
        
    - name: change_tracking
      value: boolean
      description: >
        Change tracking is enabled or disabled
        
    - name: data_retention_time_in_days
      value: integer
      description: >
        Specifies the retention period for the table so that Time Travel actions SELECT, CLONE, UNDROP can be performed on historical data in the table
        
    - name: max_data_extension_time_in_days
      value: integer
      description: >
        Specifies the retention period for the table so that Time Travel actions SELECT, CLONE, UNDROP can be performed on historical data in the table
        
    - name: default_ddl_collation
      value: string
      description: >
        Specifies a default collation specification for the columns in the table, including columns added to the table in the future
        
    - name: columns
      value: array
    - name: constraints
      value: array
    - name: comment
      value: string
      description: >
        Comment for the table
        
    - name: createMode
      value: string
      description: Query parameter allowing support for different modes of resource creation. Possible values include: - `errorIfExists`: Throws an error if you try to create a resource that already exists. - `orReplace`: Automatically replaces the existing resource with the current one. - `ifNotExists`: Creates a new resource when an alter is requested for a non-existent resource. (enum: [errorIfExists, orReplace, ifNotExists], example: ifNotExists, default: errorIfExists)
    - name: copyGrants
      value: boolean
      description: Query parameter to enable copy grants when creating the object. (example: false, default: false)
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_alter_table"
    values={[
        { label: 'create_or_alter_table', value: 'create_or_alter_table' }
    ]}
>
<TabItem value="create_or_alter_table">

Create a (or alter an existing) table. Even if the operation is just an alter, the full property set must be provided.

```sql
REPLACE snowflake.table.tables
SET 
data__name = '{{ name }}',
data__kind = '{{ kind }}',
data__cluster_by = '{{ cluster_by }}',
data__enable_schema_evolution = {{ enable_schema_evolution }},
data__change_tracking = {{ change_tracking }},
data__data_retention_time_in_days = {{ data_retention_time_in_days }},
data__max_data_extension_time_in_days = {{ max_data_extension_time_in_days }},
data__default_ddl_collation = '{{ default_ddl_collation }}',
data__columns = '{{ columns }}',
data__constraints = '{{ constraints }}',
data__comment = '{{ comment }}'
WHERE 
database_name = '{{ database_name }}' --required
AND schema_name = '{{ schema_name }}' --required
AND name = '{{ name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND data__name = '{{ name }}' --required;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_table"
    values={[
        { label: 'delete_table', value: 'delete_table' }
    ]}
>
<TabItem value="delete_table">

Delete a table with the given name.

```sql
DELETE FROM snowflake.table.tables
WHERE database_name = '{{ database_name }}' --required
AND schema_name = '{{ schema_name }}' --required
AND name = '{{ name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND ifExists = '{{ ifExists }}';
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="create_table_as_select_deprecated"
    values={[
        { label: 'create_table_as_select_deprecated', value: 'create_table_as_select_deprecated' },
        { label: 'create_table_as_select', value: 'create_table_as_select' },
        { label: 'create_table_using_template_deprecated', value: 'create_table_using_template_deprecated' },
        { label: 'create_table_using_template', value: 'create_table_using_template' },
        { label: 'clone_table', value: 'clone_table' },
        { label: 'create_table_like_deprecated', value: 'create_table_like_deprecated' },
        { label: 'create_table_like', value: 'create_table_like' },
        { label: 'undrop_table', value: 'undrop_table' },
        { label: 'suspend_recluster_table_deprecated', value: 'suspend_recluster_table_deprecated' },
        { label: 'suspend_recluster_table', value: 'suspend_recluster_table' },
        { label: 'resume_recluster_table_deprecated', value: 'resume_recluster_table_deprecated' },
        { label: 'resume_recluster_table', value: 'resume_recluster_table' },
        { label: 'swap_with_table_deprecated', value: 'swap_with_table_deprecated' },
        { label: 'swap_with_table', value: 'swap_with_table' }
    ]}
>
<TabItem value="create_table_as_select_deprecated">

Create a table as select.

```sql
EXEC snowflake.table.tables.create_table_as_select_deprecated 
@database_name='{{ database_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@name='{{ name }}' --required, 
@query='{{ query }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@createMode='{{ createMode }}', 
@copyGrants={{ copyGrants }} 
@@json=
'{
"name": "{{ name }}", 
"kind": "{{ kind }}", 
"cluster_by": "{{ cluster_by }}", 
"enable_schema_evolution": {{ enable_schema_evolution }}, 
"change_tracking": {{ change_tracking }}, 
"data_retention_time_in_days": {{ data_retention_time_in_days }}, 
"max_data_extension_time_in_days": {{ max_data_extension_time_in_days }}, 
"default_ddl_collation": "{{ default_ddl_collation }}", 
"columns": "{{ columns }}", 
"constraints": "{{ constraints }}", 
"comment": "{{ comment }}"
}';
```
</TabItem>
<TabItem value="create_table_as_select">

Create a table as select.

```sql
EXEC snowflake.table.tables.create_table_as_select 
@database_name='{{ database_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@query='{{ query }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@createMode='{{ createMode }}', 
@copyGrants={{ copyGrants }} 
@@json=
'{
"name": "{{ name }}", 
"columns": "{{ columns }}", 
"cluster_by": "{{ cluster_by }}"
}';
```
</TabItem>
<TabItem value="create_table_using_template_deprecated">

Create a table using template.

```sql
EXEC snowflake.table.tables.create_table_using_template_deprecated 
@database_name='{{ database_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@name='{{ name }}' --required, 
@query='{{ query }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@createMode='{{ createMode }}', 
@copyGrants={{ copyGrants }};
```
</TabItem>
<TabItem value="create_table_using_template">

Create a table using template.

```sql
EXEC snowflake.table.tables.create_table_using_template 
@database_name='{{ database_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@query='{{ query }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@createMode='{{ createMode }}', 
@copyGrants={{ copyGrants }} 
@@json=
'{
"name": "{{ name }}"
}';
```
</TabItem>
<TabItem value="clone_table">

Create a new table by cloning from the specified resource

```sql
EXEC snowflake.table.tables.clone_table 
@database_name='{{ database_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@createMode='{{ createMode }}', 
@copyGrants={{ copyGrants }}, 
@targetDatabase='{{ targetDatabase }}', 
@targetSchema='{{ targetSchema }}' 
@@json=
'{
"name": "{{ name }}", 
"kind": "{{ kind }}", 
"cluster_by": "{{ cluster_by }}", 
"enable_schema_evolution": {{ enable_schema_evolution }}, 
"change_tracking": {{ change_tracking }}, 
"data_retention_time_in_days": {{ data_retention_time_in_days }}, 
"max_data_extension_time_in_days": {{ max_data_extension_time_in_days }}, 
"default_ddl_collation": "{{ default_ddl_collation }}", 
"columns": "{{ columns }}", 
"constraints": "{{ constraints }}", 
"comment": "{{ comment }}"
}';
```
</TabItem>
<TabItem value="create_table_like_deprecated">

Create a new table like the specified resource, but empty

```sql
EXEC snowflake.table.tables.create_table_like_deprecated 
@database_name='{{ database_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@name='{{ name }}' --required, 
@newTableName='{{ newTableName }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@createMode='{{ createMode }}', 
@copyGrants={{ copyGrants }};
```
</TabItem>
<TabItem value="create_table_like">

Create a new table like the specified resource, but empty

```sql
EXEC snowflake.table.tables.create_table_like 
@database_name='{{ database_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@createMode='{{ createMode }}', 
@copyGrants={{ copyGrants }} 
@@json=
'{
"name": "{{ name }}"
}';
```
</TabItem>
<TabItem value="undrop_table">

Undrop specified table

```sql
EXEC snowflake.table.tables.undrop_table 
@database_name='{{ database_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required;
```
</TabItem>
<TabItem value="suspend_recluster_table_deprecated">

Suspend recluster of a table

```sql
EXEC snowflake.table.tables.suspend_recluster_table_deprecated 
@database_name='{{ database_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@ifExists={{ ifExists }};
```
</TabItem>
<TabItem value="suspend_recluster_table">

Suspend recluster of a table

```sql
EXEC snowflake.table.tables.suspend_recluster_table 
@database_name='{{ database_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@ifExists={{ ifExists }};
```
</TabItem>
<TabItem value="resume_recluster_table_deprecated">

Resume recluster of a table

```sql
EXEC snowflake.table.tables.resume_recluster_table_deprecated 
@database_name='{{ database_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@ifExists={{ ifExists }};
```
</TabItem>
<TabItem value="resume_recluster_table">

Resume recluster of a table

```sql
EXEC snowflake.table.tables.resume_recluster_table 
@database_name='{{ database_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@ifExists={{ ifExists }};
```
</TabItem>
<TabItem value="swap_with_table_deprecated">

Swap with another table

```sql
EXEC snowflake.table.tables.swap_with_table_deprecated 
@database_name='{{ database_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@name='{{ name }}' --required, 
@targetTableName='{{ targetTableName }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@ifExists={{ ifExists }};
```
</TabItem>
<TabItem value="swap_with_table">

Swap with another table

```sql
EXEC snowflake.table.tables.swap_with_table 
@database_name='{{ database_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@name='{{ name }}' --required, 
@targetName='{{ targetName }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@ifExists={{ ifExists }}, 
@targetDatabase='{{ targetDatabase }}', 
@targetSchema='{{ targetSchema }}';
```
</TabItem>
</Tabs>
