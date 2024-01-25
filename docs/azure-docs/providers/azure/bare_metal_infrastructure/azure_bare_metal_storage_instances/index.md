---
title: azure_bare_metal_storage_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - azure_bare_metal_storage_instances
  - bare_metal_infrastructure
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
<tr><td><b>Name</b></td><td><code>azure_bare_metal_storage_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.bare_metal_infrastructure.azure_bare_metal_storage_instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Identity for Azure Bare Metal Storage Instance. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Describes the properties of an AzureBareMetalStorageInstance. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `azureBareMetalStorageInstanceName, resourceGroupName, subscriptionId` | Gets an Azure Bare Metal Storage instance for the specified subscription, resource group, and instance name. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Gets a list of AzureBareMetalStorage instances in the specified subscription and resource group. The operations returns various properties of each Azure Bare Metal Instance. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Gets a list of AzureBareMetalStorage instances in the specified subscription. The operations returns various properties of each Azure Bare Metal Instance. |
| `create` | `INSERT` | `azureBareMetalStorageInstanceName, resourceGroupName, subscriptionId` |  |
| `delete` | `DELETE` | `azureBareMetalStorageInstanceName, resourceGroupName, subscriptionId` |  |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Gets a list of AzureBareMetalStorage instances in the specified subscription and resource group. The operations returns various properties of each Azure Bare Metal Instance. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Gets a list of AzureBareMetalStorage instances in the specified subscription. The operations returns various properties of each Azure Bare Metal Instance. |
| `update` | `EXEC` | `azureBareMetalStorageInstanceName, resourceGroupName, subscriptionId` | Patches the Tags field of a Azure Bare Metal Storage instance for the specified subscription, resource group, and instance name. |
