---
title: marketplace_listing_stubbed_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - marketplace_listing_stubbed_accounts
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>marketplace_listing_stubbed_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.apps.marketplace_listing_stubbed_accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `integer` |
| `login` | `string` |
| `marketplace_pending_change` | `object` |
| `marketplace_purchase` | `object` |
| `organization_billing_email` | `string` |
| `type` | `string` |
| `url` | `string` |
| `email` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_subscription_plan_for_account_stubbed` | `SELECT` | `account_id` |
