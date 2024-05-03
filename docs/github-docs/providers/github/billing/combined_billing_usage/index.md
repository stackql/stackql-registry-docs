---
title: combined_billing_usage
hide_title: false
hide_table_of_contents: false
keywords:
  - combined_billing_usage
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
<tr><td><b>Name</b></td><td><code>combined_billing_usage</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.billing.combined_billing_usage" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="days_left_in_billing_cycle" /> | `integer` | Numbers of days left in billing cycle. |
| <CopyableCode code="estimated_paid_storage_for_month" /> | `integer` | Estimated storage space (GB) used in billing cycle. |
| <CopyableCode code="estimated_storage_for_month" /> | `integer` | Estimated sum of free and paid storage space (GB) used in billing cycle. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_shared_storage_billing_org" /> | `SELECT` | <CopyableCode code="org" /> | Gets the estimated paid and estimated total storage used for GitHub Actions and GitHub Packages.<br /><br />Paid minutes only apply to packages stored for private repositories. For more information, see "[Managing billing for GitHub Packages](https://docs.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-packages)."<br /><br />Access tokens must have the `repo` or `admin:org` scope. |
| <CopyableCode code="get_shared_storage_billing_user" /> | `SELECT` | <CopyableCode code="username" /> | Gets the estimated paid and estimated total storage used for GitHub Actions and GitHub Packages.<br /><br />Paid minutes only apply to packages stored for private repositories. For more information, see "[Managing billing for GitHub Packages](https://docs.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-packages)."<br /><br />Access tokens must have the `user` scope. |
