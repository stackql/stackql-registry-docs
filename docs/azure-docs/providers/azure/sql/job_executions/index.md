---
title: job_executions
hide_title: false
hide_table_of_contents: false
keywords:
  - job_executions
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
<tr><td><b>Name</b></td><td><code>job_executions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.job_executions" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="jobAgentName, jobExecutionId, jobName, resourceGroupName, serverName, subscriptionId" /> | Gets a job execution. |
| <CopyableCode code="list_by_agent" /> | `SELECT` | <CopyableCode code="jobAgentName, resourceGroupName, serverName, subscriptionId" /> | Lists all executions in a job agent. |
| <CopyableCode code="list_by_job" /> | `SELECT` | <CopyableCode code="jobAgentName, jobName, resourceGroupName, serverName, subscriptionId" /> | Lists a job's executions. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="jobAgentName, jobName, resourceGroupName, serverName, subscriptionId" /> | Starts an elastic job execution. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="jobAgentName, jobExecutionId, jobName, resourceGroupName, serverName, subscriptionId" /> | Creates or updates a job execution. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="jobAgentName, jobExecutionId, jobName, resourceGroupName, serverName, subscriptionId" /> | Requests cancellation of a job execution. |
