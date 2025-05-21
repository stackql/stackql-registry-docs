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
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="fetch_stream" /> | `SELECT` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | Fetch a stream |
| <CopyableCode code="list_streams" /> | `SELECT` | <CopyableCode code="database_name, schema_name, endpoint" /> | List streams |
| <CopyableCode code="create_stream" /> | `INSERT` | <CopyableCode code="database_name, schema_name, data__name, data__stream_source, endpoint" /> | Create a stream |
| <CopyableCode code="delete_stream" /> | `DELETE` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | Delete a stream |
| <CopyableCode code="clone_stream" /> | `EXEC` | <CopyableCode code="database_name, name, schema_name, targetDatabase, targetSchema, data__name, endpoint" /> | Clone a stream |

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
WHERE database_name = '{{ database_name }}' AND schema_name = '{{ schema_name }}' AND endpoint = '{{ endpoint }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>streams</code> resource.

<Tabs     defaultValue="all"    values={[        { label: 'All Properties', value: 'all' }, { label: 'Manifest', value: 'manifest' }    ]}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO snowflake.streams.streams (
data__stream_source,
endpoint,
schema_name,
database_name,
data__name
)
SELECT 
'{ stream_source }',
'{ database_name }',
'{ name }',
'{ endpoint }',
'{ schema_name }'
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

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>streams</code> resource.

```sql
/*+ delete */
DELETE FROM snowflake.streams.streams
WHERE database_name = '{ database_name }' AND name = '{ name }' AND schema_name = '{ schema_name }' AND endpoint = '{ endpoint }';
```
