---
title: virtual_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_networks
  - dev_test_labs
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>virtual_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.dev_test_labs.virtual_networks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The identifier of the resource. |
| `name` | `string` | The name of the resource. |
| `location` | `string` | The location of the resource. |
| `properties` | `object` | Properties of a virtual network. |
| `tags` | `object` | The tags of the resource. |
| `type` | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualNetworks_Get` | `SELECT` | `api-version, labName, name, resourceGroupName, subscriptionId` | Get virtual network. |
| `VirtualNetworks_List` | `SELECT` | `api-version, labName, resourceGroupName, subscriptionId` | List virtual networks in a given lab. |
| `VirtualNetworks_CreateOrUpdate` | `INSERT` | `api-version, labName, name, resourceGroupName, subscriptionId` | Create or replace an existing virtual network. This operation can take a while to complete. |
| `VirtualNetworks_Delete` | `DELETE` | `api-version, labName, name, resourceGroupName, subscriptionId` | Delete virtual network. This operation can take a while to complete. |
| `VirtualNetworks_Update` | `EXEC` | `api-version, labName, name, resourceGroupName, subscriptionId` | Allows modifying tags of virtual networks. All other properties will be ignored. |
