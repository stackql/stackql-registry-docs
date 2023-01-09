---
title: pos
hide_title: false
hide_table_of_contents: false
keywords:
  - pos
  - content
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pos</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.content.pos</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `phoneNumber` | `string` | The store phone number. |
| `placeId` | `string` | The Google Place Id of the store location. |
| `storeAddress` | `string` | Required. The street address of the store. |
| `storeCode` | `string` | Required. A store identifier that is unique for the given merchant. |
| `storeName` | `string` | The merchant or store name. |
| `websiteUrl` | `string` | The website url for the store or merchant. |
| `gcidCategory` | `array` | The business type of the store. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "`content#posStore`" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `merchantId, storeCode, targetMerchantId` | Retrieves information about the given store. |
| `list` | `SELECT` | `merchantId, targetMerchantId` | Lists the stores of the target merchant. |
| `insert` | `INSERT` | `merchantId, targetMerchantId` | Creates a store for the given merchant. |
| `delete` | `DELETE` | `merchantId, storeCode, targetMerchantId` | Deletes a store for the given merchant. |
| `custombatch` | `EXEC` |  | Batches multiple POS-related calls in a single request. |
| `inventory` | `EXEC` | `merchantId, targetMerchantId` | Submit inventory for the given merchant. |
| `sale` | `EXEC` | `merchantId, targetMerchantId` | Submit a sale event for the given merchant. |
