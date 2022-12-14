---
title: app_service_environments
hide_title: false
hide_table_of_contents: false
keywords:
  - app_service_environments
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
<tr><td><b>Name</b></td><td><code>app_service_environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.web_apps.app_service_environments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource Name. |
| `properties` | `object` | Description of an App Service Environment. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
| `kind` | `string` | Kind of resource. |
| `location` | `string` | Resource Location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AppServiceEnvironments_Get` | `SELECT` | `name, resourceGroupName, subscriptionId` | Description for Get the properties of an App Service Environment. |
| `AppServiceEnvironments_List` | `SELECT` | `subscriptionId` | Description for Get all App Service Environments for a subscription. |
| `AppServiceEnvironments_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Description for Get all App Service Environments in a resource group. |
| `AppServiceEnvironments_CreateOrUpdate` | `INSERT` | `name, resourceGroupName, subscriptionId` | Description for Create or update an App Service Environment. |
| `AppServiceEnvironments_Delete` | `DELETE` | `name, resourceGroupName, subscriptionId` | Description for Delete an App Service Environment. |
| `AppServiceEnvironments_ApproveOrRejectPrivateEndpointConnection` | `EXEC` | `name, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Description for Approves or rejects a private endpoint connection |
| `AppServiceEnvironments_ChangeVnet` | `EXEC` | `name, resourceGroupName, subscriptionId, data__id` | Description for Move an App Service Environment to a different VNET. |
| `AppServiceEnvironments_CreateOrUpdateMultiRolePool` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Create or update a multi-role pool. |
| `AppServiceEnvironments_CreateOrUpdateWorkerPool` | `EXEC` | `name, resourceGroupName, subscriptionId, workerPoolName` | Description for Create or update a worker pool. |
| `AppServiceEnvironments_DeleteAseCustomDnsSuffixConfiguration` | `EXEC` | `name, resourceGroupName, subscriptionId` |  |
| `AppServiceEnvironments_DeletePrivateEndpointConnection` | `EXEC` | `name, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Description for Deletes a private endpoint connection |
| `AppServiceEnvironments_GetAseCustomDnsSuffixConfiguration` | `EXEC` | `name, resourceGroupName, subscriptionId` |  |
| `AppServiceEnvironments_GetAseV3NetworkingConfiguration` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Get networking configuration of an App Service Environment |
| `AppServiceEnvironments_GetDiagnosticsItem` | `EXEC` | `diagnosticsName, name, resourceGroupName, subscriptionId` | Description for Get a diagnostics item for an App Service Environment. |
| `AppServiceEnvironments_GetInboundNetworkDependenciesEndpoints` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Get the network endpoints of all inbound dependencies of an App Service Environment. |
| `AppServiceEnvironments_GetMultiRolePool` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Get properties of a multi-role pool. |
| `AppServiceEnvironments_GetOutboundNetworkDependenciesEndpoints` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Get the network endpoints of all outbound dependencies of an App Service Environment. |
| `AppServiceEnvironments_GetPrivateEndpointConnection` | `EXEC` | `name, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Description for Gets a private endpoint connection |
| `AppServiceEnvironments_GetPrivateEndpointConnectionList` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets the list of private endpoints associated with a hosting environment |
| `AppServiceEnvironments_GetPrivateLinkResources` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets the private link resources |
| `AppServiceEnvironments_GetVipInfo` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Get IP addresses assigned to an App Service Environment. |
| `AppServiceEnvironments_GetWorkerPool` | `EXEC` | `name, resourceGroupName, subscriptionId, workerPoolName` | Description for Get properties of a worker pool. |
| `AppServiceEnvironments_ListAppServicePlans` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Get all App Service plans in an App Service Environment. |
| `AppServiceEnvironments_ListCapacities` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Get the used, available, and total worker capacity an App Service Environment. |
| `AppServiceEnvironments_ListDiagnostics` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Get diagnostic information for an App Service Environment. |
| `AppServiceEnvironments_ListMultiRoleMetricDefinitions` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Get metric definitions for a multi-role pool of an App Service Environment. |
| `AppServiceEnvironments_ListMultiRolePoolInstanceMetricDefinitions` | `EXEC` | `instance, name, resourceGroupName, subscriptionId` | Description for Get metric definitions for a specific instance of a multi-role pool of an App Service Environment. |
| `AppServiceEnvironments_ListMultiRolePoolSkus` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Get available SKUs for scaling a multi-role pool. |
| `AppServiceEnvironments_ListMultiRolePools` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Get all multi-role pools. |
| `AppServiceEnvironments_ListMultiRoleUsages` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Get usage metrics for a multi-role pool of an App Service Environment. |
| `AppServiceEnvironments_ListOperations` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for List all currently running operations on the App Service Environment. |
| `AppServiceEnvironments_ListUsages` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Get global usage metrics of an App Service Environment. |
| `AppServiceEnvironments_ListWebApps` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Get all apps in an App Service Environment. |
| `AppServiceEnvironments_ListWebWorkerMetricDefinitions` | `EXEC` | `name, resourceGroupName, subscriptionId, workerPoolName` | Description for Get metric definitions for a worker pool of an App Service Environment. |
| `AppServiceEnvironments_ListWebWorkerUsages` | `EXEC` | `name, resourceGroupName, subscriptionId, workerPoolName` | Description for Get usage metrics for a worker pool of an App Service Environment. |
| `AppServiceEnvironments_ListWorkerPoolInstanceMetricDefinitions` | `EXEC` | `instance, name, resourceGroupName, subscriptionId, workerPoolName` | Description for Get metric definitions for a specific instance of a worker pool of an App Service Environment. |
| `AppServiceEnvironments_ListWorkerPoolSkus` | `EXEC` | `name, resourceGroupName, subscriptionId, workerPoolName` | Description for Get available SKUs for scaling a worker pool. |
| `AppServiceEnvironments_ListWorkerPools` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Get all worker pools of an App Service Environment. |
| `AppServiceEnvironments_Reboot` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Reboot all machines in an App Service Environment. |
| `AppServiceEnvironments_Resume` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Resume an App Service Environment. |
| `AppServiceEnvironments_Suspend` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Suspend an App Service Environment. |
| `AppServiceEnvironments_TestUpgradeAvailableNotification` | `EXEC` | `name, resourceGroupName, subscriptionId` |  |
| `AppServiceEnvironments_Update` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Create or update an App Service Environment. |
| `AppServiceEnvironments_UpdateAseCustomDnsSuffixConfiguration` | `EXEC` | `name, resourceGroupName, subscriptionId` |  |
| `AppServiceEnvironments_UpdateAseNetworkingConfiguration` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Update networking configuration of an App Service Environment |
| `AppServiceEnvironments_UpdateMultiRolePool` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Create or update a multi-role pool. |
| `AppServiceEnvironments_UpdateWorkerPool` | `EXEC` | `name, resourceGroupName, subscriptionId, workerPoolName` | Description for Create or update a worker pool. |
| `AppServiceEnvironments_Upgrade` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Initiate an upgrade of an App Service Environment if one is available. |
