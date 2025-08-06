--- 
title: statements
hide_title: false
hide_table_of_contents: false
keywords:
  - statements
  - sqlapi
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

Creates, updates, deletes, gets or lists a <code>statements</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>statements</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.sqlapi.statements" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_statement_status"
    values={[
        { label: 'get_statement_status', value: 'get_statement_status' }
    ]}
>
<TabItem value="get_statement_status">

The statement was executed successfully, and the response includes any data requested.

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
    <td><CopyableCode code="code" /></td>
    <td><code>string</code></td>
    <td> (example: 000123)</td>
</tr>
<tr>
    <td><CopyableCode code="createdOn" /></td>
    <td><code>integer (int64)</code></td>
    <td>Timestamp that specifies when the statement execution started.‌ The timestamp is expressed in milliseconds since the epoch.‌</td>
</tr>
<tr>
    <td><CopyableCode code="data" /></td>
    <td><code>array</code></td>
    <td>Result set data.</td>
</tr>
<tr>
    <td><CopyableCode code="message" /></td>
    <td><code>string</code></td>
    <td> (example: successfully executed)</td>
</tr>
<tr>
    <td><CopyableCode code="resultSetMetaData" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="sqlState" /></td>
    <td><code>string</code></td>
    <td> (example: 42601)</td>
</tr>
<tr>
    <td><CopyableCode code="statementHandle" /></td>
    <td><code>string (uuid)</code></td>
    <td> (example: 536fad38-b564-4dc5-9892-a4543504df6c)</td>
</tr>
<tr>
    <td><CopyableCode code="statementStatusUrl" /></td>
    <td><code>string (uri)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="stats" /></td>
    <td><code>object</code></td>
    <td>these stats might not be available for each request.</td>
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
    <td><a href="#get_statement_status"><CopyableCode code="get_statement_status" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint">endpoint</a></td>
    <td></td>
    <td>Checks the status of the execution of the statement with the specified statement handle. If the statement was executed successfully, the operation returns the requested partition of the result set.</td>
</tr>
<tr>
    <td><a href="#submit_statement"><CopyableCode code="submit_statement" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-endpoint">endpoint</a></td>
    <td></td>
    <td>Submits one or more statements for execution. You can specify that the statement should be executed asynchronously.</td>
</tr>
<tr>
    <td><a href="#cancel_statement"><CopyableCode code="cancel_statement" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-endpoint">endpoint</a></td>
    <td></td>
    <td>Cancels the execution of the statement with the specified statement handle.</td>
</tr>
</tbody>
</table>## Parameters

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
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>Organization and Account Name (default: orgid-acctid)</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_statement_status"
    values={[
        { label: 'get_statement_status', value: 'get_statement_status' }
    ]}
>
<TabItem value="get_statement_status">

Checks the status of the execution of the statement with the specified statement handle. If the statement was executed successfully, the operation returns the requested partition of the result set.

```sql
SELECT
code,
createdOn,
data,
message,
resultSetMetaData,
sqlState,
statementHandle,
statementStatusUrl,
stats
FROM snowflake.sqlapi.statements
WHERE endpoint = '{{ endpoint }}' -- required;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="submit_statement"
    values={[
        { label: 'submit_statement', value: 'submit_statement' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="submit_statement">

Submits one or more statements for execution. You can specify that the statement should be executed asynchronously.

```sql
INSERT INTO snowflake.sqlapi.statements (
data__statement,
data__timeout,
data__database,
data__schema,
data__warehouse,
data__role,
data__bindings,
data__parameters,
endpoint
)
SELECT 
'{{ statement }}',
{{ timeout }},
'{{ database }}',
'{{ schema }}',
'{{ warehouse }}',
'{{ role }}',
'{{ bindings }}',
'{{ parameters }}',
'{{ endpoint }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: statements
  props:
    - name: endpoint
      value: string
      description: Required parameter for the statements resource.
    - name: statement
      value: string
      description: >
        SQL statement or batch of SQL statements to execute. You can specify query, DML and DDL statements. The following statements are not supported: PUT, GET, USE, ALTER SESSION, BEGIN, COMMIT, ROLLBACK, statements that set session variables, and statements that create temporary tables and stages.
        
    - name: timeout
      value: integer
      description: >
        Timeout in seconds for statement execution. If the execution of a statement takes longer than the specified timeout, the execution is automatically canceled. To set the timeout to the maximum value (604800 seconds), set timeout to 0.
        
    - name: database
      value: string
      description: >
        Database in which the statement should be executed. The value in this field is case-sensitive.
        
    - name: schema
      value: string
      description: >
        Schema in which the statement should be executed. The value in this field is case-sensitive.
        
    - name: warehouse
      value: string
      description: >
        Warehouse to use when executing the statement. The value in this field is case-sensitive.
        
    - name: role
      value: string
      description: >
        Role to use when executing the statement. The value in this field is case-sensitive.
        
    - name: bindings
      value: object
      description: >
        Values of bind variables in the SQL statement. When executing the statement, Snowflake replaces placeholders ('?' and ':name') in the statement with these specified values.
        
    - name: parameters
      value: object
      description: >
        Session parameters that should be set before executing the statement.
        
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="cancel_statement"
    values={[
        { label: 'cancel_statement', value: 'cancel_statement' }
    ]}
>
<TabItem value="cancel_statement">

Cancels the execution of the statement with the specified statement handle.

```sql
DELETE FROM snowflake.sqlapi.statements
WHERE endpoint = '{{ endpoint }}' --required;
```
</TabItem>
</Tabs>
