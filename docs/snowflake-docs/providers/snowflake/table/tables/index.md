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
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Specifies the name for the table, must be unique for the schema in which the table is created |
| <CopyableCode code="automatic_clustering" /> | `boolean` | If Automatic Clustering is enabled for your account, specifies whether it is explicitly enabled or disabled for the table. |
| <CopyableCode code="budget" /> | `string` | Name of the budget if the object is monitored by a budget |
| <CopyableCode code="bytes" /> | `integer` | Number of bytes that will be scanned if the entire table is scanned in a query. Note that this number may be different than the number of actual physical bytes stored on-disk for the table |
| <CopyableCode code="change_tracking" /> | `boolean` | Change tracking is enabled or disabled |
| <CopyableCode code="cluster_by" /> | `array` | Specifies one or more columns or column expressions in the table as the clustering key |
| <CopyableCode code="columns" /> | `array` |  |
| <CopyableCode code="comment" /> | `string` | Comment for the table |
| <CopyableCode code="constraints" /> | `array` |  |
| <CopyableCode code="created_on" /> | `string` | Date and time when the table was created. |
| <CopyableCode code="data_retention_time_in_days" /> | `integer` | Specifies the retention period for the table so that Time Travel actions SELECT, CLONE, UNDROP can be performed on historical data in the table |
| <CopyableCode code="database_name" /> | `string` | Database in which the table is stored |
| <CopyableCode code="default_ddl_collation" /> | `string` | Specifies a default collation specification for the columns in the table, including columns added to the table in the future |
| <CopyableCode code="dropped_on" /> | `string` | Date and time when the table was dropped |
| <CopyableCode code="enable_schema_evolution" /> | `boolean` | Table has schema evolution enabled or disabled |
| <CopyableCode code="kind" /> | `string` | Table type - permanent, transient, or temporary |
| <CopyableCode code="max_data_extension_time_in_days" /> | `integer` | Specifies the retention period for the table so that Time Travel actions SELECT, CLONE, UNDROP can be performed on historical data in the table |
| <CopyableCode code="owner" /> | `string` | Role that owns the table |
| <CopyableCode code="owner_role_type" /> | `string` | The type of role that owns the object. |
| <CopyableCode code="rows" /> | `integer` | Number of rows in the table. Returns NULL for external tables. |
| <CopyableCode code="schema_name" /> | `string` | Schema in which the table is stored |
| <CopyableCode code="search_optimization" /> | `boolean` | If ON, the table has the search optimization service enabled |
| <CopyableCode code="search_optimization_bytes" /> | `integer` | Number of additional bytes of storage that the search optimization service consumes for this table |
| <CopyableCode code="search_optimization_progress" /> | `integer` | Percentage of the table that has been optimized for search. |
| <CopyableCode code="table_type" /> | `string` | Type of the table |

## Methods
| Name | Accessible by | Required Params | Optional Params | Description |
|:-----|:--------------|:----------------|:----------------|:------------|
| <CopyableCode code="fetch_table" /> | `SELECT` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | - | Fetch a Table using the describe command output. |
| <CopyableCode code="list_tables" /> | `SELECT` | <CopyableCode code="database_name, schema_name, endpoint" /> | <CopyableCode code="like" />, <CopyableCode code="startsWith" />, <CopyableCode code="showLimit" />, <CopyableCode code="fromName" />, <CopyableCode code="history" />, <CopyableCode code="deep" /> | Lists the tables under the database and schema. |
| <CopyableCode code="create_table" /> | `INSERT` | <CopyableCode code="database_name, schema_name, data__name, endpoint" /> | <CopyableCode code="createMode" />, <CopyableCode code="copyGrants" /> | Create a table. |
| <CopyableCode code="delete_table" /> | `DELETE` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | <CopyableCode code="ifExists" /> | Delete a table with the given name. |
| <CopyableCode code="create_or_alter_table" /> | `REPLACE` | <CopyableCode code="database_name, name, schema_name, data__name, endpoint" /> | - | Create a (or alter an existing) table. Even if the operation is just an alter, the full property set must be provided. |
| <CopyableCode code="clone_table" /> | `EXEC` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | <CopyableCode code="createMode" />, <CopyableCode code="copyGrants" />, <CopyableCode code="targetDatabase" />, <CopyableCode code="targetSchema" /> | Create a new table by cloning from the specified resource |
| <CopyableCode code="create_table_as_select" /> | `EXEC` | <CopyableCode code="database_name, query, schema_name, endpoint" /> | <CopyableCode code="createMode" />, <CopyableCode code="copyGrants" /> | Create a table as select. |
| <CopyableCode code="create_table_as_select_deprecated" /> | `EXEC` | <CopyableCode code="database_name, name, query, schema_name, data__name, endpoint" /> | <CopyableCode code="createMode" />, <CopyableCode code="copyGrants" /> | Create a table as select. |
| <CopyableCode code="create_table_like" /> | `EXEC` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | <CopyableCode code="createMode" />, <CopyableCode code="copyGrants" /> | Create a new table like the specified resource, but empty |
| <CopyableCode code="create_table_like_deprecated" /> | `EXEC` | <CopyableCode code="database_name, name, newTableName, schema_name, endpoint" /> | <CopyableCode code="createMode" />, <CopyableCode code="copyGrants" /> | Create a new table like the specified resource, but empty |
| <CopyableCode code="create_table_using_template" /> | `EXEC` | <CopyableCode code="database_name, query, schema_name, endpoint" /> | <CopyableCode code="createMode" />, <CopyableCode code="copyGrants" /> | Create a table using template. |
| <CopyableCode code="create_table_using_template_deprecated" /> | `EXEC` | <CopyableCode code="database_name, name, query, schema_name, endpoint" /> | <CopyableCode code="createMode" />, <CopyableCode code="copyGrants" /> | Create a table using template. |
| <CopyableCode code="resume_recluster_table" /> | `EXEC` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | <CopyableCode code="ifExists" /> | Resume recluster of a table |
| <CopyableCode code="resume_recluster_table_deprecated" /> | `EXEC` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | <CopyableCode code="ifExists" /> | Resume recluster of a table |
| <CopyableCode code="suspend_recluster_table" /> | `EXEC` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | <CopyableCode code="ifExists" /> | Suspend recluster of a table |
| <CopyableCode code="suspend_recluster_table_deprecated" /> | `EXEC` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | <CopyableCode code="ifExists" /> | Suspend recluster of a table |
| <CopyableCode code="swap_with_table" /> | `EXEC` | <CopyableCode code="database_name, name, schema_name, targetName, endpoint" /> | <CopyableCode code="ifExists" />, <CopyableCode code="targetDatabase" />, <CopyableCode code="targetSchema" /> | Swap with another table |
| <CopyableCode code="swap_with_table_deprecated" /> | `EXEC` | <CopyableCode code="database_name, name, schema_name, targetTableName, endpoint" /> | <CopyableCode code="ifExists" /> | Swap with another table |
| <CopyableCode code="undrop_table" /> | `EXEC` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | - | Undrop specified table |

<br />


<details>
<summary>Optional Parameter Details</summary>

| Name | Description | Type | Default |
|------|-------------|------|---------|
| <CopyableCode code="copyGrants" /> | Query parameter to enable copy grants when creating the object. | `boolean` | `false` |
| <CopyableCode code="createMode" /> | Query parameter allowing support for different modes of resource creation. Possible values include: - `errorIfExists`: Throws an error if you try to create a resource that already exists. - `orReplace`: Automatically replaces the existing resource with the current one. - `ifNotExists`: Creates a new resource when an alter is requested for a non-existent resource. | `string` | `errorIfExists` |
| <CopyableCode code="deep" /> | Optionally includes dependency information of the table. | `boolean` | `-` |
| <CopyableCode code="fromName" /> | Query parameter to enable fetching rows only following the first row whose object name matches the specified string. Case-sensitive and does not have to be the full name. | `string` | `-` |
| <CopyableCode code="history" /> | Optionally includes dropped tables that have not yet been purged. | `boolean` | `-` |
| <CopyableCode code="ifExists" /> | Query parameter that specifies how to handle the request for a resource that does not exist: - `true`: The endpoint does not throw an error if the resource does not exist. It returns a 200 success response, but does not take any action on the resource. - `false`: The endpoint throws an error if the resource doesn't exist. | `boolean` | `false` |
| <CopyableCode code="like" /> | Query parameter to filter the command output by resource name. Uses case-insensitive pattern matching, with support for SQL wildcard characters. | `string` | `-` |
| <CopyableCode code="showLimit" /> | Query parameter to limit the maximum number of rows returned by a command. | `integer` | `-` |
| <CopyableCode code="startsWith" /> | Query parameter to filter the command output based on the string of characters that appear at the beginning of the object name. Uses case-sensitive pattern matching. | `string` | `-` |
| <CopyableCode code="targetDatabase" /> | Database of the newly created table. Defaults to the source table's database. | `string` | `-` |
| <CopyableCode code="targetSchema" /> | Schema of the newly created table. Defaults to the source table's schema. | `string` | `-` |

</details>

## `SELECT` examples

<Tabs
    defaultValue="list_tables"
    values={[
        { label: 'list_tables', value: 'list_tables' },
        { label: 'fetch_table', value: 'fetch_table' }
    ]
}>
<TabItem value="list_tables">

Lists the tables under the database and schema.

```sql
SELECT
name,
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
database_name,
default_ddl_collation,
dropped_on,
enable_schema_evolution,
kind,
max_data_extension_time_in_days,
owner,
owner_role_type,
rows,
schema_name,
search_optimization,
search_optimization_bytes,
search_optimization_progress,
table_type
FROM snowflake.table.tables
WHERE database_name = '{{ database_name }}'
AND schema_name = '{{ schema_name }}'
AND endpoint = '{{ endpoint }}';
```
</TabItem>
<TabItem value="fetch_table">

Fetch a Table using the describe command output.

```sql
SELECT
name,
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
database_name,
default_ddl_collation,
dropped_on,
enable_schema_evolution,
kind,
max_data_extension_time_in_days,
owner,
owner_role_type,
rows,
schema_name,
search_optimization,
search_optimization_bytes,
search_optimization_progress,
table_type
FROM snowflake.table.tables
WHERE database_name = '{{ database_name }}'
AND name = '{{ name }}'
AND schema_name = '{{ schema_name }}'
AND endpoint = '{{ endpoint }}';
```
</TabItem>
</Tabs>

## `INSERT` example

Create a table.

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
endpoint
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
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO snowflake.table.tables (
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
# Description fields below are for documentation purposes only and are not required in the manifest
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
      description: >-
        Specifies the name for the table, must be unique for the schema in which
        the table is created (Required parameter for the tables resource.)
    - name: kind
      value: string
      description: >-
        Table type - permanent, transient, or temporary (valid values:
        'PERMANENT', 'TRANSIENT', 'TEMPORARY', '', 'transient', 'temporary')
      default: PERMANENT
    - name: cluster_by
      value: array
      description: >-
        Specifies one or more columns or column expressions in the table as the
        clustering key
    - name: enable_schema_evolution
      value: boolean
      description: Table has schema evolution enabled or disabled
    - name: change_tracking
      value: boolean
      description: Change tracking is enabled or disabled
    - name: data_retention_time_in_days
      value: integer
      description: >-
        Specifies the retention period for the table so that Time Travel actions
        SELECT, CLONE, UNDROP can be performed on historical data in the table
    - name: max_data_extension_time_in_days
      value: integer
      description: >-
        Specifies the retention period for the table so that Time Travel actions
        SELECT, CLONE, UNDROP can be performed on historical data in the table
    - name: default_ddl_collation
      value: string
      description: >-
        Specifies a default collation specification for the columns in the
        table, including columns added to the table in the future
    - name: columns
      value:
        - name: name
          value: string
          description: Column name
        - name: datatype
          value: string
          description: The data type for the column
        - name: nullable
          value: boolean
          description: Specifies that the column does allow NULL values or not.
          default: true
        - name: collate
          value: string
          description: >-
            Specifies the collation to use for column operations such as string
            comparison
        - name: default
          value: string
          description: >-
            Specifies whether a default value is automatically inserted in the
            column if a value is not explicitly specified via an INSERT or
            CREATE TABLE AS SELECT statement
        - name: autoincrement
          value: boolean
        - name: autoincrement_start
          value: integer
          description: The default value for the column starts with the specified number
        - name: autoincrement_increment
          value: integer
          description: >-
            Each successive value for the column automatically increments by the
            specified amount
        - name: constraints
          value:
            - name: name
              value: string
              description: Name of the Constraint
            - name: column_names
              value: array
            - name: constraint_type
              value: string
              description: Type of the constraint
        - name: comment
          value: string
          description: Specifies a comment for the column
    - name: constraints
      value:
        - name: name
          value: string
          description: Name of the Constraint
        - name: column_names
          value: array
        - name: constraint_type
          value: string
          description: Type of the constraint
    - name: comment
      value: string
      description: Comment for the table
```
</TabItem>
</Tabs>

## `REPLACE` example

Create a (or alter an existing) table. Even if the operation is just an alter, the full property set must be provided.

```sql
/*+ update */
REPLACE snowflake.table.tables
SET 
name = '{{ name }}',
kind = '{{ kind }}',
cluster_by = '{{ cluster_by }}',
enable_schema_evolution = {{ enable_schema_evolution }},
change_tracking = {{ change_tracking }},
data_retention_time_in_days = {{ data_retention_time_in_days }},
max_data_extension_time_in_days = {{ max_data_extension_time_in_days }},
default_ddl_collation = '{{ default_ddl_collation }}',
columns = '{{ columns }}',
constraints = '{{ constraints }}',
comment = '{{ comment }}'
WHERE 
database_name = '{{ database_name }}'
AND name = '{{ name }}'
AND schema_name = '{{ schema_name }}'
AND data__name = '{{ data__name }}'
AND endpoint = '{{ endpoint }}';
```

## `DELETE` example

Delete a table with the given name.

```sql
/*+ delete */
DELETE FROM snowflake.table.tables
WHERE database_name = '{{ database_name }}'
AND name = '{{ name }}'
AND schema_name = '{{ schema_name }}'
AND endpoint = '{{ endpoint }}';
```
