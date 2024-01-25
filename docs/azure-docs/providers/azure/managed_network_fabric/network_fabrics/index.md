---
title: network_fabrics
hide_title: false
hide_table_of_contents: false
keywords:
  - network_fabrics
  - managed_network_fabric
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
<tr><td><b>Name</b></td><td><code>network_fabrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.managed_network_fabric.network_fabrics</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Network Fabric Properties defines the properties of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `networkFabricName, resourceGroupName, subscriptionId` | Get Network Fabric resource details. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List all the Network Fabric resources in the given resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List all the Network Fabric resources in the given subscription. |
| `create` | `INSERT` | `networkFabricName, resourceGroupName, subscriptionId, data__properties` | Create Network Fabric resource. |
| `delete` | `DELETE` | `networkFabricName, resourceGroupName, subscriptionId` | Delete Network Fabric resource. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List all the Network Fabric resources in the given resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List all the Network Fabric resources in the given subscription. |
| `commit_configuration` | `EXEC` | `networkFabricName, resourceGroupName, subscriptionId` | Atomic update of the given Network Fabric instance. Sync update of NFA resources at Fabric level. |
| `deprovision` | `EXEC` | `networkFabricName, resourceGroupName, subscriptionId` | Deprovisions the underlying resources in the given Network Fabric instance. |
| `provision` | `EXEC` | `networkFabricName, resourceGroupName, subscriptionId` | Provisions the underlying resources in the given Network Fabric instance. |
| `refresh_configuration` | `EXEC` | `networkFabricName, resourceGroupName, subscriptionId` | Refreshes the configuration of the underlying resources in the given Network Fabric instance. |
| `update` | `EXEC` | `networkFabricName, resourceGroupName, subscriptionId` | Update certain properties of the Network Fabric resource. |
| `upgrade` | `EXEC` | `networkFabricName, resourceGroupName, subscriptionId` | Upgrades the version of the underlying resources in the given Network Fabric instance. |
| `validate_configuration` | `EXEC` | `networkFabricName, resourceGroupName, subscriptionId` | Validates the configuration of the underlying resources in the given Network Fabric instance. |
