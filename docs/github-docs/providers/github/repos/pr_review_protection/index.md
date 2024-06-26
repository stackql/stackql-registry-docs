---
title: pr_review_protection
hide_title: false
hide_table_of_contents: false
keywords:
  - pr_review_protection
  - repos
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
<tr><td><b>Name</b></td><td><code>pr_review_protection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.repos.pr_review_protection" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="bypass_pull_request_allowances" /> | `object` | Allow specific users, teams, or apps to bypass pull request requirements. |
| <CopyableCode code="dismiss_stale_reviews" /> | `boolean` |  |
| <CopyableCode code="dismissal_restrictions" /> | `object` |  |
| <CopyableCode code="require_code_owner_reviews" /> | `boolean` |  |
| <CopyableCode code="require_last_push_approval" /> | `boolean` | Whether the most recent push must be approved by someone other than the person who pushed it. |
| <CopyableCode code="required_approving_review_count" /> | `integer` |  |
| <CopyableCode code="url" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_pull_request_review_protection" /> | `SELECT` | <CopyableCode code="branch, owner, repo" /> | Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation. |
| <CopyableCode code="delete_pull_request_review_protection" /> | `DELETE` | <CopyableCode code="branch, owner, repo" /> | Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation. |
| <CopyableCode code="update_pull_request_review_protection" /> | `EXEC` | <CopyableCode code="branch, owner, repo" /> | Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.<br /><br />Updating pull request review enforcement requires admin or owner permissions to the repository and branch protection to be enabled.<br /><br />**Note**: Passing new arrays of `users` and `teams` replaces their previous values. |
