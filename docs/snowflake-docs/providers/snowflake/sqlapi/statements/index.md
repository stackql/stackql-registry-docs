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
| <CopyableCode code="submit_statement" /> | `SELECT` | <CopyableCode code="User-Agent, endpoint" /> | Submits one or more statements for execution. You can specify that the statement should be executed asynchronously. |
| <CopyableCode code="cancel_statement" /> | `EXEC` | <CopyableCode code="User-Agent, statementHandle, endpoint" /> | Cancels the execution of the statement with the specified statement handle. |

## `SELECT` examples

Submits one or more statements for execution. You can specify that the statement should be executed asynchronously.


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
AND endpoint = '{{ endpoint }}';
```