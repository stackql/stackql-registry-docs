---
title: private_dns_zone_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - private_dns_zone_groups
  - network
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
<tr><td><b>Name</b></td><td><code>private_dns_zone_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.private_dns_zone_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Name of the resource that is unique within a resource group. This name can be used to access the resource. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `properties` | `object` | Properties of the private dns zone group. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PrivateDnsZoneGroups_Get` | `SELECT` | `privateDnsZoneGroupName, privateEndpointName, resourceGroupName, subscriptionId` | Gets the private dns zone group resource by specified private dns zone group name. |
| `PrivateDnsZoneGroups_List` | `SELECT` | `privateEndpointName, resourceGroupName, subscriptionId` | Gets all private dns zone groups in a private endpoint. |
| `PrivateDnsZoneGroups_CreateOrUpdate` | `INSERT` | `privateDnsZoneGroupName, privateEndpointName, resourceGroupName, subscriptionId` | Creates or updates a private dns zone group in the specified private endpoint. |
| `PrivateDnsZoneGroups_Delete` | `DELETE` | `privateDnsZoneGroupName, privateEndpointName, resourceGroupName, subscriptionId` | Deletes the specified private dns zone group. |
