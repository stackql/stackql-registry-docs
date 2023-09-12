---
title: orgs_discussions_comments
hide_title: false
hide_table_of_contents: false
keywords:
  - orgs_discussions_comments
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
<tr><td><b>Name</b></td><td><code>orgs_discussions_comments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.teams.orgs_discussions_comments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `updated_at` | `string` |  |
| `node_id` | `string` |  |
| `last_edited_at` | `string` |  |
| `reactions` | `object` |  |
| `discussion_url` | `string` |  |
| `body` | `string` | The main text of the comment. |
| `number` | `integer` | The unique sequence number of a team discussion comment. |
| `body_version` | `string` | The current version of the body content. If provided, this update operation will be rejected if the given version does not match the latest version on the server. |
| `body_html` | `string` |  |
| `created_at` | `string` |  |
| `html_url` | `string` |  |
| `url` | `string` |  |
| `author` | `object` | A GitHub user. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_discussion_comment_in_org` | `SELECT` | `comment_number, discussion_number, org, team_slug` | Get a specific comment on a team discussion. OAuth access tokens require the `read:discussion` [scope](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/&#123;org_id&#125;/team/&#123;team_id&#125;/discussions/&#123;discussion_number&#125;/comments/&#123;comment_number&#125;`. |
| `list_discussion_comments_in_org` | `SELECT` | `discussion_number, org, team_slug` | List all comments on a team discussion. OAuth access tokens require the `read:discussion` [scope](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/&#123;org_id&#125;/team/&#123;team_id&#125;/discussions/&#123;discussion_number&#125;/comments`. |
| `create_discussion_comment_in_org` | `INSERT` | `discussion_number, org, team_slug, data__body` | Creates a new comment on a team discussion. OAuth access tokens require the `write:discussion` [scope](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).<br /><br />This endpoint triggers [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See "[Secondary rate limits](https://docs.github.com/rest/overview/resources-in-the-rest-api#secondary-rate-limits)" and "[Dealing with secondary rate limits](https://docs.github.com/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)" for details.<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `POST /organizations/&#123;org_id&#125;/team/&#123;team_id&#125;/discussions/&#123;discussion_number&#125;/comments`. |
| `delete_discussion_comment_in_org` | `DELETE` | `comment_number, discussion_number, org, team_slug` | Deletes a comment on a team discussion. OAuth access tokens require the `write:discussion` [scope](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `DELETE /organizations/&#123;org_id&#125;/team/&#123;team_id&#125;/discussions/&#123;discussion_number&#125;/comments/&#123;comment_number&#125;`. |
| `update_discussion_comment_in_org` | `EXEC` | `comment_number, discussion_number, org, team_slug, data__body` | Edits the body text of a discussion comment. OAuth access tokens require the `write:discussion` [scope](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `PATCH /organizations/&#123;org_id&#125;/team/&#123;team_id&#125;/discussions/&#123;discussion_number&#125;/comments/&#123;comment_number&#125;`. |
