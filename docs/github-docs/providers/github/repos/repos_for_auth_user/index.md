---
title: repos_for_auth_user
hide_title: false
hide_table_of_contents: false
keywords:
  - repos_for_auth_user
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
<tr><td><b>Name</b></td><td><code>repos_for_auth_user</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.repos.repos_for_auth_user" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | Unique identifier of the repository |
| <CopyableCode code="name" /> | `string` | The name of the repository. |
| <CopyableCode code="description" /> | `string` |  |
| <CopyableCode code="allow_auto_merge" /> | `boolean` | Whether to allow Auto-merge to be used on pull requests. |
| <CopyableCode code="allow_forking" /> | `boolean` | Whether to allow forking this repo |
| <CopyableCode code="allow_merge_commit" /> | `boolean` | Whether to allow merge commits for pull requests. |
| <CopyableCode code="allow_rebase_merge" /> | `boolean` | Whether to allow rebase merges for pull requests. |
| <CopyableCode code="allow_squash_merge" /> | `boolean` | Whether to allow squash merges for pull requests. |
| <CopyableCode code="allow_update_branch" /> | `boolean` | Whether or not a pull request head branch that is behind its base branch can always be updated even if it is not required to be up to date before merging. |
| <CopyableCode code="anonymous_access_enabled" /> | `boolean` | Whether anonymous git access is enabled for this repository |
| <CopyableCode code="archive_url" /> | `string` |  |
| <CopyableCode code="archived" /> | `boolean` | Whether the repository is archived. |
| <CopyableCode code="assignees_url" /> | `string` |  |
| <CopyableCode code="blobs_url" /> | `string` |  |
| <CopyableCode code="branches_url" /> | `string` |  |
| <CopyableCode code="clone_url" /> | `string` |  |
| <CopyableCode code="collaborators_url" /> | `string` |  |
| <CopyableCode code="comments_url" /> | `string` |  |
| <CopyableCode code="commits_url" /> | `string` |  |
| <CopyableCode code="compare_url" /> | `string` |  |
| <CopyableCode code="contents_url" /> | `string` |  |
| <CopyableCode code="contributors_url" /> | `string` |  |
| <CopyableCode code="created_at" /> | `string` |  |
| <CopyableCode code="default_branch" /> | `string` | The default branch of the repository. |
| <CopyableCode code="delete_branch_on_merge" /> | `boolean` | Whether to delete head branches when pull requests are merged |
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
| <CopyableCode code="has_discussions" /> | `boolean` | Whether discussions are enabled. |
| <CopyableCode code="has_downloads" /> | `boolean` | Whether downloads are enabled. |
| <CopyableCode code="has_issues" /> | `boolean` | Whether issues are enabled. |
| <CopyableCode code="has_pages" /> | `boolean` |  |
| <CopyableCode code="has_projects" /> | `boolean` | Whether projects are enabled. |
| <CopyableCode code="has_wiki" /> | `boolean` | Whether the wiki is enabled. |
| <CopyableCode code="homepage" /> | `string` |  |
| <CopyableCode code="hooks_url" /> | `string` |  |
| <CopyableCode code="html_url" /> | `string` |  |
| <CopyableCode code="is_template" /> | `boolean` | Whether this repository acts as a template that can be used to generate new repositories. |
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
| <CopyableCode code="merge_commit_title" /> | `string` | The default value for a merge commit title.<br /><br />- `PR_TITLE` - default to the pull request's title.<br />- `MERGE_MESSAGE` - default to the classic title for a merge message (e.g., Merge pull request #123 from branch-name). |
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
| <CopyableCode code="permissions" /> | `object` |  |
| <CopyableCode code="private" /> | `boolean` | Whether the repository is private or public. |
| <CopyableCode code="pulls_url" /> | `string` |  |
| <CopyableCode code="pushed_at" /> | `string` |  |
| <CopyableCode code="releases_url" /> | `string` |  |
| <CopyableCode code="size" /> | `integer` | The size of the repository. Size is calculated hourly. When a repository is initially created, the size is 0. |
| <CopyableCode code="squash_merge_commit_message" /> | `string` | The default value for a squash merge commit message:<br /><br />- `PR_BODY` - default to the pull request's body.<br />- `COMMIT_MESSAGES` - default to the branch's commit messages.<br />- `BLANK` - default to a blank commit message. |
| <CopyableCode code="squash_merge_commit_title" /> | `string` | The default value for a squash merge commit title:<br /><br />- `PR_TITLE` - default to the pull request's title.<br />- `COMMIT_OR_PR_TITLE` - default to the commit's title (if only one commit) or the pull request's title (when more than one commit). |
| <CopyableCode code="ssh_url" /> | `string` |  |
| <CopyableCode code="stargazers_count" /> | `integer` |  |
| <CopyableCode code="stargazers_url" /> | `string` |  |
| <CopyableCode code="starred_at" /> | `string` |  |
| <CopyableCode code="statuses_url" /> | `string` |  |
| <CopyableCode code="subscribers_count" /> | `integer` |  |
| <CopyableCode code="subscribers_url" /> | `string` |  |
| <CopyableCode code="subscription_url" /> | `string` |  |
| <CopyableCode code="svn_url" /> | `string` |  |
| <CopyableCode code="tags_url" /> | `string` |  |
| <CopyableCode code="teams_url" /> | `string` |  |
| <CopyableCode code="temp_clone_token" /> | `string` |  |
| <CopyableCode code="template_repository" /> | `object` |  |
| <CopyableCode code="topics" /> | `array` |  |
| <CopyableCode code="trees_url" /> | `string` |  |
| <CopyableCode code="updated_at" /> | `string` |  |
| <CopyableCode code="url" /> | `string` |  |
| <CopyableCode code="use_squash_pr_title_as_default" /> | `boolean` | Whether a squash merge commit can use the pull request title as default. **This property has been deprecated. Please use `squash_merge_commit_title` instead. |
| <CopyableCode code="visibility" /> | `string` | The repository visibility: public, private, or internal. |
| <CopyableCode code="watchers" /> | `integer` |  |
| <CopyableCode code="watchers_count" /> | `integer` |  |
| <CopyableCode code="web_commit_signoff_required" /> | `boolean` | Whether to require contributors to sign off on web-based commits |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_for_authenticated_user" /> | `SELECT` |  | Lists repositories that the authenticated user has explicit permission (`:read`, `:write`, or `:admin`) to access.<br /><br />The authenticated user has explicit permission to access repositories they own, repositories where they are a collaborator, and repositories that they can access through an organization membership. |
| <CopyableCode code="create_for_authenticated_user" /> | `INSERT` | <CopyableCode code="data__name" /> | Creates a new repository for the authenticated user.<br /><br />**OAuth scope requirements**<br /><br />When using [OAuth](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/), authorizations must include:<br /><br />*   `public_repo` scope or `repo` scope to create a public repository. Note: For GitHub AE, use `repo` scope to create an internal repository.<br />*   `repo` scope to create a private repository. |
