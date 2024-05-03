---
title: packages_billing_usage
hide_title: false
hide_table_of_contents: false
keywords:
  - packages_billing_usage
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>packages_billing_usage</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.billing.packages_billing_usage" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="included_gigabytes_bandwidth" /> | `integer` | Free storage space (GB) for GitHub Packages. |
| <CopyableCode code="total_gigabytes_bandwidth_used" /> | `integer` | Sum of the free and paid storage space (GB) for GitHuub Packages. |
| <CopyableCode code="total_paid_gigabytes_bandwidth_used" /> | `integer` | Total paid storage space (GB) for GitHuub Packages. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_github_packages_billing_org" /> | `SELECT` | <CopyableCode code="org" /> | Gets the free and paid storage used for GitHub Packages in gigabytes.<br /><br />Paid minutes only apply to packages stored for private repositories. For more information, see "[Managing billing for GitHub Packages](https://docs.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-packages)."<br /><br />Access tokens must have the `repo` or `admin:org` scope. |
| <CopyableCode code="get_github_packages_billing_user" /> | `SELECT` | <CopyableCode code="username" /> | Gets the free and paid storage used for GitHub Packages in gigabytes.<br /><br />Paid minutes only apply to packages stored for private repositories. For more information, see "[Managing billing for GitHub Packages](https://docs.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-packages)."<br /><br />Access tokens must have the `user` scope. |
