---
title: vendor_sku_preview
hide_title: false
hide_table_of_contents: false
keywords:
  - vendor_sku_preview
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
<tr><td><b>Name</b></td><td><code>vendor_sku_preview</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_network.vendor_sku_preview</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ARM ID of the resource. |
| `name` | `string` | The preview subscription ID. |
| `properties` | `object` | PreviewSubscription properties |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VendorSkuPreview_Get` | `SELECT` | `previewSubscription, skuName, subscriptionId, vendorName` | Gets the preview information of a vendor sku. |
| `VendorSkuPreview_List` | `SELECT` | `skuName, subscriptionId, vendorName` | Lists all the preview information of a vendor sku. |
| `VendorSkuPreview_CreateOrUpdate` | `INSERT` | `previewSubscription, skuName, subscriptionId, vendorName` | Creates or updates preview information of a vendor sku. |
| `VendorSkuPreview_Delete` | `DELETE` | `previewSubscription, skuName, subscriptionId, vendorName` | Deletes the preview information of a vendor sku. |
