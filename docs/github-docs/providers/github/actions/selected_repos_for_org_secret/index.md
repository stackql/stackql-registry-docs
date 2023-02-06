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
| `mirror_url` | `string` |  |
| `private` | `boolean` |  |
| `template_repository` | `object` | A git repository |
| `git_commits_url` | `string` |  |
| `permissions` | `object` |  |
| `pushed_at` | `string` |  |
| `has_projects` | `boolean` |  |
| `language` | `string` |  |
| `comments_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `keys_url` | `string` |  |
| `is_template` | `boolean` |  |
| `owner` | `object` | Simple User |
| `issues_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `subscribers_count` | `integer` |  |
| `issue_comment_url` | `string` |  |
| `branches_url` | `string` |  |
| `disabled` | `boolean` |  |
| `hooks_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `languages_url` | `string` |  |
| `full_name` | `string` |  |
| `git_refs_url` | `string` |  |
| `forks_url` | `string` |  |
| `url` | `string` |  |
| `merges_url` | `string` |  |
| `created_at` | `string` |  |
| `downloads_url` | `string` |  |
| `deployments_url` | `string` |  |
| `size` | `integer` |  |
| `watchers_count` | `integer` |  |
| `ssh_url` | `string` |  |
| `open_issues` | `integer` |  |
| `updated_at` | `string` |  |
| `trees_url` | `string` |  |
| `contents_url` | `string` |  |
| `license` | `object` |  |
| `teams_url` | `string` |  |
| `watchers` | `integer` |  |
| `allow_forking` | `boolean` |  |
| `pulls_url` | `string` |  |
| `visibility` | `string` |  |
| `archive_url` | `string` |  |
| `subscription_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `html_url` | `string` |  |
| `fork` | `boolean` |  |
| `blobs_url` | `string` |  |
| `compare_url` | `string` |  |
| `commits_url` | `string` |  |
| `svn_url` | `string` |  |
| `notifications_url` | `string` |  |
| `git_url` | `string` |  |
| `forks_count` | `integer` |  |
| `contributors_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `assignees_url` | `string` |  |
| `labels_url` | `string` |  |
| `archived` | `boolean` |  |
| `has_issues` | `boolean` |  |
| `clone_url` | `string` |  |
| `statuses_url` | `string` |  |
| `events_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `node_id` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `default_branch` | `string` |  |
| `forks` | `integer` |  |
| `releases_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `homepage` | `string` |  |
| `tags_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `network_count` | `integer` |  |
| `milestones_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `role_name` | `string` |  |
| `topics` | `array` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_selected_repos_for_org_secret` | `SELECT` | `org, secret_name` | Lists all repositories that have been selected when the `visibility` for repository access to a secret is set to `selected`. You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `secrets` organization permission to use this endpoint. |
| `add_selected_repo_to_org_secret` | `INSERT` | `org, repository_id, secret_name` | Adds a repository to an organization secret when the `visibility` for repository access is set to `selected`. The visibility is set when you [Create or update an organization secret](https://docs.github.com/rest/reference/actions#create-or-update-an-organization-secret). You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `secrets` organization permission to use this endpoint. |
| `remove_selected_repo_from_org_secret` | `DELETE` | `org, repository_id, secret_name` | Removes a repository from an organization secret when the `visibility` for repository access is set to `selected`. The visibility is set when you [Create or update an organization secret](https://docs.github.com/rest/reference/actions#create-or-update-an-organization-secret). You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `secrets` organization permission to use this endpoint. |
| `set_selected_repos_for_org_secret` | `EXEC` | `org, secret_name, data__selected_repository_ids` | Replaces all repositories for an organization secret when the `visibility` for repository access is set to `selected`. The visibility is set when you [Create or update an organization secret](https://docs.github.com/rest/reference/actions#create-or-update-an-organization-secret). You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `secrets` organization permission to use this endpoint. |
