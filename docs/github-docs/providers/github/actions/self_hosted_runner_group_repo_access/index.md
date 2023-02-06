---
title: self_hosted_runner_group_repo_access
hide_title: false
hide_table_of_contents: false
keywords:
  - self_hosted_runner_group_repo_access
  - actions
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
<tr><td><b>Name</b></td><td><code>self_hosted_runner_group_repo_access</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.actions.self_hosted_runner_group_repo_access</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `commits_url` | `string` |  |
| `permissions` | `object` |  |
| `forks_count` | `integer` |  |
| `git_commits_url` | `string` |  |
| `blobs_url` | `string` |  |
| `assignees_url` | `string` |  |
| `template_repository` | `object` | A git repository |
| `html_url` | `string` |  |
| `notifications_url` | `string` |  |
| `open_issues` | `integer` |  |
| `clone_url` | `string` |  |
| `archived` | `boolean` |  |
| `owner` | `object` | Simple User |
| `contents_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `subscription_url` | `string` |  |
| `license` | `object` |  |
| `topics` | `array` |  |
| `svn_url` | `string` |  |
| `forks_url` | `string` |  |
| `homepage` | `string` |  |
| `git_refs_url` | `string` |  |
| `labels_url` | `string` |  |
| `contributors_url` | `string` |  |
| `visibility` | `string` |  |
| `collaborators_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `forks` | `integer` |  |
| `issue_events_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `open_issues_count` | `integer` |  |
| `watchers` | `integer` |  |
| `stargazers_url` | `string` |  |
| `language` | `string` |  |
| `trees_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `network_count` | `integer` |  |
| `size` | `integer` |  |
| `milestones_url` | `string` |  |
| `keys_url` | `string` |  |
| `url` | `string` |  |
| `hooks_url` | `string` |  |
| `created_at` | `string` |  |
| `deployments_url` | `string` |  |
| `mirror_url` | `string` |  |
| `events_url` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `is_template` | `boolean` |  |
| `has_downloads` | `boolean` |  |
| `merges_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `disabled` | `boolean` |  |
| `watchers_count` | `integer` |  |
| `compare_url` | `string` |  |
| `tags_url` | `string` |  |
| `issues_url` | `string` |  |
| `node_id` | `string` |  |
| `temp_clone_token` | `string` |  |
| `git_tags_url` | `string` |  |
| `private` | `boolean` |  |
| `downloads_url` | `string` |  |
| `ssh_url` | `string` |  |
| `pushed_at` | `string` |  |
| `releases_url` | `string` |  |
| `role_name` | `string` |  |
| `subscribers_count` | `integer` |  |
| `updated_at` | `string` |  |
| `git_url` | `string` |  |
| `branches_url` | `string` |  |
| `pulls_url` | `string` |  |
| `teams_url` | `string` |  |
| `fork` | `boolean` |  |
| `statuses_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `archive_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `languages_url` | `string` |  |
| `comments_url` | `string` |  |
| `full_name` | `string` |  |
| `default_branch` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_repo_access_to_self_hosted_runner_group_in_org` | `SELECT` | `org, runner_group_id` | The self-hosted runner groups REST API is available with GitHub Enterprise Cloud and GitHub Enterprise Server. For more information, see "[GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)."<br /><br />Lists the repositories with access to a self-hosted runner group configured in an organization.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
| `add_repo_access_to_self_hosted_runner_group_in_org` | `EXEC` | `org, repository_id, runner_group_id` | The self-hosted runner groups REST API is available with GitHub Enterprise Cloud. For more information, see "[GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)."<br /><br /><br />Adds a repository to the list of selected repositories that can access a self-hosted runner group. The runner group must have `visibility` set to `selected`. For more information, see "[Create a self-hosted runner group for an organization](#create-a-self-hosted-runner-group-for-an-organization)."<br /><br />You must authenticate using an access token with the `admin:org`<br />scope to use this endpoint. |
| `remove_repo_access_to_self_hosted_runner_group_in_org` | `EXEC` | `org, repository_id, runner_group_id` | The self-hosted runner groups REST API is available with GitHub Enterprise Cloud. For more information, see "[GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)."<br /><br /><br />Removes a repository from the list of selected repositories that can access a self-hosted runner group. The runner group must have `visibility` set to `selected`. For more information, see "[Create a self-hosted runner group for an organization](#create-a-self-hosted-runner-group-for-an-organization)."<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
| `set_repo_access_to_self_hosted_runner_group_in_org` | `EXEC` | `org, runner_group_id, data__selected_repository_ids` | The self-hosted runner groups REST API is available with GitHub Enterprise Cloud. For more information, see "[GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)."<br /><br />Replaces the list of repositories that have access to a self-hosted runner group configured in an organization.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
