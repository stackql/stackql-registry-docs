---
title: variable
hide_title: false
hide_table_of_contents: false
keywords:
  - variable
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
<tr><td><b>Name</b></td><td><code>variable</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.automation.variable</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Variable_Get` | `SELECT` | `automationAccountName, resourceGroupName, subscriptionId, variableName` | Retrieve the variable identified by variable name. |
| `Variable_ListByAutomationAccount` | `SELECT` | `automationAccountName, resourceGroupName, subscriptionId` | Retrieve a list of variables. |
| `Variable_CreateOrUpdate` | `INSERT` | `automationAccountName, resourceGroupName, subscriptionId, variableName, data__name, data__properties` | Create a variable. |
| `Variable_Delete` | `DELETE` | `automationAccountName, resourceGroupName, subscriptionId, variableName` | Delete the variable. |
| `Variable_Update` | `EXEC` | `automationAccountName, resourceGroupName, subscriptionId, variableName` | Update a variable. |
