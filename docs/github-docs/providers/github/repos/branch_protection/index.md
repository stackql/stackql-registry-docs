---
title: branch_protection
hide_title: false
hide_table_of_contents: false
keywords:
  - branch_protection
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
<tr><td><b>Name</b></td><td><code>branch_protection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.repos.branch_protection" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` |  |
| <CopyableCode code="allow_deletions" /> | `object` |  |
| <CopyableCode code="allow_force_pushes" /> | `object` |  |
| <CopyableCode code="allow_fork_syncing" /> | `object` | Whether users can pull changes from upstream when the branch is locked. Set to `true` to allow fork syncing. Set to `false` to prevent fork syncing. |
| <CopyableCode code="block_creations" /> | `object` |  |
| <CopyableCode code="enabled" /> | `boolean` |  |
| <CopyableCode code="enforce_admins" /> | `object` | Protected Branch Admin Enforced |
| <CopyableCode code="lock_branch" /> | `object` | Whether to set the branch as read-only. If this is true, users will not be able to push to the branch. |
| <CopyableCode code="protection_url" /> | `string` |  |
| <CopyableCode code="required_conversation_resolution" /> | `object` |  |
| <CopyableCode code="required_linear_history" /> | `object` |  |
| <CopyableCode code="required_pull_request_reviews" /> | `object` | Protected Branch Pull Request Review |
| <CopyableCode code="required_signatures" /> | `object` |  |
| <CopyableCode code="required_status_checks" /> | `object` | Protected Branch Required Status Check |
| <CopyableCode code="restrictions" /> | `object` | Branch Restriction Policy |
| <CopyableCode code="url" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_branch_protection" /> | `SELECT` | <CopyableCode code="branch, owner, repo" /> | Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation. |
| <CopyableCode code="delete_branch_protection" /> | `DELETE` | <CopyableCode code="branch, owner, repo" /> | Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation. |
| <CopyableCode code="update_branch_protection" /> | `EXEC` | <CopyableCode code="branch, owner, repo, data__enforce_admins, data__required_pull_request_reviews, data__required_status_checks, data__restrictions" /> | Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.<br /><br />Protecting a branch requires admin or owner permissions to the repository.<br /><br />**Note**: Passing new arrays of `users` and `teams` replaces their previous values.<br /><br />**Note**: The list of users, apps, and teams in total is limited to 100 items. |
