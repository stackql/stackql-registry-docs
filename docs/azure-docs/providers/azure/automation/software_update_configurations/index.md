---
title: software_update_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - software_update_configurations
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
<tr><td><b>Name</b></td><td><code>software_update_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.automation.software_update_configurations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id of the software update configuration |
| `name` | `string` | Name of the software update configuration. |
| `properties` | `object` | Software update configuration collection item properties. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `automationAccountName, resourceGroupName, subscriptionId` | Get all software update configurations for the account. |
| `create` | `INSERT` | `automationAccountName, resourceGroupName, softwareUpdateConfigurationName, subscriptionId, data__properties` | Create a new software update configuration with the name given in the URI. |
| `delete` | `DELETE` | `automationAccountName, resourceGroupName, softwareUpdateConfigurationName, subscriptionId` | delete a specific software update configuration. |
| `_list` | `EXEC` | `automationAccountName, resourceGroupName, subscriptionId` | Get all software update configurations for the account. |
| `get_by_name` | `EXEC` | `automationAccountName, resourceGroupName, softwareUpdateConfigurationName, subscriptionId` | Get a single software update configuration by name. |
