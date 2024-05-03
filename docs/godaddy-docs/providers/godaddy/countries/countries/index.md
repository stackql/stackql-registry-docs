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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>countries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="godaddy.countries.countries" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="callingCode" /> | `string` | The calling code prefix used for phone numbers in this country |
| <CopyableCode code="countryKey" /> | `string` | The ISO country-code |
| <CopyableCode code="label" /> | `string` | The localized name of the country |
| <CopyableCode code="states" /> | `array` | List of states/provinces in this country |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_countries" /> | `SELECT` | <CopyableCode code="marketId" /> | Retrieves summary country information for the provided marketId and filters.  Authorization is not required. |
| <CopyableCode code="get_country" /> | `SELECT` | <CopyableCode code="country_key, marketId" /> | Retrieves country and summary state information for provided countryKey. Authorization is not required. |
