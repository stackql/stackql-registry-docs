---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - kusto
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
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.kusto.clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `tags` | `object` | Resource tags. |
| `zones` | `array` | An array represents the availability zones of the cluster. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `identity` | `object` | Identity for the resource. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Class representing the Kusto cluster properties. |
| `sku` | `object` | Azure SKU definition. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Clusters_Get` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Gets a Kusto cluster. |
| `Clusters_List` | `SELECT` | `subscriptionId` | Lists all Kusto clusters within a subscription. |
| `Clusters_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all Kusto clusters within a resource group. |
| `Clusters_CreateOrUpdate` | `INSERT` | `clusterName, resourceGroupName, subscriptionId, data__sku` | Create or update a Kusto cluster. |
| `Clusters_Delete` | `DELETE` | `clusterName, resourceGroupName, subscriptionId` | Deletes a Kusto cluster. |
| `Clusters_AddLanguageExtensions` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Add a list of language extensions that can run within KQL queries. |
| `Clusters_CheckNameAvailability` | `EXEC` | `location, subscriptionId, data__name, data__type` | Checks that the cluster name is valid and is not already in use. |
| `Clusters_DetachFollowerDatabases` | `EXEC` | `clusterName, resourceGroupName, subscriptionId, data__attachedDatabaseConfigurationName, data__clusterResourceId` | Detaches all followers of a database owned by this cluster. |
| `Clusters_DiagnoseVirtualNetwork` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Diagnoses network connectivity status for external resources on which the service is dependent on. |
| `Clusters_ListFollowerDatabases` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Returns a list of databases that are owned by this cluster and were followed by another cluster. |
| `Clusters_ListLanguageExtensions` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Returns a list of language extensions that can run within KQL queries. |
| `Clusters_ListOutboundNetworkDependenciesEndpoints` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Gets the network endpoints of all outbound dependencies of a Kusto cluster |
| `Clusters_ListSkus` | `EXEC` | `subscriptionId` | Lists eligible SKUs for Kusto resource provider. |
| `Clusters_ListSkusByResource` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Returns the SKUs available for the provided resource. |
| `Clusters_RemoveLanguageExtensions` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Remove a list of language extensions that can run within KQL queries. |
| `Clusters_Start` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Starts a Kusto cluster. |
| `Clusters_Stop` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Stops a Kusto cluster. |
| `Clusters_Update` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Update a Kusto cluster. |
