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

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_pipes"
    values={[
        { label: 'list_pipes', value: 'list_pipes' },
        { label: 'fetch_pipe', value: 'fetch_pipe' }
    ]}
>
<TabItem value="list_pipes">

A Snowflake pipe

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the pipe</td>
</tr>
<tr>
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>Database in which the pipe is stored</td>
</tr>
<tr>
    <td><CopyableCode code="schema_name" /></td>
    <td><code>string</code></td>
    <td>Schema in which the pipe is stored</td>
</tr>
<tr>
    <td><CopyableCode code="auto_ingest" /></td>
    <td><code>boolean</code></td>
    <td>TRUE if all files from stage need to be auto-ingested</td>
</tr>
<tr>
    <td><CopyableCode code="aws_sns_topic" /></td>
    <td><code>string</code></td>
    <td>Optional, if provided, auto_ingest pipe will only receive messages from this SNS topic.</td>
</tr>
<tr>
    <td><CopyableCode code="budget" /></td>
    <td><code>string</code></td>
    <td>Name of the budget if the pipe is monitored by a budget</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>user comment associated to an object in the dictionary</td>
</tr>
<tr>
    <td><CopyableCode code="copy_statement" /></td>
    <td><code>string</code></td>
    <td>COPY INTO &lt;table&gt; statement used to load data from queued files into a Snowflake table. This statement serves as the text/definition for the pipe and is displayed in the SHOW PIPES output (pattern: (?i)^COPY INTO .*)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the pipe was created.</td>
</tr>
<tr>
    <td><CopyableCode code="error_integration" /></td>
    <td><code>string</code></td>
    <td>Link to integration object that point to a user provided Azure storage queue / SQS. When present,  errors (e.g. ingest failure for Snowpipe or a user task failure or replication failure) will be sent to this queue to notify customers</td>
</tr>
<tr>
    <td><CopyableCode code="integration" /></td>
    <td><code>string</code></td>
    <td>Link to integration object that ties a user provided storage queue to an auto_ingest enabled pipe. Required for auto_ingest to work on azure.</td>
</tr>
<tr>
    <td><CopyableCode code="invalid_reason" /></td>
    <td><code>string</code></td>
    <td>Displays some detailed information for your pipes that may have issues</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td>Role that owns the pipe</td>
</tr>
<tr>
    <td><CopyableCode code="owner_role_type" /></td>
    <td><code>string</code></td>
    <td>The type of role that owns the pipe</td>
</tr>
<tr>
    <td><CopyableCode code="pattern" /></td>
    <td><code>string</code></td>
    <td>PATTERN copy option value in the COPY INTO &lt;table&gt; statement in the pipe definition, if the copy option was specified.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="fetch_pipe">

A Snowflake pipe

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the pipe</td>
</tr>
<tr>
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>Database in which the pipe is stored</td>
</tr>
<tr>
    <td><CopyableCode code="schema_name" /></td>
    <td><code>string</code></td>
    <td>Schema in which the pipe is stored</td>
</tr>
<tr>
    <td><CopyableCode code="auto_ingest" /></td>
    <td><code>boolean</code></td>
    <td>TRUE if all files from stage need to be auto-ingested</td>
</tr>
<tr>
    <td><CopyableCode code="aws_sns_topic" /></td>
    <td><code>string</code></td>
    <td>Optional, if provided, auto_ingest pipe will only receive messages from this SNS topic.</td>
</tr>
<tr>
    <td><CopyableCode code="budget" /></td>
    <td><code>string</code></td>
    <td>Name of the budget if the pipe is monitored by a budget</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>user comment associated to an object in the dictionary</td>
</tr>
<tr>
    <td><CopyableCode code="copy_statement" /></td>
    <td><code>string</code></td>
    <td>COPY INTO &lt;table&gt; statement used to load data from queued files into a Snowflake table. This statement serves as the text/definition for the pipe and is displayed in the SHOW PIPES output (pattern: (?i)^COPY INTO .*)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the pipe was created.</td>
</tr>
<tr>
    <td><CopyableCode code="error_integration" /></td>
    <td><code>string</code></td>
    <td>Link to integration object that point to a user provided Azure storage queue / SQS. When present,  errors (e.g. ingest failure for Snowpipe or a user task failure or replication failure) will be sent to this queue to notify customers</td>
</tr>
<tr>
    <td><CopyableCode code="integration" /></td>
    <td><code>string</code></td>
    <td>Link to integration object that ties a user provided storage queue to an auto_ingest enabled pipe. Required for auto_ingest to work on azure.</td>
</tr>
<tr>
    <td><CopyableCode code="invalid_reason" /></td>
    <td><code>string</code></td>
    <td>Displays some detailed information for your pipes that may have issues</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td>Role that owns the pipe</td>
</tr>
<tr>
    <td><CopyableCode code="owner_role_type" /></td>
    <td><code>string</code></td>
    <td>The type of role that owns the pipe</td>
</tr>
<tr>
    <td><CopyableCode code="pattern" /></td>
    <td><code>string</code></td>
    <td>PATTERN copy option value in the COPY INTO &lt;table&gt; statement in the pipe definition, if the copy option was specified.</td>
</tr>
</tbody>
</table>
</TabItem>
</Tabs>

## Methods

The following methods are available for this resource:

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
    <th>Optional Params</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><a href="#list_pipes"><CopyableCode code="list_pipes" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-like"><code>like</code></a></td>
    <td>List pipes</td>
</tr>
<tr>
    <td><a href="#fetch_pipe"><CopyableCode code="fetch_pipe" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Fetch a pipe</td>
</tr>
<tr>
    <td><a href="#create_pipe"><CopyableCode code="create_pipe" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-createMode"><code>createMode</code></a></td>
    <td>Create a pipe</td>
</tr>
<tr>
    <td><a href="#delete_pipe"><CopyableCode code="delete_pipe" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-ifExists"><code>ifExists</code></a></td>
    <td>Delete a pipe</td>
</tr>
<tr>
    <td><a href="#refresh_pipe"><CopyableCode code="refresh_pipe" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-ifExists"><code>ifExists</code></a>, <a href="#parameter-prefix"><code>prefix</code></a>, <a href="#parameter-modified_after"><code>modified_after</code></a></td>
    <td>Refresh the pipe</td>
</tr>
</tbody>
</table>

## Parameters

Parameters can be passed in the `WHERE` clause of a query. Check the [Methods](#methods) section to see which parameters are required or optional for each operation.

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr id="parameter-database_name">
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>Identifier (i.e. name) for the database to which the resource belongs. You can use the <code>/api/v2/databases</code> GET request to get a list of available databases.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>Organization and Account Name (default: orgid-acctid)</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Identifier (i.e. name) for the resource.</td>
</tr>
<tr id="parameter-schema_name">
    <td><CopyableCode code="schema_name" /></td>
    <td><code>string</code></td>
    <td>Identifier (i.e. name) for the schema to which the resource belongs. You can use the <code>/api/v2/databases/&#123;database&#125;/schemas</code> GET request to get a list of available schemas for the specified database.</td>
</tr>
<tr id="parameter-createMode">
    <td><CopyableCode code="createMode" /></td>
    <td><code>string</code></td>
    <td>Query parameter allowing support for different modes of resource creation. Possible values include: - <code>errorIfExists</code>: Throws an error if you try to create a resource that already exists. - <code>orReplace</code>: Automatically replaces the existing resource with the current one. - <code>ifNotExists</code>: Creates a new resource when an alter is requested for a non-existent resource.</td>
</tr>
<tr id="parameter-ifExists">
    <td><CopyableCode code="ifExists" /></td>
    <td><code>boolean</code></td>
    <td>Query parameter that specifies how to handle the request for a resource that does not exist: - <code>true</code>: The endpoint does not throw an error if the resource does not exist. It returns a 200 success response, but does not take any action on the resource. - <code>false</code>: The endpoint throws an error if the resource doesn't exist.</td>
</tr>
<tr id="parameter-like">
    <td><CopyableCode code="like" /></td>
    <td><code>string</code></td>
    <td>Query parameter to filter the command output by resource name. Uses case-insensitive pattern matching, with support for SQL wildcard characters.</td>
</tr>
<tr id="parameter-modified_after">
    <td><CopyableCode code="modified_after" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp (in ISO-8601 format) of the oldest data files to copy into the Snowpipe ingest queue based on the LAST_MODIFIED date (i.e. date when a file was staged)</td>
</tr>
<tr id="parameter-prefix">
    <td><CopyableCode code="prefix" /></td>
    <td><code>string</code></td>
    <td>Path (or prefix) appended to the stage reference in the pipe definition. The path limits the set of files to load.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_pipes"
    values={[
        { label: 'list_pipes', value: 'list_pipes' },
        { label: 'fetch_pipe', value: 'fetch_pipe' }
    ]}
>
<TabItem value="list_pipes">

List pipes

```sql
SELECT
name,
database_name,
schema_name,
auto_ingest,
aws_sns_topic,
budget,
comment,
copy_statement,
created_on,
error_integration,
integration,
invalid_reason,
owner,
owner_role_type,
pattern
FROM snowflake.pipe.pipes
WHERE database_name = '{{ database_name }}' -- required
AND schema_name = '{{ schema_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND like = '{{ like }}';
```
</TabItem>
<TabItem value="fetch_pipe">

Fetch a pipe

```sql
SELECT
name,
database_name,
schema_name,
auto_ingest,
aws_sns_topic,
budget,
comment,
copy_statement,
created_on,
error_integration,
integration,
invalid_reason,
owner,
owner_role_type,
pattern
FROM snowflake.pipe.pipes
WHERE database_name = '{{ database_name }}' -- required
AND schema_name = '{{ schema_name }}' -- required
AND name = '{{ name }}' -- required
AND endpoint = '{{ endpoint }}' -- required;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_pipe"
    values={[
        { label: 'create_pipe', value: 'create_pipe' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_pipe">

Create a pipe

```sql
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
endpoint,
createMode
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
'{{ endpoint }}',
'{{ createMode }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
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
      description: >
        Name of the pipe
        
    - name: comment
      value: string
      description: >
        user comment associated to an object in the dictionary
        
    - name: auto_ingest
      value: boolean
      description: >
        TRUE if all files from stage need to be auto-ingested
        
    - name: error_integration
      value: string
      description: >
        Link to integration object that point to a user provided Azure storage queue / SQS. When present,  errors (e.g. ingest failure for Snowpipe or a user task failure or replication failure) will be sent to this queue to notify customers
        
    - name: aws_sns_topic
      value: string
      description: >
        Optional, if provided, auto_ingest pipe will only receive messages from this SNS topic.
        
    - name: integration
      value: string
      description: >
        Link to integration object that ties a user provided storage queue to an auto_ingest enabled pipe. Required for auto_ingest to work on azure.
        
    - name: copy_statement
      value: string
      description: >
        COPY INTO <table> statement used to load data from queued files into a Snowflake table. This statement serves as the text/definition for the pipe and is displayed in the SHOW PIPES output
        
    - name: createMode
      value: string
      description: Query parameter allowing support for different modes of resource creation. Possible values include: - `errorIfExists`: Throws an error if you try to create a resource that already exists. - `orReplace`: Automatically replaces the existing resource with the current one. - `ifNotExists`: Creates a new resource when an alter is requested for a non-existent resource.
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_pipe"
    values={[
        { label: 'delete_pipe', value: 'delete_pipe' }
    ]}
>
<TabItem value="delete_pipe">

Delete a pipe

```sql
DELETE FROM snowflake.pipe.pipes
WHERE database_name = '{{ database_name }}' --required
AND schema_name = '{{ schema_name }}' --required
AND name = '{{ name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND ifExists = '{{ ifExists }}';
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="refresh_pipe"
    values={[
        { label: 'refresh_pipe', value: 'refresh_pipe' }
    ]}
>
<TabItem value="refresh_pipe">

Refresh the pipe

```sql
EXEC snowflake.pipe.pipes.refresh_pipe 
@database_name='{{ database_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@ifExists={{ ifExists }}, 
@prefix='{{ prefix }}', 
@modified_after='{{ modified_after }}';
```
</TabItem>
</Tabs>
