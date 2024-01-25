---
title: extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - extensions
  - kubernetes_configuration
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
<tr><td><b>Name</b></td><td><code>extensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.kubernetes_configuration.extensions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Identity for the resource. |
| `plan` | `object` | Plan for the resource. |
| `properties` | `object` | Properties of an Extension resource |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `clusterName, clusterResourceName, clusterRp, extensionName, resourceGroupName, subscriptionId` | Gets Kubernetes Cluster Extension. |
| `list` | `SELECT` | `clusterName, clusterResourceName, clusterRp, resourceGroupName, subscriptionId` | List all Extensions in the cluster. |
| `create` | `INSERT` | `clusterName, clusterResourceName, clusterRp, extensionName, resourceGroupName, subscriptionId` | Create a new Kubernetes Cluster Extension. |
| `delete` | `DELETE` | `clusterName, clusterResourceName, clusterRp, extensionName, resourceGroupName, subscriptionId` | Delete a Kubernetes Cluster Extension. This will cause the Agent to Uninstall the extension from the cluster. |
| `_list` | `EXEC` | `clusterName, clusterResourceName, clusterRp, resourceGroupName, subscriptionId` | List all Extensions in the cluster. |
| `update` | `EXEC` | `clusterName, clusterResourceName, clusterRp, extensionName, resourceGroupName, subscriptionId` | Patch an existing Kubernetes Cluster Extension. |
