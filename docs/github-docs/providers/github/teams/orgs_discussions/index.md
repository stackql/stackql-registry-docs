---
title: orgs_discussions
hide_title: false
hide_table_of_contents: false
keywords:
  - orgs_discussions
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
<tr><td><b>Name</b></td><td><code>orgs_discussions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.teams.orgs_discussions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `body` | `string` | The main text of the discussion. |
| `body_html` | `string` |  |
| `comments_count` | `integer` |  |
| `title` | `string` | The title of the discussion. |
| `number` | `integer` | The unique sequence number of a team discussion. |
| `private` | `boolean` | Whether or not this discussion should be restricted to team members and organization administrators. |
| `last_edited_at` | `string` |  |
| `comments_url` | `string` |  |
| `author` | `object` | A GitHub user. |
| `updated_at` | `string` |  |
| `url` | `string` |  |
| `pinned` | `boolean` | Whether or not this discussion should be pinned for easy retrieval. |
| `reactions` | `object` |  |
| `node_id` | `string` |  |
| `body_version` | `string` | The current version of the body content. If provided, this update operation will be rejected if the given version does not match the latest version on the server. |
| `team_url` | `string` |  |
| `created_at` | `string` |  |
| `html_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_discussion_in_org` | `SELECT` | `discussion_number, org, team_slug` | Get a specific discussion on a team's page. OAuth access tokens require the `read:discussion` [scope](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/&#123;org_id&#125;/team/&#123;team_id&#125;/discussions/&#123;discussion_number&#125;`. |
| `list_discussions_in_org` | `SELECT` | `org, team_slug` | List all discussions on a team's page. OAuth access tokens require the `read:discussion` [scope](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/&#123;org_id&#125;/team/&#123;team_id&#125;/discussions`. |
| `create_discussion_in_org` | `INSERT` | `org, team_slug, data__body, data__title` | Creates a new discussion post on a team's page. OAuth access tokens require the `write:discussion` [scope](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).<br /><br />This endpoint triggers [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See "[Secondary rate limits](https://docs.github.com/rest/overview/resources-in-the-rest-api#secondary-rate-limits)" and "[Dealing with secondary rate limits](https://docs.github.com/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)" for details.<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `POST /organizations/&#123;org_id&#125;/team/&#123;team_id&#125;/discussions`. |
| `delete_discussion_in_org` | `DELETE` | `discussion_number, org, team_slug` | Delete a discussion from a team's page. OAuth access tokens require the `write:discussion` [scope](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `DELETE /organizations/&#123;org_id&#125;/team/&#123;team_id&#125;/discussions/&#123;discussion_number&#125;`. |
| `update_discussion_in_org` | `EXEC` | `discussion_number, org, team_slug` | Edits the title and body text of a discussion post. Only the parameters you provide are updated. OAuth access tokens require the `write:discussion` [scope](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `PATCH /organizations/&#123;org_id&#125;/team/&#123;team_id&#125;/discussions/&#123;discussion_number&#125;`. |
