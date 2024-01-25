---
title: test_job
hide_title: false
hide_table_of_contents: false
keywords:
  - test_job
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
<tr><td><b>Name</b></td><td><code>test_job</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.automation.test_job</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `creationTime` | `string` | Gets or sets the creation time of the test job. |
| `endTime` | `string` | Gets or sets the end time of the test job. |
| `exception` | `string` | Gets or sets the exception of the test job. |
| `lastModifiedTime` | `string` | Gets or sets the last modified time of the test job. |
| `lastStatusModifiedTime` | `string` | Gets or sets the last status modified time of the test job. |
| `logActivityTrace` | `integer` | The activity-level tracing options of the runbook. |
| `parameters` | `object` | Gets or sets the parameters of the test job. |
| `runOn` | `string` | Gets or sets the runOn which specifies the group name where the job is to be executed. |
| `startTime` | `string` | Gets or sets the start time of the test job. |
| `status` | `string` | Gets or sets the status of the test job. |
| `statusDetails` | `string` | Gets or sets the status details of the test job. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `automationAccountName, resourceGroupName, runbookName, subscriptionId` | Retrieve the test job for the specified runbook. |
| `create` | `INSERT` | `automationAccountName, resourceGroupName, runbookName, subscriptionId` | Create a test job of the runbook. |
| `resume` | `EXEC` | `automationAccountName, resourceGroupName, runbookName, subscriptionId` | Resume the test job. |
| `stop` | `EXEC` | `automationAccountName, resourceGroupName, runbookName, subscriptionId` | Stop the test job. |
| `suspend` | `EXEC` | `automationAccountName, resourceGroupName, runbookName, subscriptionId` | Suspend the test job. |
