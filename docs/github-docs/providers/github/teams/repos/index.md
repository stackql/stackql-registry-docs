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
| `license` | `object` |  |
| `role_name` | `string` |  |
| `allow_forking` | `boolean` |  |
| `mirror_url` | `string` |  |
| `collaborators_url` | `string` |  |
| `fork` | `boolean` |  |
| `branches_url` | `string` |  |
| `statuses_url` | `string` |  |
| `git_url` | `string` |  |
| `comments_url` | `string` |  |
| `stargazers_url` | `string` |  |
| `tags_url` | `string` |  |
| `node_id` | `string` |  |
| `is_template` | `boolean` |  |
| `archived` | `boolean` |  |
| `commits_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `forks_url` | `string` |  |
| `forks_count` | `integer` |  |
| `owner` | `object` | A GitHub user. |
| `delete_branch_on_merge` | `boolean` |  |
| `pulls_url` | `string` |  |
| `updated_at` | `string` |  |
| `subscribers_url` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `keys_url` | `string` |  |
| `downloads_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `archive_url` | `string` |  |
| `milestones_url` | `string` |  |
| `contents_url` | `string` |  |
| `teams_url` | `string` |  |
| `permissions` | `object` |  |
| `languages_url` | `string` |  |
| `watchers` | `integer` |  |
| `url` | `string` |  |
| `html_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `notifications_url` | `string` |  |
| `deployments_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `svn_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `git_commits_url` | `string` |  |
| `private` | `boolean` |  |
| `web_commit_signoff_required` | `boolean` |  |
| `git_refs_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `pushed_at` | `string` |  |
| `default_branch` | `string` |  |
| `security_and_analysis` | `object` |  |
| `homepage` | `string` |  |
| `trees_url` | `string` |  |
| `releases_url` | `string` |  |
| `clone_url` | `string` |  |
| `contributors_url` | `string` |  |
| `subscription_url` | `string` |  |
| `has_discussions` | `boolean` |  |
| `temp_clone_token` | `string` |  |
| `ssh_url` | `string` |  |
| `open_issues` | `integer` |  |
| `full_name` | `string` |  |
| `language` | `string` |  |
| `compare_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `blobs_url` | `string` |  |
| `size` | `integer` | The size of the repository. Size is calculated hourly. When a repository is initially created, the size is 0. |
| `has_pages` | `boolean` |  |
| `created_at` | `string` |  |
| `open_issues_count` | `integer` |  |
| `events_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `disabled` | `boolean` |  |
| `issue_comment_url` | `string` |  |
| `hooks_url` | `string` |  |
| `topics` | `array` |  |
| `visibility` | `string` |  |
| `has_issues` | `boolean` |  |
| `assignees_url` | `string` |  |
| `forks` | `integer` |  |
| `merges_url` | `string` |  |
| `network_count` | `integer` |  |
| `labels_url` | `string` |  |
| `issues_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_repos_in_org` | `SELECT` | `org, team_slug` | Lists a team's repositories visible to the authenticated user.<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/&#123;org_id&#125;/team/&#123;team_id&#125;/repos`. |
| `list_repos_legacy` | `SELECT` | `team_id` | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [List team repositories](https://docs.github.com/rest/teams/teams#list-team-repositories) endpoint. |
| `remove_repo_in_org` | `DELETE` | `org, owner, repo, team_slug` | If the authenticated user is an organization owner or a team maintainer, they can remove any repositories from the team. To remove a repository from a team as an organization member, the authenticated user must have admin access to the repository and must be able to see the team. This does not delete the repository, it just removes it from the team.<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `DELETE /organizations/&#123;org_id&#125;/team/&#123;team_id&#125;/repos/&#123;owner&#125;/&#123;repo&#125;`. |
| `remove_repo_legacy` | `EXEC` | `owner, repo, team_id` | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Remove a repository from a team](https://docs.github.com/rest/teams/teams#remove-a-repository-from-a-team) endpoint.<br /><br />If the authenticated user is an organization owner or a team maintainer, they can remove any repositories from the team. To remove a repository from a team as an organization member, the authenticated user must have admin access to the repository and must be able to see the team. NOTE: This does not delete the repository, it just removes it from the team. |
