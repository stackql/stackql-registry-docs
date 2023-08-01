---
title: rate_card
hide_title: false
hide_table_of_contents: false
keywords:
  - rate_card
  - commerce
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
<tr><td><b>Name</b></td><td><code>rate_card</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.commerce.rate_card</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `OfferTerms` | `array` | A list of offer terms. |
| `Currency` | `string` | The currency in which the rates are provided. |
| `IsTaxIncluded` | `boolean` | All rates are pretax, so this will always be returned as 'false'. |
| `Locale` | `string` | The culture in which the resource information is localized. |
| `Meters` | `array` | A list of meters. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `RateCard_Get` | `SELECT` | `$filter, subscriptionId` |
