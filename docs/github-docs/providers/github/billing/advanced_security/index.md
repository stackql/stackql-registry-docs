---
title: advanced_security
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - github
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>advanced_security</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.billing.advanced_security</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `repositories` | `array` |
| `total_advanced_security_committers` | `integer` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_github_advanced_security_billing_ghe` | `SELECT` | `enterprise` | Gets the GitHub Advanced Security active committers for an enterprise per repository.<br />Each distinct user login across all repositories is counted as a single Advanced Security seat, so the total_advanced_security_committers is not the sum of active_users for each repository. |
| `get_github_advanced_security_billing_org` | `SELECT` | `org` | Gets the GitHub Advanced Security active committers for an organization per repository.<br />Each distinct user login across all repositories is counted as a single Advanced Security seat, so the total_advanced_security_committers is not the sum of advanced_security_committers for each repository.<br />If this organization defers to an enterprise for billing, the total_advanced_security_committers returned from the organization API may include some users that are in more than one organization, so they will only consume a single Advanced Security seat at the enterprise level. |
