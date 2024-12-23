---
title: statement_execution
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - statement_execution
  - dbsql
  - databricks_workspace
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Databricks resources using SQL
custom_edit_url: null
image: /img/providers/databricks_workspace/stackql-databricks-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Operations on a <code>statement_execution</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>statement_execution</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.dbsql.statement_execution" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="manifest" /> | `object` |
| <CopyableCode code="result" /> | `object` |
| <CopyableCode code="statement_id" /> | `string` |
| <CopyableCode code="status" /> | `object` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getstatement" /> | `SELECT` | <CopyableCode code="statement_id, deployment_name" /> | This request can be used to poll for the statement's status. When the |
| <CopyableCode code="cancelexecution" /> | `EXEC` | <CopyableCode code="statement_id, deployment_name" /> | Requests that an executing statement be canceled. Callers must poll for status to see the terminal state. |
| <CopyableCode code="executestatement" /> | `EXEC` | <CopyableCode code="deployment_name" /> | Execute a SQL statement and optionally await its results for a specified time. |

## `SELECT` examples

```sql
SELECT
manifest,
result,
statement_id,
status
FROM databricks_workspace.dbsql.statement_execution
WHERE statement_id = '{{ statement_id }}' AND
deployment_name = '{{ deployment_name }}';
```
