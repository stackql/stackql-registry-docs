---
title: virtual_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_networks
  - connected_vsphere
  - azure_isv    
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
<tr><td><b>Id</b></td><td><code>azure_isv.connected_vsphere.virtual_networks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Gets or sets the Id. |
| `name` | `string` | Gets or sets the name. |
| `extendedLocation` | `object` | The extended location. |
| `kind` | `string` | Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value. |
| `location` | `string` | Gets or sets the location. |
| `properties` | `object` | Describes the properties of a Virtual Network. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Gets or sets the Resource tags. |
| `type` | `string` | Gets or sets the type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, resourceGroupName, subscriptionId, virtualNetworkName` | Implements virtual network GET method. |
| `list` | `SELECT` | `api-version, subscriptionId` | List of virtualNetworks in a subscription. |
| `list_by_resource_group` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | List of virtualNetworks in a resource group. |
| `create` | `INSERT` | `api-version, resourceGroupName, subscriptionId, virtualNetworkName, data__location, data__properties` | Create Or Update virtual network. |
| `delete` | `DELETE` | `api-version, resourceGroupName, subscriptionId, virtualNetworkName` | Implements virtual network DELETE method. |
| `_list` | `EXEC` | `api-version, subscriptionId` | List of virtualNetworks in a subscription. |
| `_list_by_resource_group` | `EXEC` | `api-version, resourceGroupName, subscriptionId` | List of virtualNetworks in a resource group. |
| `update` | `EXEC` | `api-version, resourceGroupName, subscriptionId, virtualNetworkName` | API to update certain properties of the virtual network resource. |
