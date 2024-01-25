---
title: web_apps_slot_configuration_names
hide_title: false
hide_table_of_contents: false
keywords:
  - web_apps_slot_configuration_names
  - app_service
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
<tr><td><b>Name</b></td><td><code>web_apps_slot_configuration_names</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_service.web_apps_slot_configuration_names</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource Name. |
| `kind` | `string` | Kind of resource. |
| `properties` | `object` | Names for connection strings, application settings, and external Azure storage account configuration<br />identifiers to be marked as sticky to the deployment slot and not moved during a swap operation.<br />This is valid for all deployment slots in an app. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `name, resourceGroupName, subscriptionId` | Description for Gets the names of app settings and connection strings that stick to the slot (not swapped). |
| `update` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Updates the names of application settings and connection string that remain with the slot during swap operation. |
