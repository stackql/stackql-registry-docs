---
title: gateway
hide_title: false
hide_table_of_contents: false
keywords:
  - gateway
  - service_fabric_mesh
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
<tr><td><b>Name</b></td><td><code>gateway</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_fabric_mesh.gateway</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | This type describes properties of a gateway resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, gatewayResourceName, resourceGroupName, subscriptionId` | Gets the information about the gateway resource with the given name. The information include the description and other properties of the gateway. |
| `list_by_resource_group` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | Gets the information about all gateway resources in a given resource group. The information include the description and other properties of the Gateway. |
| `list_by_subscription` | `SELECT` | `api-version, subscriptionId` | Gets the information about all gateway resources in a given resource group. The information include the description and other properties of the gateway. |
| `create` | `INSERT` | `api-version, gatewayResourceName, resourceGroupName, subscriptionId, data__properties` | Creates a gateway resource with the specified name, description and properties. If a gateway resource with the same name exists, then it is updated with the specified description and properties. Use gateway resources to create a gateway for public connectivity for services within your application. |
| `delete` | `DELETE` | `api-version, gatewayResourceName, resourceGroupName, subscriptionId` | Deletes the gateway resource identified by the name. |
| `_list_by_resource_group` | `EXEC` | `api-version, resourceGroupName, subscriptionId` | Gets the information about all gateway resources in a given resource group. The information include the description and other properties of the Gateway. |
| `_list_by_subscription` | `EXEC` | `api-version, subscriptionId` | Gets the information about all gateway resources in a given resource group. The information include the description and other properties of the gateway. |
