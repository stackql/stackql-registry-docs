---
title: pipes
hide_title: false
hide_table_of_contents: false
keywords:
  - pipes
  - pipe
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

Creates, updates, deletes, gets or lists a <code>pipes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pipes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.pipe.pipes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the pipe |
| <CopyableCode code="auto_ingest" /> | `boolean` | TRUE if all files from stage need to be auto-ingested |
| <CopyableCode code="aws_sns_topic" /> | `string` | Optional, if provided, auto_ingest pipe will only receive messages from this SNS topic. |
| <CopyableCode code="budget" /> | `string` | Name of the budget if the pipe is monitored by a budget |
| <CopyableCode code="comment" /> | `string` | user comment associated to an object in the dictionary |
| <CopyableCode code="copy_statement" /> | `string` | COPY INTO statement used to load data from queued files into a Snowflake table. This statement serves as the text/definition for the pipe and is displayed in the SHOW PIPES output |
| <CopyableCode code="created_on" /> | `string` | Date and time when the pipe was created. |
| <CopyableCode code="database_name" /> | `string` | Database in which the pipe is stored |
| <CopyableCode code="error_integration" /> | `string` | Link to integration object that point to a user provided Azure storage queue / SQS. When present, errors (e.g. ingest failure for Snowpipe or a user task failure or replication failure) will be sent to this queue to notify customers |
| <CopyableCode code="integration" /> | `string` | Link to integration object that ties a user provided storage queue to an auto_ingest enabled pipe. Required for auto_ingest to work on azure. |
| <CopyableCode code="invalid_reason" /> | `string` | Displays some detailed information for your pipes that may have issues |
| <CopyableCode code="owner" /> | `string` | Role that owns the pipe |
| <CopyableCode code="owner_role_type" /> | `string` | The type of role that owns the pipe |
| <CopyableCode code="pattern" /> | `string` | PATTERN copy option value in the COPY INTO statement in the pipe definition, if the copy option was specified. |
| <CopyableCode code="schema_name" /> | `string` | Schema in which the pipe is stored |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="fetch_pipe" /> | `SELECT` | <CopyableCode code="database, name, schema, endpoint" /> | Fetch a pipe |
| <CopyableCode code="list_pipes" /> | `SELECT` | <CopyableCode code="database, schema, endpoint" /> | List pipes |
| <CopyableCode code="create_pipe" /> | `INSERT` | <CopyableCode code="database, schema, data__copy_statement, data__name, endpoint" /> | Create a pipe |
| <CopyableCode code="delete_pipe" /> | `DELETE` | <CopyableCode code="database, name, schema, endpoint" /> | Delete a pipe |
| <CopyableCode code="refresh_pipe" /> | `EXEC` | <CopyableCode code="database, name, schema, endpoint" /> | Refresh the pipe |

## `SELECT` examples

List pipes


```sql
SELECT
name,
auto_ingest,
aws_sns_topic,
budget,
comment,
copy_statement,
created_on,
database_name,
error_integration,
integration,
invalid_reason,
owner,
owner_role_type,
pattern,
schema_name
FROM snowflake.pipe.pipes
WHERE database = '{{ database }}' AND schema = '{{ schema }}' AND endpoint = '{{ endpoint }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>pipes</code> resource.

<Tabs     defaultValue="all"    values={[        { label: 'All Properties', value: 'all' }, { label: 'Manifest', value: 'manifest' }    ]}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO snowflake.pipe.pipes (
data__name,
endpoint,
data__copy_statement,
database,
schema
)
SELECT 
'{ database }',
'{ name }',
'{ schema }',
'{ copy_statement }',
'{ endpoint }'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: pipes
  props:
  - name: database
    value: string
  - name: schema
    value: string
  - name: data__copy_statement
    value: string
  - name: data__name
    value: string
  - name: endpoint
    value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>pipes</code> resource.

```sql
/*+ delete */
DELETE FROM snowflake.pipe.pipes
WHERE database = '{ database }' AND name = '{ name }' AND schema = '{ schema }' AND endpoint = '{ endpoint }';
```
