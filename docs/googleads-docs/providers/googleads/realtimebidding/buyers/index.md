---
title: buyers
hide_title: false
hide_table_of_contents: false
keywords:
  - buyers
  - realtimebidding
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
<tr><td><b>Name</b></td><td><code>buyers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.realtimebidding.buyers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Name of the buyer resource that must follow the pattern `buyers/&#123;buyerAccountId&#125;`, where `&#123;buyerAccountId&#125;` is the account ID of the buyer account whose information is to be received. One can get their account ID on the Authorized Buyers or Open Bidding UI, or by contacting their Google account manager. |
| `billingIds` | `array` | Output only. A list of billing IDs associated with this account. These IDs appear on: 1. A bid request, to signal which buyers are eligible to bid on a given opportunity, and which pretargeting configurations were matched for each eligible buyer. 2. The bid response, to attribute a winning impression to a specific account for billing, reporting, policy and publisher block enforcement. |
| `displayName` | `string` | Output only. The diplay name associated with this buyer account, as visible to sellers. |
| `maximumActiveCreativeCount` | `string` | Output only. The maximum number of active creatives that this buyer can have. |
| `activeCreativeCount` | `string` | Output only. The number of creatives that this buyer submitted through the API or bid with in the last 30 days. This is counted against the maximum number of active creatives. |
| `bidder` | `string` | Output only. The name of the bidder resource that is responsible for receiving bidding traffic for this account. The bidder name must follow the pattern `bidders/&#123;bidderAccountId&#125;`, where `&#123;bidderAccountId&#125;` is the account ID of the bidder receiving traffic for this buyer. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `buyersId` | Gets a buyer account by its name. |
| `list` | `SELECT` |  | Lists all buyer account information the calling buyer user or service account is permissioned to manage. |
