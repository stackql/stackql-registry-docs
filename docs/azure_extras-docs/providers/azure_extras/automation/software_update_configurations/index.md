---
title: software_update_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - software_update_configurations
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
<tr><td><b>Name</b></td><td><code>software_update_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.automation.software_update_configurations</code></td></tr>
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
| `SoftwareUpdateConfigurations_List` | `SELECT` | `automationAccountName, resourceGroupName, subscriptionId` | Get all software update configurations for the account. |
| `SoftwareUpdateConfigurations_Create` | `INSERT` | `automationAccountName, resourceGroupName, softwareUpdateConfigurationName, subscriptionId, data__properties` | Create a new software update configuration with the name given in the URI. |
| `SoftwareUpdateConfigurations_Delete` | `DELETE` | `automationAccountName, resourceGroupName, softwareUpdateConfigurationName, subscriptionId` | delete a specific software update configuration. |
| `SoftwareUpdateConfigurations_GetByName` | `EXEC` | `automationAccountName, resourceGroupName, softwareUpdateConfigurationName, subscriptionId` | Get a single software update configuration by name. |
