---
title: details
hide_title: false
hide_table_of_contents: false
keywords:
  - details
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
<tr><td><b>Name</b></td><td><code>details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.details</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `assignees_url` | `string` |  |
| `pulls_url` | `string` |  |
| `watchers` | `integer` |  |
| `pushed_at` | `string` |  |
| `squash_merge_commit_message` | `string` | The default value for a squash merge commit message:<br /><br />- `PR_BODY` - default to the pull request's body.<br />- `COMMIT_MESSAGES` - default to the branch's commit messages.<br />- `BLANK` - default to a blank commit message. |
| `permissions` | `object` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `git_url` | `string` |  |
| `statuses_url` | `string` |  |
| `allow_merge_commit` | `boolean` |  |
| `contents_url` | `string` |  |
| `subscription_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `deployments_url` | `string` |  |
| `clone_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `disabled` | `boolean` | Returns whether or not this repository disabled. |
| `forks` | `integer` |  |
| `milestones_url` | `string` |  |
| `comments_url` | `string` |  |
| `template_repository` | `object` | A repository on GitHub. |
| `forks_url` | `string` |  |
| `contributors_url` | `string` |  |
| `hooks_url` | `string` |  |
| `compare_url` | `string` |  |
| `allow_rebase_merge` | `boolean` |  |
| `archive_url` | `string` |  |
| `issues_url` | `string` |  |
| `allow_update_branch` | `boolean` |  |
| `releases_url` | `string` |  |
| `has_discussions` | `boolean` |  |
| `git_refs_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `merge_commit_title` | `string` | The default value for a merge commit title.<br /><br />  - `PR_TITLE` - default to the pull request's title.<br />  - `MERGE_MESSAGE` - default to the classic title for a merge message (e.g., Merge pull request #123 from branch-name). |
| `anonymous_access_enabled` | `boolean` | Whether anonymous git access is allowed. |
| `node_id` | `string` |  |
| `homepage` | `string` |  |
| `blobs_url` | `string` |  |
| `html_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `merge_commit_message` | `string` | The default value for a merge commit message.<br /><br />- `PR_TITLE` - default to the pull request's title.<br />- `PR_BODY` - default to the pull request's body.<br />- `BLANK` - default to a blank commit message. |
| `issue_comment_url` | `string` |  |
| `fork` | `boolean` |  |
| `code_of_conduct` | `object` | Code of Conduct Simple |
| `has_wiki` | `boolean` |  |
| `topics` | `array` |  |
| `temp_clone_token` | `string` |  |
| `full_name` | `string` |  |
| `has_pages` | `boolean` |  |
| `git_tags_url` | `string` |  |
| `mirror_url` | `string` |  |
| `created_at` | `string` |  |
| `allow_squash_merge` | `boolean` |  |
| `private` | `boolean` |  |
| `network_count` | `integer` |  |
| `collaborators_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `security_and_analysis` | `object` |  |
| `url` | `string` |  |
| `allow_auto_merge` | `boolean` |  |
| `open_issues_count` | `integer` |  |
| `branches_url` | `string` |  |
| `license` | `object` | License Simple |
| `has_projects` | `boolean` |  |
| `organization` | `object` | A GitHub user. |
| `git_commits_url` | `string` |  |
| `svn_url` | `string` |  |
| `labels_url` | `string` |  |
| `archived` | `boolean` |  |
| `open_issues` | `integer` |  |
| `visibility` | `string` | The repository visibility: public, private, or internal. |
| `languages_url` | `string` |  |
| `commits_url` | `string` |  |
| `events_url` | `string` |  |
| `downloads_url` | `string` |  |
| `size` | `integer` | The size of the repository. Size is calculated hourly. When a repository is initially created, the size is 0. |
| `source` | `object` | A repository on GitHub. |
| `is_template` | `boolean` |  |
| `teams_url` | `string` |  |
| `web_commit_signoff_required` | `boolean` |  |
| `allow_forking` | `boolean` |  |
| `subscribers_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `tags_url` | `string` |  |
| `keys_url` | `string` |  |
| `use_squash_pr_title_as_default` | `boolean` |  |
| `master_branch` | `string` |  |
| `trees_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `default_branch` | `string` |  |
| `notifications_url` | `string` |  |
| `ssh_url` | `string` |  |
| `squash_merge_commit_title` | `string` | The default value for a squash merge commit title:<br /><br />- `PR_TITLE` - default to the pull request's title.<br />- `COMMIT_OR_PR_TITLE` - default to the commit's title (if only one commit) or the pull request's title (when more than one commit). |
| `forks_count` | `integer` |  |
| `updated_at` | `string` |  |
| `parent` | `object` | A repository on GitHub. |
| `owner` | `object` | A GitHub user. |
| `language` | `string` |  |
| `merges_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `owner, repo` |
