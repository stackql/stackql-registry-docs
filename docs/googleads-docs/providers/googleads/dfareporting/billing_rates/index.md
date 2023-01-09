---
title: billing_rates
hide_title: false
hide_table_of_contents: false
keywords:
  - billing_rates
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
<tr><td><b>Name</b></td><td><code>billing_rates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.billing_rates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | Pagination token to be used for the next list operation. |
| `billingRates` | `array` | Billing rates collection. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#billingRatesListResponse". |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `billingRates_list` | `SELECT` | `billingProfileId, profileId` |
