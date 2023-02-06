---
title: selected_repositories_enabled
hide_title: false
hide_table_of_contents: false
keywords:
  - selected_repositories_enabled
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
<tr><td><b>Name</b></td><td><code>selected_repositories_enabled</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.actions.selected_repositories_enabled</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | Unique identifier of the repository |
| `name` | `string` | The name of the repository. |
| `description` | `string` |  |
| `merges_url` | `string` |  |
| `archive_url` | `string` |  |
| `is_template` | `boolean` | Whether this repository acts as a template that can be used to generate new repositories. |
| `contents_url` | `string` |  |
| `allow_auto_merge` | `boolean` | Whether to allow Auto-merge to be used on pull requests. |
| `permissions` | `object` |  |
| `has_projects` | `boolean` | Whether projects are enabled. |
| `license` | `object` | License Simple |
| `subscription_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `issues_url` | `string` |  |
| `labels_url` | `string` |  |
| `full_name` | `string` |  |
| `has_pages` | `boolean` |  |
| `git_url` | `string` |  |
| `has_downloads` | `boolean` | Whether downloads are enabled. |
| `events_url` | `string` |  |
| `size` | `integer` |  |
| `releases_url` | `string` |  |
| `created_at` | `string` |  |
| `stargazers_count` | `integer` |  |
| `topics` | `array` |  |
| `mirror_url` | `string` |  |
| `html_url` | `string` |  |
| `allow_forking` | `boolean` | Whether to allow forking this repo |
| `node_id` | `string` |  |
| `allow_squash_merge` | `boolean` | Whether to allow squash merges for pull requests. |
| `temp_clone_token` | `string` |  |
| `has_wiki` | `boolean` | Whether the wiki is enabled. |
| `fork` | `boolean` |  |
| `issue_events_url` | `string` |  |
| `deployments_url` | `string` |  |
| `visibility` | `string` | The repository visibility: public, private, or internal. |
| `forks_count` | `integer` |  |
| `branches_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `template_repository` | `object` |  |
| `updated_at` | `string` |  |
| `watchers` | `integer` |  |
| `blobs_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `contributors_url` | `string` |  |
| `forks_url` | `string` |  |
| `master_branch` | `string` |  |
| `open_issues` | `integer` |  |
| `owner` | `object` | Simple User |
| `subscribers_count` | `integer` |  |
| `teams_url` | `string` |  |
| `language` | `string` |  |
| `statuses_url` | `string` |  |
| `allow_rebase_merge` | `boolean` | Whether to allow rebase merges for pull requests. |
| `svn_url` | `string` |  |
| `url` | `string` |  |
| `has_issues` | `boolean` | Whether issues are enabled. |
| `hooks_url` | `string` |  |
| `allow_merge_commit` | `boolean` | Whether to allow merge commits for pull requests. |
| `assignees_url` | `string` |  |
| `starred_at` | `string` |  |
| `forks` | `integer` |  |
| `open_issues_count` | `integer` |  |
| `ssh_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `trees_url` | `string` |  |
| `tags_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `archived` | `boolean` | Whether the repository is archived. |
| `keys_url` | `string` |  |
| `comments_url` | `string` |  |
| `compare_url` | `string` |  |
| `pulls_url` | `string` |  |
| `pushed_at` | `string` |  |
| `private` | `boolean` | Whether the repository is private or public. |
| `disabled` | `boolean` | Returns whether or not this repository disabled. |
| `network_count` | `integer` |  |
| `delete_branch_on_merge` | `boolean` | Whether to delete head branches when pull requests are merged |
| `collaborators_url` | `string` |  |
| `clone_url` | `string` |  |
| `homepage` | `string` |  |
| `downloads_url` | `string` |  |
| `organization` | `object` | Simple User |
| `commits_url` | `string` |  |
| `notifications_url` | `string` |  |
| `languages_url` | `string` |  |
| `default_branch` | `string` | The default branch of the repository. |
| `milestones_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_selected_repositories_enabled_github_actions_organization` | `SELECT` | `org` | Lists the selected repositories that are enabled for GitHub Actions in an organization. To use this endpoint, the organization permission policy for `enabled_repositories` must be configured to `selected`. For more information, see "[Set GitHub Actions permissions for an organization](#set-github-actions-permissions-for-an-organization)."<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `administration` organization permission to use this API. |
| `disable_selected_repository_github_actions_organization` | `EXEC` | `org, repository_id` | Removes a repository from the list of selected repositories that are enabled for GitHub Actions in an organization. To use this endpoint, the organization permission policy for `enabled_repositories` must be configured to `selected`. For more information, see "[Set GitHub Actions permissions for an organization](#set-github-actions-permissions-for-an-organization)."<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `administration` organization permission to use this API. |
| `enable_selected_repository_github_actions_organization` | `EXEC` | `org, repository_id` | Adds a repository to the list of selected repositories that are enabled for GitHub Actions in an organization. To use this endpoint, the organization permission policy for `enabled_repositories` must be must be configured to `selected`. For more information, see "[Set GitHub Actions permissions for an organization](#set-github-actions-permissions-for-an-organization)."<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `administration` organization permission to use this API. |
| `set_selected_repositories_enabled_github_actions_organization` | `EXEC` | `org, data__selected_repository_ids` | Replaces the list of selected repositories that are enabled for GitHub Actions in an organization. To use this endpoint, the organization permission policy for `enabled_repositories` must be configured to `selected`. For more information, see "[Set GitHub Actions permissions for an organization](#set-github-actions-permissions-for-an-organization)."<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `administration` organization permission to use this API. |
