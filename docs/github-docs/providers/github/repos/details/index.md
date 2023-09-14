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
| `visibility` | `string` | The repository visibility: public, private, or internal. |
| `default_branch` | `string` |  |
| `teams_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `forks` | `integer` |  |
| `branches_url` | `string` |  |
| `clone_url` | `string` |  |
| `security_and_analysis` | `object` |  |
| `downloads_url` | `string` |  |
| `notifications_url` | `string` |  |
| `master_branch` | `string` |  |
| `issues_url` | `string` |  |
| `contributors_url` | `string` |  |
| `fork` | `boolean` |  |
| `web_commit_signoff_required` | `boolean` |  |
| `commits_url` | `string` |  |
| `events_url` | `string` |  |
| `blobs_url` | `string` |  |
| `organization` | `object` | A GitHub user. |
| `full_name` | `string` |  |
| `merge_commit_title` | `string` | The default value for a merge commit title.<br /><br />  - `PR_TITLE` - default to the pull request's title.<br />  - `MERGE_MESSAGE` - default to the classic title for a merge message (e.g., Merge pull request #123 from branch-name). |
| `has_discussions` | `boolean` |  |
| `url` | `string` |  |
| `allow_rebase_merge` | `boolean` |  |
| `forks_count` | `integer` |  |
| `has_issues` | `boolean` |  |
| `template_repository` | `object` | A repository on GitHub. |
| `assignees_url` | `string` |  |
| `deployments_url` | `string` |  |
| `keys_url` | `string` |  |
| `topics` | `array` |  |
| `statuses_url` | `string` |  |
| `forks_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `pulls_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `html_url` | `string` |  |
| `squash_merge_commit_title` | `string` | The default value for a squash merge commit title:<br /><br />- `PR_TITLE` - default to the pull request's title.<br />- `COMMIT_OR_PR_TITLE` - default to the commit's title (if only one commit) or the pull request's title (when more than one commit). |
| `allow_merge_commit` | `boolean` |  |
| `source` | `object` | A repository on GitHub. |
| `watchers` | `integer` |  |
| `code_of_conduct` | `object` | Code of Conduct Simple |
| `use_squash_pr_title_as_default` | `boolean` |  |
| `archive_url` | `string` |  |
| `hooks_url` | `string` |  |
| `tags_url` | `string` |  |
| `releases_url` | `string` |  |
| `squash_merge_commit_message` | `string` | The default value for a squash merge commit message:<br /><br />- `PR_BODY` - default to the pull request's body.<br />- `COMMIT_MESSAGES` - default to the branch's commit messages.<br />- `BLANK` - default to a blank commit message. |
| `permissions` | `object` |  |
| `git_refs_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `subscription_url` | `string` |  |
| `network_count` | `integer` |  |
| `languages_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `created_at` | `string` |  |
| `comments_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `subscribers_url` | `string` |  |
| `git_url` | `string` |  |
| `size` | `integer` | The size of the repository. Size is calculated hourly. When a repository is initially created, the size is 0. |
| `watchers_count` | `integer` |  |
| `git_commits_url` | `string` |  |
| `svn_url` | `string` |  |
| `anonymous_access_enabled` | `boolean` | Whether anonymous git access is allowed. |
| `has_pages` | `boolean` |  |
| `language` | `string` |  |
| `has_projects` | `boolean` |  |
| `git_tags_url` | `string` |  |
| `merge_commit_message` | `string` | The default value for a merge commit message.<br /><br />- `PR_TITLE` - default to the pull request's title.<br />- `PR_BODY` - default to the pull request's body.<br />- `BLANK` - default to a blank commit message. |
| `ssh_url` | `string` |  |
| `milestones_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `labels_url` | `string` |  |
| `private` | `boolean` |  |
| `allow_update_branch` | `boolean` |  |
| `compare_url` | `string` |  |
| `allow_squash_merge` | `boolean` |  |
| `license` | `object` | License Simple |
| `open_issues` | `integer` |  |
| `pushed_at` | `string` |  |
| `allow_auto_merge` | `boolean` |  |
| `disabled` | `boolean` | Returns whether or not this repository disabled. |
| `updated_at` | `string` |  |
| `contents_url` | `string` |  |
| `homepage` | `string` |  |
| `is_template` | `boolean` |  |
| `stargazers_count` | `integer` |  |
| `open_issues_count` | `integer` |  |
| `mirror_url` | `string` |  |
| `owner` | `object` | A GitHub user. |
| `node_id` | `string` |  |
| `issue_comment_url` | `string` |  |
| `parent` | `object` | A repository on GitHub. |
| `temp_clone_token` | `string` |  |
| `collaborators_url` | `string` |  |
| `trees_url` | `string` |  |
| `archived` | `boolean` |  |
| `merges_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `owner, repo` |
