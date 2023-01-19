---
title: productstatuses
hide_title: false
hide_table_of_contents: false
keywords:
  - productstatuses
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
<tr><td><b>Name</b></td><td><code>productstatuses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.content.productstatuses</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `itemLevelIssues` | `array` | A list of all issues associated with the product. |
| `creationDate` | `string` | Date on which the item has been created, in ISO 8601 format. |
| `lastUpdateDate` | `string` | Date on which the item has been last updated, in ISO 8601 format. |
| `googleExpirationDate` | `string` | Date on which the item expires in Google Shopping, in ISO 8601 format. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "`content#productStatus`" |
| `productId` | `string` | The ID of the product for which status is reported. |
| `link` | `string` | The link to the product. |
| `destinationStatuses` | `array` | The intended destinations for the product. |
| `title` | `string` | The title of the product. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `merchantId, productId` | Gets the status of a product from your Merchant Center account. |
| `list` | `SELECT` | `merchantId` | Lists the statuses of the products in your Merchant Center account. |
| `custombatch` | `EXEC` |  | Gets the statuses of multiple products in a single request. |
