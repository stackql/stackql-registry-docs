---
title: discussions
hide_title: false
hide_table_of_contents: false
keywords:
  - discussions
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
<tr><td><b>Name</b></td><td><code>discussions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.teams.discussions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `body_version` | `string` | The current version of the body content. If provided, this update operation will be rejected if the given version does not match the latest version on the server. |
| `node_id` | `string` |  |
| `updated_at` | `string` |  |
| `pinned` | `boolean` | Whether or not this discussion should be pinned for easy retrieval. |
| `comments_url` | `string` |  |
| `team_url` | `string` |  |
| `title` | `string` | The title of the discussion. |
| `comments_count` | `integer` |  |
| `last_edited_at` | `string` |  |
| `body` | `string` | The main text of the discussion. |
| `number` | `integer` | The unique sequence number of a team discussion. |
| `html_url` | `string` |  |
| `created_at` | `string` |  |
| `url` | `string` |  |
| `reactions` | `object` |  |
| `private` | `boolean` | Whether or not this discussion should be restricted to team members and organization administrators. |
| `author` | `object` | A GitHub user. |
| `body_html` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_discussion_legacy` | `SELECT` | `discussion_number, team_id` | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Get a discussion](https://docs.github.com/rest/teams/discussions#get-a-discussion) endpoint.<br /><br />Get a specific discussion on a team's page. OAuth access tokens require the `read:discussion` [scope](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). |
| `list_discussions_legacy` | `SELECT` | `team_id` | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [`List discussions`](https://docs.github.com/rest/teams/discussions#list-discussions) endpoint.<br /><br />List all discussions on a team's page. OAuth access tokens require the `read:discussion` [scope](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). |
| `create_discussion_legacy` | `INSERT` | `team_id, data__body, data__title` | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [`Create a discussion`](https://docs.github.com/rest/teams/discussions#create-a-discussion) endpoint.<br /><br />Creates a new discussion post on a team's page. OAuth access tokens require the `write:discussion` [scope](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).<br /><br />This endpoint triggers [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See "[Secondary rate limits](https://docs.github.com/rest/overview/resources-in-the-rest-api#secondary-rate-limits)" and "[Dealing with secondary rate limits](https://docs.github.com/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)" for details. |
| `delete_discussion_legacy` | `DELETE` | `discussion_number, team_id` | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [`Delete a discussion`](https://docs.github.com/rest/teams/discussions#delete-a-discussion) endpoint.<br /><br />Delete a discussion from a team's page. OAuth access tokens require the `write:discussion` [scope](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). |
| `update_discussion_legacy` | `EXEC` | `discussion_number, team_id` | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Update a discussion](https://docs.github.com/rest/teams/discussions#update-a-discussion) endpoint.<br /><br />Edits the title and body text of a discussion post. Only the parameters you provide are updated. OAuth access tokens require the `write:discussion` [scope](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). |
