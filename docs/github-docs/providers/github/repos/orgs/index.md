---
title: orgs
hide_title: false
hide_table_of_contents: false
keywords:
  - orgs
  - repos
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
<tr><td><b>Name</b></td><td><code>orgs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.orgs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `hooks_url` | `string` |  |
| `full_name` | `string` |  |
| `statuses_url` | `string` |  |
| `events_url` | `string` |  |
| `has_discussions` | `boolean` |  |
| `temp_clone_token` | `string` |  |
| `commits_url` | `string` |  |
| `disabled` | `boolean` |  |
| `created_at` | `string` |  |
| `url` | `string` |  |
| `milestones_url` | `string` |  |
| `releases_url` | `string` |  |
| `ssh_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `contributors_url` | `string` |  |
| `html_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `fork` | `boolean` |  |
| `archived` | `boolean` |  |
| `subscription_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `visibility` | `string` |  |
| `network_count` | `integer` |  |
| `size` | `integer` | The size of the repository. Size is calculated hourly. When a repository is initially created, the size is 0. |
| `code_of_conduct` | `object` | Code Of Conduct |
| `has_projects` | `boolean` |  |
| `security_and_analysis` | `object` |  |
| `keys_url` | `string` |  |
| `downloads_url` | `string` |  |
| `languages_url` | `string` |  |
| `tags_url` | `string` |  |
| `pulls_url` | `string` |  |
| `svn_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `is_template` | `boolean` |  |
| `has_pages` | `boolean` |  |
| `git_tags_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `license` | `object` |  |
| `forks_count` | `integer` |  |
| `issues_url` | `string` |  |
| `web_commit_signoff_required` | `boolean` |  |
| `open_issues` | `integer` |  |
| `archive_url` | `string` |  |
| `role_name` | `string` |  |
| `merges_url` | `string` |  |
| `clone_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `subscribers_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `mirror_url` | `string` |  |
| `notifications_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `compare_url` | `string` |  |
| `assignees_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `owner` | `object` | A GitHub user. |
| `comments_url` | `string` |  |
| `homepage` | `string` |  |
| `permissions` | `object` |  |
| `topics` | `array` |  |
| `pushed_at` | `string` |  |
| `trees_url` | `string` |  |
| `contents_url` | `string` |  |
| `blobs_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `private` | `boolean` |  |
| `forks_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `node_id` | `string` |  |
| `watchers` | `integer` |  |
| `labels_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `forks` | `integer` |  |
| `language` | `string` |  |
| `deployments_url` | `string` |  |
| `teams_url` | `string` |  |
| `default_branch` | `string` |  |
| `git_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `updated_at` | `string` |  |
| `branches_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_for_org` | `SELECT` | `org` | Lists repositories for the specified organization.<br /><br />**Note:** In order to see the `security_and_analysis` block for a repository you must have admin permissions for the repository or be an owner or security manager for the organization that owns the repository. For more information, see "[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)." |
| `create_in_org` | `INSERT` | `org, data__name` | Creates a new repository in the specified organization. The authenticated user must be a member of the organization.<br /><br />**OAuth scope requirements**<br /><br />When using [OAuth](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/), authorizations must include:<br /><br />*   `public_repo` scope or `repo` scope to create a public repository. Note: For GitHub AE, use `repo` scope to create an internal repository.<br />*   `repo` scope to create a private repository |
