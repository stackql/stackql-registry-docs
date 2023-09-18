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
| `contributors_url` | `string` |  |
| `code_of_conduct` | `object` | Code Of Conduct |
| `size` | `integer` | The size of the repository. Size is calculated hourly. When a repository is initially created, the size is 0. |
| `open_issues` | `integer` |  |
| `pulls_url` | `string` |  |
| `assignees_url` | `string` |  |
| `git_tags_url` | `string` |  |
| `private` | `boolean` |  |
| `has_issues` | `boolean` |  |
| `git_url` | `string` |  |
| `subscribers_count` | `integer` |  |
| `git_commits_url` | `string` |  |
| `issues_url` | `string` |  |
| `branches_url` | `string` |  |
| `license` | `object` |  |
| `open_issues_count` | `integer` |  |
| `topics` | `array` |  |
| `hooks_url` | `string` |  |
| `stargazers_count` | `integer` |  |
| `languages_url` | `string` |  |
| `forks_url` | `string` |  |
| `url` | `string` |  |
| `security_and_analysis` | `object` |  |
| `labels_url` | `string` |  |
| `disabled` | `boolean` |  |
| `milestones_url` | `string` |  |
| `network_count` | `integer` |  |
| `role_name` | `string` |  |
| `node_id` | `string` |  |
| `fork` | `boolean` |  |
| `trees_url` | `string` |  |
| `releases_url` | `string` |  |
| `default_branch` | `string` |  |
| `tags_url` | `string` |  |
| `events_url` | `string` |  |
| `temp_clone_token` | `string` |  |
| `notifications_url` | `string` |  |
| `has_wiki` | `boolean` |  |
| `mirror_url` | `string` |  |
| `issue_comment_url` | `string` |  |
| `merges_url` | `string` |  |
| `watchers` | `integer` |  |
| `allow_forking` | `boolean` |  |
| `pushed_at` | `string` |  |
| `subscribers_url` | `string` |  |
| `has_downloads` | `boolean` |  |
| `comments_url` | `string` |  |
| `visibility` | `string` |  |
| `web_commit_signoff_required` | `boolean` |  |
| `forks` | `integer` |  |
| `homepage` | `string` |  |
| `permissions` | `object` |  |
| `delete_branch_on_merge` | `boolean` |  |
| `owner` | `object` | A GitHub user. |
| `archive_url` | `string` |  |
| `full_name` | `string` |  |
| `updated_at` | `string` |  |
| `archived` | `boolean` |  |
| `clone_url` | `string` |  |
| `teams_url` | `string` |  |
| `statuses_url` | `string` |  |
| `downloads_url` | `string` |  |
| `contents_url` | `string` |  |
| `ssh_url` | `string` |  |
| `svn_url` | `string` |  |
| `commits_url` | `string` |  |
| `has_pages` | `boolean` |  |
| `blobs_url` | `string` |  |
| `subscription_url` | `string` |  |
| `has_projects` | `boolean` |  |
| `stargazers_url` | `string` |  |
| `html_url` | `string` |  |
| `created_at` | `string` |  |
| `has_discussions` | `boolean` |  |
| `collaborators_url` | `string` |  |
| `deployments_url` | `string` |  |
| `git_refs_url` | `string` |  |
| `language` | `string` |  |
| `keys_url` | `string` |  |
| `issue_events_url` | `string` |  |
| `watchers_count` | `integer` |  |
| `forks_count` | `integer` |  |
| `compare_url` | `string` |  |
| `is_template` | `boolean` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_repos_in_org` | `SELECT` | `org, team_slug` | Lists a team's repositories visible to the authenticated user.<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/&#123;org_id&#125;/team/&#123;team_id&#125;/repos`. |
| `list_repos_legacy` | `SELECT` | `team_id` | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [List team repositories](https://docs.github.com/rest/teams/teams#list-team-repositories) endpoint. |
| `remove_repo_in_org` | `DELETE` | `org, owner, repo, team_slug` | If the authenticated user is an organization owner or a team maintainer, they can remove any repositories from the team. To remove a repository from a team as an organization member, the authenticated user must have admin access to the repository and must be able to see the team. This does not delete the repository, it just removes it from the team.<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `DELETE /organizations/&#123;org_id&#125;/team/&#123;team_id&#125;/repos/&#123;owner&#125;/&#123;repo&#125;`. |
| `remove_repo_legacy` | `EXEC` | `owner, repo, team_id` | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Remove a repository from a team](https://docs.github.com/rest/teams/teams#remove-a-repository-from-a-team) endpoint.<br /><br />If the authenticated user is an organization owner or a team maintainer, they can remove any repositories from the team. To remove a repository from a team as an organization member, the authenticated user must have admin access to the repository and must be able to see the team. NOTE: This does not delete the repository, it just removes it from the team. |
