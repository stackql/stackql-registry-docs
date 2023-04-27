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
| `fork` | `boolean` |  |
| `milestones_url` | `string` |  |
| `license` | `object` |  |
| `node_id` | `string` |  |
| `events_url` | `string` |  |
| `forks` | `integer` |  |
| `topics` | `array` |  |
| `branches_url` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `visibility` | `string` |  |
| `private` | `boolean` |  |
| `commits_url` | `string` |  |
| `notifications_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `watchers_count` | `integer` |  |
| `pulls_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `url` | `string` |  |
| `role_name` | `string` |  |
| `trees_url` | `string` |  |
| `network_count` | `integer` |  |
| `size` | `integer` |  |
| `issues_url` | `string` |  |
| `blobs_url` | `string` |  |
| `owner` | `object` | Simple User |
| `comments_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `clone_url` | `string` |  |
| `template_repository` | `object` | A git repository |
| `pushed_at` | `string` |  |
| `hooks_url` | `string` |  |
| `downloads_url` | `string` |  |
| `archive_url` | `string` |  |
| `watchers` | `integer` |  |
| `updated_at` | `string` |  |
| `issue_comment_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `default_branch` | `string` |  |
| `forks_url` | `string` |  |
| `statuses_url` | `string` |  |
| `svn_url` | `string` |  |
| `language` | `string` |  |
| `tags_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `homepage` | `string` |  |
| `open_issues` | `integer` |  |
| `collaborators_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `contents_url` | `string` |  |
| `teams_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `git_commits_url` | `string` |  |
| `releases_url` | `string` |  |
| `forks_count` | `integer` |  |
| `subscription_url` | `string` |  |
| `disabled` | `boolean` |  |
| `has_pages` | `boolean` |  |
| `has_downloads` | `boolean` |  |
| `deployments_url` | `string` |  |
| `assignees_url` | `string` |  |
| `full_name` | `string` |  |
| `archived` | `boolean` |  |
| `git_tags_url` | `string` |  |
| `git_url` | `string` |  |
| `keys_url` | `string` |  |
| `created_at` | `string` |  |
| `is_template` | `boolean` |  |
| `has_projects` | `boolean` |  |
| `ssh_url` | `string` |  |
| `merges_url` | `string` |  |
| `languages_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `html_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `permissions` | `object` |  |
| `stargazers_url` | `string` |  |
| `mirror_url` | `string` |  |
| `contributors_url` | `string` |  |
| `labels_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `compare_url` | `string` |  |
| `issue_events_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_repo_access_to_self_hosted_runner_group_in_org` | `SELECT` | `org, runner_group_id` | The self-hosted runner groups REST API is available with GitHub Enterprise Cloud and GitHub Enterprise Server. For more information, see "[GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)."<br /><br />Lists the repositories with access to a self-hosted runner group configured in an organization.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
| `add_repo_access_to_self_hosted_runner_group_in_org` | `EXEC` | `org, repository_id, runner_group_id` | The self-hosted runner groups REST API is available with GitHub Enterprise Cloud. For more information, see "[GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)."<br /><br /><br />Adds a repository to the list of selected repositories that can access a self-hosted runner group. The runner group must have `visibility` set to `selected`. For more information, see "[Create a self-hosted runner group for an organization](#create-a-self-hosted-runner-group-for-an-organization)."<br /><br />You must authenticate using an access token with the `admin:org`<br />scope to use this endpoint. |
| `remove_repo_access_to_self_hosted_runner_group_in_org` | `EXEC` | `org, repository_id, runner_group_id` | The self-hosted runner groups REST API is available with GitHub Enterprise Cloud. For more information, see "[GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)."<br /><br /><br />Removes a repository from the list of selected repositories that can access a self-hosted runner group. The runner group must have `visibility` set to `selected`. For more information, see "[Create a self-hosted runner group for an organization](#create-a-self-hosted-runner-group-for-an-organization)."<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
| `set_repo_access_to_self_hosted_runner_group_in_org` | `EXEC` | `org, runner_group_id, data__selected_repository_ids` | The self-hosted runner groups REST API is available with GitHub Enterprise Cloud. For more information, see "[GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)."<br /><br />Replaces the list of repositories that have access to a self-hosted runner group configured in an organization.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
