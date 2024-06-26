---
title: actions_billing_usage
hide_title: false
hide_table_of_contents: false
keywords:
  - actions_billing_usage
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
<tr><td><b>Name</b></td><td><code>actions_billing_usage</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.billing.actions_billing_usage" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="included_minutes" /> | `integer` | The amount of free GitHub Actions minutes available. |
| <CopyableCode code="minutes_used_breakdown" /> | `object` |  |
| <CopyableCode code="total_minutes_used" /> | `integer` | The sum of the free and paid GitHub Actions minutes used. |
| <CopyableCode code="total_paid_minutes_used" /> | `integer` | The total paid GitHub Actions minutes used. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_github_actions_billing_org" /> | `SELECT` | <CopyableCode code="org" /> | Gets the summary of the free and paid GitHub Actions minutes used.<br /><br />Paid minutes only apply to workflows in private repositories that use GitHub-hosted runners. Minutes used is listed for each GitHub-hosted runner operating system. Any job re-runs are also included in the usage. The usage returned includes any minute multipliers for macOS and Windows runners, and is rounded up to the nearest whole minute. For more information, see "[Managing billing for GitHub Actions](https://docs.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-actions)".<br /><br />Access tokens must have the `repo` or `admin:org` scope. |
| <CopyableCode code="get_github_actions_billing_user" /> | `SELECT` | <CopyableCode code="username" /> | Gets the summary of the free and paid GitHub Actions minutes used.<br /><br />Paid minutes only apply to workflows in private repositories that use GitHub-hosted runners. Minutes used is listed for each GitHub-hosted runner operating system. Any job re-runs are also included in the usage. The usage returned includes any minute multipliers for macOS and Windows runners, and is rounded up to the nearest whole minute. For more information, see "[Managing billing for GitHub Actions](https://docs.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-actions)".<br /><br />Access tokens must have the `user` scope. |
