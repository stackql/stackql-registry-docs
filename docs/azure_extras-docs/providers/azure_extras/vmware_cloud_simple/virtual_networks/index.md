---
title: virtual_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_networks
  - vmware_cloud_simple
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
<tr><td><b>Id</b></td><td><code>azure_extras.vmware_cloud_simple.virtual_networks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | virtual network id (privateCloudId:vsphereId) |
| `name` | `string` | &#123;VirtualNetworkName&#125; |
| `properties` | `object` | Properties of virtual network |
| `type` | `string` | &#123;resourceProviderNamespace&#125;/&#123;resourceType&#125; |
| `assignable` | `boolean` | can be used in vm creation/deletion |
| `location` | `string` | Azure region |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualNetworks_Get` | `SELECT` | `api-version, pcName, regionId, subscriptionId, virtualNetworkName` | Return virtual network by its name |
| `VirtualNetworks_List` | `SELECT` | `api-version, pcName, regionId, resourcePoolName, subscriptionId` | Return list of virtual networks in location for private cloud |
