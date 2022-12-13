---
title: vendors
hide_title: false
hide_table_of_contents: false
keywords:
  - vendors
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
<tr><td><b>Name</b></td><td><code>vendors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_network.vendors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Vendor properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Vendors_Get` | `SELECT` | `subscriptionId, vendorName` | Gets information about the specified vendor. |
| `Vendors_ListBySubscription` | `SELECT` | `subscriptionId` | Lists all the vendors in a subscription. |
| `Vendors_CreateOrUpdate` | `INSERT` | `subscriptionId, vendorName` | Creates or updates a vendor. |
| `Vendors_Delete` | `DELETE` | `subscriptionId, vendorName` | Deletes the specified vendor. |
