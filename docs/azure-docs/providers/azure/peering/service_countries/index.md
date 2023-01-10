---
title: service_countries
hide_title: false
hide_table_of_contents: false
keywords:
  - service_countries
  - peering
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
<tr><td><b>Name</b></td><td><code>service_countries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.peering.service_countries</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextLink` | `string` | The link to fetch the next page of peering service countries. |
| `value` | `array` | The list of peering service countries. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `PeeringServiceCountries_List` | `SELECT` | `subscriptionId` |
