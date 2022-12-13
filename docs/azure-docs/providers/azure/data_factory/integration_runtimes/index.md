---
title: integration_runtimes
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_runtimes
  - data_factory
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
<tr><td><b>Name</b></td><td><code>integration_runtimes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_factory.integration_runtimes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource identifier. |
| `name` | `string` | The resource name. |
| `type` | `string` | The resource type. |
| `etag` | `string` | Etag identifies change in the resource. |
| `properties` | `object` | Azure Data Factory nested object which serves as a compute resource for activities. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `IntegrationRuntimes_Get` | `SELECT` | `api-version, factoryName, integrationRuntimeName, resourceGroupName, subscriptionId` | Gets an integration runtime. |
| `IntegrationRuntimes_ListByFactory` | `SELECT` | `api-version, factoryName, resourceGroupName, subscriptionId` | Lists integration runtimes. |
| `IntegrationRuntimes_CreateOrUpdate` | `INSERT` | `api-version, factoryName, integrationRuntimeName, resourceGroupName, subscriptionId, data__properties` | Creates or updates an integration runtime. |
| `IntegrationRuntimes_Delete` | `DELETE` | `api-version, factoryName, integrationRuntimeName, resourceGroupName, subscriptionId` | Deletes an integration runtime. |
| `IntegrationRuntimes_CreateLinkedIntegrationRuntime` | `EXEC` | `api-version, factoryName, integrationRuntimeName, resourceGroupName, subscriptionId` | Create a linked integration runtime entry in a shared integration runtime. |
| `IntegrationRuntimes_GetConnectionInfo` | `EXEC` | `api-version, factoryName, integrationRuntimeName, resourceGroupName, subscriptionId` | Gets the on-premises integration runtime connection information for encrypting the on-premises data source credentials. |
| `IntegrationRuntimes_GetMonitoringData` | `EXEC` | `api-version, factoryName, integrationRuntimeName, resourceGroupName, subscriptionId` | Get the integration runtime monitoring data, which includes the monitor data for all the nodes under this integration runtime. |
| `IntegrationRuntimes_GetStatus` | `EXEC` | `api-version, factoryName, integrationRuntimeName, resourceGroupName, subscriptionId` | Gets detailed status information for an integration runtime. |
| `IntegrationRuntimes_ListAuthKeys` | `EXEC` | `api-version, factoryName, integrationRuntimeName, resourceGroupName, subscriptionId` | Retrieves the authentication keys for an integration runtime. |
| `IntegrationRuntimes_ListOutboundNetworkDependenciesEndpoints` | `EXEC` | `api-version, factoryName, integrationRuntimeName, resourceGroupName, subscriptionId` | Gets the list of outbound network dependencies for a given Azure-SSIS integration runtime. |
| `IntegrationRuntimes_RegenerateAuthKey` | `EXEC` | `api-version, factoryName, integrationRuntimeName, resourceGroupName, subscriptionId` | Regenerates the authentication key for an integration runtime. |
| `IntegrationRuntimes_RemoveLinks` | `EXEC` | `api-version, factoryName, integrationRuntimeName, resourceGroupName, subscriptionId, data__factoryName` | Remove all linked integration runtimes under specific data factory in a self-hosted integration runtime. |
| `IntegrationRuntimes_Start` | `EXEC` | `api-version, factoryName, integrationRuntimeName, resourceGroupName, subscriptionId` | Starts a ManagedReserved type integration runtime. |
| `IntegrationRuntimes_Stop` | `EXEC` | `api-version, factoryName, integrationRuntimeName, resourceGroupName, subscriptionId` | Stops a ManagedReserved type integration runtime. |
| `IntegrationRuntimes_SyncCredentials` | `EXEC` | `api-version, factoryName, integrationRuntimeName, resourceGroupName, subscriptionId` | Force the integration runtime to synchronize credentials across integration runtime nodes, and this will override the credentials across all worker nodes with those available on the dispatcher node. If you already have the latest credential backup file, you should manually import it (preferred) on any self-hosted integration runtime node than using this API directly. |
| `IntegrationRuntimes_Update` | `EXEC` | `api-version, factoryName, integrationRuntimeName, resourceGroupName, subscriptionId` | Updates an integration runtime. |
| `IntegrationRuntimes_Upgrade` | `EXEC` | `api-version, factoryName, integrationRuntimeName, resourceGroupName, subscriptionId` | Upgrade self-hosted integration runtime to latest version if availability. |
