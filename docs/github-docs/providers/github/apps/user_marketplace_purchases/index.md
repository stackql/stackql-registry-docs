---
title: user_marketplace_purchases
hide_title: false
hide_table_of_contents: false
keywords:
  - user_marketplace_purchases
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
<tr><td><b>Name</b></td><td><code>user_marketplace_purchases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.apps.user_marketplace_purchases</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `next_billing_date` | `string` |  |
| `on_free_trial` | `boolean` |  |
| `plan` | `object` | Marketplace Listing Plan |
| `unit_count` | `integer` |  |
| `updated_at` | `string` |  |
| `account` | `object` |  |
| `billing_cycle` | `string` |  |
| `free_trial_ends_on` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_subscriptions_for_authenticated_user` | `SELECT` |  |
