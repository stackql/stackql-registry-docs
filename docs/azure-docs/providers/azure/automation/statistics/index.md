---
title: statistics
hide_title: false
hide_table_of_contents: false
keywords:
  - statistics
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
<tr><td><b>Name</b></td><td><code>statistics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.automation.statistics</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Gets the id. |
| `counterProperty` | `string` | Gets the property value of the statistic. |
| `counterValue` | `integer` | Gets the value of the statistic. |
| `endTime` | `string` | Gets the endTime of the statistic. |
| `startTime` | `string` | Gets the startTime of the statistic. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_by_automation_account` | `SELECT` | `automationAccountName, resourceGroupName, subscriptionId` |
| `_list_by_automation_account` | `EXEC` | `automationAccountName, resourceGroupName, subscriptionId` |
