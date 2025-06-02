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
| Name | Accessible by | Required Params | Optional Params | Description |
|:-----|:--------------|:----------------|:----------------|:------------|
| <CopyableCode code="fetch_pipe" /> | `SELECT` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | - | Fetch a pipe |
| <CopyableCode code="list_pipes" /> | `SELECT` | <CopyableCode code="database_name, schema_name, endpoint" /> | <CopyableCode code="like" /> | List pipes |
| <CopyableCode code="create_pipe" /> | `INSERT` | <CopyableCode code="database_name, schema_name, data__copy_statement, data__name, endpoint" /> | <CopyableCode code="createMode" /> | Create a pipe |
| <CopyableCode code="delete_pipe" /> | `DELETE` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | <CopyableCode code="ifExists" /> | Delete a pipe |
| <CopyableCode code="refresh_pipe" /> | `EXEC` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | <CopyableCode code="ifExists" />, <CopyableCode code="prefix" />, <CopyableCode code="modified_after" /> | Refresh the pipe |

<br />


<details>
<summary>Optional Parameter Details</summary>

| Name | Description | Type | Default |
|------|-------------|------|---------|
| <CopyableCode code="createMode" /> | Query parameter allowing support for different modes of resource creation. Possible values include: - `errorIfExists`: Throws an error if you try to create a resource that already exists. - `orReplace`: Automatically replaces the existing resource with the current one. - `ifNotExists`: Creates a new resource when an alter is requested for a non-existent resource. | `string` | `errorIfExists` |
| <CopyableCode code="ifExists" /> | Query parameter that specifies how to handle the request for a resource that does not exist: - `true`: The endpoint does not throw an error if the resource does not exist. It returns a 200 success response, but does not take any action on the resource. - `false`: The endpoint throws an error if the resource doesn't exist. | `boolean` | `false` |
| <CopyableCode code="like" /> | Query parameter to filter the command output by resource name. Uses case-insensitive pattern matching, with support for SQL wildcard characters. | `string` | `-` |
| <CopyableCode code="modified_after" /> | Timestamp (in ISO-8601 format) of the oldest data files to copy into the Snowpipe ingest queue based on the LAST_MODIFIED date (i.e. date when a file was staged) | `string` | `-` |
| <CopyableCode code="prefix" /> | Path (or prefix) appended to the stage reference in the pipe definition. The path limits the set of files to load. | `string` | `-` |

</details>

## `SELECT` examples

<Tabs
    defaultValue="list_pipes"
    values={[
        { label: 'list_pipes', value: 'list_pipes' },
        { label: 'fetch_pipe', value: 'fetch_pipe' }
    ]
}>
<TabItem value="list_pipes">

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
WHERE database_name = '{{ database_name }}'
AND schema_name = '{{ schema_name }}'
AND endpoint = '{{ endpoint }}';
```
</TabItem>
<TabItem value="fetch_pipe">

Fetch a pipe

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
WHERE database_name = '{{ database_name }}'
AND name = '{{ name }}'
AND schema_name = '{{ schema_name }}'
AND endpoint = '{{ endpoint }}';
```
</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>pipes</code> resource.

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
INSERT INTO snowflake.pipe.pipes (
data__name,
data__comment,
data__auto_ingest,
data__error_integration,
data__aws_sns_topic,
data__integration,
data__copy_statement,
database_name,
schema_name,
endpoint
)
SELECT 
'{{ name }}',
'{{ comment }}',
{{ auto_ingest }},
'{{ error_integration }}',
'{{ aws_sns_topic }}',
'{{ integration }}',
'{{ copy_statement }}',
'{{ database_name }}',
'{{ schema_name }}',
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO snowflake.pipe.pipes (
data__name,
data__copy_statement,
database_name,
schema_name,
endpoint
)
SELECT 
'{{ name }}',
'{{ copy_statement }}',
'{{ database_name }}',
'{{ schema_name }}',
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
# Description fields below are for documentation purposes only and are not required in the manifest
- name: pipes
  props:
    - name: database_name
      value: string
      description: Required parameter for the pipes resource.
    - name: schema_name
      value: string
      description: Required parameter for the pipes resource.
    - name: endpoint
      value: string
      description: Required parameter for the pipes resource.
    - name: name
      value: string
      description: Name of the pipe
    - name: comment
      value: string
      description: user comment associated to an object in the dictionary
    - name: auto_ingest
      value: boolean
      description: TRUE if all files from stage need to be auto-ingested
    - name: error_integration
      value: string
      description: >-
        Link to integration object that point to a user provided Azure storage
        queue / SQS. When present, errors (e.g. ingest failure for Snowpipe or a
        user task failure or replication failure) will be sent to this queue to
        notify customers
    - name: aws_sns_topic
      value: string
      description: >-
        Optional, if provided, auto_ingest pipe will only receive messages from
        this SNS topic.
    - name: integration
      value: string
      description: >-
        Link to integration object that ties a user provided storage queue to an
        auto_ingest enabled pipe. Required for auto_ingest to work on azure.
    - name: copy_statement
      value: string
      description: >-
        COPY INTO statement used to load data from queued files into a Snowflake
        table. This statement serves as the text/definition for the pipe and is
        displayed in the SHOW PIPES output
```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>pipes</code> resource.

```sql
/*+ delete */
DELETE FROM snowflake.pipe.pipes
WHERE database_name = '{{ database_name }}'
AND name = '{{ name }}'
AND schema_name = '{{ schema_name }}'
AND endpoint = '{{ endpoint }}';
```
