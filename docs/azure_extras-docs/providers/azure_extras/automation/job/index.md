---
title: job
hide_title: false
hide_table_of_contents: false
keywords:
  - job
  - automation
  - azure_extras    
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
<tr><td><b>Id</b></td><td><code>azure_extras.automation.job</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Job_Get` | `SELECT` | `automationAccountName, jobName, resourceGroupName, subscriptionId` | Retrieve the job identified by job name. |
| `Job_ListByAutomationAccount` | `SELECT` | `automationAccountName, resourceGroupName, subscriptionId` | Retrieve a list of jobs. |
| `Job_Create` | `INSERT` | `automationAccountName, jobName, resourceGroupName, subscriptionId, data__properties` | Create a job of the runbook. |
| `Job_GetOutput` | `EXEC` | `automationAccountName, jobName, resourceGroupName, subscriptionId` | Retrieve the job output identified by job name. |
| `Job_GetRunbookContent` | `EXEC` | `automationAccountName, jobName, resourceGroupName, subscriptionId` | Retrieve the runbook content of the job identified by job name. |
| `Job_Resume` | `EXEC` | `automationAccountName, jobName, resourceGroupName, subscriptionId` | Resume the job identified by jobName. |
| `Job_Stop` | `EXEC` | `automationAccountName, jobName, resourceGroupName, subscriptionId` | Stop the job identified by jobName. |
| `Job_Suspend` | `EXEC` | `automationAccountName, jobName, resourceGroupName, subscriptionId` | Suspend the job identified by job name. |
