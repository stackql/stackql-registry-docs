---
title: statement_execution_results
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - statement_execution_results
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

Operations on a <code>statement_execution_results</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>statement_execution_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.dbsql.statement_execution_results" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="chunk_index" /> | `integer` |
| <CopyableCode code="data_array" /> | `array` |
| <CopyableCode code="next_chunk_index" /> | `integer` |
| <CopyableCode code="next_chunk_internal_link" /> | `string` |
| <CopyableCode code="row_count" /> | `integer` |
| <CopyableCode code="row_offset" /> | `integer` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getstatementresultchunkn" /> | `SELECT` | <CopyableCode code="chunk_index, statement_id, deployment_name" /> | After the statement execution has |

## `SELECT` examples

```sql
SELECT
chunk_index,
data_array,
next_chunk_index,
next_chunk_internal_link,
row_count,
row_offset
FROM databricks_workspace.dbsql.statement_execution_results
WHERE chunk_index = '{{ chunk_index }}' AND
statement_id = '{{ statement_id }}' AND
deployment_name = '{{ deployment_name }}';
```
