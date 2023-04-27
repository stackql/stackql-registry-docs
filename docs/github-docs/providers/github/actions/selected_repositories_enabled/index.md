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
| `permissions` | `object` |  |
| `forks` | `integer` |  |
| `allow_forking` | `boolean` | Whether to allow forking this repo |
| `updated_at` | `string` |  |
| `owner` | `object` | Simple User |
| `allow_rebase_merge` | `boolean` | Whether to allow rebase merges for pull requests. |
| `forks_count` | `integer` |  |
| `is_template` | `boolean` | Whether this repository acts as a template that can be used to generate new repositories. |
| `contents_url` | `string` |  |
| `private` | `boolean` | Whether the repository is private or public. |
| `has_pages` | `boolean` |  |
| `has_projects` | `boolean` | Whether projects are enabled. |
| `git_refs_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `git_url` | `string` |  |
| `mirror_url` | `string` |  |
| `has_wiki` | `boolean` | Whether the wiki is enabled. |
| `merges_url` | `string` |  |
| `events_url` | `string` |  |
| `archive_url` | `string` |  |
| `allow_merge_commit` | `boolean` | Whether to allow merge commits for pull requests. |
| `languages_url` | `string` |  |
| `blobs_url` | `string` |  |
| `organization` | `object` | Simple User |
| `topics` | `array` |  |
| `allow_auto_merge` | `boolean` | Whether to allow Auto-merge to be used on pull requests. |
| `has_issues` | `boolean` | Whether issues are enabled. |
| `clone_url` | `string` |  |
| `deployments_url` | `string` |  |
| `statuses_url` | `string` |  |
| `master_branch` | `string` |  |
| `issue_events_url` | `string` |  |
| `watchers` | `integer` |  |
| `collaborators_url` | `string` |  |
| `visibility` | `string` | The repository visibility: public, private, or internal. |
| `subscription_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `full_name` | `string` |  |
| `template_repository` | `object` |  |
| `disabled` | `boolean` | Returns whether or not this repository disabled. |
| `git_tags_url` | `string` |  |
| `milestones_url` | `string` |  |
| `has_downloads` | `boolean` | Whether downloads are enabled. |
| `html_url` | `string` |  |
| `archived` | `boolean` | Whether the repository is archived. |
| `created_at` | `string` |  |
| `comments_url` | `string` |  |
| `teams_url` | `string` |  |
| `ssh_url` | `string` |  |
| `issues_url` | `string` |  |
| `url` | `string` |  |
| `contributors_url` | `string` |  |
| `releases_url` | `string` |  |
| `license` | `object` | License Simple |
| `labels_url` | `string` |  |
| `svn_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `pushed_at` | `string` |  |
| `assignees_url` | `string` |  |
| `starred_at` | `string` |  |
| `notifications_url` | `string` |  |
| `default_branch` | `string` | The default branch of the repository. |
| `pulls_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `size` | `integer` |  |
| `hooks_url` | `string` |  |
| `tags_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `network_count` | `integer` |  |
| `language` | `string` |  |
| `node_id` | `string` |  |
| `homepage` | `string` |  |
| `stargazers_count` | `integer` |  |
| `git_commits_url` | `string` |  |
| `compare_url` | `string` |  |
| `forks_url` | `string` |  |
| `keys_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `commits_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `fork` | `boolean` |  |
| `allow_squash_merge` | `boolean` | Whether to allow squash merges for pull requests. |
| `trees_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` | Whether to delete head branches when pull requests are merged |
| `downloads_url` | `string` |  |
| `branches_url` | `string` |  |
| `open_issues` | `integer` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_selected_repositories_enabled_github_actions_organization` | `SELECT` | `org` | Lists the selected repositories that are enabled for GitHub Actions in an organization. To use this endpoint, the organization permission policy for `enabled_repositories` must be configured to `selected`. For more information, see "[Set GitHub Actions permissions for an organization](#set-github-actions-permissions-for-an-organization)."<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `administration` organization permission to use this API. |
| `disable_selected_repository_github_actions_organization` | `EXEC` | `org, repository_id` | Removes a repository from the list of selected repositories that are enabled for GitHub Actions in an organization. To use this endpoint, the organization permission policy for `enabled_repositories` must be configured to `selected`. For more information, see "[Set GitHub Actions permissions for an organization](#set-github-actions-permissions-for-an-organization)."<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `administration` organization permission to use this API. |
| `enable_selected_repository_github_actions_organization` | `EXEC` | `org, repository_id` | Adds a repository to the list of selected repositories that are enabled for GitHub Actions in an organization. To use this endpoint, the organization permission policy for `enabled_repositories` must be must be configured to `selected`. For more information, see "[Set GitHub Actions permissions for an organization](#set-github-actions-permissions-for-an-organization)."<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `administration` organization permission to use this API. |
| `set_selected_repositories_enabled_github_actions_organization` | `EXEC` | `org, data__selected_repository_ids` | Replaces the list of selected repositories that are enabled for GitHub Actions in an organization. To use this endpoint, the organization permission policy for `enabled_repositories` must be configured to `selected`. For more information, see "[Set GitHub Actions permissions for an organization](#set-github-actions-permissions-for-an-organization)."<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `administration` organization permission to use this API. |
