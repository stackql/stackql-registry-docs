---
title: users_settings_packages
hide_title: false
hide_table_of_contents: false
keywords:
  - users_settings_packages
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
<tr><td><b>Name</b></td><td><code>users_settings_packages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.billing.users_settings_packages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `total_gigabytes_bandwidth_used` | `integer` | Sum of the free and paid storage space (GB) for GitHuub Packages. |
| `total_paid_gigabytes_bandwidth_used` | `integer` | Total paid storage space (GB) for GitHuub Packages. |
| `included_gigabytes_bandwidth` | `integer` | Free storage space (GB) for GitHub Packages. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_github_packages_billing_user` | `SELECT` | `username` |
