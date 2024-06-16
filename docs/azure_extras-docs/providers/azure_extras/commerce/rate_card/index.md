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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rate_card</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.commerce.rate_card" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="Currency" /> | `string` | The currency in which the rates are provided. |
| <CopyableCode code="IsTaxIncluded" /> | `boolean` | All rates are pretax, so this will always be returned as 'false'. |
| <CopyableCode code="Locale" /> | `string` | The culture in which the resource information is localized. |
| <CopyableCode code="Meters" /> | `array` | A list of meters. |
| <CopyableCode code="OfferTerms" /> | `array` | A list of offer terms. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="$filter, subscriptionId" /> |
