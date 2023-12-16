---
title: countries
hide_title: false
hide_table_of_contents: false
keywords:
  - countries
  - countries
  - godaddy    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GoDaddy resources using SQL
custom_edit_url: null
image: /img/providers/godaddy/stackql-godaddy-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>countries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>godaddy.countries.countries</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `callingCode` | `string` | The calling code prefix used for phone numbers in this country |
| `countryKey` | `string` | The ISO country-code |
| `label` | `string` | The localized name of the country |
| `states` | `array` | List of states/provinces in this country |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_countries` | `SELECT` | `marketId` | Retrieves summary country information for the provided marketId and filters.  Authorization is not required. |
| `get_country` | `SELECT` | `country_key, marketId` | Retrieves country and summary state information for provided countryKey. Authorization is not required. |
