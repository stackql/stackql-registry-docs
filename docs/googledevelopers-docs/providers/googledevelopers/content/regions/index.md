---
title: regions
hide_title: false
hide_table_of_contents: false
keywords:
  - regions
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
<tr><td><b>Name</b></td><td><code>regions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.content.regions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `merchantId` | `string` | Output only. Immutable. Merchant that owns the region. |
| `postalCodeArea` | `object` | A list of postal codes that defines the region area. Note: All regions defined using postal codes are accessible via the account's `ShippingSettings.postalCodeGroups` resource. |
| `regionId` | `string` | Output only. Immutable. The ID uniquely identifying each region. |
| `regionalInventoryEligible` | `boolean` | Output only. Indicates if the region is eligible to use in the Regional Inventory configuration. |
| `shippingEligible` | `boolean` | Output only. Indicates if the region is eligible to use in the Shipping Services configuration. |
| `displayName` | `string` | The display name of the region. |
| `geotargetArea` | `object` | A list of geotargets that defines the region area. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `merchantId, regionId` | Retrieves a region defined in your Merchant Center account. |
| `list` | `SELECT` | `merchantId` | Lists the regions in your Merchant Center account. |
| `create` | `INSERT` | `merchantId` | Creates a region definition in your Merchant Center account. |
| `delete` | `DELETE` | `merchantId, regionId` | Deletes a region definition from your Merchant Center account. |
| `patch` | `EXEC` | `merchantId, regionId` | Updates a region definition in your Merchant Center account. |
