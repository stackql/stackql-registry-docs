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
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="code" /> | `string` |  |
| <CopyableCode code="createdOn" /> | `integer` | Timestamp that specifies when the statement execution started.‌ The timestamp is expressed in milliseconds since the epoch.‌ |
| <CopyableCode code="data" /> | `array` | Result set data. |
| <CopyableCode code="message" /> | `string` |  |
| <CopyableCode code="resultSetMetaData" /> | `object` |  |
| <CopyableCode code="sqlState" /> | `string` |  |
| <CopyableCode code="statementHandle" /> | `string` |  |
| <CopyableCode code="statementStatusUrl" /> | `string` |  |
| <CopyableCode code="stats" /> | `object` | these stats might not be available for each request. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_statement_status" /> | `SELECT` | <CopyableCode code="User-Agent, statementHandle, endpoint" /> | Checks the status of the execution of the statement with the specified statement handle. If the statement was executed successfully, the operation returns the requested partition of the result set. |
| <CopyableCode code="submit_statement" /> | `INSERT` | <CopyableCode code="User-Agent, endpoint" /> | Submits one or more statements for execution. You can specify that the statement should be executed asynchronously. |
| <CopyableCode code="cancel_statement" /> | `DELETE` | <CopyableCode code="User-Agent, statementHandle, endpoint" /> | Cancels the execution of the statement with the specified statement handle. |

<br />

## `SELECT` examples

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
WHERE User-Agent = '{{ User-Agent }}'
AND statementHandle = '{{ statementHandle }}'
AND endpoint = '{{ endpoint }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>statements</code> resource.

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
INSERT INTO snowflake.sqlapi.statements (
data__statement,
data__timeout,
data__database,
data__schema,
data__warehouse,
data__role,
data__bindings,
data__parameters,
User-Agent,
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
'{{ User-Agent }}',
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO snowflake.sqlapi.statements (
User-Agent,
endpoint
)
SELECT 
'{{ User-Agent }}',
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
# Description fields below are for documentation purposes only and are not required in the manifest
- name: statements
  props:
    - name: User-Agent
      value: string
      description: Required parameter for the statements resource.
    - name: endpoint
      value: string
      description: Required parameter for the statements resource.
    - name: statement
      value: string
      description: >-
        SQL statement or batch of SQL statements to execute. You can specify
        query, DML and DDL statements. The following statements are not
        supported: PUT, GET, USE, ALTER SESSION, BEGIN, COMMIT, ROLLBACK,
        statements that set session variables, and statements that create
        temporary tables and stages.
    - name: timeout
      value: integer
      description: >-
        Timeout in seconds for statement execution. If the execution of a
        statement takes longer than the specified timeout, the execution is
        automatically canceled. To set the timeout to the maximum value (604800
        seconds), set timeout to 0.
    - name: database
      value: string
      description: >-
        Database in which the statement should be executed. The value in this
        field is case-sensitive.
    - name: schema
      value: string
      description: >-
        Schema in which the statement should be executed. The value in this
        field is case-sensitive.
    - name: warehouse
      value: string
      description: >-
        Warehouse to use when executing the statement. The value in this field
        is case-sensitive.
    - name: role
      value: string
      description: >-
        Role to use when executing the statement. The value in this field is
        case-sensitive.
    - name: bindings
      value: {}
      description: >-
        Values of bind variables in the SQL statement. When executing the
        statement, Snowflake replaces placeholders ('?' and ':name') in the
        statement with these specified values.
    - name: parameters
      value:
        timezone: string
        query_tag: string
        binary_output_format: string
        date_output_format: string
        time_output_format: string
        timestamp_output_format: string
        timestamp_ltz_output_format: string
        timestamp_ntz_output_format: string
        timestamp_tz_output_format: string
        multi_statement_count: integer
      description: Session parameters that should be set before executing the statement.
```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>statements</code> resource.

```sql
/*+ delete */
DELETE FROM snowflake.sqlapi.statements
WHERE User-Agent = '{{ User-Agent }}'
AND statementHandle = '{{ statementHandle }}'
AND endpoint = '{{ endpoint }}';
```
