---
title: job_run_output
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - job_run_output
  - workflows
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

Operations on a <code>job_run_output</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>job_run_output</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.workflows.job_run_output" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="dbt_output" /> | `object` |
| <CopyableCode code="error" /> | `string` |
| <CopyableCode code="error_trace" /> | `string` |
| <CopyableCode code="info" /> | `string` |
| <CopyableCode code="logs" /> | `string` |
| <CopyableCode code="logs_truncated" /> | `boolean` |
| <CopyableCode code="metadata" /> | `object` |
| <CopyableCode code="notebook_output" /> | `object` |
| <CopyableCode code="run_job_output" /> | `object` |
| <CopyableCode code="sql_output" /> | `object` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getrunoutput" /> | `SELECT` | <CopyableCode code="run_id, deployment_name" /> | Retrieve the output and metadata of a single task run. When a notebook task returns a value through the |

## `SELECT` examples

```sql
SELECT
dbt_output,
error,
error_trace,
info,
logs,
logs_truncated,
metadata,
notebook_output,
run_job_output,
sql_output
FROM databricks_workspace.workflows.job_run_output
WHERE run_id = '{{ run_id }}' AND
deployment_name = '{{ deployment_name }}';
```
