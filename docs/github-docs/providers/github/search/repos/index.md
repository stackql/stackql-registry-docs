---
title: repos
hide_title: false
hide_table_of_contents: false
keywords:
  - repos
  - search
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
<tr><td><b>Name</b></td><td><code>repos</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.search.repos" /></td></tr>
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
| <CopyableCode code="archive_url" /> | `string` |  |
| <CopyableCode code="archived" /> | `boolean` |  |
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
| <CopyableCode code="merges_url" /> | `string` |  |
| <CopyableCode code="milestones_url" /> | `string` |  |
| <CopyableCode code="mirror_url" /> | `string` |  |
| <CopyableCode code="node_id" /> | `string` |  |
| <CopyableCode code="notifications_url" /> | `string` |  |
| <CopyableCode code="open_issues" /> | `integer` |  |
| <CopyableCode code="open_issues_count" /> | `integer` |  |
| <CopyableCode code="owner" /> | `object` | A GitHub user. |
| <CopyableCode code="permissions" /> | `object` |  |
| <CopyableCode code="private" /> | `boolean` |  |
| <CopyableCode code="pulls_url" /> | `string` |  |
| <CopyableCode code="pushed_at" /> | `string` |  |
| <CopyableCode code="releases_url" /> | `string` |  |
| <CopyableCode code="score" /> | `number` |  |
| <CopyableCode code="size" /> | `integer` |  |
| <CopyableCode code="ssh_url" /> | `string` |  |
| <CopyableCode code="stargazers_count" /> | `integer` |  |
| <CopyableCode code="stargazers_url" /> | `string` |  |
| <CopyableCode code="statuses_url" /> | `string` |  |
| <CopyableCode code="subscribers_url" /> | `string` |  |
| <CopyableCode code="subscription_url" /> | `string` |  |
| <CopyableCode code="svn_url" /> | `string` |  |
| <CopyableCode code="tags_url" /> | `string` |  |
| <CopyableCode code="teams_url" /> | `string` |  |
| <CopyableCode code="temp_clone_token" /> | `string` |  |
| <CopyableCode code="text_matches" /> | `array` |  |
| <CopyableCode code="topics" /> | `array` |  |
| <CopyableCode code="trees_url" /> | `string` |  |
| <CopyableCode code="updated_at" /> | `string` |  |
| <CopyableCode code="url" /> | `string` |  |
| <CopyableCode code="visibility" /> | `string` | The repository visibility: public, private, or internal. |
| <CopyableCode code="watchers" /> | `integer` |  |
| <CopyableCode code="watchers_count" /> | `integer` |  |
| <CopyableCode code="web_commit_signoff_required" /> | `boolean` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="repos" /> | `SELECT` | <CopyableCode code="q" /> |
