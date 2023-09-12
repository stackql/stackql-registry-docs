---
title: repos
hide_title: false
hide_table_of_contents: false
keywords:
  - repos
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
<tr><td><b>Name</b></td><td><code>repos</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.repos</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `events_url` | `string` |  |
| `source` | `object` | A repository on GitHub. |
| `parent` | `object` | A repository on GitHub. |
| `languages_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `commits_url` | `string` |  |
| `fork` | `boolean` |  |
| `template_repository` | `object` | A repository on GitHub. |
| `has_pages` | `boolean` |  |
| `allow_update_branch` | `boolean` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `permissions` | `object` |  |
| `is_template` | `boolean` |  |
| `watchers_count` | `integer` |  |
| `pulls_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `branches_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `archive_url` | `string` |  |
| `merge_commit_title` | `string` | The default value for a merge commit title.<br /><br />  - `PR_TITLE` - default to the pull request's title.<br />  - `MERGE_MESSAGE` - default to the classic title for a merge message (e.g., Merge pull request #123 from branch-name). |
| `git_tags_url` | `string` |  |
| `watchers` | `integer` |  |
| `keys_url` | `string` |  |
| `created_at` | `string` |  |
| `assignees_url` | `string` |  |
| `node_id` | `string` |  |
| `squash_merge_commit_title` | `string` | The default value for a squash merge commit title:<br /><br />- `PR_TITLE` - default to the pull request's title.<br />- `COMMIT_OR_PR_TITLE` - default to the commit's title (if only one commit) or the pull request's title (when more than one commit). |
| `clone_url` | `string` |  |
| `network_count` | `integer` |  |
| `allow_merge_commit` | `boolean` |  |
| `compare_url` | `string` |  |
| `deployments_url` | `string` |  |
| `statuses_url` | `string` |  |
| `homepage` | `string` |  |
| `downloads_url` | `string` |  |
| `mirror_url` | `string` |  |
| `has_discussions` | `boolean` |  |
| `html_url` | `string` |  |
| `open_issues` | `integer` |  |
| `disabled` | `boolean` | Returns whether or not this repository disabled. |
| `pushed_at` | `string` |  |
| `default_branch` | `string` |  |
| `collaborators_url` | `string` |  |
| `organization` | `object` | A GitHub user. |
| `issue_comment_url` | `string` |  |
| `size` | `integer` | The size of the repository. Size is calculated hourly. When a repository is initially created, the size is 0. |
| `use_squash_pr_title_as_default` | `boolean` |  |
| `forks` | `integer` |  |
| `comments_url` | `string` |  |
| `owner` | `object` | A GitHub user. |
| `git_url` | `string` |  |
| `updated_at` | `string` |  |
| `releases_url` | `string` |  |
| `license` | `object` | License Simple |
| `forks_url` | `string` |  |
| `forks_count` | `integer` |  |
| `stargazers_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `trees_url` | `string` |  |
| `blobs_url` | `string` |  |
| `master_branch` | `string` |  |
| `hooks_url` | `string` |  |
| `ssh_url` | `string` |  |
| `visibility` | `string` | The repository visibility: public, private, or internal. |
| `web_commit_signoff_required` | `boolean` |  |
| `contributors_url` | `string` |  |
| `anonymous_access_enabled` | `boolean` | Whether anonymous git access is allowed. |
| `tags_url` | `string` |  |
| `allow_rebase_merge` | `boolean` |  |
| `has_wiki` | `boolean` |  |
| `private` | `boolean` |  |
| `code_of_conduct` | `object` | Code of Conduct Simple |
| `notifications_url` | `string` |  |
| `contents_url` | `string` |  |
| `merge_commit_message` | `string` | The default value for a merge commit message.<br /><br />- `PR_TITLE` - default to the pull request's title.<br />- `PR_BODY` - default to the pull request's body.<br />- `BLANK` - default to a blank commit message. |
| `topics` | `array` |  |
| `milestones_url` | `string` |  |
| `language` | `string` |  |
| `issue_events_url` | `string` |  |
| `svn_url` | `string` |  |
| `subscription_url` | `string` |  |
| `url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `full_name` | `string` |  |
| `allow_squash_merge` | `boolean` |  |
| `subscribers_url` | `string` |  |
| `labels_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `teams_url` | `string` |  |
| `allow_auto_merge` | `boolean` |  |
| `subscribers_count` | `integer` |  |
| `allow_forking` | `boolean` |  |
| `squash_merge_commit_message` | `string` | The default value for a squash merge commit message:<br /><br />- `PR_BODY` - default to the pull request's body.<br />- `COMMIT_MESSAGES` - default to the branch's commit messages.<br />- `BLANK` - default to a blank commit message. |
| `merges_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `git_commits_url` | `string` |  |
| `issues_url` | `string` |  |
| `archived` | `boolean` |  |
| `security_and_analysis` | `object` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `owner, repo` | The `parent` and `source` objects are present when the repository is a fork. `parent` is the repository this repository was forked from, `source` is the ultimate source for the network.<br /><br />**Note:** In order to see the `security_and_analysis` block for a repository you must have admin permissions for the repository or be an owner or security manager for the organization that owns the repository. For more information, see "[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)." |
| `delete` | `DELETE` | `owner, repo` | Deleting a repository requires admin access. If OAuth is used, the `delete_repo` scope is required.<br /><br />If an organization owner has configured the organization to prevent members from deleting organization-owned<br />repositories, you will get a `403 Forbidden` response. |
| `update` | `EXEC` | `owner, repo` | **Note**: To edit a repository's topics, use the [Replace all repository topics](https://docs.github.com/rest/repos/repos#replace-all-repository-topics) endpoint. |
