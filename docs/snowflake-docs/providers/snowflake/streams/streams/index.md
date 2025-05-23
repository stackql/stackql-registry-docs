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
| <CopyableCode code="list_streams" /> | `SELECT` | <CopyableCode code="database_name, schema_name, endpoint" /> | [`like`](#like), [`startsWith`](#startsWith), [`showLimit`](#showLimit), [`fromName`](#fromName) | List streams |
| <CopyableCode code="create_stream" /> | `INSERT` | <CopyableCode code="database_name, schema_name, data__name, data__stream_source, endpoint" /> | [`createMode`](#createMode), [`copyGrants`](#copyGrants) | Create a stream |
| <CopyableCode code="delete_stream" /> | `DELETE` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | [`ifExists`](#ifExists) | Delete a stream |
| <CopyableCode code="clone_stream" /> | `EXEC` | <CopyableCode code="database_name, name, schema_name, targetDatabase, targetSchema, data__name, endpoint" /> | [`createMode`](#createMode), [`copyGrants`](#copyGrants) | Clone a stream |

<br />


<details>
<summary>Optional Parameter Details</summary>

| Name | Description | Type | Default |
|------|-------------|------|---------|
| <a id="copyGrants"></a><CopyableCode code="copyGrants" /> | Query parameter to enable copy grants when creating the object. | `boolean` | `false` |
| <a id="createMode"></a><CopyableCode code="createMode" /> | Query parameter allowing support for different modes of resource creation. Possible values include: - `errorIfExists`: Throws an error if you try to create a resource that already exists. - `orReplace`: Automatically replaces the existing resource with the current one. - `ifNotExists`: Creates a new resource when an alter is requested for a non-existent resource. | `string` | `errorIfExists` |
| <a id="fromName"></a><CopyableCode code="fromName" /> | Query parameter to enable fetching rows only following the first row whose object name matches the specified string. Case-sensitive and does not have to be the full name. | `string` | `-` |
| <a id="ifExists"></a><CopyableCode code="ifExists" /> | Query parameter that specifies how to handle the request for a resource that does not exist: - `true`: The endpoint does not throw an error if the resource does not exist. It returns a 200 success response, but does not take any action on the resource. - `false`: The endpoint throws an error if the resource doesn't exist. | `boolean` | `false` |
| <a id="like"></a><CopyableCode code="like" /> | Query parameter to filter the command output by resource name. Uses case-insensitive pattern matching, with support for SQL wildcard characters. | `string` | `-` |
| <a id="showLimit"></a><CopyableCode code="showLimit" /> | Query parameter to limit the maximum number of rows returned by a command. | `integer` | `-` |
| <a id="startsWith"></a><CopyableCode code="startsWith" /> | Query parameter to filter the command output based on the string of characters that appear at the beginning of the object name. Uses case-sensitive pattern matching. | `string` | `-` |

</details>

## `SELECT` examples

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
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>streams</code> resource.

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
- name: streams
  props:
    - name: database_name
      value: string
    - name: schema_name
      value: string
    - name: data__name
      value: string
    - name: data__stream_source
      value: string
    - name: endpoint
      value: string
    - name: name
      value: string
    - name: stream_source
      value:
        - name: src_type
          value: string
        - name: name
          value: string
        - name: database_name
          value: string
        - name: schema_name
          value: string
    - name: comment
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>streams</code> resource.

```sql
/*+ delete */
DELETE FROM snowflake.streams.streams
WHERE database_name = '{{ database_name }}'
AND name = '{{ name }}'
AND schema_name = '{{ schema_name }}'
AND endpoint = '{{ endpoint }}';
```
