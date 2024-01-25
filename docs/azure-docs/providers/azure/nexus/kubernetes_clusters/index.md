---
title: kubernetes_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - kubernetes_clusters
  - nexus
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
<tr><td><b>Name</b></td><td><code>kubernetes_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.nexus.kubernetes_clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `extendedLocation` | `object` |  |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` |  |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `kubernetesClusterName, resourceGroupName, subscriptionId` | Get properties of the provided the Kubernetes cluster. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Get a list of Kubernetes clusters in the provided resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Get a list of Kubernetes clusters in the provided subscription. |
| `create_or_update` | `INSERT` | `kubernetesClusterName, resourceGroupName, subscriptionId, data__extendedLocation, data__properties` | Create a new Kubernetes cluster or update the properties of the existing one. |
| `delete` | `DELETE` | `kubernetesClusterName, resourceGroupName, subscriptionId` | Delete the provided Kubernetes cluster. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Get a list of Kubernetes clusters in the provided resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Get a list of Kubernetes clusters in the provided subscription. |
| `restart_node` | `EXEC` | `kubernetesClusterName, resourceGroupName, subscriptionId, data__nodeName` | Restart a targeted node of a Kubernetes cluster. |
| `update` | `EXEC` | `kubernetesClusterName, resourceGroupName, subscriptionId` | Patch the properties of the provided Kubernetes cluster, or update the tags associated with the Kubernetes cluster. Properties and tag updates can be done independently. |
