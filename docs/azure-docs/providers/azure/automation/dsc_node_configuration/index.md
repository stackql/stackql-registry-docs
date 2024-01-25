---
title: dsc_node_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - dsc_node_configuration
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
<tr><td><b>Name</b></td><td><code>dsc_node_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.automation.dsc_node_configuration</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `automationAccountName, nodeConfigurationName, resourceGroupName, subscriptionId` | Retrieve the Dsc node configurations by node configuration. |
| `list_by_automation_account` | `SELECT` | `automationAccountName, resourceGroupName, subscriptionId` | Retrieve a list of dsc node configurations. |
| `create_or_update` | `INSERT` | `automationAccountName, nodeConfigurationName, resourceGroupName, subscriptionId` | Create the node configuration identified by node configuration name. |
| `delete` | `DELETE` | `automationAccountName, nodeConfigurationName, resourceGroupName, subscriptionId` | Delete the Dsc node configurations by node configuration. |
| `_list_by_automation_account` | `EXEC` | `automationAccountName, resourceGroupName, subscriptionId` | Retrieve a list of dsc node configurations. |
