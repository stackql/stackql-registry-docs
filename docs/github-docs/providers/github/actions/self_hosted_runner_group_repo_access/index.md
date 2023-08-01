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
| `created_at` | `string` |  |
| `has_downloads` | `boolean` |  |
| `events_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `assignees_url` | `string` |  |
| `owner` | `object` | Simple User |
| `language` | `string` |  |
| `stargazers_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `issues_url` | `string` |  |
| `size` | `integer` |  |
| `allow_forking` | `boolean` |  |
| `merges_url` | `string` |  |
| `blobs_url` | `string` |  |
| `archive_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `full_name` | `string` |  |
| `fork` | `boolean` |  |
| `forks` | `integer` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `archived` | `boolean` |  |
| `url` | `string` |  |
| `commits_url` | `string` |  |
| `node_id` | `string` |  |
| `watchers_count` | `integer` |  |
| `private` | `boolean` |  |
| `has_wiki` | `boolean` |  |
| `issue_events_url` | `string` |  |
| `downloads_url` | `string` |  |
| `html_url` | `string` |  |
| `tags_url` | `string` |  |
| `svn_url` | `string` |  |
| `keys_url` | `string` |  |
| `milestones_url` | `string` |  |
| `ssh_url` | `string` |  |
| `languages_url` | `string` |  |
| `statuses_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `hooks_url` | `string` |  |
| `homepage` | `string` |  |
| `visibility` | `string` |  |
| `template_repository` | `object` | A git repository |
| `permissions` | `object` |  |
| `notifications_url` | `string` |  |
| `forks_url` | `string` |  |
| `trees_url` | `string` |  |
| `role_name` | `string` |  |
| `forks_count` | `integer` |  |
| `clone_url` | `string` |  |
| `contributors_url` | `string` |  |
| `network_count` | `integer` |  |
| `git_url` | `string` |  |
| `releases_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `git_tags_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `deployments_url` | `string` |  |
| `pulls_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `default_branch` | `string` |  |
| `subscription_url` | `string` |  |
| `watchers` | `integer` |  |
| `has_issues` | `boolean` |  |
| `license` | `object` |  |
| `branches_url` | `string` |  |
| `teams_url` | `string` |  |
| `updated_at` | `string` |  |
| `labels_url` | `string` |  |
| `compare_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `mirror_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `comments_url` | `string` |  |
| `is_template` | `boolean` |  |
| `topics` | `array` |  |
| `disabled` | `boolean` |  |
| `issue_comment_url` | `string` |  |
| `contents_url` | `string` |  |
| `open_issues` | `integer` |  |
| `pushed_at` | `string` |  |
| `collaborators_url` | `string` |  |
| `stargazers_count` | `integer` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_repo_access_to_self_hosted_runner_group_in_org` | `SELECT` | `org, runner_group_id` | The self-hosted runner groups REST API is available with GitHub Enterprise Cloud and GitHub Enterprise Server. For more information, see "[GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)."<br /><br />Lists the repositories with access to a self-hosted runner group configured in an organization.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
| `add_repo_access_to_self_hosted_runner_group_in_org` | `EXEC` | `org, repository_id, runner_group_id` | The self-hosted runner groups REST API is available with GitHub Enterprise Cloud. For more information, see "[GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)."<br /><br /><br />Adds a repository to the list of selected repositories that can access a self-hosted runner group. The runner group must have `visibility` set to `selected`. For more information, see "[Create a self-hosted runner group for an organization](#create-a-self-hosted-runner-group-for-an-organization)."<br /><br />You must authenticate using an access token with the `admin:org`<br />scope to use this endpoint. |
| `remove_repo_access_to_self_hosted_runner_group_in_org` | `EXEC` | `org, repository_id, runner_group_id` | The self-hosted runner groups REST API is available with GitHub Enterprise Cloud. For more information, see "[GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)."<br /><br /><br />Removes a repository from the list of selected repositories that can access a self-hosted runner group. The runner group must have `visibility` set to `selected`. For more information, see "[Create a self-hosted runner group for an organization](#create-a-self-hosted-runner-group-for-an-organization)."<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
| `set_repo_access_to_self_hosted_runner_group_in_org` | `EXEC` | `org, runner_group_id, data__selected_repository_ids` | The self-hosted runner groups REST API is available with GitHub Enterprise Cloud. For more information, see "[GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)."<br /><br />Replaces the list of repositories that have access to a self-hosted runner group configured in an organization.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
