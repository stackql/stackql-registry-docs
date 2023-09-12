---
title: users_settings_shared_storage
hide_title: false
hide_table_of_contents: false
keywords:
  - users_settings_shared_storage
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
<tr><td><b>Name</b></td><td><code>users_settings_shared_storage</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.billing.users_settings_shared_storage</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `days_left_in_billing_cycle` | `integer` | Numbers of days left in billing cycle. |
| `estimated_paid_storage_for_month` | `integer` | Estimated storage space (GB) used in billing cycle. |
| `estimated_storage_for_month` | `integer` | Estimated sum of free and paid storage space (GB) used in billing cycle. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_shared_storage_billing_user` | `SELECT` | `username` |
