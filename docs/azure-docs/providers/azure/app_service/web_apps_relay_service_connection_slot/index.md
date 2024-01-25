---
title: web_apps_relay_service_connection_slot
hide_title: false
hide_table_of_contents: false
keywords:
  - web_apps_relay_service_connection_slot
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
<tr><td><b>Name</b></td><td><code>web_apps_relay_service_connection_slot</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_service.web_apps_relay_service_connection_slot</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource Name. |
| `kind` | `string` | Kind of resource. |
| `properties` | `object` | RelayServiceConnectionEntity resource specific properties |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `entityName, name, resourceGroupName, slot, subscriptionId` | Description for Gets a hybrid connection configuration by its name. |
| `create_or_update` | `INSERT` | `entityName, name, resourceGroupName, slot, subscriptionId` | Description for Creates a new hybrid connection configuration (PUT), or updates an existing one (PATCH). |
| `delete` | `DELETE` | `entityName, name, resourceGroupName, slot, subscriptionId` | Description for Deletes a relay service connection by its name. |
| `update` | `EXEC` | `entityName, name, resourceGroupName, slot, subscriptionId` | Description for Creates a new hybrid connection configuration (PUT), or updates an existing one (PATCH). |
