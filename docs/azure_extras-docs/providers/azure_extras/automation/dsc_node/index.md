---
title: dsc_node
hide_title: false
hide_table_of_contents: false
keywords:
  - dsc_node
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
<tr><td><b>Name</b></td><td><code>dsc_node</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.automation.dsc_node</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DscNode_Get` | `SELECT` | `automationAccountName, nodeId, resourceGroupName, subscriptionId` | Retrieve the dsc node identified by node id. |
| `DscNode_ListByAutomationAccount` | `SELECT` | `automationAccountName, resourceGroupName, subscriptionId` | Retrieve a list of dsc nodes. |
| `DscNode_Delete` | `DELETE` | `automationAccountName, nodeId, resourceGroupName, subscriptionId` | Delete the dsc node identified by node id. |
| `DscNode_Update` | `EXEC` | `automationAccountName, nodeId, resourceGroupName, subscriptionId` | Update the dsc node. |
