---
title: virtual_appliance_sites
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_appliance_sites
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
<tr><td><b>Name</b></td><td><code>virtual_appliance_sites</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.virtual_appliance_sites</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Name of the virtual appliance site. |
| `properties` | `object` | Properties of the rule group. |
| `type` | `string` | Site type. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualApplianceSites_Get` | `SELECT` | `networkVirtualApplianceName, resourceGroupName, siteName, subscriptionId` | Gets the specified Virtual Appliance Site. |
| `VirtualApplianceSites_List` | `SELECT` | `networkVirtualApplianceName, resourceGroupName, subscriptionId` | Lists all Network Virtual Appliance Sites in a Network Virtual Appliance resource. |
| `VirtualApplianceSites_CreateOrUpdate` | `INSERT` | `networkVirtualApplianceName, resourceGroupName, siteName, subscriptionId` | Creates or updates the specified Network Virtual Appliance Site. |
| `VirtualApplianceSites_Delete` | `DELETE` | `networkVirtualApplianceName, resourceGroupName, siteName, subscriptionId` | Deletes the specified site from a Virtual Appliance. |
