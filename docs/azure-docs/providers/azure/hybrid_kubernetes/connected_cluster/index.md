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
| `identity` | `object` | Identity for the connected cluster. |
| `kind` | `string` | Indicates the kind of Arc connected cluster based on host infrastructure. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties of the connected cluster. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Returns the properties of the specified connected cluster, including name, identity, properties, and additional cluster details. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | API to enumerate registered connected K8s clusters under a Resource Group |
| `list_by_subscription` | `SELECT` | `subscriptionId` | API to enumerate registered connected K8s clusters under a Subscription |
| `create` | `INSERT` | `clusterName, resourceGroupName, subscriptionId, data__identity, data__properties` | API to register a new Kubernetes cluster and create a tracked resource in Azure Resource Manager (ARM). |
| `delete` | `DELETE` | `clusterName, resourceGroupName, subscriptionId` | Delete a connected cluster, removing the tracked resource in Azure Resource Manager (ARM). |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | API to enumerate registered connected K8s clusters under a Resource Group |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | API to enumerate registered connected K8s clusters under a Subscription |
| `update` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | API to update certain properties of the connected cluster resource |
