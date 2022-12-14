---
title: connected_cluster
hide_title: false
hide_table_of_contents: false
keywords:
  - connected_cluster
  - hybrid_kubernetes
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
<tr><td><b>Name</b></td><td><code>connected_cluster</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_kubernetes.connected_cluster</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
| `identity` | `object` | Identity for the connected cluster. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties of the connected cluster. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ConnectedCluster_Get` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Returns the properties of the specified connected cluster, including name, identity, properties, and additional cluster details. |
| `ConnectedCluster_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | API to enumerate registered connected K8s clusters under a Resource Group |
| `ConnectedCluster_ListBySubscription` | `SELECT` | `subscriptionId` | API to enumerate registered connected K8s clusters under a Subscription |
| `ConnectedCluster_Create` | `INSERT` | `clusterName, resourceGroupName, subscriptionId, data__identity, data__properties` | API to register a new Kubernetes cluster and create a tracked resource in Azure Resource Manager (ARM). |
| `ConnectedCluster_Delete` | `DELETE` | `clusterName, resourceGroupName, subscriptionId` | Delete a connected cluster, removing the tracked resource in Azure Resource Manager (ARM). |
| `ConnectedCluster_ListClusterUserCredential` | `EXEC` | `clusterName, resourceGroupName, subscriptionId, data__authenticationMethod, data__clientProxy` | Gets cluster user credentials of the connected cluster with a specified resource group and name. |
| `ConnectedCluster_Update` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | API to update certain properties of the connected cluster resource |
