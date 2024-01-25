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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>job</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.automation.job</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `automationAccountName, jobName, resourceGroupName, subscriptionId` | Retrieve the job identified by job name. |
| `list_by_automation_account` | `SELECT` | `automationAccountName, resourceGroupName, subscriptionId` | Retrieve a list of jobs. |
| `create` | `INSERT` | `automationAccountName, jobName, resourceGroupName, subscriptionId, data__properties` | Create a job of the runbook. |
| `_list_by_automation_account` | `EXEC` | `automationAccountName, resourceGroupName, subscriptionId` | Retrieve a list of jobs. |
| `resume` | `EXEC` | `automationAccountName, jobName, resourceGroupName, subscriptionId` | Resume the job identified by jobName. |
| `stop` | `EXEC` | `automationAccountName, jobName, resourceGroupName, subscriptionId` | Stop the job identified by jobName. |
| `suspend` | `EXEC` | `automationAccountName, jobName, resourceGroupName, subscriptionId` | Suspend the job identified by job name. |
