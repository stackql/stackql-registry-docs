---
title: reservation_recommendation_details
hide_title: false
hide_table_of_contents: false
keywords:
  - reservation_recommendation_details
  - consumption
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
<tr><td><b>Name</b></td><td><code>reservation_recommendation_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.consumption.reservation_recommendation_details</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The full qualified ARM ID of an event. |
| `name` | `string` | The ID that uniquely identifies an event.  |
| `type` | `string` | Resource type. |
| `etag` | `string` | The etag for the resource. |
| `location` | `string` | Resource Location. |
| `properties` | `object` | The properties of the reservation recommendation. |
| `sku` | `string` | Resource sku |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ReservationRecommendationDetails_Get` | `SELECT` | `lookBackPeriod, product, region, resourceScope, scope, term` |
