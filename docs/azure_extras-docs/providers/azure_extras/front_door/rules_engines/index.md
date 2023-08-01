---
title: rules_engines
hide_title: false
hide_table_of_contents: false
keywords:
  - rules_engines
  - front_door
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
<tr><td><b>Name</b></td><td><code>rules_engines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.front_door.rules_engines</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `type` | `string` | Resource type. |
| `properties` | `object` | The JSON object that contains the properties required to create a Rules Engine Configuration. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `RulesEngines_Get` | `SELECT` | `frontDoorName, resourceGroupName, rulesEngineName, subscriptionId` | Gets a Rules Engine Configuration with the specified name within the specified Front Door. |
| `RulesEngines_ListByFrontDoor` | `SELECT` | `frontDoorName, resourceGroupName, subscriptionId` | Lists all of the Rules Engine Configurations within a Front Door. |
| `RulesEngines_CreateOrUpdate` | `INSERT` | `frontDoorName, resourceGroupName, rulesEngineName, subscriptionId` | Creates a new Rules Engine Configuration with the specified name within the specified Front Door. |
| `RulesEngines_Delete` | `DELETE` | `frontDoorName, resourceGroupName, rulesEngineName, subscriptionId` | Deletes an existing Rules Engine Configuration with the specified parameters. |
