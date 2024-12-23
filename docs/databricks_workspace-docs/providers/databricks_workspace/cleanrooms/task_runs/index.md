---
title: task_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - task_runs
  - cleanrooms
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

Operations on a <code>task_runs</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>task_runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.cleanrooms.task_runs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="collaborator_job_run_info" /> | `object` |
| <CopyableCode code="notebook_job_run_state" /> | `object` |
| <CopyableCode code="notebook_name" /> | `string` |
| <CopyableCode code="output_schema_expiration_time" /> | `integer` |
| <CopyableCode code="output_schema_name" /> | `string` |
| <CopyableCode code="run_duration" /> | `integer` |
| <CopyableCode code="start_time" /> | `integer` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="clean_room_name, deployment_name" /> | List all the historical notebook task runs in a clean room. |

## `SELECT` examples

```sql
SELECT
collaborator_job_run_info,
notebook_job_run_state,
notebook_name,
output_schema_expiration_time,
output_schema_name,
run_duration,
start_time
FROM databricks_workspace.cleanrooms.task_runs
WHERE clean_room_name = '{{ clean_room_name }}' AND
deployment_name = '{{ deployment_name }}';
```
