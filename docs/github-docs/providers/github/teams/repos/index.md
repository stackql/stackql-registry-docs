---
title: repos
hide_title: false
hide_table_of_contents: false
keywords:
  - repos
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
<tr><td><b>Name</b></td><td><code>repos</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.teams.repos</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `allow_forking` | `boolean` |  |
| `mirror_url` | `string` |  |
| `trees_url` | `string` |  |
| `teams_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `has_wiki` | `boolean` |  |
| `contents_url` | `string` |  |
| `deployments_url` | `string` |  |
| `releases_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `subscription_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `tags_url` | `string` |  |
| `url` | `string` |  |
| `git_refs_url` | `string` |  |
| `svn_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `commits_url` | `string` |  |
| `labels_url` | `string` |  |
| `clone_url` | `string` |  |
| `owner` | `object` | A GitHub user. |
| `has_discussions` | `boolean` |  |
| `html_url` | `string` |  |
| `archive_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `compare_url` | `string` |  |
| `git_url` | `string` |  |
| `keys_url` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `disabled` | `boolean` |  |
| `stargazers_url` | `string` |  |
| `open_issues` | `integer` |  |
| `private` | `boolean` |  |
| `network_count` | `integer` |  |
| `role_name` | `string` |  |
| `updated_at` | `string` |  |
| `size` | `integer` | The size of the repository. Size is calculated hourly. When a repository is initially created, the size is 0. |
| `stargazers_count` | `integer` |  |
| `blobs_url` | `string` |  |
| `assignees_url` | `string` |  |
| `language` | `string` |  |
| `full_name` | `string` |  |
| `node_id` | `string` |  |
| `issue_comment_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `security_and_analysis` | `object` |  |
| `branches_url` | `string` |  |
| `events_url` | `string` |  |
| `forks_count` | `integer` |  |
| `ssh_url` | `string` |  |
| `issues_url` | `string` |  |
| `archived` | `boolean` |  |
| `git_commits_url` | `string` |  |
| `merges_url` | `string` |  |
| `forks_url` | `string` |  |
| `permissions` | `object` |  |
| `milestones_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `topics` | `array` |  |
| `issue_events_url` | `string` |  |
| `forks` | `integer` |  |
| `hooks_url` | `string` |  |
| `statuses_url` | `string` |  |
| `visibility` | `string` |  |
| `collaborators_url` | `string` |  |
| `is_template` | `boolean` |  |
| `license` | `object` |  |
| `default_branch` | `string` |  |
| `comments_url` | `string` |  |
| `languages_url` | `string` |  |
| `watchers` | `integer` |  |
| `web_commit_signoff_required` | `boolean` |  |
| `contributors_url` | `string` |  |
| `fork` | `boolean` |  |
| `has_issues` | `boolean` |  |
| `created_at` | `string` |  |
| `downloads_url` | `string` |  |
| `homepage` | `string` |  |
| `subscribers_url` | `string` |  |
| `pushed_at` | `string` |  |
| `notifications_url` | `string` |  |
| `pulls_url` | `string` |  |
| `has_projects` | `boolean` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_repos_legacy` | `SELECT` | `team_id` | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [List team repositories](https://docs.github.com/rest/teams/teams#list-team-repositories) endpoint. |
| `remove_repo_legacy` | `DELETE` | `owner, repo, team_id` | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Remove a repository from a team](https://docs.github.com/rest/teams/teams#remove-a-repository-from-a-team) endpoint.<br /><br />If the authenticated user is an organization owner or a team maintainer, they can remove any repositories from the team. To remove a repository from a team as an organization member, the authenticated user must have admin access to the repository and must be able to see the team. NOTE: This does not delete the repository, it just removes it from the team. |
| `add_or_update_repo_permissions_legacy` | `EXEC` | `owner, repo, team_id` | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new "[Add or update team repository permissions](https://docs.github.com/rest/teams/teams#add-or-update-team-repository-permissions)" endpoint.<br /><br />To add a repository to a team or update the team's permission on a repository, the authenticated user must have admin access to the repository, and must be able to see the team. The repository must be owned by the organization, or a direct fork of a repository owned by the organization. You will get a `422 Unprocessable Entity` status if you attempt to add a repository to a team that is not owned by the organization.<br /><br />Note that, if you choose not to pass any parameters, you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/rest/overview/resources-in-the-rest-api#http-verbs)." |
| `check_permissions_for_repo_legacy` | `EXEC` | `owner, repo, team_id` | **Note**: Repositories inherited through a parent team will also be checked.<br /><br />**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Check team permissions for a repository](https://docs.github.com/rest/teams/teams#check-team-permissions-for-a-repository) endpoint.<br /><br />You can also get information about the specified repository, including what permissions the team grants on it, by passing the following custom [media type](https://docs.github.com/rest/overview/media-types/) via the `Accept` header: |
