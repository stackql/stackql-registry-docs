---
title: selected_repos_for_org_secret
hide_title: false
hide_table_of_contents: false
keywords:
  - selected_repos_for_org_secret
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
<tr><td><b>Name</b></td><td><code>selected_repos_for_org_secret</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.actions.selected_repos_for_org_secret</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `trees_url` | `string` |  |
| `fork` | `boolean` |  |
| `temp_clone_token` | `string` |  |
| `collaborators_url` | `string` |  |
| `updated_at` | `string` |  |
| `created_at` | `string` |  |
| `branches_url` | `string` |  |
| `owner` | `object` | Simple User |
| `topics` | `array` |  |
| `compare_url` | `string` |  |
| `pulls_url` | `string` |  |
| `svn_url` | `string` |  |
| `releases_url` | `string` |  |
| `downloads_url` | `string` |  |
| `forks_count` | `integer` |  |
| `open_issues` | `integer` |  |
| `archive_url` | `string` |  |
| `language` | `string` |  |
| `allow_forking` | `boolean` |  |
| `teams_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `role_name` | `string` |  |
| `assignees_url` | `string` |  |
| `merges_url` | `string` |  |
| `visibility` | `string` |  |
| `git_url` | `string` |  |
| `notifications_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `issues_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `has_issues` | `boolean` |  |
| `permissions` | `object` |  |
| `keys_url` | `string` |  |
| `html_url` | `string` |  |
| `statuses_url` | `string` |  |
| `watchers` | `integer` |  |
| `has_wiki` | `boolean` |  |
| `commits_url` | `string` |  |
| `forks_url` | `string` |  |
| `archived` | `boolean` |  |
| `clone_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `full_name` | `string` |  |
| `comments_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `private` | `boolean` |  |
| `url` | `string` |  |
| `tags_url` | `string` |  |
| `node_id` | `string` |  |
| `network_count` | `integer` |  |
| `mirror_url` | `string` |  |
| `default_branch` | `string` |  |
| `events_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `subscribers_url` | `string` |  |
| `hooks_url` | `string` |  |
| `subscription_url` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `has_pages` | `boolean` |  |
| `is_template` | `boolean` |  |
| `stargazers_count` | `integer` |  |
| `contributors_url` | `string` |  |
| `pushed_at` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `forks` | `integer` |  |
| `disabled` | `boolean` |  |
| `labels_url` | `string` |  |
| `license` | `object` |  |
| `homepage` | `string` |  |
| `template_repository` | `object` | A git repository |
| `languages_url` | `string` |  |
| `blobs_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `deployments_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `contents_url` | `string` |  |
| `size` | `integer` |  |
| `watchers_count` | `integer` |  |
| `milestones_url` | `string` |  |
| `ssh_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_selected_repos_for_org_secret` | `SELECT` | `org, secret_name` | Lists all repositories that have been selected when the `visibility` for repository access to a secret is set to `selected`. You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `secrets` organization permission to use this endpoint. |
| `add_selected_repo_to_org_secret` | `INSERT` | `org, repository_id, secret_name` | Adds a repository to an organization secret when the `visibility` for repository access is set to `selected`. The visibility is set when you [Create or update an organization secret](https://docs.github.com/rest/reference/actions#create-or-update-an-organization-secret). You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `secrets` organization permission to use this endpoint. |
| `remove_selected_repo_from_org_secret` | `DELETE` | `org, repository_id, secret_name` | Removes a repository from an organization secret when the `visibility` for repository access is set to `selected`. The visibility is set when you [Create or update an organization secret](https://docs.github.com/rest/reference/actions#create-or-update-an-organization-secret). You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `secrets` organization permission to use this endpoint. |
| `set_selected_repos_for_org_secret` | `EXEC` | `org, secret_name, data__selected_repository_ids` | Replaces all repositories for an organization secret when the `visibility` for repository access is set to `selected`. The visibility is set when you [Create or update an organization secret](https://docs.github.com/rest/reference/actions#create-or-update-an-organization-secret). You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `secrets` organization permission to use this endpoint. |
