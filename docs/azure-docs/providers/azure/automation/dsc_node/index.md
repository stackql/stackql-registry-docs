---
title: dsc_node
hide_title: false
hide_table_of_contents: false
keywords:
  - dsc_node
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
<tr><td><b>Name</b></td><td><code>dsc_node</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.automation.dsc_node</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `automationAccountName, nodeId, resourceGroupName, subscriptionId` | Retrieve the dsc node identified by node id. |
| `list_by_automation_account` | `SELECT` | `automationAccountName, resourceGroupName, subscriptionId` | Retrieve a list of dsc nodes. |
| `delete` | `DELETE` | `automationAccountName, nodeId, resourceGroupName, subscriptionId` | Delete the dsc node identified by node id. |
| `_list_by_automation_account` | `EXEC` | `automationAccountName, resourceGroupName, subscriptionId` | Retrieve a list of dsc nodes. |
| `update` | `EXEC` | `automationAccountName, nodeId, resourceGroupName, subscriptionId` | Update the dsc node. |
