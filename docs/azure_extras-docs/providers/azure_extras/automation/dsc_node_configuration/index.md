---
title: dsc_node_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - dsc_node_configuration
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
<tr><td><b>Name</b></td><td><code>dsc_node_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.automation.dsc_node_configuration</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DscNodeConfiguration_Get` | `SELECT` | `automationAccountName, nodeConfigurationName, resourceGroupName, subscriptionId` | Retrieve the Dsc node configurations by node configuration. |
| `DscNodeConfiguration_ListByAutomationAccount` | `SELECT` | `automationAccountName, resourceGroupName, subscriptionId` | Retrieve a list of dsc node configurations. |
| `DscNodeConfiguration_CreateOrUpdate` | `INSERT` | `automationAccountName, nodeConfigurationName, resourceGroupName, subscriptionId` | Create the node configuration identified by node configuration name. |
| `DscNodeConfiguration_Delete` | `DELETE` | `automationAccountName, nodeConfigurationName, resourceGroupName, subscriptionId` | Delete the Dsc node configurations by node configuration. |
