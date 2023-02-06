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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>branch_protection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.branch_protection</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` |  |
| `allow_force_pushes` | `object` |  |
| `restrictions` | `object` | Branch Restriction Policy |
| `required_conversation_resolution` | `object` |  |
| `required_linear_history` | `object` |  |
| `url` | `string` |  |
| `required_status_checks` | `object` | Protected Branch Required Status Check |
| `protection_url` | `string` |  |
| `enabled` | `boolean` |  |
| `required_signatures` | `object` |  |
| `allow_deletions` | `object` |  |
| `required_pull_request_reviews` | `object` | Protected Branch Pull Request Review |
| `enforce_admins` | `object` | Protected Branch Admin Enforced |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_branch_protection` | `SELECT` | `branch, owner, repo` | Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation. |
| `delete_branch_protection` | `DELETE` | `branch, owner, repo` | Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation. |
| `update_branch_protection` | `EXEC` | `branch, owner, repo, data__enforce_admins, data__required_pull_request_reviews, data__required_status_checks, data__restrictions` | Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.<br /><br />Protecting a branch requires admin or owner permissions to the repository.<br /><br />**Note**: Passing new arrays of `users` and `teams` replaces their previous values.<br /><br />**Note**: The list of users, apps, and teams in total is limited to 100 items. |
