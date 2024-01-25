---
title: offers
hide_title: false
hide_table_of_contents: false
keywords:
  - offers
  - edge_marketplace
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
<tr><td><b>Name</b></td><td><code>offers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.edge_marketplace.offers</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `offerId, resourceUri` | Get a Offer |
| `list` | `SELECT` | `resourceUri` | List Offer resources by parent |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List Offer resources by subscription |
| `_list` | `EXEC` | `resourceUri` | List Offer resources by parent |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List Offer resources by subscription |
| `generate_access_token` | `EXEC` | `offerId, resourceUri, data__edgeMarketPlaceRegion` | A long-running resource action. |
