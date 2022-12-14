---
title: vendor_network_functions
hide_title: false
hide_table_of_contents: false
keywords:
  - vendor_network_functions
  - hybrid_network
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
<tr><td><b>Name</b></td><td><code>vendor_network_functions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_network.vendor_network_functions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Vendor network function properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VendorNetworkFunctions_Get` | `SELECT` | `locationName, serviceKey, subscriptionId, vendorName` | Gets information about the specified vendor network function. |
| `VendorNetworkFunctions_List` | `SELECT` | `locationName, subscriptionId, vendorName` | Lists all the vendor network function sub resources in an Azure region, filtered by skuType, skuName, vendorProvisioningState. |
| `VendorNetworkFunctions_CreateOrUpdate` | `INSERT` | `locationName, serviceKey, subscriptionId, vendorName` | Creates or updates a vendor network function. This operation can take up to 6 hours to complete. This is expected service behavior. |
