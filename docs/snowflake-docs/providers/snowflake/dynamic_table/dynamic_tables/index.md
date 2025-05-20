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
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="fetch_dynamic_table" /> | `SELECT` | <CopyableCode code="database, name, schema, endpoint" /> | Fetch a Dynamic Table. |
| <CopyableCode code="list_dynamic_tables" /> | `SELECT` | <CopyableCode code="database, schema, endpoint" /> | Lists the dynamic tables under the database and schema. |
| <CopyableCode code="create_dynamic_table" /> | `INSERT` | <CopyableCode code="database, schema, data__name, data__query, data__target_lag, data__warehouse, endpoint" /> | Create a dynamic table, with standard create modifiers as query parameters. See the Dynamic Table component definition for what is required to be provided in the request body. |
| <CopyableCode code="delete_dynamic_table" /> | `DELETE` | <CopyableCode code="database, name, schema, endpoint" /> | Delete a dynamic table with the given name. If ifExists is used, the operation will succeed even if the object does not exist. Otherwise, there will be a failure if the drop is unsuccessful. |
| <CopyableCode code="clone_dynamic_table" /> | `EXEC` | <CopyableCode code="database, name, schema, data__name, endpoint" /> | Create a new dynamic table by cloning from the specified resource |
| <CopyableCode code="refresh_dynamic_table" /> | `EXEC` | <CopyableCode code="database, name, schema, endpoint" /> | Specifies that the dynamic table should be manually refreshed |
| <CopyableCode code="resume_dynamic_table" /> | `EXEC` | <CopyableCode code="database, name, schema, endpoint" /> | Resume refreshes on the dynamic table |
| <CopyableCode code="resume_recluster_dynamic_table" /> | `EXEC` | <CopyableCode code="database, name, schema, endpoint" /> | Resume recluster of a dynamic table |
| <CopyableCode code="suspend_dynamic_table" /> | `EXEC` | <CopyableCode code="database, name, schema, endpoint" /> | Suspend refreshes on the dynamic table |
| <CopyableCode code="suspend_recluster_dynamic_table" /> | `EXEC` | <CopyableCode code="database, name, schema, endpoint" /> | Suspend recluster of a dynamic table |
| <CopyableCode code="swap_with_dynamic_table" /> | `EXEC` | <CopyableCode code="database, name, schema, targetName, endpoint" /> | Swap with another dynamic table |
| <CopyableCode code="undrop_dynamic_table" /> | `EXEC` | <CopyableCode code="database, name, schema, endpoint" /> | Undrop specified dynamic table |

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
WHERE database = '{{ database }}' AND schema = '{{ schema }}' AND endpoint = '{{ endpoint }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dynamic_tables</code> resource.

<Tabs     defaultValue="all"    values={[        { label: 'All Properties', value: 'all' }, { label: 'Manifest', value: 'manifest' }    ]}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO snowflake.dynamic_table.dynamic_tables (
data__warehouse,
data__query,
data__name,
endpoint,
data__target_lag,
schema,
database
)
SELECT 
'{ database }',
'{ query }',
'{ endpoint }',
'{ target_lag }',
'{ warehouse }',
'{ schema }',
'{ name }'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: dynamic_tables
  props:
  - name: database
    value: string
  - name: schema
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

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>dynamic_tables</code> resource.

```sql
/*+ delete */
DELETE FROM snowflake.dynamic_table.dynamic_tables
WHERE database = '{ database }' AND name = '{ name }' AND schema = '{ schema }' AND endpoint = '{ endpoint }';
```
