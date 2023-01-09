---
title: ad_units
hide_title: false
hide_table_of_contents: false
keywords:
  - ad_units
  - admob
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
<tr><td><b>Name</b></td><td><code>ad_units</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.admob.ad_units</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `adUnits` | `array` | The resulting ad units for the requested account. |
| `nextPageToken` | `string` | If not empty, indicates that there may be more ad units for the request; this value should be passed in a new `ListAdUnitsRequest`. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `accounts_adUnits_list` | `SELECT` | `accountsId` |
