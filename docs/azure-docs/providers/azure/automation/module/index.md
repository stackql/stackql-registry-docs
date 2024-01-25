---
title: module
hide_title: false
hide_table_of_contents: false
keywords:
  - module
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
<tr><td><b>Name</b></td><td><code>module</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.automation.module</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | Gets the etag of the resource. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Definition of the module property type. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `automationAccountName, moduleName, resourceGroupName, subscriptionId` | Retrieve the module identified by module name. |
| `list_by_automation_account` | `SELECT` | `automationAccountName, resourceGroupName, subscriptionId` | Retrieve a list of modules. |
| `create_or_update` | `INSERT` | `automationAccountName, moduleName, resourceGroupName, subscriptionId, data__properties` | Create or Update the module identified by module name. |
| `delete` | `DELETE` | `automationAccountName, moduleName, resourceGroupName, subscriptionId` | Delete the module by name. |
| `_list_by_automation_account` | `EXEC` | `automationAccountName, resourceGroupName, subscriptionId` | Retrieve a list of modules. |
| `update` | `EXEC` | `automationAccountName, moduleName, resourceGroupName, subscriptionId` | Update the module identified by module name. |
