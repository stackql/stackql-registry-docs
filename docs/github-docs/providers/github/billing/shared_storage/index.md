---
title: shared_storage
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
<tr><td><b>Name</b></td><td><code>shared_storage</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.billing.shared_storage</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `estimated_storage_for_month` | `integer` | Estimated sum of free and paid storage space (GB) used in billing cycle. |
| `days_left_in_billing_cycle` | `integer` | Numbers of days left in billing cycle. |
| `estimated_paid_storage_for_month` | `integer` | Estimated storage space (GB) used in billing cycle. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_shared_storage_billing_ghe` | `SELECT` | `enterprise` | Gets the estimated paid and estimated total storage used for GitHub Actions and GitHub Packages.<br /><br />Paid minutes only apply to packages stored for private repositories. For more information, see "[Managing billing for GitHub Packages](https://docs.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-packages)."<br /><br />The authenticated user must be an enterprise admin. |
| `get_shared_storage_billing_org` | `SELECT` | `org` | Gets the estimated paid and estimated total storage used for GitHub Actions and GitHub Packages.<br /><br />Paid minutes only apply to packages stored for private repositories. For more information, see "[Managing billing for GitHub Packages](https://docs.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-packages)."<br /><br />Access tokens must have the `repo` or `admin:org` scope. |
| `get_shared_storage_billing_user` | `SELECT` | `username` | Gets the estimated paid and estimated total storage used for GitHub Actions and GitHub Packages.<br /><br />Paid minutes only apply to packages stored for private repositories. For more information, see "[Managing billing for GitHub Packages](https://docs.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-packages)."<br /><br />Access tokens must have the `user` scope. |
