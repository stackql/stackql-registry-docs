---
title: marketplace_listings_stubbed
hide_title: false
hide_table_of_contents: false
keywords:
  - marketplace_listings_stubbed
  - apps
  - github    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: /img/providers/github/stackql-github-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>marketplace_listings_stubbed</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.apps.marketplace_listings_stubbed" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `integer` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="description" /> | `string` |
| <CopyableCode code="accounts_url" /> | `string` |
| <CopyableCode code="bullets" /> | `array` |
| <CopyableCode code="has_free_trial" /> | `boolean` |
| <CopyableCode code="monthly_price_in_cents" /> | `integer` |
| <CopyableCode code="number" /> | `integer` |
| <CopyableCode code="price_model" /> | `string` |
| <CopyableCode code="state" /> | `string` |
| <CopyableCode code="unit_name" /> | `string` |
| <CopyableCode code="url" /> | `string` |
| <CopyableCode code="yearly_price_in_cents" /> | `integer` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_plans_stubbed" /> | `SELECT` |  |
