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
| `subscribers_url` | `string` |  |
| `labels_url` | `string` |  |
| `open_issues` | `integer` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `notifications_url` | `string` |  |
| `watchers` | `integer` |  |
| `role_name` | `string` |  |
| `template_repository` | `object` | A git repository |
| `tags_url` | `string` |  |
| `git_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `mirror_url` | `string` |  |
| `license` | `object` |  |
| `open_issues_count` | `integer` |  |
| `has_projects` | `boolean` |  |
| `disabled` | `boolean` |  |
| `releases_url` | `string` |  |
| `full_name` | `string` |  |
| `hooks_url` | `string` |  |
| `languages_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `comments_url` | `string` |  |
| `subscription_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `watchers_count` | `integer` |  |
| `branches_url` | `string` |  |
| `blobs_url` | `string` |  |
| `node_id` | `string` |  |
| `has_pages` | `boolean` |  |
| `archived` | `boolean` |  |
| `svn_url` | `string` |  |
| `forks` | `integer` |  |
| `created_at` | `string` |  |
| `contributors_url` | `string` |  |
| `downloads_url` | `string` |  |
| `pulls_url` | `string` |  |
| `issues_url` | `string` |  |
| `commits_url` | `string` |  |
| `forks_url` | `string` |  |
| `owner` | `object` | Simple User |
| `language` | `string` |  |
| `stargazers_count` | `integer` |  |
| `default_branch` | `string` |  |
| `fork` | `boolean` |  |
| `collaborators_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `visibility` | `string` |  |
| `size` | `integer` |  |
| `git_tags_url` | `string` |  |
| `clone_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `topics` | `array` |  |
| `ssh_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `pushed_at` | `string` |  |
| `html_url` | `string` |  |
| `private` | `boolean` |  |
| `issue_events_url` | `string` |  |
| `keys_url` | `string` |  |
| `updated_at` | `string` |  |
| `compare_url` | `string` |  |
| `milestones_url` | `string` |  |
| `permissions` | `object` |  |
| `git_refs_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `is_template` | `boolean` |  |
| `teams_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `statuses_url` | `string` |  |
| `network_count` | `integer` |  |
| `allow_forking` | `boolean` |  |
| `url` | `string` |  |
| `deployments_url` | `string` |  |
| `events_url` | `string` |  |
| `merges_url` | `string` |  |
| `homepage` | `string` |  |
| `assignees_url` | `string` |  |
| `contents_url` | `string` |  |
| `forks_count` | `integer` |  |
| `trees_url` | `string` |  |
| `archive_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_selected_repos_for_org_secret` | `SELECT` | `org, secret_name` | Lists all repositories that have been selected when the `visibility` for repository access to a secret is set to `selected`. You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `dependabot_secrets` organization permission to use this endpoint. |
| `add_selected_repo_to_org_secret` | `INSERT` | `org, repository_id, secret_name` | Adds a repository to an organization secret when the `visibility` for repository access is set to `selected`. The visibility is set when you [Create or update an organization secret](https://docs.github.com/rest/reference/dependabot#create-or-update-an-organization-secret). You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `dependabot_secrets` organization permission to use this endpoint. |
| `remove_selected_repo_from_org_secret` | `DELETE` | `org, repository_id, secret_name` | Removes a repository from an organization secret when the `visibility` for repository access is set to `selected`. The visibility is set when you [Create or update an organization secret](https://docs.github.com/rest/reference/dependabot#create-or-update-an-organization-secret). You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `dependabot_secrets` organization permission to use this endpoint. |
| `set_selected_repos_for_org_secret` | `EXEC` | `org, secret_name, data__selected_repository_ids` | Replaces all repositories for an organization secret when the `visibility` for repository access is set to `selected`. The visibility is set when you [Create or update an organization secret](https://docs.github.com/rest/reference/dependabot#create-or-update-an-organization-secret). You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `dependabot_secrets` organization permission to use this endpoint. |
