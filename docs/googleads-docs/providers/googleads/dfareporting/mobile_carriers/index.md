---
title: mobile_carriers
hide_title: false
hide_table_of_contents: false
keywords:
  - mobile_carriers
  - dfareporting
  - googleads    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleads/stackql-googleads-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mobile_carriers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.mobile_carriers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of this mobile carrier. |
| `name` | `string` | Name of this mobile carrier. |
| `countryCode` | `string` | Country code of the country to which this mobile carrier belongs. |
| `countryDartId` | `string` | DART ID of the country to which this mobile carrier belongs. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#mobileCarrier". |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `mobileCarriers_get` | `SELECT` | `id, profileId` | Gets one mobile carrier by ID. |
| `mobileCarriers_list` | `SELECT` | `profileId` | Retrieves a list of mobile carriers. |
