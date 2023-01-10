---
title: license_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - license_assignments
  - licensing
  - googleworkspace    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleworkspace/stackql-googleworkspace-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>license_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.licensing.license_assignments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `selfLink` | `string` | Link to this page. |
| `skuId` | `string` | A product SKU's unique identifier. For more information about available SKUs in this version of the API, see Products and SKUs. |
| `skuName` | `string` | Display Name of the sku of the product. |
| `userId` | `string` | The user's current primary email address. If the user's email address changes, use the new email address in your API requests. Since a `userId` is subject to change, do not use a `userId` value as a key for persistent data. This key could break if the current user's email address changes. If the `userId` is suspended, the license status changes. |
| `etags` | `string` | ETag of the resource. |
| `kind` | `string` | Identifies the resource as a LicenseAssignment, which is `licensing#licenseAssignment`. |
| `productId` | `string` | A product's unique identifier. For more information about products in this version of the API, see Product and SKU IDs. |
| `productName` | `string` | Display Name of the product. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `licenseAssignments_get` | `SELECT` | `productId, skuId, userId` | Get a specific user's license by product SKU. |
| `licenseAssignments_delete` | `DELETE` | `productId, skuId, userId` | Revoke a license. |
| `licenseAssignments_insert` | `EXEC` | `productId, skuId` | Assign a license. |
| `licenseAssignments_patch` | `EXEC` | `productId, skuId, userId` | Reassign a user's product SKU with a different SKU in the same product. This method supports patch semantics. |
| `licenseAssignments_update` | `EXEC` | `productId, skuId, userId` | Reassign a user's product SKU with a different SKU in the same product. |
