---
title: legacy_repos
hide_title: false
hide_table_of_contents: false
keywords:
  - legacy_repos
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
<tr><td><b>Name</b></td><td><code>legacy_repos</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.teams.legacy_repos</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `compare_url` | `string` |  |
| `releases_url` | `string` |  |
| `topics` | `array` |  |
| `subscribers_count` | `integer` |  |
| `issue_comment_url` | `string` |  |
| `forks_count` | `integer` |  |
| `temp_clone_token` | `string` |  |
| `archived` | `boolean` |  |
| `watchers` | `integer` |  |
| `stargazers_count` | `integer` |  |
| `milestones_url` | `string` |  |
| `subscription_url` | `string` |  |
| `fork` | `boolean` |  |
| `has_projects` | `boolean` |  |
| `svn_url` | `string` |  |
| `contents_url` | `string` |  |
| `trees_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `downloads_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `keys_url` | `string` |  |
| `branches_url` | `string` |  |
| `languages_url` | `string` |  |
| `template_repository` | `object` | A git repository |
| `pushed_at` | `string` |  |
| `blobs_url` | `string` |  |
| `node_id` | `string` |  |
| `assignees_url` | `string` |  |
| `language` | `string` |  |
| `deployments_url` | `string` |  |
| `network_count` | `integer` |  |
| `git_refs_url` | `string` |  |
| `notifications_url` | `string` |  |
| `issues_url` | `string` |  |
| `disabled` | `boolean` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `html_url` | `string` |  |
| `created_at` | `string` |  |
| `default_branch` | `string` |  |
| `stargazers_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `events_url` | `string` |  |
| `url` | `string` |  |
| `comments_url` | `string` |  |
| `visibility` | `string` |  |
| `collaborators_url` | `string` |  |
| `size` | `integer` |  |
| `forks_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `watchers_count` | `integer` |  |
| `merges_url` | `string` |  |
| `tags_url` | `string` |  |
| `updated_at` | `string` |  |
| `permissions` | `object` |  |
| `role_name` | `string` |  |
| `teams_url` | `string` |  |
| `clone_url` | `string` |  |
| `contributors_url` | `string` |  |
| `private` | `boolean` |  |
| `git_url` | `string` |  |
| `mirror_url` | `string` |  |
| `full_name` | `string` |  |
| `commits_url` | `string` |  |
| `statuses_url` | `string` |  |
| `is_template` | `boolean` |  |
| `homepage` | `string` |  |
| `open_issues` | `integer` |  |
| `pulls_url` | `string` |  |
| `ssh_url` | `string` |  |
| `hooks_url` | `string` |  |
| `license` | `object` |  |
| `forks` | `integer` |  |
| `owner` | `object` | Simple User |
| `labels_url` | `string` |  |
| `archive_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `open_issues_count` | `integer` |  |
| `has_pages` | `boolean` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_repos_legacy` | `SELECT` | `team_id` | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [List team repositories](https://docs.github.com/rest/reference/teams#list-team-repositories) endpoint. |
| `remove_repo_legacy` | `DELETE` | `owner, repo, team_id` | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Remove a repository from a team](https://docs.github.com/rest/reference/teams#remove-a-repository-from-a-team) endpoint.<br /><br />If the authenticated user is an organization owner or a team maintainer, they can remove any repositories from the team. To remove a repository from a team as an organization member, the authenticated user must have admin access to the repository and must be able to see the team. NOTE: This does not delete the repository, it just removes it from the team. |
| `add_or_update_repo_permissions_legacy` | `EXEC` | `owner, repo, team_id` | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new "[Add or update team repository permissions](https://docs.github.com/rest/reference/teams#add-or-update-team-repository-permissions)" endpoint.<br /><br />To add a repository to a team or update the team's permission on a repository, the authenticated user must have admin access to the repository, and must be able to see the team. The repository must be owned by the organization, or a direct fork of a repository owned by the organization. You will get a `422 Unprocessable Entity` status if you attempt to add a repository to a team that is not owned by the organization.<br /><br />Note that, if you choose not to pass any parameters, you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/rest/overview/resources-in-the-rest-api#http-verbs)." |
| `check_permissions_for_repo_legacy` | `EXEC` | `owner, repo, team_id` | **Note**: Repositories inherited through a parent team will also be checked.<br /><br />**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Check team permissions for a repository](https://docs.github.com/rest/reference/teams#check-team-permissions-for-a-repository) endpoint.<br /><br />You can also get information about the specified repository, including what permissions the team grants on it, by passing the following custom [media type](https://docs.github.com/rest/overview/media-types/) via the `Accept` header: |
