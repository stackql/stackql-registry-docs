---
title: vendor_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - vendor_skus
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
<tr><td><b>Name</b></td><td><code>vendor_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_network.vendor_skus</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Sku properties |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VendorSkus_Get` | `SELECT` | `skuName, subscriptionId, vendorName` | Gets information about the specified sku. |
| `VendorSkus_List` | `SELECT` | `subscriptionId, vendorName` | Lists all the skus of a vendor. |
| `VendorSkus_CreateOrUpdate` | `INSERT` | `skuName, subscriptionId, vendorName` | Creates or updates a sku. This operation can take up to 2 hours to complete. This is expected service behavior. |
| `VendorSkus_Delete` | `DELETE` | `skuName, subscriptionId, vendorName` | Deletes the specified sku. This operation can take up to 2 hours to complete. This is expected service behavior. |
| `VendorSkus_ListCredential` | `EXEC` | `skuName, subscriptionId, vendorName` | Generate credentials for publishing SKU images. |
