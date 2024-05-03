---
title: job_target_executions
hide_title: false
hide_table_of_contents: false
keywords:
  - job_target_executions
  - sql
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>job_target_executions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.job_target_executions" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="jobAgentName, jobExecutionId, jobName, resourceGroupName, serverName, stepName, subscriptionId, targetId" /> | Gets a target execution. |
| <CopyableCode code="list_by_job_execution" /> | `SELECT` | <CopyableCode code="jobAgentName, jobExecutionId, jobName, resourceGroupName, serverName, subscriptionId" /> | Lists target executions for all steps of a job execution. |
| <CopyableCode code="list_by_step" /> | `SELECT` | <CopyableCode code="jobAgentName, jobExecutionId, jobName, resourceGroupName, serverName, stepName, subscriptionId" /> | Lists the target executions of a job step execution. |
| <CopyableCode code="_list_by_job_execution" /> | `EXEC` | <CopyableCode code="jobAgentName, jobExecutionId, jobName, resourceGroupName, serverName, subscriptionId" /> | Lists target executions for all steps of a job execution. |
| <CopyableCode code="_list_by_step" /> | `EXEC` | <CopyableCode code="jobAgentName, jobExecutionId, jobName, resourceGroupName, serverName, stepName, subscriptionId" /> | Lists the target executions of a job step execution. |
