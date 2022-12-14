---
title: network_function_vendor_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - network_function_vendor_skus
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
<tr><td><b>Name</b></td><td><code>network_function_vendor_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_network.network_function_vendor_skus</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `userDataTemplate` | `object` | The user data template. |
| `networkInterfaces` | `array` | The network interface configuration. |
| `roleName` | `string` | The name of the network function role. |
| `userDataParameters` | `object` | The user data parameters. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `NetworkFunctionVendorSkus_ListByVendor` | `SELECT` | `subscriptionId, vendorName` | Lists all network function vendor sku details in a vendor. |
| `networkFunctionVendorSkus_ListBySku` | `SELECT` | `subscriptionId, vendorName, vendorSkuName` | Lists information about network function vendor sku details. |
