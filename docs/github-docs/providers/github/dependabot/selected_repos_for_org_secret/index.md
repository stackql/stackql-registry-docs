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
| `has_projects` | `boolean` |  |
| `languages_url` | `string` |  |
| `statuses_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `permissions` | `object` |  |
| `allow_forking` | `boolean` |  |
| `watchers` | `integer` |  |
| `teams_url` | `string` |  |
| `pushed_at` | `string` |  |
| `labels_url` | `string` |  |
| `assignees_url` | `string` |  |
| `releases_url` | `string` |  |
| `blobs_url` | `string` |  |
| `url` | `string` |  |
| `git_url` | `string` |  |
| `forks_url` | `string` |  |
| `archived` | `boolean` |  |
| `has_issues` | `boolean` |  |
| `watchers_count` | `integer` |  |
| `events_url` | `string` |  |
| `forks` | `integer` |  |
| `contents_url` | `string` |  |
| `downloads_url` | `string` |  |
| `keys_url` | `string` |  |
| `compare_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `subscribers_count` | `integer` |  |
| `has_wiki` | `boolean` |  |
| `stargazers_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `issues_url` | `string` |  |
| `license` | `object` |  |
| `hooks_url` | `string` |  |
| `role_name` | `string` |  |
| `git_tags_url` | `string` |  |
| `milestones_url` | `string` |  |
| `notifications_url` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `open_issues` | `integer` |  |
| `subscribers_url` | `string` |  |
| `branches_url` | `string` |  |
| `commits_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `svn_url` | `string` |  |
| `mirror_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `pulls_url` | `string` |  |
| `updated_at` | `string` |  |
| `homepage` | `string` |  |
| `owner` | `object` | Simple User |
| `stargazers_count` | `integer` |  |
| `trees_url` | `string` |  |
| `is_template` | `boolean` |  |
| `template_repository` | `object` | A git repository |
| `default_branch` | `string` |  |
| `contributors_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `full_name` | `string` |  |
| `node_id` | `string` |  |
| `archive_url` | `string` |  |
| `private` | `boolean` |  |
| `ssh_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `deployments_url` | `string` |  |
| `subscription_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `disabled` | `boolean` |  |
| `topics` | `array` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `tags_url` | `string` |  |
| `comments_url` | `string` |  |
| `merges_url` | `string` |  |
| `created_at` | `string` |  |
| `forks_count` | `integer` |  |
| `clone_url` | `string` |  |
| `visibility` | `string` |  |
| `html_url` | `string` |  |
| `network_count` | `integer` |  |
| `language` | `string` |  |
| `size` | `integer` |  |
| `fork` | `boolean` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_selected_repos_for_org_secret` | `SELECT` | `org, secret_name` | Lists all repositories that have been selected when the `visibility` for repository access to a secret is set to `selected`. You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `dependabot_secrets` organization permission to use this endpoint. |
| `add_selected_repo_to_org_secret` | `INSERT` | `org, repository_id, secret_name` | Adds a repository to an organization secret when the `visibility` for repository access is set to `selected`. The visibility is set when you [Create or update an organization secret](https://docs.github.com/rest/reference/dependabot#create-or-update-an-organization-secret). You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `dependabot_secrets` organization permission to use this endpoint. |
| `remove_selected_repo_from_org_secret` | `DELETE` | `org, repository_id, secret_name` | Removes a repository from an organization secret when the `visibility` for repository access is set to `selected`. The visibility is set when you [Create or update an organization secret](https://docs.github.com/rest/reference/dependabot#create-or-update-an-organization-secret). You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `dependabot_secrets` organization permission to use this endpoint. |
| `set_selected_repos_for_org_secret` | `EXEC` | `org, secret_name, data__selected_repository_ids` | Replaces all repositories for an organization secret when the `visibility` for repository access is set to `selected`. The visibility is set when you [Create or update an organization secret](https://docs.github.com/rest/reference/dependabot#create-or-update-an-organization-secret). You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `dependabot_secrets` organization permission to use this endpoint. |
