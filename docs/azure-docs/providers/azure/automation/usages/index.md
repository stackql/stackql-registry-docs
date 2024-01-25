---
title: usages
hide_title: false
hide_table_of_contents: false
keywords:
  - usages
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
<tr><td><b>Name</b></td><td><code>usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.automation.usages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Gets or sets the id of the resource. |
| `name` | `object` | Definition of usage counter name. |
| `currentValue` | `number` | Gets or sets the current usage value. |
| `limit` | `integer` | Gets or sets max limit. -1 for unlimited |
| `throttleStatus` | `string` | Gets or sets the throttle status. |
| `unit` | `string` | Gets or sets the usage unit name. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_by_automation_account` | `SELECT` | `automationAccountName, resourceGroupName, subscriptionId` |
| `_list_by_automation_account` | `EXEC` | `automationAccountName, resourceGroupName, subscriptionId` |
