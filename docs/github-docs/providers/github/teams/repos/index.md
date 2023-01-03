---
title: repos
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - github
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `license` | `object` |  |
| `merges_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `compare_url` | `string` |  |
| `assignees_url` | `string` |  |
| `forks_count` | `integer` |  |
| `hooks_url` | `string` |  |
| `pushed_at` | `string` |  |
| `has_issues` | `boolean` |  |
| `size` | `integer` |  |
| `archive_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `trees_url` | `string` |  |
| `default_branch` | `string` |  |
| `statuses_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `archived` | `boolean` |  |
| `language` | `string` |  |
| `pulls_url` | `string` |  |
| `template_repository` | `object` | A git repository |
| `fork` | `boolean` |  |
| `html_url` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `visibility` | `string` |  |
| `forks` | `integer` |  |
| `full_name` | `string` |  |
| `role_name` | `string` |  |
| `milestones_url` | `string` |  |
| `open_issues` | `integer` |  |
| `labels_url` | `string` |  |
| `languages_url` | `string` |  |
| `contents_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `deployments_url` | `string` |  |
| `disabled` | `boolean` |  |
| `commits_url` | `string` |  |
| `url` | `string` |  |
| `git_commits_url` | `string` |  |
| `node_id` | `string` |  |
| `keys_url` | `string` |  |
| `issues_url` | `string` |  |
| `blobs_url` | `string` |  |
| `teams_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `watchers` | `integer` |  |
| `is_template` | `boolean` |  |
| `subscription_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `releases_url` | `string` |  |
| `tags_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `owner` | `object` | Simple User |
| `forks_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `watchers_count` | `integer` |  |
| `allow_forking` | `boolean` |  |
| `events_url` | `string` |  |
| `downloads_url` | `string` |  |
| `comments_url` | `string` |  |
| `branches_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `notifications_url` | `string` |  |
| `mirror_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `permissions` | `object` |  |
| `topics` | `array` |  |
| `subscribers_count` | `integer` |  |
| `network_count` | `integer` |  |
| `contributors_url` | `string` |  |
| `git_url` | `string` |  |
| `homepage` | `string` |  |
| `created_at` | `string` |  |
| `ssh_url` | `string` |  |
| `open_issues_count` | `integer` |  |
| `issue_comment_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `clone_url` | `string` |  |
| `private` | `boolean` |  |
| `has_projects` | `boolean` |  |
| `svn_url` | `string` |  |
| `updated_at` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_repos_in_org` | `SELECT` | `org, team_slug` | Lists a team's repositories visible to the authenticated user.<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/repos`. |
| `add_or_update_repo_permissions_in_org` | `INSERT` | `org, owner, repo, team_slug` | To add a repository to a team or update the team's permission on a repository, the authenticated user must have admin access to the repository, and must be able to see the team. The repository must be owned by the organization, or a direct fork of a repository owned by the organization. You will get a `422 Unprocessable Entity` status if you attempt to add a repository to a team that is not owned by the organization. Note that, if you choose not to pass any parameters, you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/rest/overview/resources-in-the-rest-api#http-verbs)."<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `PUT /organizations/{org_id}/team/{team_id}/repos/{owner}/{repo}`.<br /><br />For more information about the permission levels, see "[Repository permission levels for an organization](https://docs.github.com/en/github/setting-up-and-managing-organizations-and-teams/repository-permission-levels-for-an-organization#permission-levels-for-repositories-owned-by-an-organization)". |
| `remove_repo_in_org` | `DELETE` | `org, owner, repo, team_slug` | If the authenticated user is an organization owner or a team maintainer, they can remove any repositories from the team. To remove a repository from a team as an organization member, the authenticated user must have admin access to the repository and must be able to see the team. This does not delete the repository, it just removes it from the team.<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `DELETE /organizations/{org_id}/team/{team_id}/repos/{owner}/{repo}`. |
| `check_permissions_for_repo_in_org` | `EXEC` | `org, owner, repo, team_slug` | Checks whether a team has `admin`, `push`, `maintain`, `triage`, or `pull` permission for a repository. Repositories inherited through a parent team will also be checked.<br /><br />You can also get information about the specified repository, including what permissions the team grants on it, by passing the following custom [media type](https://docs.github.com/rest/overview/media-types/) via the `application/vnd.github.v3.repository+json` accept header.<br /><br />If a team doesn't have permission for the repository, you will receive a `404 Not Found` response status.<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/repos/{owner}/{repo}`. |
