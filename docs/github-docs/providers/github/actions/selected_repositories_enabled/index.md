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
| `notifications_url` | `string` |  |
| `fork` | `boolean` |  |
| `downloads_url` | `string` |  |
| `has_downloads` | `boolean` | Whether downloads are enabled. |
| `languages_url` | `string` |  |
| `forks_count` | `integer` |  |
| `assignees_url` | `string` |  |
| `ssh_url` | `string` |  |
| `merges_url` | `string` |  |
| `private` | `boolean` | Whether the repository is private or public. |
| `permissions` | `object` |  |
| `hooks_url` | `string` |  |
| `allow_merge_commit` | `boolean` | Whether to allow merge commits for pull requests. |
| `stargazers_count` | `integer` |  |
| `commits_url` | `string` |  |
| `teams_url` | `string` |  |
| `keys_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `archive_url` | `string` |  |
| `pushed_at` | `string` |  |
| `full_name` | `string` |  |
| `updated_at` | `string` |  |
| `tags_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` | Whether to delete head branches when pull requests are merged |
| `comments_url` | `string` |  |
| `network_count` | `integer` |  |
| `allow_rebase_merge` | `boolean` | Whether to allow rebase merges for pull requests. |
| `template_repository` | `object` |  |
| `homepage` | `string` |  |
| `forks_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `statuses_url` | `string` |  |
| `disabled` | `boolean` | Returns whether or not this repository disabled. |
| `subscribers_url` | `string` |  |
| `blobs_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `open_issues` | `integer` |  |
| `node_id` | `string` |  |
| `subscription_url` | `string` |  |
| `visibility` | `string` | The repository visibility: public, private, or internal. |
| `created_at` | `string` |  |
| `license` | `object` | License Simple |
| `size` | `integer` |  |
| `svn_url` | `string` |  |
| `compare_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `stargazers_url` | `string` |  |
| `archived` | `boolean` | Whether the repository is archived. |
| `contributors_url` | `string` |  |
| `has_projects` | `boolean` | Whether projects are enabled. |
| `has_issues` | `boolean` | Whether issues are enabled. |
| `has_pages` | `boolean` |  |
| `url` | `string` |  |
| `git_tags_url` | `string` |  |
| `clone_url` | `string` |  |
| `mirror_url` | `string` |  |
| `master_branch` | `string` |  |
| `git_refs_url` | `string` |  |
| `allow_squash_merge` | `boolean` | Whether to allow squash merges for pull requests. |
| `deployments_url` | `string` |  |
| `releases_url` | `string` |  |
| `allow_forking` | `boolean` | Whether to allow forking this repo |
| `topics` | `array` |  |
| `is_template` | `boolean` | Whether this repository acts as a template that can be used to generate new repositories. |
| `watchers` | `integer` |  |
| `starred_at` | `string` |  |
| `issue_comment_url` | `string` |  |
| `forks` | `integer` |  |
| `allow_auto_merge` | `boolean` | Whether to allow Auto-merge to be used on pull requests. |
| `pulls_url` | `string` |  |
| `labels_url` | `string` |  |
| `git_url` | `string` |  |
| `contents_url` | `string` |  |
| `has_wiki` | `boolean` | Whether the wiki is enabled. |
| `owner` | `object` | Simple User |
| `default_branch` | `string` | The default branch of the repository. |
| `temp_clone_token` | `string` |  |
| `html_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `events_url` | `string` |  |
| `milestones_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `branches_url` | `string` |  |
| `language` | `string` |  |
| `organization` | `object` | Simple User |
| `trees_url` | `string` |  |
| `issues_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_selected_repositories_enabled_github_actions_organization` | `SELECT` | `org` | Lists the selected repositories that are enabled for GitHub Actions in an organization. To use this endpoint, the organization permission policy for `enabled_repositories` must be configured to `selected`. For more information, see "[Set GitHub Actions permissions for an organization](#set-github-actions-permissions-for-an-organization)."<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `administration` organization permission to use this API. |
| `disable_selected_repository_github_actions_organization` | `EXEC` | `org, repository_id` | Removes a repository from the list of selected repositories that are enabled for GitHub Actions in an organization. To use this endpoint, the organization permission policy for `enabled_repositories` must be configured to `selected`. For more information, see "[Set GitHub Actions permissions for an organization](#set-github-actions-permissions-for-an-organization)."<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `administration` organization permission to use this API. |
| `enable_selected_repository_github_actions_organization` | `EXEC` | `org, repository_id` | Adds a repository to the list of selected repositories that are enabled for GitHub Actions in an organization. To use this endpoint, the organization permission policy for `enabled_repositories` must be must be configured to `selected`. For more information, see "[Set GitHub Actions permissions for an organization](#set-github-actions-permissions-for-an-organization)."<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `administration` organization permission to use this API. |
| `set_selected_repositories_enabled_github_actions_organization` | `EXEC` | `org, data__selected_repository_ids` | Replaces the list of selected repositories that are enabled for GitHub Actions in an organization. To use this endpoint, the organization permission policy for `enabled_repositories` must be configured to `selected`. For more information, see "[Set GitHub Actions permissions for an organization](#set-github-actions-permissions-for-an-organization)."<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `administration` organization permission to use this API. |
