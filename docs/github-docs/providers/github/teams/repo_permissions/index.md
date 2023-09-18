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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>repo_permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.teams.repo_permissions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | Unique identifier of the repository |
| `name` | `string` | The name of the repository. |
| `description` | `string` |  |
| `svn_url` | `string` |  |
| `allow_auto_merge` | `boolean` | Whether to allow Auto-merge to be used on pull requests. |
| `watchers_count` | `integer` |  |
| `collaborators_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `comments_url` | `string` |  |
| `deployments_url` | `string` |  |
| `is_template` | `boolean` | Whether this repository acts as a template that can be used to generate new repositories. |
| `size` | `integer` |  |
| `teams_url` | `string` |  |
| `owner` | `object` | A GitHub user. |
| `git_tags_url` | `string` |  |
| `merges_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` | Whether to delete head branches when pull requests are merged |
| `template_repository` | `object` | A repository on GitHub. |
| `issues_url` | `string` |  |
| `branches_url` | `string` |  |
| `permissions` | `object` |  |
| `trees_url` | `string` |  |
| `allow_merge_commit` | `boolean` | Whether to allow merge commits for pull requests. |
| `language` | `string` |  |
| `stargazers_count` | `integer` |  |
| `milestones_url` | `string` |  |
| `forks_count` | `integer` |  |
| `has_issues` | `boolean` | Whether issues are enabled. |
| `languages_url` | `string` |  |
| `events_url` | `string` |  |
| `default_branch` | `string` | The default branch of the repository. |
| `full_name` | `string` |  |
| `web_commit_signoff_required` | `boolean` | Whether to require contributors to sign off on web-based commits |
| `updated_at` | `string` |  |
| `contents_url` | `string` |  |
| `labels_url` | `string` |  |
| `pulls_url` | `string` |  |
| `role_name` | `string` |  |
| `pushed_at` | `string` |  |
| `clone_url` | `string` |  |
| `statuses_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `forks_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `contributors_url` | `string` |  |
| `blobs_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `subscription_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `homepage` | `string` |  |
| `allow_forking` | `boolean` | Whether to allow forking this repo |
| `downloads_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `releases_url` | `string` |  |
| `forks` | `integer` |  |
| `notifications_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `has_downloads` | `boolean` | Whether downloads are enabled. |
| `license` | `object` | License Simple |
| `archive_url` | `string` |  |
| `private` | `boolean` | Whether the repository is private or public. |
| `fork` | `boolean` |  |
| `keys_url` | `string` |  |
| `has_projects` | `boolean` | Whether projects are enabled. |
| `allow_squash_merge` | `boolean` | Whether to allow squash merges for pull requests. |
| `assignees_url` | `string` |  |
| `url` | `string` |  |
| `master_branch` | `string` |  |
| `node_id` | `string` |  |
| `git_url` | `string` |  |
| `ssh_url` | `string` |  |
| `allow_rebase_merge` | `boolean` | Whether to allow rebase merges for pull requests. |
| `has_pages` | `boolean` |  |
| `network_count` | `integer` |  |
| `tags_url` | `string` |  |
| `archived` | `boolean` | Whether the repository is archived. |
| `visibility` | `string` | The repository visibility: public, private, or internal. |
| `created_at` | `string` |  |
| `temp_clone_token` | `string` |  |
| `has_wiki` | `boolean` | Whether the wiki is enabled. |
| `watchers` | `integer` |  |
| `hooks_url` | `string` |  |
| `topics` | `array` |  |
| `open_issues` | `integer` |  |
| `html_url` | `string` |  |
| `compare_url` | `string` |  |
| `disabled` | `boolean` | Returns whether or not this repository disabled. |
| `mirror_url` | `string` |  |
| `commits_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `check_permissions_for_repo_in_org` | `SELECT` | `org, owner, repo, team_slug` | Checks whether a team has `admin`, `push`, `maintain`, `triage`, or `pull` permission for a repository. Repositories inherited through a parent team will also be checked.<br /><br />You can also get information about the specified repository, including what permissions the team grants on it, by passing the following custom [media type](https://docs.github.com/rest/overview/media-types/) via the `application/vnd.github.v3.repository+json` accept header.<br /><br />If a team doesn't have permission for the repository, you will receive a `404 Not Found` response status.<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/&#123;org_id&#125;/team/&#123;team_id&#125;/repos/&#123;owner&#125;/&#123;repo&#125;`. |
| `check_permissions_for_repo_legacy` | `SELECT` | `owner, repo, team_id` | **Note**: Repositories inherited through a parent team will also be checked.<br /><br />**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Check team permissions for a repository](https://docs.github.com/rest/teams/teams#check-team-permissions-for-a-repository) endpoint.<br /><br />You can also get information about the specified repository, including what permissions the team grants on it, by passing the following custom [media type](https://docs.github.com/rest/overview/media-types/) via the `Accept` header: |
| `add_or_update_repo_permissions_in_org` | `EXEC` | `org, owner, repo, team_slug` | To add a repository to a team or update the team's permission on a repository, the authenticated user must have admin access to the repository, and must be able to see the team. The repository must be owned by the organization, or a direct fork of a repository owned by the organization. You will get a `422 Unprocessable Entity` status if you attempt to add a repository to a team that is not owned by the organization. Note that, if you choose not to pass any parameters, you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/rest/overview/resources-in-the-rest-api#http-verbs)."<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `PUT /organizations/&#123;org_id&#125;/team/&#123;team_id&#125;/repos/&#123;owner&#125;/&#123;repo&#125;`.<br /><br />For more information about the permission levels, see "[Repository permission levels for an organization](https://docs.github.com/github/setting-up-and-managing-organizations-and-teams/repository-permission-levels-for-an-organization#permission-levels-for-repositories-owned-by-an-organization)". |
| `add_or_update_repo_permissions_legacy` | `EXEC` | `owner, repo, team_id` | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new "[Add or update team repository permissions](https://docs.github.com/rest/teams/teams#add-or-update-team-repository-permissions)" endpoint.<br /><br />To add a repository to a team or update the team's permission on a repository, the authenticated user must have admin access to the repository, and must be able to see the team. The repository must be owned by the organization, or a direct fork of a repository owned by the organization. You will get a `422 Unprocessable Entity` status if you attempt to add a repository to a team that is not owned by the organization.<br /><br />Note that, if you choose not to pass any parameters, you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/rest/overview/resources-in-the-rest-api#http-verbs)." |
