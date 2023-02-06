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
| `keys_url` | `string` |  |
| `created_at` | `string` |  |
| `issue_comment_url` | `string` |  |
| `trees_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `full_name` | `string` |  |
| `subscribers_url` | `string` |  |
| `topics` | `array` |  |
| `forks` | `integer` |  |
| `merges_url` | `string` |  |
| `releases_url` | `string` |  |
| `contents_url` | `string` |  |
| `network_count` | `integer` |  |
| `notifications_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `git_url` | `string` |  |
| `deployments_url` | `string` |  |
| `events_url` | `string` |  |
| `languages_url` | `string` |  |
| `labels_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `owner` | `object` | Simple User |
| `downloads_url` | `string` |  |
| `git_commits_url` | `string` |  |
| `pulls_url` | `string` |  |
| `has_issues` | `boolean` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `open_issues_count` | `integer` |  |
| `assignees_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `tags_url` | `string` |  |
| `html_url` | `string` |  |
| `fork` | `boolean` |  |
| `has_pages` | `boolean` |  |
| `commits_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `language` | `string` |  |
| `mirror_url` | `string` |  |
| `archive_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `milestones_url` | `string` |  |
| `updated_at` | `string` |  |
| `disabled` | `boolean` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `has_downloads` | `boolean` |  |
| `license` | `object` |  |
| `blobs_url` | `string` |  |
| `forks_url` | `string` |  |
| `ssh_url` | `string` |  |
| `permissions` | `object` |  |
| `clone_url` | `string` |  |
| `compare_url` | `string` |  |
| `issues_url` | `string` |  |
| `private` | `boolean` |  |
| `branches_url` | `string` |  |
| `size` | `integer` |  |
| `svn_url` | `string` |  |
| `hooks_url` | `string` |  |
| `forks_count` | `integer` |  |
| `watchers_count` | `integer` |  |
| `template_repository` | `object` | A git repository |
| `watchers` | `integer` |  |
| `temp_clone_token` | `string` |  |
| `contributors_url` | `string` |  |
| `teams_url` | `string` |  |
| `is_template` | `boolean` |  |
| `default_branch` | `string` |  |
| `visibility` | `string` |  |
| `archived` | `boolean` |  |
| `role_name` | `string` |  |
| `url` | `string` |  |
| `homepage` | `string` |  |
| `open_issues` | `integer` |  |
| `subscription_url` | `string` |  |
| `allow_forking` | `boolean` |  |
| `pushed_at` | `string` |  |
| `git_refs_url` | `string` |  |
| `statuses_url` | `string` |  |
| `comments_url` | `string` |  |
| `node_id` | `string` |  |
| `stargazers_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_repos_in_org` | `SELECT` | `org, team_slug` | Lists a team's repositories visible to the authenticated user.<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/&#123;org_id&#125;/team/&#123;team_id&#125;/repos`. |
| `add_or_update_repo_permissions_in_org` | `INSERT` | `org, owner, repo, team_slug` | To add a repository to a team or update the team's permission on a repository, the authenticated user must have admin access to the repository, and must be able to see the team. The repository must be owned by the organization, or a direct fork of a repository owned by the organization. You will get a `422 Unprocessable Entity` status if you attempt to add a repository to a team that is not owned by the organization. Note that, if you choose not to pass any parameters, you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/rest/overview/resources-in-the-rest-api#http-verbs)."<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `PUT /organizations/&#123;org_id&#125;/team/&#123;team_id&#125;/repos/&#123;owner&#125;/&#123;repo&#125;`.<br /><br />For more information about the permission levels, see "[Repository permission levels for an organization](https://docs.github.com/en/github/setting-up-and-managing-organizations-and-teams/repository-permission-levels-for-an-organization#permission-levels-for-repositories-owned-by-an-organization)". |
| `remove_repo_in_org` | `DELETE` | `org, owner, repo, team_slug` | If the authenticated user is an organization owner or a team maintainer, they can remove any repositories from the team. To remove a repository from a team as an organization member, the authenticated user must have admin access to the repository and must be able to see the team. This does not delete the repository, it just removes it from the team.<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `DELETE /organizations/&#123;org_id&#125;/team/&#123;team_id&#125;/repos/&#123;owner&#125;/&#123;repo&#125;`. |
| `check_permissions_for_repo_in_org` | `EXEC` | `org, owner, repo, team_slug` | Checks whether a team has `admin`, `push`, `maintain`, `triage`, or `pull` permission for a repository. Repositories inherited through a parent team will also be checked.<br /><br />You can also get information about the specified repository, including what permissions the team grants on it, by passing the following custom [media type](https://docs.github.com/rest/overview/media-types/) via the `application/vnd.github.v3.repository+json` accept header.<br /><br />If a team doesn't have permission for the repository, you will receive a `404 Not Found` response status.<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/&#123;org_id&#125;/team/&#123;team_id&#125;/repos/&#123;owner&#125;/&#123;repo&#125;`. |
