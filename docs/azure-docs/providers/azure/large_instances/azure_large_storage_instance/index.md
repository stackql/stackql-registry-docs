---
title: azure_large_storage_instance
hide_title: false
hide_table_of_contents: false
keywords:
  - azure_large_storage_instance
  - large_instances
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
<tr><td><b>Name</b></td><td><code>azure_large_storage_instance</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.large_instances.azure_large_storage_instance</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Describes the properties of an AzureLargeStorageInstance. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `azureLargeStorageInstanceName, resourceGroupName, subscriptionId` | Gets an Azure Large Storage instance for the specified subscription, resource<br />group, and instance name. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Gets a list of AzureLargeStorageInstances in the specified subscription and<br />resource group. The operations returns various properties of each Azure<br />LargeStorage instance. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Gets a list of AzureLargeStorageInstances in the specified subscription. The<br />operations returns various properties of each Azure LargeStorage instance. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Gets a list of AzureLargeStorageInstances in the specified subscription and<br />resource group. The operations returns various properties of each Azure<br />LargeStorage instance. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Gets a list of AzureLargeStorageInstances in the specified subscription. The<br />operations returns various properties of each Azure LargeStorage instance. |
| `update` | `EXEC` | `azureLargeStorageInstanceName, resourceGroupName, subscriptionId` | Patches the Tags field of a Azure Large Storage Instance for the specified<br />subscription, resource group, and instance name. |
