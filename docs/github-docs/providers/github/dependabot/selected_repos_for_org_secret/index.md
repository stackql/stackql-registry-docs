---
title: selected_repos_for_org_secret
hide_title: false
hide_table_of_contents: false
keywords:
  - selected_repos_for_org_secret
  - dependabot
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
<tr><td><b>Id</b></td><td><code>github.dependabot.selected_repos_for_org_secret</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `has_wiki` | `boolean` |  |
| `releases_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `mirror_url` | `string` |  |
| `svn_url` | `string` |  |
| `downloads_url` | `string` |  |
| `tags_url` | `string` |  |
| `disabled` | `boolean` |  |
| `issue_events_url` | `string` |  |
| `forks_url` | `string` |  |
| `created_at` | `string` |  |
| `notifications_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `visibility` | `string` |  |
| `topics` | `array` |  |
| `updated_at` | `string` |  |
| `role_name` | `string` |  |
| `license` | `object` |  |
| `archive_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `deployments_url` | `string` |  |
| `node_id` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `ssh_url` | `string` |  |
| `watchers` | `integer` |  |
| `is_template` | `boolean` |  |
| `size` | `integer` |  |
| `milestones_url` | `string` |  |
| `commits_url` | `string` |  |
| `contributors_url` | `string` |  |
| `homepage` | `string` |  |
| `collaborators_url` | `string` |  |
| `contents_url` | `string` |  |
| `assignees_url` | `string` |  |
| `fork` | `boolean` |  |
| `issue_comment_url` | `string` |  |
| `clone_url` | `string` |  |
| `comments_url` | `string` |  |
| `pulls_url` | `string` |  |
| `trees_url` | `string` |  |
| `default_branch` | `string` |  |
| `issues_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `languages_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `allow_forking` | `boolean` |  |
| `network_count` | `integer` |  |
| `language` | `string` |  |
| `subscription_url` | `string` |  |
| `url` | `string` |  |
| `hooks_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `template_repository` | `object` | A git repository |
| `has_pages` | `boolean` |  |
| `archived` | `boolean` |  |
| `events_url` | `string` |  |
| `forks` | `integer` |  |
| `full_name` | `string` |  |
| `labels_url` | `string` |  |
| `blobs_url` | `string` |  |
| `teams_url` | `string` |  |
| `branches_url` | `string` |  |
| `private` | `boolean` |  |
| `git_commits_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `owner` | `object` | Simple User |
| `open_issues` | `integer` |  |
| `merges_url` | `string` |  |
| `compare_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `pushed_at` | `string` |  |
| `keys_url` | `string` |  |
| `git_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `html_url` | `string` |  |
| `permissions` | `object` |  |
| `forks_count` | `integer` |  |
| `stargazers_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `git_refs_url` | `string` |  |
| `statuses_url` | `string` |  |
| `open_issues_count` | `integer` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_selected_repos_for_org_secret` | `SELECT` | `org, secret_name` | Lists all repositories that have been selected when the `visibility` for repository access to a secret is set to `selected`. You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `dependabot_secrets` organization permission to use this endpoint. |
| `add_selected_repo_to_org_secret` | `INSERT` | `org, repository_id, secret_name` | Adds a repository to an organization secret when the `visibility` for repository access is set to `selected`. The visibility is set when you [Create or update an organization secret](https://docs.github.com/rest/reference/dependabot#create-or-update-an-organization-secret). You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `dependabot_secrets` organization permission to use this endpoint. |
| `remove_selected_repo_from_org_secret` | `DELETE` | `org, repository_id, secret_name` | Removes a repository from an organization secret when the `visibility` for repository access is set to `selected`. The visibility is set when you [Create or update an organization secret](https://docs.github.com/rest/reference/dependabot#create-or-update-an-organization-secret). You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `dependabot_secrets` organization permission to use this endpoint. |
| `set_selected_repos_for_org_secret` | `EXEC` | `org, secret_name, data__selected_repository_ids` | Replaces all repositories for an organization secret when the `visibility` for repository access is set to `selected`. The visibility is set when you [Create or update an organization secret](https://docs.github.com/rest/reference/dependabot#create-or-update-an-organization-secret). You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `dependabot_secrets` organization permission to use this endpoint. |
