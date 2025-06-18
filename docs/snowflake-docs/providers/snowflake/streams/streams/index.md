---
title: streams
hide_title: false
hide_table_of_contents: false
keywords:
  - streams
  - streams
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

Creates, updates, deletes, gets or lists a <code>streams</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>streams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.streams.streams" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the stream |
| <CopyableCode code="comment" /> | `string` | user comment associated to an object in the dictionary |
| <CopyableCode code="created_on" /> | `string` | Date and time when the stream was created. |
| <CopyableCode code="database_name" /> | `string` | Database in which the stream is stored |
| <CopyableCode code="invalid_reason" /> | `string` | Reason why the stream cannot be queried successfully. This column supports future functionality. Currently, the only value returned is N/A. |
| <CopyableCode code="mode" /> | `string` | Mode of the stream. Possible values include: APPEND_ONLY, INSERT_ONLY. For streams on tables, the column displays DEFAULT. |
| <CopyableCode code="owner" /> | `string` | Role that owns the stream |
| <CopyableCode code="owner_role_type" /> | `string` | The type of role that owns the stream |
| <CopyableCode code="schema_name" /> | `string` | Schema in which the stream is stored |
| <CopyableCode code="stale" /> | `boolean` | Specifies whether the stream is stale or not |
| <CopyableCode code="stale_after" /> | `string` | Timestamp when the stream became stale or may become stale if not consumed. |
| <CopyableCode code="stream_source" /> | `object` |  |
| <CopyableCode code="table_name" /> | `string` | Table name whose changes are tracked by the stream |
| <CopyableCode code="type" /> | `string` | Type of the stream; currently DELTA only. |

## Methods
| Name | Accessible by | Required Params | Optional Params | Description |
|:-----|:--------------|:----------------|:----------------|:------------|
| <CopyableCode code="fetch_stream" /> | `SELECT` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | - | Fetch a stream |
| <CopyableCode code="list_streams" /> | `SELECT` | <CopyableCode code="database_name, schema_name, endpoint" /> | <CopyableCode code="like" />, <CopyableCode code="startsWith" />, <CopyableCode code="showLimit" />, <CopyableCode code="fromName" /> | List streams |
| <CopyableCode code="create_stream" /> | `INSERT` | <CopyableCode code="database_name, schema_name, data__name, data__stream_source, endpoint" /> | <CopyableCode code="createMode" />, <CopyableCode code="copyGrants" /> | Create a stream |
| <CopyableCode code="delete_stream" /> | `DELETE` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | <CopyableCode code="ifExists" /> | Delete a stream |
| <CopyableCode code="clone_stream" /> | `EXEC` | <CopyableCode code="database_name, name, schema_name, targetDatabase, targetSchema, data__name, endpoint" /> | <CopyableCode code="createMode" />, <CopyableCode code="copyGrants" /> | Clone a stream |

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
    defaultValue="list_streams"
    values={[
        { label: 'list_streams', value: 'list_streams' },
        { label: 'fetch_stream', value: 'fetch_stream' }
    ]
}>
<TabItem value="list_streams">

List streams

```sql
SELECT
name,
comment,
created_on,
database_name,
invalid_reason,
mode,
owner,
owner_role_type,
schema_name,
stale,
stale_after,
stream_source,
table_name,
type
FROM snowflake.streams.streams
WHERE database_name = '{{ database_name }}'
AND schema_name = '{{ schema_name }}'
AND endpoint = '{{ endpoint }}';
```
</TabItem>
<TabItem value="fetch_stream">

Fetch a stream

```sql
SELECT
name,
comment,
created_on,
database_name,
invalid_reason,
mode,
owner,
owner_role_type,
schema_name,
stale,
stale_after,
stream_source,
table_name,
type
FROM snowflake.streams.streams
WHERE database_name = '{{ database_name }}'
AND name = '{{ name }}'
AND schema_name = '{{ schema_name }}'
AND endpoint = '{{ endpoint }}';
```
</TabItem>
</Tabs>

## `INSERT` example

Create a stream

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
INSERT INTO snowflake.streams.streams (
data__name,
data__stream_source,
data__comment,
database_name,
schema_name,
endpoint
)
SELECT 
'{{ name }}',
'{{ stream_source }}',
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
INSERT INTO snowflake.streams.streams (
data__name,
data__stream_source,
database_name,
schema_name,
endpoint
)
SELECT 
'{{ name }}',
'{{ stream_source }}',
'{{ database_name }}',
'{{ schema_name }}',
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
# Description fields below are for documentation purposes only and are not required in the manifest
- name: streams
  props:
    - name: database_name
      value: string
      description: Required parameter for the streams resource.
    - name: schema_name
      value: string
      description: Required parameter for the streams resource.
    - name: endpoint
      value: string
      description: Required parameter for the streams resource.
    - name: name
      value: string
      description: Name of the stream (Required parameter for the streams resource.)
    - name: stream_source
      value:
        src_type: string
        name: string
        database_name: string
        schema_name: string
      description: Required parameter for the streams resource.
    - name: comment
      value: string
      description: user comment associated to an object in the dictionary
```
</TabItem>
</Tabs>

## `DELETE` example

Delete a stream

```sql
/*+ delete */
DELETE FROM snowflake.streams.streams
WHERE database_name = '{{ database_name }}'
AND name = '{{ name }}'
AND schema_name = '{{ schema_name }}'
AND endpoint = '{{ endpoint }}';
```
