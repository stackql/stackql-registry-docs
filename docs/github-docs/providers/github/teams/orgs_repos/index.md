---
title: orgs_repos
hide_title: false
hide_table_of_contents: false
keywords:
  - orgs_repos
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
<tr><td><b>Name</b></td><td><code>orgs_repos</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.teams.orgs_repos</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `web_commit_signoff_required` | `boolean` |  |
| `permissions` | `object` |  |
| `branches_url` | `string` |  |
| `size` | `integer` | The size of the repository. Size is calculated hourly. When a repository is initially created, the size is 0. |
| `mirror_url` | `string` |  |
| `releases_url` | `string` |  |
| `svn_url` | `string` |  |
| `trees_url` | `string` |  |
| `git_url` | `string` |  |
| `downloads_url` | `string` |  |
| `merges_url` | `string` |  |
| `notifications_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `has_pages` | `boolean` |  |
| `forks` | `integer` |  |
| `watchers` | `integer` |  |
| `tags_url` | `string` |  |
| `updated_at` | `string` |  |
| `network_count` | `integer` |  |
| `license` | `object` |  |
| `comments_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `languages_url` | `string` |  |
| `topics` | `array` |  |
| `has_projects` | `boolean` |  |
| `open_issues` | `integer` |  |
| `issue_events_url` | `string` |  |
| `visibility` | `string` |  |
| `private` | `boolean` |  |
| `role_name` | `string` |  |
| `watchers_count` | `integer` |  |
| `contributors_url` | `string` |  |
| `forks_url` | `string` |  |
| `statuses_url` | `string` |  |
| `hooks_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `labels_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `forks_count` | `integer` |  |
| `deployments_url` | `string` |  |
| `assignees_url` | `string` |  |
| `contents_url` | `string` |  |
| `subscribers_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `homepage` | `string` |  |
| `open_issues_count` | `integer` |  |
| `git_tags_url` | `string` |  |
| `language` | `string` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `security_and_analysis` | `object` |  |
| `milestones_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `subscription_url` | `string` |  |
| `has_discussions` | `boolean` |  |
| `full_name` | `string` |  |
| `keys_url` | `string` |  |
| `disabled` | `boolean` |  |
| `fork` | `boolean` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `url` | `string` |  |
| `archive_url` | `string` |  |
| `commits_url` | `string` |  |
| `html_url` | `string` |  |
| `issues_url` | `string` |  |
| `archived` | `boolean` |  |
| `stargazers_url` | `string` |  |
| `events_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `owner` | `object` | A GitHub user. |
| `blobs_url` | `string` |  |
| `is_template` | `boolean` |  |
| `clone_url` | `string` |  |
| `pulls_url` | `string` |  |
| `ssh_url` | `string` |  |
| `node_id` | `string` |  |
| `collaborators_url` | `string` |  |
| `default_branch` | `string` |  |
| `git_refs_url` | `string` |  |
| `teams_url` | `string` |  |
| `pushed_at` | `string` |  |
| `stargazers_count` | `integer` |  |
| `created_at` | `string` |  |
| `compare_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_repos_in_org` | `SELECT` | `org, team_slug` | Lists a team's repositories visible to the authenticated user.<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/&#123;org_id&#125;/team/&#123;team_id&#125;/repos`. |
| `remove_repo_in_org` | `DELETE` | `org, owner, repo, team_slug` | If the authenticated user is an organization owner or a team maintainer, they can remove any repositories from the team. To remove a repository from a team as an organization member, the authenticated user must have admin access to the repository and must be able to see the team. This does not delete the repository, it just removes it from the team.<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `DELETE /organizations/&#123;org_id&#125;/team/&#123;team_id&#125;/repos/&#123;owner&#125;/&#123;repo&#125;`. |
| `add_or_update_repo_permissions_in_org` | `EXEC` | `org, owner, repo, team_slug` | To add a repository to a team or update the team's permission on a repository, the authenticated user must have admin access to the repository, and must be able to see the team. The repository must be owned by the organization, or a direct fork of a repository owned by the organization. You will get a `422 Unprocessable Entity` status if you attempt to add a repository to a team that is not owned by the organization. Note that, if you choose not to pass any parameters, you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/rest/overview/resources-in-the-rest-api#http-verbs)."<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `PUT /organizations/&#123;org_id&#125;/team/&#123;team_id&#125;/repos/&#123;owner&#125;/&#123;repo&#125;`.<br /><br />For more information about the permission levels, see "[Repository permission levels for an organization](https://docs.github.com/github/setting-up-and-managing-organizations-and-teams/repository-permission-levels-for-an-organization#permission-levels-for-repositories-owned-by-an-organization)". |
| `check_permissions_for_repo_in_org` | `EXEC` | `org, owner, repo, team_slug` | Checks whether a team has `admin`, `push`, `maintain`, `triage`, or `pull` permission for a repository. Repositories inherited through a parent team will also be checked.<br /><br />You can also get information about the specified repository, including what permissions the team grants on it, by passing the following custom [media type](https://docs.github.com/rest/overview/media-types/) via the `application/vnd.github.v3.repository+json` accept header.<br /><br />If a team doesn't have permission for the repository, you will receive a `404 Not Found` response status.<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/&#123;org_id&#125;/team/&#123;team_id&#125;/repos/&#123;owner&#125;/&#123;repo&#125;`. |
