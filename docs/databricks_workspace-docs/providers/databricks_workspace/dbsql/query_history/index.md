---
title: query_history
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - query_history
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

Operations on a <code>query_history</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>query_history</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.dbsql.query_history" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="channel_used" /> | `object` |
| <CopyableCode code="duration" /> | `integer` |
| <CopyableCode code="endpoint_id" /> | `string` |
| <CopyableCode code="error_message" /> | `string` |
| <CopyableCode code="executed_as_user_id" /> | `integer` |
| <CopyableCode code="executed_as_user_name" /> | `string` |
| <CopyableCode code="execution_end_time_ms" /> | `integer` |
| <CopyableCode code="is_final" /> | `boolean` |
| <CopyableCode code="lookup_key" /> | `string` |
| <CopyableCode code="metrics" /> | `object` |
| <CopyableCode code="plans_state" /> | `string` |
| <CopyableCode code="query_end_time_ms" /> | `integer` |
| <CopyableCode code="query_id" /> | `string` |
| <CopyableCode code="query_start_time_ms" /> | `integer` |
| <CopyableCode code="query_text" /> | `string` |
| <CopyableCode code="rows_produced" /> | `integer` |
| <CopyableCode code="spark_ui_url" /> | `string` |
| <CopyableCode code="statement_type" /> | `string` |
| <CopyableCode code="status" /> | `string` |
| <CopyableCode code="user_id" /> | `integer` |
| <CopyableCode code="user_name" /> | `string` |
| <CopyableCode code="warehouse_id" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deployment_name" /> | List the history of queries through SQL warehouses, and serverless compute. |

## `SELECT` examples

```sql
SELECT
channel_used,
duration,
endpoint_id,
error_message,
executed_as_user_id,
executed_as_user_name,
execution_end_time_ms,
is_final,
lookup_key,
metrics,
plans_state,
query_end_time_ms,
query_id,
query_start_time_ms,
query_text,
rows_produced,
spark_ui_url,
statement_type,
status,
user_id,
user_name,
warehouse_id
FROM databricks_workspace.dbsql.query_history
WHERE deployment_name = '{{ deployment_name }}';
```
