---
title: app_service_plans
hide_title: false
hide_table_of_contents: false
keywords:
  - app_service_plans
  - web_apps
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
<tr><td><b>Name</b></td><td><code>app_service_plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.web_apps.app_service_plans</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource Name. |
| `tags` | `object` | Resource tags. |
| `kind` | `string` | Kind of resource. |
| `sku` | `object` | Description of a SKU for a scalable resource. |
| `location` | `string` | Resource Location. |
| `extendedLocation` | `object` | Extended Location. |
| `properties` | `object` | AppServicePlan resource specific properties |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AppServicePlans_Get` | `SELECT` | `name, resourceGroupName, subscriptionId` | Description for Get an App Service plan. |
| `AppServicePlans_List` | `SELECT` | `subscriptionId` | Description for Get all App Service plans for a subscription. |
| `AppServicePlans_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Description for Get all App Service plans in a resource group. |
| `AppServicePlans_CreateOrUpdate` | `INSERT` | `name, resourceGroupName, subscriptionId` | Description for Creates or updates an App Service Plan. |
| `AppServicePlans_Delete` | `DELETE` | `name, resourceGroupName, subscriptionId` | Description for Delete an App Service plan. |
| `AppServicePlans_CreateOrUpdateVnetRoute` | `EXEC` | `name, resourceGroupName, routeName, subscriptionId, vnetName` | Description for Create or update a Virtual Network route in an App Service plan. |
| `AppServicePlans_DeleteHybridConnection` | `EXEC` | `name, namespaceName, relayName, resourceGroupName, subscriptionId` | Description for Delete a Hybrid Connection in use in an App Service plan. |
| `AppServicePlans_DeleteVnetRoute` | `EXEC` | `name, resourceGroupName, routeName, subscriptionId, vnetName` | Description for Delete a Virtual Network route in an App Service plan. |
| `AppServicePlans_GetHybridConnection` | `EXEC` | `name, namespaceName, relayName, resourceGroupName, subscriptionId` | Description for Retrieve a Hybrid Connection in use in an App Service plan. |
| `AppServicePlans_GetHybridConnectionPlanLimit` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Get the maximum number of Hybrid Connections allowed in an App Service plan. |
| `AppServicePlans_GetRouteForVnet` | `EXEC` | `name, resourceGroupName, routeName, subscriptionId, vnetName` | Description for Get a Virtual Network route in an App Service plan. |
| `AppServicePlans_GetServerFarmSkus` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets all selectable SKUs for a given App Service Plan |
| `AppServicePlans_GetVnetFromServerFarm` | `EXEC` | `name, resourceGroupName, subscriptionId, vnetName` | Description for Get a Virtual Network associated with an App Service plan. |
| `AppServicePlans_GetVnetGateway` | `EXEC` | `gatewayName, name, resourceGroupName, subscriptionId, vnetName` | Description for Get a Virtual Network gateway. |
| `AppServicePlans_ListCapabilities` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for List all capabilities of an App Service plan. |
| `AppServicePlans_ListHybridConnectionKeys` | `EXEC` | `name, namespaceName, relayName, resourceGroupName, subscriptionId` | Description for Get the send key name and value of a Hybrid Connection. |
| `AppServicePlans_ListHybridConnections` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Retrieve all Hybrid Connections in use in an App Service plan. |
| `AppServicePlans_ListRoutesForVnet` | `EXEC` | `name, resourceGroupName, subscriptionId, vnetName` | Description for Get all routes that are associated with a Virtual Network in an App Service plan. |
| `AppServicePlans_ListUsages` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets server farm usage information |
| `AppServicePlans_ListVnets` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Get all Virtual Networks associated with an App Service plan. |
| `AppServicePlans_ListWebApps` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Get all apps associated with an App Service plan. |
| `AppServicePlans_ListWebAppsByHybridConnection` | `EXEC` | `name, namespaceName, relayName, resourceGroupName, subscriptionId` | Description for Get all apps that use a Hybrid Connection in an App Service Plan. |
| `AppServicePlans_RebootWorker` | `EXEC` | `name, resourceGroupName, subscriptionId, workerName` | Description for Reboot a worker machine in an App Service plan. |
| `AppServicePlans_RestartWebApps` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Restart all apps in an App Service plan. |
| `AppServicePlans_Update` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Creates or updates an App Service Plan. |
| `AppServicePlans_UpdateVnetGateway` | `EXEC` | `gatewayName, name, resourceGroupName, subscriptionId, vnetName` | Description for Update a Virtual Network gateway. |
| `AppServicePlans_UpdateVnetRoute` | `EXEC` | `name, resourceGroupName, routeName, subscriptionId, vnetName` | Description for Create or update a Virtual Network route in an App Service plan. |
