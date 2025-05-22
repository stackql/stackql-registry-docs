---
title: dynamic_tables
hide_title: false
hide_table_of_contents: false
keywords:
  - dynamic_tables
  - dynamic_table
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

Creates, updates, deletes, gets or lists a <code>dynamic_tables</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dynamic_tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.dynamic_table.dynamic_tables" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Specifies the name for the dynamic table, must be unique for the schema in which the dynamic table is created |
| <CopyableCode code="automatic_clustering" /> | `boolean` | If Automatic Clustering is enabled for your account, specifies whether it is explicitly enabled or disabled for the dynamic table. |
| <CopyableCode code="budget" /> | `string` | Name of the budget if the object is monitored by a budget |
| <CopyableCode code="bytes" /> | `integer` | Number of bytes that will be scanned if the entire table is scanned in a query. Note that this number may be different than the number of actual physical bytes stored on-disk for the table |
| <CopyableCode code="cluster_by" /> | `array` | Specifies one or more columns or column expressions in the dynamic table as the clustering key |
| <CopyableCode code="columns" /> | `array` |  |
| <CopyableCode code="comment" /> | `string` | Specifies a comment for the dynamic table. |
| <CopyableCode code="created_on" /> | `string` | Date and time when the dynamic table was created. |
| <CopyableCode code="data_retention_time_in_days" /> | `integer` | Specifies the retention period for the dynamic table so that Time Travel actions (SELECT, CLONE) can be performed on historical data in the dynamic table |
| <CopyableCode code="database_name" /> | `string` | Database in which the dynamic table is stored |
| <CopyableCode code="initialize" /> | `string` | Specifies the behavior of the initial refresh of the dynamic table |
| <CopyableCode code="kind" /> | `string` | Specifies the dynamic table type, permanent (default) or transient. |
| <CopyableCode code="max_data_extension_time_in_days" /> | `integer` | Specifies the retention period for the dynamic table so that Time Travel actions (SELECT, CLONE) can be performed on historical data in the dynamic table |
| <CopyableCode code="owner" /> | `string` | Role that owns the table |
| <CopyableCode code="owner_role_type" /> | `string` | The type of role that owns the object. |
| <CopyableCode code="query" /> | `string` | Specifies the query whose results the dynamic table should contain |
| <CopyableCode code="refresh_mode" /> | `string` | Specifies the refresh type for the dynamic table |
| <CopyableCode code="rows" /> | `integer` | Number of rows in the dynamic table. |
| <CopyableCode code="scheduling_state" /> | `string` | Scheduling state (RUNNING or SUSPENDED) |
| <CopyableCode code="schema_name" /> | `string` | Schema in which the dynamic table is stored |
| <CopyableCode code="target_lag" /> | `object` | Specifies the schedule for periodically refreshing the dynamic table. |
| <CopyableCode code="warehouse" /> | `string` | Specifies the name of the warehouse that provides the compute resources for refreshing the dynamic table |

## Methods
| Name | Accessible by | Required Params | Optional Params | Description |
|:-----|:--------------|:----------------|:----------------|:------------|
| <CopyableCode code="fetch_dynamic_table" /> | `SELECT` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | - | Fetch a Dynamic Table. |
| <CopyableCode code="list_dynamic_tables" /> | `SELECT` | <CopyableCode code="database_name, schema_name, endpoint" /> | <CopyableCode code="like" />, <CopyableCode code="startsWith" />, <CopyableCode code="showLimit" />, <CopyableCode code="fromName" />, <CopyableCode code="deep" /> | Lists the dynamic tables under the database and schema. |
| <CopyableCode code="create_dynamic_table" /> | `INSERT` | <CopyableCode code="database_name, schema_name, data__name, data__query, data__target_lag, data__warehouse, endpoint" /> | <CopyableCode code="createMode" /> | Create a dynamic table, with standard create modifiers as query parameters. See the Dynamic Table component definition for what is required to be provided in the request body. |
| <CopyableCode code="delete_dynamic_table" /> | `DELETE` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | <CopyableCode code="ifExists" /> | Delete a dynamic table with the given name. If ifExists is used, the operation will succeed even if the object does not exist. Otherwise, there will be a failure if the drop is unsuccessful. |
| <CopyableCode code="clone_dynamic_table" /> | `EXEC` | <CopyableCode code="database_name, name, schema_name, data__name, endpoint" /> | <CopyableCode code="createMode" />, <CopyableCode code="copyGrants" />, <CopyableCode code="targetDatabase" />, <CopyableCode code="targetSchema" /> | Create a new dynamic table by cloning from the specified resource |
| <CopyableCode code="refresh_dynamic_table" /> | `EXEC` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | <CopyableCode code="ifExists" /> | Specifies that the dynamic table should be manually refreshed |
| <CopyableCode code="resume_dynamic_table" /> | `EXEC` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | <CopyableCode code="ifExists" /> | Resume refreshes on the dynamic table |
| <CopyableCode code="resume_recluster_dynamic_table" /> | `EXEC` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | <CopyableCode code="ifExists" /> | Resume recluster of a dynamic table |
| <CopyableCode code="suspend_dynamic_table" /> | `EXEC` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | <CopyableCode code="ifExists" /> | Suspend refreshes on the dynamic table |
| <CopyableCode code="suspend_recluster_dynamic_table" /> | `EXEC` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | <CopyableCode code="ifExists" /> | Suspend recluster of a dynamic table |
| <CopyableCode code="swap_with_dynamic_table" /> | `EXEC` | <CopyableCode code="database_name, name, schema_name, targetName, endpoint" /> | <CopyableCode code="ifExists" />, <CopyableCode code="targetDatabase" />, <CopyableCode code="targetSchema" /> | Swap with another dynamic table |
| <CopyableCode code="undrop_dynamic_table" /> | `EXEC` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | - | Undrop specified dynamic table |


Expand this to view optional parameter details for all methods in this resource.


<details>
<summary>Optional Parameter Details</summary>

| Name | Description | Type | Default |
|------|-------------|------|---------|
| <CopyableCode code="copyGrants" /> | Query parameter to enable copy grants when creating the object. | `boolean` | `false` |
| <CopyableCode code="createMode" /> | Query parameter allowing support for different modes of resource creation. Possible values include: - `errorIfExists`: Throws an error if you try to create a resource that already exists. - `orReplace`: Automatically replaces the existing resource with the current one. - `ifNotExists`: Creates a new resource when an alter is requested for a non-existent resource. | `string` | `errorIfExists` |
| <CopyableCode code="deep" /> | Optionally includes dependency information of the dynamic table. | `boolean` | `-` |
| <CopyableCode code="fromName" /> | Query parameter to enable fetching rows only following the first row whose object name matches the specified string. Case-sensitive and does not have to be the full name. | `string` | `-` |
| <CopyableCode code="ifExists" /> | Query parameter that specifies how to handle the request for a resource that does not exist: - `true`: The endpoint does not throw an error if the resource does not exist. It returns a 200 success response, but does not take any action on the resource. - `false`: The endpoint throws an error if the resource doesn't exist. | `boolean` | `false` |
| <CopyableCode code="like" /> | Query parameter to filter the command output by resource name. Uses case-insensitive pattern matching, with support for SQL wildcard characters. | `string` | `-` |
| <CopyableCode code="showLimit" /> | Query parameter to limit the maximum number of rows returned by a command. | `integer` | `-` |
| <CopyableCode code="startsWith" /> | Query parameter to filter the command output based on the string of characters that appear at the beginning of the object name. Uses case-sensitive pattern matching. | `string` | `-` |
| <CopyableCode code="targetDatabase" /> | Database of the newly created dynamic table. Defaults to the source table's database. | `string` | `-` |
| <CopyableCode code="targetSchema" /> | Schema of the newly created dynamic table. Defaults to the source table's schema. | `string` | `-` |

</details>

## `SELECT` examples

Lists the dynamic tables under the database and schema.


```sql
SELECT
name,
automatic_clustering,
budget,
bytes,
cluster_by,
columns,
comment,
created_on,
data_retention_time_in_days,
database_name,
initialize,
kind,
max_data_extension_time_in_days,
owner,
owner_role_type,
query,
refresh_mode,
rows,
scheduling_state,
schema_name,
target_lag,
warehouse
FROM snowflake.dynamic_table.dynamic_tables
WHERE database_name = '{{ database_name }}'
AND schema_name = '{{ schema_name }}'
AND endpoint = '{{ endpoint }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dynamic_tables</code> resource.

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
INSERT INTO snowflake.dynamic_table.dynamic_tables (
data__name,
data__kind,
data__columns,
data__target_lag,
data__refresh_mode,
data__initialize,
data__warehouse,
data__cluster_by,
data__query,
data__data_retention_time_in_days,
data__max_data_extension_time_in_days,
data__comment,
database_name,
schema_name,
endpoint
)
SELECT 
'{{ name }}',
'{{ kind }}',
'{{ columns }}',
'{{ target_lag }}',
'{{ refresh_mode }}',
'{{ initialize }}',
'{{ warehouse }}',
'{{ cluster_by }}',
'{{ query }}',
'{{ data_retention_time_in_days }}',
'{{ max_data_extension_time_in_days }}',
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
INSERT INTO snowflake.dynamic_table.dynamic_tables (
data__name,
data__target_lag,
data__warehouse,
data__query,
database_name,
schema_name,
endpoint
)
SELECT 
'{{ name }}',
'{{ target_lag }}',
'{{ warehouse }}',
'{{ query }}',
'{{ database_name }}',
'{{ schema_name }}',
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: dynamic_tables
  props:
    - name: database_name
      value: string
    - name: schema_name
      value: string
    - name: data__name
      value: string
    - name: data__query
      value: string
    - name: data__target_lag
      value: string
    - name: data__warehouse
      value: string
    - name: endpoint
      value: string
    - name: name
      value: string
    - name: kind
      value: string
    - name: columns
      value: array
      props:
        - name: name
          value: string
        - name: datatype
          value: string
        - name: comment
          value: string
    - name: target_lag
      props:
        - name: type
          value: string
    - name: refresh_mode
      value: string
    - name: initialize
      value: string
    - name: warehouse
      value: string
    - name: cluster_by
      value: array
    - name: query
      value: string
    - name: data_retention_time_in_days
      value: integer
    - name: max_data_extension_time_in_days
      value: integer
    - name: comment
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>dynamic_tables</code> resource.

```sql
/*+ delete */
DELETE FROM snowflake.dynamic_table.dynamic_tables
WHERE database_name = '{{ database_name }}'
AND name = '{{ name }}'
AND schema_name = '{{ schema_name }}'
AND endpoint = '{{ endpoint }}';
```
