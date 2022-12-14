---
title: managed_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_clusters
  - container_service
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
<tr><td><b>Name</b></td><td><code>managed_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_service.managed_clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `tags` | `object` | Resource tags. |
| `extendedLocation` | `object` | The complex type of the extended location. |
| `identity` | `object` | Identity for the managed cluster. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties of the managed cluster. |
| `sku` | `object` | The SKU of a Managed Cluster. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ManagedClusters_Get` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` |  |
| `ManagedClusters_List` | `SELECT` | `subscriptionId` |  |
| `ManagedClusters_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` |  |
| `ManagedClusters_CreateOrUpdate` | `INSERT` | `resourceGroupName, resourceName, subscriptionId` |  |
| `ManagedClusters_Delete` | `DELETE` | `resourceGroupName, resourceName, subscriptionId` |  |
| `ManagedClusters_AbortLatestOperation` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Aborting last running operation on managed cluster.  We return a 204 no content code here to indicate that the operation has been accepted and an abort will be attempted but is not guaranteed to complete successfully. Please look up the provisioning state of the managed cluster to keep track of whether it changes to Canceled. A canceled provisioning state indicates that the abort was successful |
| `ManagedClusters_GetAccessProfile` | `EXEC` | `resourceGroupName, resourceName, roleName, subscriptionId` | **WARNING**: This API will be deprecated. Instead use [ListClusterUserCredentials](https://docs.microsoft.com/rest/api/aks/managedclusters/listclusterusercredentials) or [ListClusterAdminCredentials](https://docs.microsoft.com/rest/api/aks/managedclusters/listclusteradmincredentials) . |
| `ManagedClusters_GetCommandResult` | `EXEC` | `commandId, resourceGroupName, resourceName, subscriptionId` |  |
| `ManagedClusters_GetOSOptions` | `EXEC` | `location, subscriptionId` |  |
| `ManagedClusters_GetUpgradeProfile` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` |  |
| `ManagedClusters_ListClusterAdminCredentials` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` |  |
| `ManagedClusters_ListClusterMonitoringUserCredentials` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` |  |
| `ManagedClusters_ListClusterUserCredentials` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` |  |
| `ManagedClusters_ListOutboundNetworkDependenciesEndpoints` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Gets a list of egress endpoints (network endpoints of all outbound dependencies) in the specified managed cluster. The operation returns properties of each egress endpoint. |
| `ManagedClusters_ResetAADProfile` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` |  |
| `ManagedClusters_ResetServicePrincipalProfile` | `EXEC` | `resourceGroupName, resourceName, subscriptionId, data__clientId` | This action cannot be performed on a cluster that is not using a service principal |
| `ManagedClusters_RotateClusterCertificates` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | See [Certificate rotation](https://docs.microsoft.com/azure/aks/certificate-rotation) for more details about rotating managed cluster certificates. |
| `ManagedClusters_RotateServiceAccountSigningKeys` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` |  |
| `ManagedClusters_RunCommand` | `EXEC` | `resourceGroupName, resourceName, subscriptionId, data__command` | AKS will create a pod to run the command. This is primarily useful for private clusters. For more information see [AKS Run Command](https://docs.microsoft.com/azure/aks/private-clusters#aks-run-command-preview). |
| `ManagedClusters_Start` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | See [starting a cluster](https://docs.microsoft.com/azure/aks/start-stop-cluster) for more details about starting a cluster. |
| `ManagedClusters_Stop` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | This can only be performed on Azure Virtual Machine Scale set backed clusters. Stopping a cluster stops the control plane and agent nodes entirely, while maintaining all object and cluster state. A cluster does not accrue charges while it is stopped. See [stopping a cluster](https://docs.microsoft.com/azure/aks/start-stop-cluster) for more details about stopping a cluster. |
| `ManagedClusters_UpdateTags` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` |  |
