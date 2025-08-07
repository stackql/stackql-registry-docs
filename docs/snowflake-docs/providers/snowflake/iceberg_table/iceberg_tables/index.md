--- 
title: iceberg_tables
hide_title: false
hide_table_of_contents: false
keywords:
  - iceberg_tables
  - iceberg_table
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

Creates, updates, deletes, gets or lists an <code>iceberg_tables</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>iceberg_tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.iceberg_table.iceberg_tables" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_iceberg_tables"
    values={[
        { label: 'list_iceberg_tables', value: 'list_iceberg_tables' },
        { label: 'fetch_iceberg_table', value: 'fetch_iceberg_table' }
    ]}
>
<TabItem value="list_iceberg_tables">

A Snowflake iceberg table

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
    <td>Name of the iceberg table (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr>
    <td><CopyableCode code="catalog_table_name" /></td>
    <td><code>string</code></td>
    <td>Name of the table as recognized by the catalog.</td>
</tr>
<tr>
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>Database in which the iceberg table is stored (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr>
    <td><CopyableCode code="schema_name" /></td>
    <td><code>string</code></td>
    <td>Schema in which the iceberg table is stored (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr>
    <td><CopyableCode code="auto_refresh" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether to automatically refresh the table metadata</td>
</tr>
<tr>
    <td><CopyableCode code="base_location" /></td>
    <td><code>string</code></td>
    <td>The path to a directory where Snowflake can write data and metadata files for the table.</td>
</tr>
<tr>
    <td><CopyableCode code="can_write_metadata" /></td>
    <td><code>string</code></td>
    <td>Signifies whether Snowflake can write metadata to the location specified by the file_path.</td>
</tr>
<tr>
    <td><CopyableCode code="catalog" /></td>
    <td><code>string</code></td>
    <td>Name of the catalog integration to use for iceberg tables</td>
</tr>
<tr>
    <td><CopyableCode code="catalog_namespace" /></td>
    <td><code>string</code></td>
    <td>Catalog namespace for the table. The namespace defined when the table was created. Otherwise, the default namespace associated with the catalog integration used by the table. If you’re syncing the table to Snowflake Open Catalog, the default is null.</td>
</tr>
<tr>
    <td><CopyableCode code="catalog_sync" /></td>
    <td><code>string</code></td>
    <td>Name of the catalog integration to sync this table</td>
</tr>
<tr>
    <td><CopyableCode code="change_tracking" /></td>
    <td><code>boolean</code></td>
    <td>True if change tracking is enabled, allowing streams and CHANGES to be used on the entity.</td>
</tr>
<tr>
    <td><CopyableCode code="cluster_by" /></td>
    <td><code>array</code></td>
    <td>Specifies one or more columns or column expressions in the table as the clustering key.</td>
</tr>
<tr>
    <td><CopyableCode code="columns" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>user comment associated to an object in the dictionary</td>
</tr>
<tr>
    <td><CopyableCode code="constraints" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the iceberg table was created.</td>
</tr>
<tr>
    <td><CopyableCode code="data_retention_time_in_days" /></td>
    <td><code>integer</code></td>
    <td>number of days to retain the old version of deleted/updated data</td>
</tr>
<tr>
    <td><CopyableCode code="external_volume" /></td>
    <td><code>string</code></td>
    <td>Name of an external volume that will be used for persisted Iceberg metadata and data files.</td>
</tr>
<tr>
    <td><CopyableCode code="iceberg_table_type" /></td>
    <td><code>string</code></td>
    <td>Type of Iceberg table. UNMANAGED if the table is not managed by Snowflake. NOT ICEBERG otherwise.</td>
</tr>
<tr>
    <td><CopyableCode code="max_data_extension_time_in_days" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of days to extend data retention beyond the retention period to prevent a stream becoming stale.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata_file_path" /></td>
    <td><code>string</code></td>
    <td>Specifies the relative path of the Iceberg metadata file to use for column definitions.</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td>Role that owns the iceberg table (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr>
    <td><CopyableCode code="owner_role_type" /></td>
    <td><code>string</code></td>
    <td>The type of role that owns the iceberg table (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr>
    <td><CopyableCode code="replace_invalid_characters" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether to replace invalid characters in the column names</td>
</tr>
<tr>
    <td><CopyableCode code="storage_serialization_policy" /></td>
    <td><code>string</code></td>
    <td>Storage serialization policy used for managed Iceberg table. This include encodings and compressions</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="fetch_iceberg_table">

A Snowflake iceberg table

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
    <td>Name of the iceberg table (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr>
    <td><CopyableCode code="catalog_table_name" /></td>
    <td><code>string</code></td>
    <td>Name of the table as recognized by the catalog.</td>
</tr>
<tr>
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>Database in which the iceberg table is stored (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr>
    <td><CopyableCode code="schema_name" /></td>
    <td><code>string</code></td>
    <td>Schema in which the iceberg table is stored (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr>
    <td><CopyableCode code="auto_refresh" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether to automatically refresh the table metadata</td>
</tr>
<tr>
    <td><CopyableCode code="base_location" /></td>
    <td><code>string</code></td>
    <td>The path to a directory where Snowflake can write data and metadata files for the table.</td>
</tr>
<tr>
    <td><CopyableCode code="can_write_metadata" /></td>
    <td><code>string</code></td>
    <td>Signifies whether Snowflake can write metadata to the location specified by the file_path.</td>
</tr>
<tr>
    <td><CopyableCode code="catalog" /></td>
    <td><code>string</code></td>
    <td>Name of the catalog integration to use for iceberg tables</td>
</tr>
<tr>
    <td><CopyableCode code="catalog_namespace" /></td>
    <td><code>string</code></td>
    <td>Catalog namespace for the table. The namespace defined when the table was created. Otherwise, the default namespace associated with the catalog integration used by the table. If you’re syncing the table to Snowflake Open Catalog, the default is null.</td>
</tr>
<tr>
    <td><CopyableCode code="catalog_sync" /></td>
    <td><code>string</code></td>
    <td>Name of the catalog integration to sync this table</td>
</tr>
<tr>
    <td><CopyableCode code="change_tracking" /></td>
    <td><code>boolean</code></td>
    <td>True if change tracking is enabled, allowing streams and CHANGES to be used on the entity.</td>
</tr>
<tr>
    <td><CopyableCode code="cluster_by" /></td>
    <td><code>array</code></td>
    <td>Specifies one or more columns or column expressions in the table as the clustering key.</td>
</tr>
<tr>
    <td><CopyableCode code="columns" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>user comment associated to an object in the dictionary</td>
</tr>
<tr>
    <td><CopyableCode code="constraints" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the iceberg table was created.</td>
</tr>
<tr>
    <td><CopyableCode code="data_retention_time_in_days" /></td>
    <td><code>integer</code></td>
    <td>number of days to retain the old version of deleted/updated data</td>
</tr>
<tr>
    <td><CopyableCode code="external_volume" /></td>
    <td><code>string</code></td>
    <td>Name of an external volume that will be used for persisted Iceberg metadata and data files.</td>
</tr>
<tr>
    <td><CopyableCode code="iceberg_table_type" /></td>
    <td><code>string</code></td>
    <td>Type of Iceberg table. UNMANAGED if the table is not managed by Snowflake. NOT ICEBERG otherwise.</td>
</tr>
<tr>
    <td><CopyableCode code="max_data_extension_time_in_days" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of days to extend data retention beyond the retention period to prevent a stream becoming stale.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata_file_path" /></td>
    <td><code>string</code></td>
    <td>Specifies the relative path of the Iceberg metadata file to use for column definitions.</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td>Role that owns the iceberg table (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr>
    <td><CopyableCode code="owner_role_type" /></td>
    <td><code>string</code></td>
    <td>The type of role that owns the iceberg table (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr>
    <td><CopyableCode code="replace_invalid_characters" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether to replace invalid characters in the column names</td>
</tr>
<tr>
    <td><CopyableCode code="storage_serialization_policy" /></td>
    <td><code>string</code></td>
    <td>Storage serialization policy used for managed Iceberg table. This include encodings and compressions</td>
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
    <td><a href="#list_iceberg_tables"><CopyableCode code="list_iceberg_tables" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-like"><code>like</code></a>, <a href="#parameter-startsWith"><code>startsWith</code></a>, <a href="#parameter-showLimit"><code>showLimit</code></a>, <a href="#parameter-fromName"><code>fromName</code></a>, <a href="#parameter-deep"><code>deep</code></a></td>
    <td>Lists the Apache Iceberg™ tables for which you have access privileges.</td>
</tr>
<tr>
    <td><a href="#fetch_iceberg_table"><CopyableCode code="fetch_iceberg_table" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Describe an iceberg table</td>
</tr>
<tr>
    <td><a href="#create_snowflake_managed_iceberg_table"><CopyableCode code="create_snowflake_managed_iceberg_table" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-createMode"><code>createMode</code></a>, <a href="#parameter-copyGrants"><code>copyGrants</code></a></td>
    <td>Create a snowflake managed iceberg table (clone and undrop are separate subresources)</td>
</tr>
<tr>
    <td><a href="#drop_iceberg_table"><CopyableCode code="drop_iceberg_table" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-ifExists"><code>ifExists</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td>Drop an iceberg table</td>
</tr>
<tr>
    <td><a href="#create_snowflake_managed_iceberg_table_as_select"><CopyableCode code="create_snowflake_managed_iceberg_table_as_select" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-createMode"><code>createMode</code></a>, <a href="#parameter-copyGrants"><code>copyGrants</code></a></td>
    <td>Create a snowflake managed iceberg table as select</td>
</tr>
<tr>
    <td><a href="#create_unmanaged_iceberg_table_from_aws_glue_catalog"><CopyableCode code="create_unmanaged_iceberg_table_from_aws_glue_catalog" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-createMode"><code>createMode</code></a></td>
    <td>Create an unmanaged iceberg table from AWS Glue catalog</td>
</tr>
<tr>
    <td><a href="#create_unmanaged_iceberg_table_from_delta"><CopyableCode code="create_unmanaged_iceberg_table_from_delta" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-createMode"><code>createMode</code></a></td>
    <td>Create an unmanaged iceberg table from Delta</td>
</tr>
<tr>
    <td><a href="#create_unmanaged_iceberg_table_from_iceberg_files"><CopyableCode code="create_unmanaged_iceberg_table_from_iceberg_files" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-createMode"><code>createMode</code></a></td>
    <td>Create an unmanaged iceberg table from Iceberg files</td>
</tr>
<tr>
    <td><a href="#create_unmanaged_iceberg_table_from_iceberg_rest"><CopyableCode code="create_unmanaged_iceberg_table_from_iceberg_rest" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-createMode"><code>createMode</code></a></td>
    <td>Create an unmanaged iceberg table from Iceberg REST</td>
</tr>
<tr>
    <td><a href="#resume_recluster_iceberg_table"><CopyableCode code="resume_recluster_iceberg_table" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-ifExists"><code>ifExists</code></a></td>
    <td>Resume recluster of an iceberg table (iceberg tables managed by an external catalog do not allow clustering)</td>
</tr>
<tr>
    <td><a href="#suspend_recluster_iceberg_table"><CopyableCode code="suspend_recluster_iceberg_table" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-ifExists"><code>ifExists</code></a></td>
    <td>Suspend recluster of an iceberg table (iceberg tables managed by an external catalog do not allow clustering)</td>
</tr>
<tr>
    <td><a href="#refresh_iceberg_table"><CopyableCode code="refresh_iceberg_table" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-ifExists"><code>ifExists</code></a></td>
    <td>Refreshes the metadata for an Apache Iceberg table that uses an external Iceberg catalog</td>
</tr>
<tr>
    <td><a href="#convert_to_managed_iceberg_table"><CopyableCode code="convert_to_managed_iceberg_table" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-ifExists"><code>ifExists</code></a></td>
    <td>Convert unmanaged iceberg table to managed iceberg table</td>
</tr>
<tr>
    <td><a href="#undrop_iceberg_table"><CopyableCode code="undrop_iceberg_table" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Undrop an iceberg table</td>
</tr>
<tr>
    <td><a href="#clone_snowflake_managed_iceberg_table"><CopyableCode code="clone_snowflake_managed_iceberg_table" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-createMode"><code>createMode</code></a>, <a href="#parameter-copyGrants"><code>copyGrants</code></a>, <a href="#parameter-targetDatabase"><code>targetDatabase</code></a>, <a href="#parameter-targetSchema"><code>targetSchema</code></a></td>
    <td>Clone a snowflake managed iceberg table</td>
</tr>
<tr>
    <td><a href="#create_snowflake_managed_iceberg_table_like"><CopyableCode code="create_snowflake_managed_iceberg_table_like" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-createMode"><code>createMode</code></a>, <a href="#parameter-copyGrants"><code>copyGrants</code></a>, <a href="#parameter-targetDatabase"><code>targetDatabase</code></a>, <a href="#parameter-targetSchema"><code>targetSchema</code></a></td>
    <td>Creates a new table with the same column definitions as an existing table, but without copying data from the existing table.</td>
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
<tr id="parameter-database_name">
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>Identifier (i.e. name) for the database to which the resource belongs. You can use the <code>/api/v2/databases</code> GET request to get a list of available databases.</td>
</tr>
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
<tr id="parameter-query">
    <td><CopyableCode code="query" /></td>
    <td><code>string</code></td>
    <td>The SQL select query to run to set up the table values (and possibly columns).</td>
</tr>
<tr id="parameter-schema_name">
    <td><CopyableCode code="schema_name" /></td>
    <td><code>string</code></td>
    <td>Identifier (i.e. name) for the schema to which the resource belongs. You can use the <code>/api/v2/databases/&#123;database&#125;/schemas</code> GET request to get a list of available schemas for the specified database.</td>
</tr>
<tr id="parameter-copyGrants">
    <td><CopyableCode code="copyGrants" /></td>
    <td><code>boolean</code></td>
    <td>Query parameter to enable copy grants when creating the object.</td>
</tr>
<tr id="parameter-createMode">
    <td><CopyableCode code="createMode" /></td>
    <td><code>string</code></td>
    <td>Query parameter allowing support for different modes of resource creation. Possible values include: - <code>errorIfExists</code>: Throws an error if you try to create a resource that already exists. - <code>orReplace</code>: Automatically replaces the existing resource with the current one. - <code>ifNotExists</code>: Creates a new resource when an alter is requested for a non-existent resource.</td>
</tr>
<tr id="parameter-deep">
    <td><CopyableCode code="deep" /></td>
    <td><code>boolean</code></td>
    <td>Optionally includes dependency information of the table.</td>
</tr>
<tr id="parameter-fromName">
    <td><CopyableCode code="fromName" /></td>
    <td><code>string</code></td>
    <td>Query parameter to enable fetching rows only following the first row whose object name matches the specified string. Case-sensitive and does not have to be the full name.</td>
</tr>
<tr id="parameter-ifExists">
    <td><CopyableCode code="ifExists" /></td>
    <td><code>boolean</code></td>
    <td>Query parameter that specifies how to handle the request for a resource that does not exist: - <code>true</code>: The endpoint does not throw an error if the resource does not exist. It returns a 200 success response, but does not take any action on the resource. - <code>false</code>: The endpoint throws an error if the resource doesn't exist.</td>
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
<tr id="parameter-targetDatabase">
    <td><CopyableCode code="targetDatabase" /></td>
    <td><code>string</code></td>
    <td>Database of the newly created table. Defaults to the source table's database.</td>
</tr>
<tr id="parameter-targetSchema">
    <td><CopyableCode code="targetSchema" /></td>
    <td><code>string</code></td>
    <td>Schema of the newly created table. Defaults to the source table's schema.</td>
</tr>
<tr id="parameter-type">
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Specifies whether the table can be dropped if foreign keys exist that reference the table.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_iceberg_tables"
    values={[
        { label: 'list_iceberg_tables', value: 'list_iceberg_tables' },
        { label: 'fetch_iceberg_table', value: 'fetch_iceberg_table' }
    ]}
>
<TabItem value="list_iceberg_tables">

Lists the Apache Iceberg™ tables for which you have access privileges.

```sql
SELECT
name,
catalog_table_name,
database_name,
schema_name,
auto_refresh,
base_location,
can_write_metadata,
catalog,
catalog_namespace,
catalog_sync,
change_tracking,
cluster_by,
columns,
comment,
constraints,
created_on,
data_retention_time_in_days,
external_volume,
iceberg_table_type,
max_data_extension_time_in_days,
metadata_file_path,
owner,
owner_role_type,
replace_invalid_characters,
storage_serialization_policy
FROM snowflake.iceberg_table.iceberg_tables
WHERE database_name = '{{ database_name }}' -- required
AND schema_name = '{{ schema_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND like = '{{ like }}'
AND startsWith = '{{ startsWith }}'
AND showLimit = '{{ showLimit }}'
AND fromName = '{{ fromName }}'
AND deep = '{{ deep }}';
```
</TabItem>
<TabItem value="fetch_iceberg_table">

Describe an iceberg table

```sql
SELECT
name,
catalog_table_name,
database_name,
schema_name,
auto_refresh,
base_location,
can_write_metadata,
catalog,
catalog_namespace,
catalog_sync,
change_tracking,
cluster_by,
columns,
comment,
constraints,
created_on,
data_retention_time_in_days,
external_volume,
iceberg_table_type,
max_data_extension_time_in_days,
metadata_file_path,
owner,
owner_role_type,
replace_invalid_characters,
storage_serialization_policy
FROM snowflake.iceberg_table.iceberg_tables
WHERE database_name = '{{ database_name }}' -- required
AND schema_name = '{{ schema_name }}' -- required
AND name = '{{ name }}' -- required
AND endpoint = '{{ endpoint }}' -- required;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_snowflake_managed_iceberg_table"
    values={[
        { label: 'create_snowflake_managed_iceberg_table', value: 'create_snowflake_managed_iceberg_table' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_snowflake_managed_iceberg_table">

Create a snowflake managed iceberg table (clone and undrop are separate subresources)

```sql
INSERT INTO snowflake.iceberg_table.iceberg_tables (
data__name,
data__comment,
data__change_tracking,
data__max_data_extension_time_in_days,
data__external_volume,
data__data_retention_time_in_days,
data__catalog_sync,
data__catalog,
data__storage_serialization_policy,
data__catalog_table_name,
data__catalog_namespace,
data__cluster_by,
data__columns,
data__base_location,
data__replace_invalid_characters,
data__metadata_file_path,
data__constraints,
database_name,
schema_name,
endpoint,
createMode,
copyGrants
)
SELECT 
'{{ name }}',
'{{ comment }}',
{{ change_tracking }},
{{ max_data_extension_time_in_days }},
'{{ external_volume }}',
{{ data_retention_time_in_days }},
'{{ catalog_sync }}',
'{{ catalog }}',
'{{ storage_serialization_policy }}',
'{{ catalog_table_name }}',
'{{ catalog_namespace }}',
'{{ cluster_by }}',
'{{ columns }}',
'{{ base_location }}',
{{ replace_invalid_characters }},
'{{ metadata_file_path }}',
'{{ constraints }}',
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
- name: iceberg_tables
  props:
    - name: database_name
      value: string
      description: Required parameter for the iceberg_tables resource.
    - name: schema_name
      value: string
      description: Required parameter for the iceberg_tables resource.
    - name: endpoint
      value: string
      description: Required parameter for the iceberg_tables resource.
    - name: name
      value: string
      description: >
        Name of the iceberg table
        
    - name: comment
      value: string
      description: >
        user comment associated to an object in the dictionary
        
    - name: change_tracking
      value: boolean
      description: >
        True if change tracking is enabled, allowing streams and CHANGES to be used on the entity.
        
    - name: max_data_extension_time_in_days
      value: integer
      description: >
        Maximum number of days to extend data retention beyond the retention period to prevent a stream becoming stale.
        
    - name: external_volume
      value: string
      description: >
        Name of an external volume that will be used for persisted Iceberg metadata and data files.
        
    - name: data_retention_time_in_days
      value: integer
      description: >
        number of days to retain the old version of deleted/updated data
        
    - name: catalog_sync
      value: string
      description: >
        Name of the catalog integration to sync this table
        
    - name: catalog
      value: string
      description: >
        Name of the catalog integration to use for iceberg tables
        
    - name: storage_serialization_policy
      value: string
      description: >
        Storage serialization policy used for managed Iceberg table. This include encodings and compressions
        
      valid_values: ['COMPATIBLE', 'OPTIMIZED']
    - name: catalog_table_name
      value: string
      description: >
        Name of the table as recognized by the catalog.
        
    - name: catalog_namespace
      value: string
      description: >
        Catalog namespace for the table. The namespace defined when the table was created. Otherwise, the default namespace associated with the catalog integration used by the table. If you’re syncing the table to Snowflake Open Catalog, the default is null.
        
    - name: cluster_by
      value: array
      description: >
        Specifies one or more columns or column expressions in the table as the clustering key.
        
    - name: columns
      value: array
    - name: base_location
      value: string
      description: >
        The path to a directory where Snowflake can write data and metadata files for the table.
        
    - name: replace_invalid_characters
      value: boolean
      description: >
        Specifies whether to replace invalid characters in the column names
        
    - name: metadata_file_path
      value: string
      description: >
        Specifies the relative path of the Iceberg metadata file to use for column definitions.
        
    - name: constraints
      value: array
    - name: createMode
      value: string
      description: Query parameter allowing support for different modes of resource creation. Possible values include: - `errorIfExists`: Throws an error if you try to create a resource that already exists. - `orReplace`: Automatically replaces the existing resource with the current one. - `ifNotExists`: Creates a new resource when an alter is requested for a non-existent resource.
    - name: copyGrants
      value: boolean
      description: Query parameter to enable copy grants when creating the object.
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="drop_iceberg_table"
    values={[
        { label: 'drop_iceberg_table', value: 'drop_iceberg_table' }
    ]}
>
<TabItem value="drop_iceberg_table">

Drop an iceberg table

```sql
DELETE FROM snowflake.iceberg_table.iceberg_tables
WHERE database_name = '{{ database_name }}' --required
AND schema_name = '{{ schema_name }}' --required
AND name = '{{ name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND ifExists = '{{ ifExists }}'
AND type = '{{ type }}';
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="create_snowflake_managed_iceberg_table_as_select"
    values={[
        { label: 'create_snowflake_managed_iceberg_table_as_select', value: 'create_snowflake_managed_iceberg_table_as_select' },
        { label: 'create_unmanaged_iceberg_table_from_aws_glue_catalog', value: 'create_unmanaged_iceberg_table_from_aws_glue_catalog' },
        { label: 'create_unmanaged_iceberg_table_from_delta', value: 'create_unmanaged_iceberg_table_from_delta' },
        { label: 'create_unmanaged_iceberg_table_from_iceberg_files', value: 'create_unmanaged_iceberg_table_from_iceberg_files' },
        { label: 'create_unmanaged_iceberg_table_from_iceberg_rest', value: 'create_unmanaged_iceberg_table_from_iceberg_rest' },
        { label: 'resume_recluster_iceberg_table', value: 'resume_recluster_iceberg_table' },
        { label: 'suspend_recluster_iceberg_table', value: 'suspend_recluster_iceberg_table' },
        { label: 'refresh_iceberg_table', value: 'refresh_iceberg_table' },
        { label: 'convert_to_managed_iceberg_table', value: 'convert_to_managed_iceberg_table' },
        { label: 'undrop_iceberg_table', value: 'undrop_iceberg_table' },
        { label: 'clone_snowflake_managed_iceberg_table', value: 'clone_snowflake_managed_iceberg_table' },
        { label: 'create_snowflake_managed_iceberg_table_like', value: 'create_snowflake_managed_iceberg_table_like' }
    ]}
>
<TabItem value="create_snowflake_managed_iceberg_table_as_select">

Create a snowflake managed iceberg table as select

```sql
EXEC snowflake.iceberg_table.iceberg_tables.create_snowflake_managed_iceberg_table_as_select 
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
"external_volume": "{{ external_volume }}", 
"cluster_by": "{{ cluster_by }}", 
"base_location": "{{ base_location }}", 
"comment": "{{ comment }}"
}';
```
</TabItem>
<TabItem value="create_unmanaged_iceberg_table_from_aws_glue_catalog">

Create an unmanaged iceberg table from AWS Glue catalog

```sql
EXEC snowflake.iceberg_table.iceberg_tables.create_unmanaged_iceberg_table_from_aws_glue_catalog 
@database_name='{{ database_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@createMode='{{ createMode }}' 
@@json=
'{
"name": "{{ name }}", 
"external_volume": "{{ external_volume }}", 
"catalog_table_name": "{{ catalog_table_name }}", 
"catalog_namespace": "{{ catalog_namespace }}", 
"replace_invalid_characters": {{ replace_invalid_characters }}, 
"auto_refresh": {{ auto_refresh }}, 
"catalog": "{{ catalog }}", 
"comment": "{{ comment }}"
}';
```
</TabItem>
<TabItem value="create_unmanaged_iceberg_table_from_delta">

Create an unmanaged iceberg table from Delta

```sql
EXEC snowflake.iceberg_table.iceberg_tables.create_unmanaged_iceberg_table_from_delta 
@database_name='{{ database_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@createMode='{{ createMode }}' 
@@json=
'{
"name": "{{ name }}", 
"external_volume": "{{ external_volume }}", 
"replace_invalid_characters": {{ replace_invalid_characters }}, 
"base_location": "{{ base_location }}", 
"catalog": "{{ catalog }}", 
"comment": "{{ comment }}"
}';
```
</TabItem>
<TabItem value="create_unmanaged_iceberg_table_from_iceberg_files">

Create an unmanaged iceberg table from Iceberg files

```sql
EXEC snowflake.iceberg_table.iceberg_tables.create_unmanaged_iceberg_table_from_iceberg_files 
@database_name='{{ database_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@createMode='{{ createMode }}' 
@@json=
'{
"name": "{{ name }}", 
"external_volume": "{{ external_volume }}", 
"replace_invalid_characters": {{ replace_invalid_characters }}, 
"metadata_file_path": "{{ metadata_file_path }}", 
"catalog": "{{ catalog }}", 
"comment": "{{ comment }}"
}';
```
</TabItem>
<TabItem value="create_unmanaged_iceberg_table_from_iceberg_rest">

Create an unmanaged iceberg table from Iceberg REST

```sql
EXEC snowflake.iceberg_table.iceberg_tables.create_unmanaged_iceberg_table_from_iceberg_rest 
@database_name='{{ database_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@createMode='{{ createMode }}' 
@@json=
'{
"name": "{{ name }}", 
"external_volume": "{{ external_volume }}", 
"catalog_table_name": "{{ catalog_table_name }}", 
"catalog_namespace": "{{ catalog_namespace }}", 
"replace_invalid_characters": {{ replace_invalid_characters }}, 
"auto_refresh": {{ auto_refresh }}, 
"catalog": "{{ catalog }}", 
"comment": "{{ comment }}"
}';
```
</TabItem>
<TabItem value="resume_recluster_iceberg_table">

Resume recluster of an iceberg table (iceberg tables managed by an external catalog do not allow clustering)

```sql
EXEC snowflake.iceberg_table.iceberg_tables.resume_recluster_iceberg_table 
@database_name='{{ database_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@ifExists={{ ifExists }};
```
</TabItem>
<TabItem value="suspend_recluster_iceberg_table">

Suspend recluster of an iceberg table (iceberg tables managed by an external catalog do not allow clustering)

```sql
EXEC snowflake.iceberg_table.iceberg_tables.suspend_recluster_iceberg_table 
@database_name='{{ database_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@ifExists={{ ifExists }};
```
</TabItem>
<TabItem value="refresh_iceberg_table">

Refreshes the metadata for an Apache Iceberg table that uses an external Iceberg catalog

```sql
EXEC snowflake.iceberg_table.iceberg_tables.refresh_iceberg_table 
@database_name='{{ database_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@ifExists={{ ifExists }} 
@@json=
'{
"metadata_file_relative_path": "{{ metadata_file_relative_path }}"
}';
```
</TabItem>
<TabItem value="convert_to_managed_iceberg_table">

Convert unmanaged iceberg table to managed iceberg table

```sql
EXEC snowflake.iceberg_table.iceberg_tables.convert_to_managed_iceberg_table 
@database_name='{{ database_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@ifExists={{ ifExists }} 
@@json=
'{
"base_location": "{{ base_location }}", 
"storage_serialization_policy": "{{ storage_serialization_policy }}"
}';
```
</TabItem>
<TabItem value="undrop_iceberg_table">

Undrop an iceberg table

```sql
EXEC snowflake.iceberg_table.iceberg_tables.undrop_iceberg_table 
@database_name='{{ database_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required;
```
</TabItem>
<TabItem value="clone_snowflake_managed_iceberg_table">

Clone a snowflake managed iceberg table

```sql
EXEC snowflake.iceberg_table.iceberg_tables.clone_snowflake_managed_iceberg_table 
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
"point_of_time": "{{ point_of_time }}"
}';
```
</TabItem>
<TabItem value="create_snowflake_managed_iceberg_table_like">

Creates a new table with the same column definitions as an existing table, but without copying data from the existing table.

```sql
EXEC snowflake.iceberg_table.iceberg_tables.create_snowflake_managed_iceberg_table_like 
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
"cluster_by": "{{ cluster_by }}", 
"external_volume": "{{ external_volume }}", 
"base_location": "{{ base_location }}", 
"comment": "{{ comment }}"
}';
```
</TabItem>
</Tabs>
