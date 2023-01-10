---
title: job_schedule
hide_title: false
hide_table_of_contents: false
keywords:
  - job_schedule
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
<tr><td><b>Name</b></td><td><code>job_schedule</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.automation.job_schedule</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Gets the id of the resource. |
| `name` | `string` | Gets the name of the variable. |
| `properties` | `object` | Definition of job schedule parameters. |
| `type` | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `JobSchedule_Get` | `SELECT` | `automationAccountName, jobScheduleId, resourceGroupName, subscriptionId` | Retrieve the job schedule identified by job schedule name. |
| `JobSchedule_ListByAutomationAccount` | `SELECT` | `automationAccountName, resourceGroupName, subscriptionId` | Retrieve a list of job schedules. |
| `JobSchedule_Create` | `INSERT` | `automationAccountName, jobScheduleId, resourceGroupName, subscriptionId, data__properties` | Create a job schedule. |
| `JobSchedule_Delete` | `DELETE` | `automationAccountName, jobScheduleId, resourceGroupName, subscriptionId` | Delete the job schedule identified by job schedule name. |
