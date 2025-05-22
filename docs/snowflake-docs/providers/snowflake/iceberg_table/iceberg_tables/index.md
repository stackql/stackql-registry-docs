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

Creates, updates, deletes, gets or lists a <code>iceberg_tables</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>iceberg_tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.iceberg_table.iceberg_tables" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the iceberg table |
| <CopyableCode code="auto_refresh" /> | `boolean` | Specifies whether to automatically refresh the table metadata |
| <CopyableCode code="base_location" /> | `string` | The path to a directory where Snowflake can write data and metadata files for the table. |
| <CopyableCode code="can_write_metadata" /> | `string` | Signifies whether Snowflake can write metadata to the location specified by the file_path. |
| <CopyableCode code="catalog" /> | `string` | Name of the catalog integration to use for iceberg tables |
| <CopyableCode code="catalog_namespace" /> | `string` | Catalog namespace for the table. The namespace defined when the table was created. Otherwise, the default namespace associated with the catalog integration used by the table. If you’re syncing the table to Snowflake Open Catalog, the default is null. |
| <CopyableCode code="catalog_sync" /> | `string` | Name of the catalog integration to sync this table |
| <CopyableCode code="catalog_table_name" /> | `string` | Name of the table as recognized by the catalog. |
| <CopyableCode code="change_tracking" /> | `boolean` | True if change tracking is enabled, allowing streams and CHANGES to be used on the entity. |
| <CopyableCode code="cluster_by" /> | `array` | Specifies one or more columns or column expressions in the table as the clustering key. |
| <CopyableCode code="columns" /> | `array` |  |
| <CopyableCode code="comment" /> | `string` | user comment associated to an object in the dictionary |
| <CopyableCode code="constraints" /> | `array` |  |
| <CopyableCode code="created_on" /> | `string` | Date and time when the iceberg table was created. |
| <CopyableCode code="data_retention_time_in_days" /> | `integer` | number of days to retain the old version of deleted/updated data |
| <CopyableCode code="database_name" /> | `string` | Database in which the iceberg table is stored |
| <CopyableCode code="external_volume" /> | `string` | Name of an external volume that will be used for persisted Iceberg metadata and data files. |
| <CopyableCode code="iceberg_table_type" /> | `string` | Type of Iceberg table. UNMANAGED if the table is not managed by Snowflake. NOT ICEBERG otherwise. |
| <CopyableCode code="max_data_extension_time_in_days" /> | `integer` | Maximum number of days to extend data retention beyond the retention period to prevent a stream becoming stale. |
| <CopyableCode code="metadata_file_path" /> | `string` | Specifies the relative path of the Iceberg metadata file to use for column definitions. |
| <CopyableCode code="owner" /> | `string` | Role that owns the iceberg table |
| <CopyableCode code="owner_role_type" /> | `string` | The type of role that owns the iceberg table |
| <CopyableCode code="replace_invalid_characters" /> | `boolean` | Specifies whether to replace invalid characters in the column names |
| <CopyableCode code="schema_name" /> | `string` | Schema in which the iceberg table is stored |
| <CopyableCode code="storage_serialization_policy" /> | `string` | Storage serialization policy used for managed Iceberg table. This include encodings and compressions |

## Methods
| Name | Accessible by | Required Params | Optional Params | Description |
|:-----|:--------------|:----------------|:----------------|:------------|
| <CopyableCode code="fetch_iceberg_table" /> | `SELECT` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | - | Describe an iceberg table |
| <CopyableCode code="list_iceberg_tables" /> | `SELECT` | <CopyableCode code="database_name, schema_name, endpoint" /> | <CopyableCode code="like" />, <CopyableCode code="startsWith" />, <CopyableCode code="showLimit" />, <CopyableCode code="fromName" />, <CopyableCode code="deep" /> | Lists the Apache Iceberg™ tables for which you have access privileges. |
| <CopyableCode code="create_snowflake_managed_iceberg_table" /> | `INSERT` | <CopyableCode code="database_name, schema_name, data__name, endpoint" /> | <CopyableCode code="createMode" />, <CopyableCode code="copyGrants" /> | Create a snowflake managed iceberg table (clone and undrop are separate subresources) |
| <CopyableCode code="drop_iceberg_table" /> | `DELETE` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | <CopyableCode code="ifExists" />, <CopyableCode code="type" /> | Drop an iceberg table |
| <CopyableCode code="clone_snowflake_managed_iceberg_table" /> | `EXEC` | <CopyableCode code="database_name, name, schema_name, data__name, endpoint" /> | <CopyableCode code="createMode" />, <CopyableCode code="copyGrants" />, <CopyableCode code="targetDatabase" />, <CopyableCode code="targetSchema" /> | Clone a snowflake managed iceberg table |
| <CopyableCode code="convert_to_managed_iceberg_table" /> | `EXEC` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | <CopyableCode code="ifExists" /> | Convert unmanaged iceberg table to managed iceberg table |
| <CopyableCode code="create_snowflake_managed_iceberg_table_as_select" /> | `EXEC` | <CopyableCode code="database_name, query, schema_name, data__base_location, data__name, endpoint" /> | <CopyableCode code="createMode" />, <CopyableCode code="copyGrants" /> | Create a snowflake managed iceberg table as select |
| <CopyableCode code="create_snowflake_managed_iceberg_table_like" /> | `EXEC` | <CopyableCode code="database_name, name, schema_name, data__name, endpoint" /> | <CopyableCode code="createMode" />, <CopyableCode code="copyGrants" />, <CopyableCode code="targetDatabase" />, <CopyableCode code="targetSchema" /> | Creates a new table with the same column definitions as an existing table, but without copying data from the existing table. |
| <CopyableCode code="create_unmanaged_iceberg_table_from_aws_glue_catalog" /> | `EXEC` | <CopyableCode code="database_name, schema_name, data__catalog_table_name, data__name, endpoint" /> | <CopyableCode code="createMode" /> | Create an unmanaged iceberg table from AWS Glue catalog |
| <CopyableCode code="create_unmanaged_iceberg_table_from_delta" /> | `EXEC` | <CopyableCode code="database_name, schema_name, data__base_location, data__name, endpoint" /> | <CopyableCode code="createMode" /> | Create an unmanaged iceberg table from Delta |
| <CopyableCode code="create_unmanaged_iceberg_table_from_iceberg_files" /> | `EXEC` | <CopyableCode code="database_name, schema_name, data__metadata_file_path, data__name, endpoint" /> | <CopyableCode code="createMode" /> | Create an unmanaged iceberg table from Iceberg files |
| <CopyableCode code="create_unmanaged_iceberg_table_from_iceberg_rest" /> | `EXEC` | <CopyableCode code="database_name, schema_name, data__catalog_table_name, data__name, endpoint" /> | <CopyableCode code="createMode" /> | Create an unmanaged iceberg table from Iceberg REST |
| <CopyableCode code="refresh_iceberg_table" /> | `EXEC` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | <CopyableCode code="ifExists" /> | Refreshes the metadata for an Apache Iceberg table that uses an external Iceberg catalog |
| <CopyableCode code="resume_recluster_iceberg_table" /> | `EXEC` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | <CopyableCode code="ifExists" /> | Resume recluster of an iceberg table (iceberg tables managed by an external catalog do not allow clustering) |
| <CopyableCode code="suspend_recluster_iceberg_table" /> | `EXEC` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | <CopyableCode code="ifExists" /> | Suspend recluster of an iceberg table (iceberg tables managed by an external catalog do not allow clustering) |
| <CopyableCode code="undrop_iceberg_table" /> | `EXEC` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | - | Undrop an iceberg table |
<br />

<details>
<summary>Optional Parameter Details</summary>

| Name | Description | Type | Default |
|------|-------------|------|---------|
| <CopyableCode code="copyGrants" /> | Query parameter to enable copy grants when creating the object. | `boolean` | `false` |
| <CopyableCode code="createMode" /> | Query parameter allowing support for different modes of resource creation. Possible values include: - `errorIfExists`: Throws an error if you try to create a resource that already exists. - `orReplace`: Automatically replaces the existing resource with the current one. - `ifNotExists`: Creates a new resource when an alter is requested for a non-existent resource. | `string` | `errorIfExists` |
| <CopyableCode code="deep" /> | Optionally includes dependency information of the table. | `boolean` | `-` |
| <CopyableCode code="fromName" /> | Query parameter to enable fetching rows only following the first row whose object name matches the specified string. Case-sensitive and does not have to be the full name. | `string` | `-` |
| <CopyableCode code="ifExists" /> | Query parameter that specifies how to handle the request for a resource that does not exist: - `true`: The endpoint does not throw an error if the resource does not exist. It returns a 200 success response, but does not take any action on the resource. - `false`: The endpoint throws an error if the resource doesn't exist. | `boolean` | `false` |
| <CopyableCode code="like" /> | Query parameter to filter the command output by resource name. Uses case-insensitive pattern matching, with support for SQL wildcard characters. | `string` | `-` |
| <CopyableCode code="showLimit" /> | Query parameter to limit the maximum number of rows returned by a command. | `integer` | `-` |
| <CopyableCode code="startsWith" /> | Query parameter to filter the command output based on the string of characters that appear at the beginning of the object name. Uses case-sensitive pattern matching. | `string` | `-` |
| <CopyableCode code="targetDatabase" /> | Database of the newly created table. Defaults to the source table's database. | `string` | `-` |
| <CopyableCode code="targetSchema" /> | Schema of the newly created table. Defaults to the source table's schema. | `string` | `-` |
| <CopyableCode code="type" /> | Specifies whether the table can be dropped if foreign keys exist that reference the table. | `string` | `-` |

</details>

## `SELECT` examples

Lists the Apache Iceberg™ tables for which you have access privileges.


```sql
SELECT
name,
auto_refresh,
base_location,
can_write_metadata,
catalog,
catalog_namespace,
catalog_sync,
catalog_table_name,
change_tracking,
cluster_by,
columns,
comment,
constraints,
created_on,
data_retention_time_in_days,
database_name,
external_volume,
iceberg_table_type,
max_data_extension_time_in_days,
metadata_file_path,
owner,
owner_role_type,
replace_invalid_characters,
schema_name,
storage_serialization_policy
FROM snowflake.iceberg_table.iceberg_tables
WHERE database_name = '{{ database_name }}'
AND schema_name = '{{ schema_name }}'
AND endpoint = '{{ endpoint }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>iceberg_tables</code> resource.

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
endpoint
)
SELECT 
'{{ name }}',
'{{ comment }}',
'{{ change_tracking }}',
'{{ max_data_extension_time_in_days }}',
'{{ external_volume }}',
'{{ data_retention_time_in_days }}',
'{{ catalog_sync }}',
'{{ catalog }}',
'{{ storage_serialization_policy }}',
'{{ catalog_table_name }}',
'{{ catalog_namespace }}',
'{{ cluster_by }}',
'{{ columns }}',
'{{ base_location }}',
'{{ replace_invalid_characters }}',
'{{ metadata_file_path }}',
'{{ constraints }}',
'{{ database_name }}',
'{{ schema_name }}',
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO snowflake.iceberg_table.iceberg_tables (
data__name,
database_name,
schema_name,
endpoint
)
SELECT 
'{{ name }}',
'{{ database_name }}',
'{{ schema_name }}',
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: iceberg_tables
  props:
    - name: database_name
      value: string
    - name: schema_name
      value: string
    - name: data__name
      value: string
    - name: endpoint
      value: string
    - name: name
      value: string
    - name: comment
      value: string
    - name: change_tracking
      value: boolean
    - name: max_data_extension_time_in_days
      value: integer
    - name: external_volume
      value: string
    - name: data_retention_time_in_days
      value: integer
    - name: catalog_sync
      value: string
    - name: catalog
      value: string
    - name: storage_serialization_policy
      value: string
    - name: catalog_table_name
      value: string
    - name: catalog_namespace
      value: string
    - name: cluster_by
      value: array
    - name: columns
      value: array
      props:
        - name: name
          value: string
        - name: datatype
          value: string
        - name: comment
          value: string
        - name: nullable
          value: boolean
        - name: default_value
          value: string
    - name: base_location
      value: string
    - name: replace_invalid_characters
      value: boolean
    - name: metadata_file_path
      value: string
    - name: constraints
      value: array
      props:
        - name: name
          value: string
        - name: column_names
          value: array
        - name: constraint_type
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>iceberg_tables</code> resource.

```sql
/*+ delete */
DELETE FROM snowflake.iceberg_table.iceberg_tables
WHERE database_name = '{{ database_name }}'
AND name = '{{ name }}'
AND schema_name = '{{ schema_name }}'
AND endpoint = '{{ endpoint }}';
```
