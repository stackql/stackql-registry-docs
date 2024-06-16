---
title: job_step_executions
hide_title: false
hide_table_of_contents: false
keywords:
  - job_step_executions
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
<tr><td><b>Name</b></td><td><code>job_step_executions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.job_step_executions" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="jobAgentName, jobExecutionId, jobName, resourceGroupName, serverName, stepName, subscriptionId" /> | Gets a step execution of a job execution. |
| <CopyableCode code="list_by_job_execution" /> | `SELECT` | <CopyableCode code="jobAgentName, jobExecutionId, jobName, resourceGroupName, serverName, subscriptionId" /> | Lists the step executions of a job execution. |
