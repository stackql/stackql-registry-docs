---
title: software_update_configuration_machine_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - software_update_configuration_machine_runs
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
<tr><td><b>Name</b></td><td><code>software_update_configuration_machine_runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.automation.software_update_configuration_machine_runs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id of the software update configuration machine run |
| `name` | `string` | Name of the software update configuration machine run |
| `properties` | `object` | Software update configuration machine run properties. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `automationAccountName, resourceGroupName, subscriptionId` | Return list of software update configuration machine runs |
| `_list` | `EXEC` | `automationAccountName, resourceGroupName, subscriptionId` | Return list of software update configuration machine runs |
| `get_by_id` | `EXEC` | `automationAccountName, resourceGroupName, softwareUpdateConfigurationMachineRunId, subscriptionId` | Get a single software update configuration machine run by Id. |
