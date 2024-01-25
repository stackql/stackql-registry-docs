---
title: front_doors
hide_title: false
hide_table_of_contents: false
keywords:
  - front_doors
  - front_door
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
<tr><td><b>Name</b></td><td><code>front_doors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.front_door.front_doors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `location` | `string` | Resource location. |
| `properties` | `object` | The JSON object that contains the properties required to create an endpoint. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `frontDoorName, resourceGroupName, subscriptionId` | Gets a Front Door with the specified Front Door name under the specified subscription and resource group. |
| `list` | `SELECT` | `subscriptionId` | Lists all of the Front Doors within an Azure subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all of the Front Doors within a resource group under a subscription. |
| `create_or_update` | `INSERT` | `frontDoorName, resourceGroupName, subscriptionId` | Creates a new Front Door with a Front Door name under the specified subscription and resource group. |
| `delete` | `DELETE` | `frontDoorName, resourceGroupName, subscriptionId` | Deletes an existing Front Door with the specified parameters. |
| `_list` | `EXEC` | `subscriptionId` | Lists all of the Front Doors within an Azure subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all of the Front Doors within a resource group under a subscription. |
| `validate_custom_domain` | `EXEC` | `frontDoorName, resourceGroupName, subscriptionId, data__hostName` | Validates the custom domain mapping to ensure it maps to the correct Front Door endpoint in DNS. |
