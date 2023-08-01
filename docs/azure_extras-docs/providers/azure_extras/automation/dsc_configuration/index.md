---
title: dsc_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - dsc_configuration
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
<tr><td><b>Name</b></td><td><code>dsc_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.automation.dsc_configuration</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Definition of the configuration property type. |
| `tags` | `object` | Resource tags. |
| `etag` | `string` | Gets or sets the etag of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DscConfiguration_Get` | `SELECT` | `automationAccountName, configurationName, resourceGroupName, subscriptionId` | Retrieve the configuration identified by configuration name. |
| `DscConfiguration_ListByAutomationAccount` | `SELECT` | `automationAccountName, resourceGroupName, subscriptionId` | Retrieve a list of configurations. |
| `DscConfiguration_CreateOrUpdate` | `INSERT` | `automationAccountName, configurationName, resourceGroupName, subscriptionId, data__properties` | Create the configuration identified by configuration name. |
| `DscConfiguration_Delete` | `DELETE` | `automationAccountName, configurationName, resourceGroupName, subscriptionId` | Delete the dsc configuration identified by configuration name. |
| `DscConfiguration_GetContent` | `EXEC` | `automationAccountName, configurationName, resourceGroupName, subscriptionId` | Retrieve the configuration script identified by configuration name. |
| `DscConfiguration_Update` | `EXEC` | `automationAccountName, configurationName, resourceGroupName, subscriptionId` | Create the configuration identified by configuration name. |
