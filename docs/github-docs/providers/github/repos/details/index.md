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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.repos.details" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` |  |
| <CopyableCode code="name" /> | `string` |  |
| <CopyableCode code="description" /> | `string` |  |
| <CopyableCode code="allow_auto_merge" /> | `boolean` |  |
| <CopyableCode code="allow_forking" /> | `boolean` |  |
| <CopyableCode code="allow_merge_commit" /> | `boolean` |  |
| <CopyableCode code="allow_rebase_merge" /> | `boolean` |  |
| <CopyableCode code="allow_squash_merge" /> | `boolean` |  |
| <CopyableCode code="allow_update_branch" /> | `boolean` |  |
| <CopyableCode code="anonymous_access_enabled" /> | `boolean` | Whether anonymous git access is allowed. |
| <CopyableCode code="archive_url" /> | `string` |  |
| <CopyableCode code="archived" /> | `boolean` |  |
| <CopyableCode code="assignees_url" /> | `string` |  |
| <CopyableCode code="blobs_url" /> | `string` |  |
| <CopyableCode code="branches_url" /> | `string` |  |
| <CopyableCode code="clone_url" /> | `string` |  |
| <CopyableCode code="code_of_conduct" /> | `object` | Code of Conduct Simple |
| <CopyableCode code="collaborators_url" /> | `string` |  |
| <CopyableCode code="comments_url" /> | `string` |  |
| <CopyableCode code="commits_url" /> | `string` |  |
| <CopyableCode code="compare_url" /> | `string` |  |
| <CopyableCode code="contents_url" /> | `string` |  |
| <CopyableCode code="contributors_url" /> | `string` |  |
| <CopyableCode code="created_at" /> | `string` |  |
| <CopyableCode code="default_branch" /> | `string` |  |
| <CopyableCode code="delete_branch_on_merge" /> | `boolean` |  |
| <CopyableCode code="deployments_url" /> | `string` |  |
| <CopyableCode code="disabled" /> | `boolean` | Returns whether or not this repository disabled. |
| <CopyableCode code="downloads_url" /> | `string` |  |
| <CopyableCode code="events_url" /> | `string` |  |
| <CopyableCode code="fork" /> | `boolean` |  |
| <CopyableCode code="forks" /> | `integer` |  |
| <CopyableCode code="forks_count" /> | `integer` |  |
| <CopyableCode code="forks_url" /> | `string` |  |
| <CopyableCode code="full_name" /> | `string` |  |
| <CopyableCode code="git_commits_url" /> | `string` |  |
| <CopyableCode code="git_refs_url" /> | `string` |  |
| <CopyableCode code="git_tags_url" /> | `string` |  |
| <CopyableCode code="git_url" /> | `string` |  |
| <CopyableCode code="has_discussions" /> | `boolean` |  |
| <CopyableCode code="has_downloads" /> | `boolean` |  |
| <CopyableCode code="has_issues" /> | `boolean` |  |
| <CopyableCode code="has_pages" /> | `boolean` |  |
| <CopyableCode code="has_projects" /> | `boolean` |  |
| <CopyableCode code="has_wiki" /> | `boolean` |  |
| <CopyableCode code="homepage" /> | `string` |  |
| <CopyableCode code="hooks_url" /> | `string` |  |
| <CopyableCode code="html_url" /> | `string` |  |
| <CopyableCode code="is_template" /> | `boolean` |  |
| <CopyableCode code="issue_comment_url" /> | `string` |  |
| <CopyableCode code="issue_events_url" /> | `string` |  |
| <CopyableCode code="issues_url" /> | `string` |  |
| <CopyableCode code="keys_url" /> | `string` |  |
| <CopyableCode code="labels_url" /> | `string` |  |
| <CopyableCode code="language" /> | `string` |  |
| <CopyableCode code="languages_url" /> | `string` |  |
| <CopyableCode code="license" /> | `object` | License Simple |
| <CopyableCode code="master_branch" /> | `string` |  |
| <CopyableCode code="merge_commit_message" /> | `string` | The default value for a merge commit message.<br /><br />- `PR_TITLE` - default to the pull request's title.<br />- `PR_BODY` - default to the pull request's body.<br />- `BLANK` - default to a blank commit message. |
| <CopyableCode code="merge_commit_title" /> | `string` | The default value for a merge commit title.<br /><br />  - `PR_TITLE` - default to the pull request's title.<br />  - `MERGE_MESSAGE` - default to the classic title for a merge message (e.g., Merge pull request #123 from branch-name). |
| <CopyableCode code="merges_url" /> | `string` |  |
| <CopyableCode code="milestones_url" /> | `string` |  |
| <CopyableCode code="mirror_url" /> | `string` |  |
| <CopyableCode code="network_count" /> | `integer` |  |
| <CopyableCode code="node_id" /> | `string` |  |
| <CopyableCode code="notifications_url" /> | `string` |  |
| <CopyableCode code="open_issues" /> | `integer` |  |
| <CopyableCode code="open_issues_count" /> | `integer` |  |
| <CopyableCode code="organization" /> | `object` | A GitHub user. |
| <CopyableCode code="owner" /> | `object` | A GitHub user. |
| <CopyableCode code="parent" /> | `object` | A repository on GitHub. |
| <CopyableCode code="permissions" /> | `object` |  |
| <CopyableCode code="private" /> | `boolean` |  |
| <CopyableCode code="pulls_url" /> | `string` |  |
| <CopyableCode code="pushed_at" /> | `string` |  |
| <CopyableCode code="releases_url" /> | `string` |  |
| <CopyableCode code="security_and_analysis" /> | `object` |  |
| <CopyableCode code="size" /> | `integer` | The size of the repository. Size is calculated hourly. When a repository is initially created, the size is 0. |
| <CopyableCode code="source" /> | `object` | A repository on GitHub. |
| <CopyableCode code="squash_merge_commit_message" /> | `string` | The default value for a squash merge commit message:<br /><br />- `PR_BODY` - default to the pull request's body.<br />- `COMMIT_MESSAGES` - default to the branch's commit messages.<br />- `BLANK` - default to a blank commit message. |
| <CopyableCode code="squash_merge_commit_title" /> | `string` | The default value for a squash merge commit title:<br /><br />- `PR_TITLE` - default to the pull request's title.<br />- `COMMIT_OR_PR_TITLE` - default to the commit's title (if only one commit) or the pull request's title (when more than one commit). |
| <CopyableCode code="ssh_url" /> | `string` |  |
| <CopyableCode code="stargazers_count" /> | `integer` |  |
| <CopyableCode code="stargazers_url" /> | `string` |  |
| <CopyableCode code="statuses_url" /> | `string` |  |
| <CopyableCode code="subscribers_count" /> | `integer` |  |
| <CopyableCode code="subscribers_url" /> | `string` |  |
| <CopyableCode code="subscription_url" /> | `string` |  |
| <CopyableCode code="svn_url" /> | `string` |  |
| <CopyableCode code="tags_url" /> | `string` |  |
| <CopyableCode code="teams_url" /> | `string` |  |
| <CopyableCode code="temp_clone_token" /> | `string` |  |
| <CopyableCode code="template_repository" /> | `object` | A repository on GitHub. |
| <CopyableCode code="topics" /> | `array` |  |
| <CopyableCode code="trees_url" /> | `string` |  |
| <CopyableCode code="updated_at" /> | `string` |  |
| <CopyableCode code="url" /> | `string` |  |
| <CopyableCode code="use_squash_pr_title_as_default" /> | `boolean` |  |
| <CopyableCode code="visibility" /> | `string` | The repository visibility: public, private, or internal. |
| <CopyableCode code="watchers" /> | `integer` |  |
| <CopyableCode code="watchers_count" /> | `integer` |  |
| <CopyableCode code="web_commit_signoff_required" /> | `boolean` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="owner, repo" /> |
