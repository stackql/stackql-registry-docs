---
title: managed_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_clusters
  - aks
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
<tr><td><b>Id</b></td><td><code>azure.aks.managed_clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `extendedLocation` | `object` | The complex type of the extended location. |
| `identity` | `object` | Identity for the managed cluster. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties of the managed cluster. |
| `sku` | `object` | The SKU of a Managed Cluster. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` |  |
| `list` | `SELECT` | `subscriptionId` |  |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` |  |
| `create_or_update` | `INSERT` | `resourceGroupName, resourceName, subscriptionId` |  |
| `delete` | `DELETE` | `resourceGroupName, resourceName, subscriptionId` |  |
| `_list` | `EXEC` | `subscriptionId` |  |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` |  |
| `abort_latest_operation` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Aborts the currently running operation on the managed cluster. The Managed Cluster will be moved to a Canceling state and eventually to a Canceled state when cancellation finishes. If the operation completes before cancellation can take place, a 409 error code is returned. |
| `reset_aad_profile` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | **WARNING**: This API will be deprecated. Please see [AKS-managed Azure Active Directory integration](https://aka.ms/aks-managed-aad) to update your cluster with AKS-managed Azure AD. |
| `reset_service_principal_profile` | `EXEC` | `resourceGroupName, resourceName, subscriptionId, data__clientId` | This action cannot be performed on a cluster that is not using a service principal |
| `rotate_cluster_certificates` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | See [Certificate rotation](https://docs.microsoft.com/azure/aks/certificate-rotation) for more details about rotating managed cluster certificates. |
| `rotate_service_account_signing_keys` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` |  |
| `run_command` | `EXEC` | `resourceGroupName, resourceName, subscriptionId, data__command` | AKS will create a pod to run the command. This is primarily useful for private clusters. For more information see [AKS Run Command](https://docs.microsoft.com/azure/aks/private-clusters#aks-run-command-preview). |
| `start` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | See [starting a cluster](https://docs.microsoft.com/azure/aks/start-stop-cluster) for more details about starting a cluster. |
| `stop` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | This can only be performed on Azure Virtual Machine Scale set backed clusters. Stopping a cluster stops the control plane and agent nodes entirely, while maintaining all object and cluster state. A cluster does not accrue charges while it is stopped. See [stopping a cluster](https://docs.microsoft.com/azure/aks/start-stop-cluster) for more details about stopping a cluster. |
