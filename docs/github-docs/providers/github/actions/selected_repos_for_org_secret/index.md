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
| `blobs_url` | `string` |  |
| `role_name` | `string` |  |
| `network_count` | `integer` |  |
| `visibility` | `string` |  |
| `issues_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `forks` | `integer` |  |
| `node_id` | `string` |  |
| `merges_url` | `string` |  |
| `archive_url` | `string` |  |
| `html_url` | `string` |  |
| `owner` | `object` | Simple User |
| `git_refs_url` | `string` |  |
| `downloads_url` | `string` |  |
| `disabled` | `boolean` |  |
| `contributors_url` | `string` |  |
| `topics` | `array` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `permissions` | `object` |  |
| `ssh_url` | `string` |  |
| `subscription_url` | `string` |  |
| `deployments_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `license` | `object` |  |
| `milestones_url` | `string` |  |
| `commits_url` | `string` |  |
| `pulls_url` | `string` |  |
| `mirror_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `is_template` | `boolean` |  |
| `assignees_url` | `string` |  |
| `contents_url` | `string` |  |
| `teams_url` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `has_pages` | `boolean` |  |
| `issue_comment_url` | `string` |  |
| `pushed_at` | `string` |  |
| `hooks_url` | `string` |  |
| `archived` | `boolean` |  |
| `events_url` | `string` |  |
| `forks_count` | `integer` |  |
| `branches_url` | `string` |  |
| `keys_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `has_projects` | `boolean` |  |
| `full_name` | `string` |  |
| `open_issues_count` | `integer` |  |
| `open_issues` | `integer` |  |
| `git_tags_url` | `string` |  |
| `default_branch` | `string` |  |
| `homepage` | `string` |  |
| `git_url` | `string` |  |
| `created_at` | `string` |  |
| `forks_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `clone_url` | `string` |  |
| `svn_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `watchers` | `integer` |  |
| `private` | `boolean` |  |
| `collaborators_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `subscribers_count` | `integer` |  |
| `fork` | `boolean` |  |
| `has_wiki` | `boolean` |  |
| `trees_url` | `string` |  |
| `labels_url` | `string` |  |
| `releases_url` | `string` |  |
| `size` | `integer` |  |
| `stargazers_count` | `integer` |  |
| `url` | `string` |  |
| `languages_url` | `string` |  |
| `comments_url` | `string` |  |
| `template_repository` | `object` | A git repository |
| `statuses_url` | `string` |  |
| `updated_at` | `string` |  |
| `compare_url` | `string` |  |
| `tags_url` | `string` |  |
| `language` | `string` |  |
| `temp_clone_token` | `string` |  |
| `notifications_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_selected_repos_for_org_secret` | `SELECT` | `org, secret_name` | Lists all repositories that have been selected when the `visibility` for repository access to a secret is set to `selected`. You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `secrets` organization permission to use this endpoint. |
| `add_selected_repo_to_org_secret` | `INSERT` | `org, repository_id, secret_name` | Adds a repository to an organization secret when the `visibility` for repository access is set to `selected`. The visibility is set when you [Create or update an organization secret](https://docs.github.com/rest/reference/actions#create-or-update-an-organization-secret). You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `secrets` organization permission to use this endpoint. |
| `remove_selected_repo_from_org_secret` | `DELETE` | `org, repository_id, secret_name` | Removes a repository from an organization secret when the `visibility` for repository access is set to `selected`. The visibility is set when you [Create or update an organization secret](https://docs.github.com/rest/reference/actions#create-or-update-an-organization-secret). You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `secrets` organization permission to use this endpoint. |
| `set_selected_repos_for_org_secret` | `EXEC` | `org, secret_name, data__selected_repository_ids` | Replaces all repositories for an organization secret when the `visibility` for repository access is set to `selected`. The visibility is set when you [Create or update an organization secret](https://docs.github.com/rest/reference/actions#create-or-update-an-organization-secret). You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `secrets` organization permission to use this endpoint. |
