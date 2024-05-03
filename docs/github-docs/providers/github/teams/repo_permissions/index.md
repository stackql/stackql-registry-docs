---
title: repo_permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - repo_permissions
  - teams
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
<tr><td><b>Name</b></td><td><code>repo_permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.teams.repo_permissions" /></td></tr>
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
| <CopyableCode code="merges_url" /> | `string` |  |
| <CopyableCode code="milestones_url" /> | `string` |  |
| <CopyableCode code="mirror_url" /> | `string` |  |
| <CopyableCode code="network_count" /> | `integer` |  |
| <CopyableCode code="node_id" /> | `string` |  |
| <CopyableCode code="notifications_url" /> | `string` |  |
| <CopyableCode code="open_issues" /> | `integer` |  |
| <CopyableCode code="open_issues_count" /> | `integer` |  |
| <CopyableCode code="owner" /> | `object` | A GitHub user. |
| <CopyableCode code="permissions" /> | `object` |  |
| <CopyableCode code="private" /> | `boolean` | Whether the repository is private or public. |
| <CopyableCode code="pulls_url" /> | `string` |  |
| <CopyableCode code="pushed_at" /> | `string` |  |
| <CopyableCode code="releases_url" /> | `string` |  |
| <CopyableCode code="role_name" /> | `string` |  |
| <CopyableCode code="size" /> | `integer` |  |
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
| <CopyableCode code="visibility" /> | `string` | The repository visibility: public, private, or internal. |
| <CopyableCode code="watchers" /> | `integer` |  |
| <CopyableCode code="watchers_count" /> | `integer` |  |
| <CopyableCode code="web_commit_signoff_required" /> | `boolean` | Whether to require contributors to sign off on web-based commits |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="check_permissions_for_repo_in_org" /> | `SELECT` | <CopyableCode code="org, owner, repo, team_slug" /> | Checks whether a team has `admin`, `push`, `maintain`, `triage`, or `pull` permission for a repository. Repositories inherited through a parent team will also be checked.<br /><br />You can also get information about the specified repository, including what permissions the team grants on it, by passing the following custom [media type](https://docs.github.com/rest/overview/media-types/) via the `application/vnd.github.v3.repository+json` accept header.<br /><br />If a team doesn't have permission for the repository, you will receive a `404 Not Found` response status.<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/&#123;org_id&#125;/team/&#123;team_id&#125;/repos/&#123;owner&#125;/&#123;repo&#125;`. |
| <CopyableCode code="check_permissions_for_repo_legacy" /> | `SELECT` | <CopyableCode code="owner, repo, team_id" /> | **Note**: Repositories inherited through a parent team will also be checked.<br /><br />**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Check team permissions for a repository](https://docs.github.com/rest/teams/teams#check-team-permissions-for-a-repository) endpoint.<br /><br />You can also get information about the specified repository, including what permissions the team grants on it, by passing the following custom [media type](https://docs.github.com/rest/overview/media-types/) via the `Accept` header: |
| <CopyableCode code="add_or_update_repo_permissions_in_org" /> | `EXEC` | <CopyableCode code="org, owner, repo, team_slug" /> | To add a repository to a team or update the team's permission on a repository, the authenticated user must have admin access to the repository, and must be able to see the team. The repository must be owned by the organization, or a direct fork of a repository owned by the organization. You will get a `422 Unprocessable Entity` status if you attempt to add a repository to a team that is not owned by the organization. Note that, if you choose not to pass any parameters, you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/rest/overview/resources-in-the-rest-api#http-verbs)."<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `PUT /organizations/&#123;org_id&#125;/team/&#123;team_id&#125;/repos/&#123;owner&#125;/&#123;repo&#125;`.<br /><br />For more information about the permission levels, see "[Repository permission levels for an organization](https://docs.github.com/github/setting-up-and-managing-organizations-and-teams/repository-permission-levels-for-an-organization#permission-levels-for-repositories-owned-by-an-organization)". |
| <CopyableCode code="add_or_update_repo_permissions_legacy" /> | `EXEC` | <CopyableCode code="owner, repo, team_id" /> | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new "[Add or update team repository permissions](https://docs.github.com/rest/teams/teams#add-or-update-team-repository-permissions)" endpoint.<br /><br />To add a repository to a team or update the team's permission on a repository, the authenticated user must have admin access to the repository, and must be able to see the team. The repository must be owned by the organization, or a direct fork of a repository owned by the organization. You will get a `422 Unprocessable Entity` status if you attempt to add a repository to a team that is not owned by the organization.<br /><br />Note that, if you choose not to pass any parameters, you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/rest/overview/resources-in-the-rest-api#http-verbs)." |
