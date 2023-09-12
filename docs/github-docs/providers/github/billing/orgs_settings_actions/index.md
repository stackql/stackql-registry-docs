---
title: orgs_settings_actions
hide_title: false
hide_table_of_contents: false
keywords:
  - orgs_settings_actions
  - billing
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
<tr><td><b>Name</b></td><td><code>orgs_settings_actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.billing.orgs_settings_actions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `total_paid_minutes_used` | `integer` | The total paid GitHub Actions minutes used. |
| `included_minutes` | `integer` | The amount of free GitHub Actions minutes available. |
| `minutes_used_breakdown` | `object` |  |
| `total_minutes_used` | `integer` | The sum of the free and paid GitHub Actions minutes used. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_github_actions_billing_org` | `SELECT` | `org` |
