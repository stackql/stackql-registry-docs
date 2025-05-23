---
title: event_tables
hide_title: false
hide_table_of_contents: false
keywords:
  - event_tables
  - event_table
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

Creates, updates, deletes, gets or lists a <code>event_tables</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.event_table.event_tables" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the event table |
| <CopyableCode code="automatic_clustering" /> | `boolean` | If Automatic Clustering is enabled for your account, specifies whether it is explicitly enabled or disabled for the table. |
| <CopyableCode code="bytes" /> | `integer` | Number of bytes that will be scanned if the entire table is scanned in a query.Note that this number may be different than the number of actual physical bytes stored on-disk for the table |
| <CopyableCode code="change_tracking" /> | `boolean` | True if change tracking is enabled, allowing streams and CHANGES to be used on the entity. |
| <CopyableCode code="cluster_by" /> | `array` | Cluster key column(s) or expression |
| <CopyableCode code="columns" /> | `array` |  |
| <CopyableCode code="comment" /> | `string` | user comment associated to an object in the dictionary |
| <CopyableCode code="created_on" /> | `string` | Date and time when the event table was created. |
| <CopyableCode code="data_retention_time_in_days" /> | `integer` | number of days to retain the old version of deleted/updated data |
| <CopyableCode code="database_name" /> | `string` | Database in which the event table is stored |
| <CopyableCode code="default_ddl_collation" /> | `string` | Collation that is used for all the new columns created by the DDL statements (if not specified) |
| <CopyableCode code="max_data_extension_time_in_days" /> | `integer` | Maximum number of days to extend data retention beyond the retention period to prevent a stream becoming stale. |
| <CopyableCode code="owner" /> | `string` | Role that owns the event table |
| <CopyableCode code="owner_role_type" /> | `string` | The type of role that owns the event table |
| <CopyableCode code="rows" /> | `integer` | Number of rows in the table. |
| <CopyableCode code="schema_name" /> | `string` | Schema in which the event table is stored |
| <CopyableCode code="search_optimization" /> | `boolean` | If ON, the table has the search optimization service enabled |
| <CopyableCode code="search_optimization_bytes" /> | `integer` | Number of additional bytes of storage that the search optimization service consumes for this table |
| <CopyableCode code="search_optimization_progress" /> | `integer` | Percentage of the table that has been optimized for search |

## Methods
| Name | Accessible by | Required Params | Optional Params | Description |
|:-----|:--------------|:----------------|:----------------|:------------|
| <CopyableCode code="fetch_event_table" /> | `SELECT` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | - | Fetch an event table |
| <CopyableCode code="list_event_tables" /> | `SELECT` | <CopyableCode code="database_name, schema_name, endpoint" /> | <CopyableCode code="like" />, <CopyableCode code="startsWith" />, <CopyableCode code="showLimit" />, <CopyableCode code="fromName" /> | List event tables |
| <CopyableCode code="create_event_table" /> | `INSERT` | <CopyableCode code="database_name, schema_name, data__name, endpoint" /> | <CopyableCode code="createMode" />, <CopyableCode code="copyGrants" /> | Create an event table |
| <CopyableCode code="delete_event_table" /> | `DELETE` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | <CopyableCode code="ifExists" /> | Delete an event table |
| <CopyableCode code="rename_event_table" /> | `EXEC` | <CopyableCode code="database_name, name, schema_name, targetName, endpoint" /> | <CopyableCode code="ifExists" /> | Rename the event table |

<br />


<details>
<summary>Optional Parameter Details</summary>

| Name | Description | Type | Default |
|------|-------------|------|---------|
| <CopyableCode code="copyGrants" /> | Query parameter to enable copy grants when creating the object. | `boolean` | `false` |
| <CopyableCode code="createMode" /> | Query parameter allowing support for different modes of resource creation. Possible values include: - `errorIfExists`: Throws an error if you try to create a resource that already exists. - `orReplace`: Automatically replaces the existing resource with the current one. - `ifNotExists`: Creates a new resource when an alter is requested for a non-existent resource. | `string` | `errorIfExists` |
| <CopyableCode code="fromName" /> | Query parameter to enable fetching rows only following the first row whose object name matches the specified string. Case-sensitive and does not have to be the full name. | `string` | `-` |
| <CopyableCode code="ifExists" /> | Query parameter that specifies how to handle the request for a resource that does not exist: - `true`: The endpoint does not throw an error if the resource does not exist. It returns a 200 success response, but does not take any action on the resource. - `false`: The endpoint throws an error if the resource doesn't exist. | `boolean` | `false` |
| <CopyableCode code="like" /> | Query parameter to filter the command output by resource name. Uses case-insensitive pattern matching, with support for SQL wildcard characters. | `string` | `-` |
| <CopyableCode code="showLimit" /> | Query parameter to limit the maximum number of rows returned by a command. | `integer` | `-` |
| <CopyableCode code="startsWith" /> | Query parameter to filter the command output based on the string of characters that appear at the beginning of the object name. Uses case-sensitive pattern matching. | `string` | `-` |

</details>

## `SELECT` examples

<Tabs
    defaultValue="list_event_tables"
    values={[
        { label: 'list_event_tables', value: 'list_event_tables' },
        { label: 'fetch_event_table', value: 'fetch_event_table' }
    ]
}>
<TabItem value="list_event_tables">

List event tables

```sql
SELECT
name,
automatic_clustering,
bytes,
change_tracking,
cluster_by,
columns,
comment,
created_on,
data_retention_time_in_days,
database_name,
default_ddl_collation,
max_data_extension_time_in_days,
owner,
owner_role_type,
rows,
schema_name,
search_optimization,
search_optimization_bytes,
search_optimization_progress
FROM snowflake.event_table.event_tables
WHERE database_name = '{{ database_name }}'
AND schema_name = '{{ schema_name }}'
AND endpoint = '{{ endpoint }}';
```
</TabItem>
<TabItem value="fetch_event_table">

Fetch an event table

```sql
SELECT
name,
automatic_clustering,
bytes,
change_tracking,
cluster_by,
columns,
comment,
created_on,
data_retention_time_in_days,
database_name,
default_ddl_collation,
max_data_extension_time_in_days,
owner,
owner_role_type,
rows,
schema_name,
search_optimization,
search_optimization_bytes,
search_optimization_progress
FROM snowflake.event_table.event_tables
WHERE database_name = '{{ database_name }}'
AND name = '{{ name }}'
AND schema_name = '{{ schema_name }}'
AND endpoint = '{{ endpoint }}';
```
</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>event_tables</code> resource.

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
INSERT INTO snowflake.event_table.event_tables (
data__name,
data__cluster_by,
data__data_retention_time_in_days,
data__max_data_extension_time_in_days,
data__change_tracking,
data__default_ddl_collation,
data__comment,
database_name,
schema_name,
endpoint
)
SELECT 
'{{ name }}',
'{{ cluster_by }}',
'{{ data_retention_time_in_days }}',
'{{ max_data_extension_time_in_days }}',
'{{ change_tracking }}',
'{{ default_ddl_collation }}',
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
INSERT INTO snowflake.event_table.event_tables (
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
- name: event_tables
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
      description: Name of the event table
    - name: cluster_by
      value: array
      description: Cluster key column(s) or expression
    - name: data_retention_time_in_days
      value: integer
      description: number of days to retain the old version of deleted/updated data
    - name: max_data_extension_time_in_days
      value: integer
      description: >-
        Maximum number of days to extend data retention beyond the retention
        period to prevent a stream becoming stale.
    - name: change_tracking
      value: boolean
      description: >-
        True if change tracking is enabled, allowing streams and CHANGES to be
        used on the entity.
    - name: default_ddl_collation
      value: string
      description: >-
        Collation that is used for all the new columns created by the DDL
        statements (if not specified)
    - name: comment
      value: string
      description: user comment associated to an object in the dictionary

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>event_tables</code> resource.

```sql
/*+ delete */
DELETE FROM snowflake.event_table.event_tables
WHERE database_name = '{{ database_name }}'
AND name = '{{ name }}'
AND schema_name = '{{ schema_name }}'
AND endpoint = '{{ endpoint }}';
```
