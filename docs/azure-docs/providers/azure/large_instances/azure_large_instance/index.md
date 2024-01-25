---
title: azure_large_instance
hide_title: false
hide_table_of_contents: false
keywords:
  - azure_large_instance
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
<tr><td><b>Name</b></td><td><code>azure_large_instance</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.large_instances.azure_large_instance</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Describes the properties of an Azure Large Instance. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `azureLargeInstanceName, resourceGroupName, subscriptionId` | Gets an Azure Large Instance for the specified subscription, resource group,<br />and instance name. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Gets a list of Azure Large Instances in the specified subscription and resource<br />group. The operations returns various properties of each Azure Large Instance. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Gets a list of Azure Large Instances in the specified subscription. The<br />operations returns various properties of each Azure Large Instance. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Gets a list of Azure Large Instances in the specified subscription and resource<br />group. The operations returns various properties of each Azure Large Instance. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Gets a list of Azure Large Instances in the specified subscription. The<br />operations returns various properties of each Azure Large Instance. |
| `restart` | `EXEC` | `azureLargeInstanceName, resourceGroupName, subscriptionId` | The operation to restart an Azure Large Instance (only for compute instances) |
| `shutdown` | `EXEC` | `azureLargeInstanceName, resourceGroupName, subscriptionId` | The operation to shutdown an Azure Large Instance (only for compute instances) |
| `start` | `EXEC` | `azureLargeInstanceName, resourceGroupName, subscriptionId` | The operation to start an Azure Large Instance (only for compute instances) |
| `update` | `EXEC` | `azureLargeInstanceName, resourceGroupName, subscriptionId` | Patches the Tags field of an Azure Large Instance for the specified<br />subscription, resource group, and instance name. |
