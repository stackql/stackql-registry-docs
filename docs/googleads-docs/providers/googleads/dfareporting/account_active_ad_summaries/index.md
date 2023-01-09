---
title: account_active_ad_summaries
hide_title: false
hide_table_of_contents: false
keywords:
  - account_active_ad_summaries
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
<tr><td><b>Name</b></td><td><code>account_active_ad_summaries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.account_active_ad_summaries</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `accountId` | `string` | ID of the account. |
| `activeAds` | `string` | Ads that have been activated for the account |
| `activeAdsLimitTier` | `string` | Maximum number of active ads allowed for the account. |
| `availableAds` | `string` | Ads that can be activated for the account. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#accountActiveAdSummary". |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `accountActiveAdSummaries_get` | `SELECT` | `profileId, summaryAccountId` |
