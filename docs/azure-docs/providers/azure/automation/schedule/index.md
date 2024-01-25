---
title: schedule
hide_title: false
hide_table_of_contents: false
keywords:
  - schedule
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
<tr><td><b>Name</b></td><td><code>schedule</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.automation.schedule</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `automationAccountName, resourceGroupName, scheduleName, subscriptionId` | Retrieve the schedule identified by schedule name. |
| `list_by_automation_account` | `SELECT` | `automationAccountName, resourceGroupName, subscriptionId` | Retrieve a list of schedules. |
| `create_or_update` | `INSERT` | `automationAccountName, resourceGroupName, scheduleName, subscriptionId, data__name, data__properties` | Create a schedule. |
| `delete` | `DELETE` | `automationAccountName, resourceGroupName, scheduleName, subscriptionId` | Delete the schedule identified by schedule name. |
| `_list_by_automation_account` | `EXEC` | `automationAccountName, resourceGroupName, subscriptionId` | Retrieve a list of schedules. |
| `update` | `EXEC` | `automationAccountName, resourceGroupName, scheduleName, subscriptionId` | Update the schedule identified by schedule name. |
