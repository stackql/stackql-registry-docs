---
title: module
hide_title: false
hide_table_of_contents: false
keywords:
  - module
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
<tr><td><b>Name</b></td><td><code>module</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.automation.module</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Definition of the module property type. |
| `tags` | `object` | Resource tags. |
| `etag` | `string` | Gets or sets the etag of the resource. |
| `location` | `string` | The geo-location where the resource lives |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Module_Get` | `SELECT` | `automationAccountName, moduleName, resourceGroupName, subscriptionId` | Retrieve the module identified by module name. |
| `Module_ListByAutomationAccount` | `SELECT` | `automationAccountName, resourceGroupName, subscriptionId` | Retrieve a list of modules. |
| `Module_CreateOrUpdate` | `INSERT` | `automationAccountName, moduleName, resourceGroupName, subscriptionId, data__properties` | Create or Update the module identified by module name. |
| `Module_Delete` | `DELETE` | `automationAccountName, moduleName, resourceGroupName, subscriptionId` | Delete the module by name. |
| `Module_Update` | `EXEC` | `automationAccountName, moduleName, resourceGroupName, subscriptionId` | Update the module identified by module name. |
