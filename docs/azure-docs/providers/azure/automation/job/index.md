---
title: job
hide_title: false
hide_table_of_contents: false
keywords:
  - job
  - automation
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
<tr><td><b>Name</b></td><td><code>job</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.job" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationAccountName, jobName, resourceGroupName, subscriptionId" /> | Retrieve the job identified by job name. |
| <CopyableCode code="list_by_automation_account" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId" /> | Retrieve a list of jobs. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="automationAccountName, jobName, resourceGroupName, subscriptionId, data__properties" /> | Create a job of the runbook. |
| <CopyableCode code="resume" /> | `EXEC` | <CopyableCode code="automationAccountName, jobName, resourceGroupName, subscriptionId" /> | Resume the job identified by jobName. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="automationAccountName, jobName, resourceGroupName, subscriptionId" /> | Stop the job identified by jobName. |
| <CopyableCode code="suspend" /> | `EXEC` | <CopyableCode code="automationAccountName, jobName, resourceGroupName, subscriptionId" /> | Suspend the job identified by job name. |
