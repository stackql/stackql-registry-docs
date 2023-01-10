---
title: software_update_configuration_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - software_update_configuration_runs
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
<tr><td><b>Name</b></td><td><code>software_update_configuration_runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.automation.software_update_configuration_runs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id of the software update configuration run |
| `name` | `string` | Name of the software update configuration run. |
| `properties` | `object` | Software update configuration properties. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SoftwareUpdateConfigurationRuns_List` | `SELECT` | `automationAccountName, resourceGroupName, subscriptionId` | Return list of software update configuration runs |
| `SoftwareUpdateConfigurationRuns_GetById` | `EXEC` | `automationAccountName, resourceGroupName, softwareUpdateConfigurationRunId, subscriptionId` | Get a single software update configuration Run by Id. |
