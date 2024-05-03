---
title: team_discussions
hide_title: false
hide_table_of_contents: false
keywords:
  - team_discussions
  - reactions
  - github    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: /img/providers/github/stackql-github-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>team_discussions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.reactions.team_discussions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` |  |
| <CopyableCode code="content" /> | `string` | The reaction to use |
| <CopyableCode code="created_at" /> | `string` |  |
| <CopyableCode code="node_id" /> | `string` |  |
| <CopyableCode code="user" /> | `object` | A GitHub user. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_for_team_discussion_comment_in_org" /> | `SELECT` | <CopyableCode code="comment_number, discussion_number, org, team_slug" /> | List the reactions to a [team discussion comment](https://docs.github.com/rest/teams/discussion-comments#get-a-discussion-comment). OAuth access tokens require the `read:discussion` [scope](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/:org_id/team/:team_id/discussions/:discussion_number/comments/:comment_number/reactions`. |
| <CopyableCode code="list_for_team_discussion_comment_legacy" /> | `SELECT` | <CopyableCode code="comment_number, discussion_number, team_id" /> | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [`List reactions for a team discussion comment`](https://docs.github.com/rest/reactions/reactions#list-reactions-for-a-team-discussion-comment) endpoint.<br /><br />List the reactions to a [team discussion comment](https://docs.github.com/rest/teams/discussion-comments#get-a-discussion-comment). OAuth access tokens require the `read:discussion` [scope](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). |
| <CopyableCode code="list_for_team_discussion_in_org" /> | `SELECT` | <CopyableCode code="discussion_number, org, team_slug" /> | List the reactions to a [team discussion](https://docs.github.com/rest/teams/discussions#get-a-discussion). OAuth access tokens require the `read:discussion` [scope](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/:org_id/team/:team_id/discussions/:discussion_number/reactions`. |
| <CopyableCode code="list_for_team_discussion_legacy" /> | `SELECT` | <CopyableCode code="discussion_number, team_id" /> | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [`List reactions for a team discussion`](https://docs.github.com/rest/reactions/reactions#list-reactions-for-a-team-discussion) endpoint.<br /><br />List the reactions to a [team discussion](https://docs.github.com/rest/teams/discussions#get-a-discussion). OAuth access tokens require the `read:discussion` [scope](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). |
| <CopyableCode code="create_for_team_discussion_comment_in_org" /> | `INSERT` | <CopyableCode code="comment_number, discussion_number, org, team_slug, data__content" /> | Create a reaction to a [team discussion comment](https://docs.github.com/rest/teams/discussion-comments#get-a-discussion-comment). OAuth access tokens require the `write:discussion` [scope](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). A response with an HTTP `200` status means that you already added the reaction type to this team discussion comment.<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `POST /organizations/:org_id/team/:team_id/discussions/:discussion_number/comments/:comment_number/reactions`. |
| <CopyableCode code="create_for_team_discussion_comment_legacy" /> | `INSERT` | <CopyableCode code="comment_number, discussion_number, team_id, data__content" /> | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new "[Create reaction for a team discussion comment](https://docs.github.com/rest/reactions/reactions#create-reaction-for-a-team-discussion-comment)" endpoint.<br /><br />Create a reaction to a [team discussion comment](https://docs.github.com/rest/teams/discussion-comments#get-a-discussion-comment). OAuth access tokens require the `write:discussion` [scope](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). A response with an HTTP `200` status means that you already added the reaction type to this team discussion comment. |
| <CopyableCode code="create_for_team_discussion_in_org" /> | `INSERT` | <CopyableCode code="discussion_number, org, team_slug, data__content" /> | Create a reaction to a [team discussion](https://docs.github.com/rest/teams/discussions#get-a-discussion). OAuth access tokens require the `write:discussion` [scope](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). A response with an HTTP `200` status means that you already added the reaction type to this team discussion.<br /><br />**Note:** You can also specify a team by `org_id` and `team_id` using the route `POST /organizations/:org_id/team/:team_id/discussions/:discussion_number/reactions`. |
| <CopyableCode code="create_for_team_discussion_legacy" /> | `INSERT` | <CopyableCode code="discussion_number, team_id, data__content" /> | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [`Create reaction for a team discussion`](https://docs.github.com/rest/reactions/reactions#create-reaction-for-a-team-discussion) endpoint.<br /><br />Create a reaction to a [team discussion](https://docs.github.com/rest/teams/discussions#get-a-discussion). OAuth access tokens require the `write:discussion` [scope](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). A response with an HTTP `200` status means that you already added the reaction type to this team discussion. |
| <CopyableCode code="delete_for_team_discussion" /> | `DELETE` | <CopyableCode code="discussion_number, org, reaction_id, team_slug" /> | **Note:** You can also specify a team or organization with `team_id` and `org_id` using the route `DELETE /organizations/:org_id/team/:team_id/discussions/:discussion_number/reactions/:reaction_id`.<br /><br />Delete a reaction to a [team discussion](https://docs.github.com/rest/teams/discussions#get-a-discussion). OAuth access tokens require the `write:discussion` [scope](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). |
| <CopyableCode code="delete_for_team_discussion_comment" /> | `DELETE` | <CopyableCode code="comment_number, discussion_number, org, reaction_id, team_slug" /> | **Note:** You can also specify a team or organization with `team_id` and `org_id` using the route `DELETE /organizations/:org_id/team/:team_id/discussions/:discussion_number/comments/:comment_number/reactions/:reaction_id`.<br /><br />Delete a reaction to a [team discussion comment](https://docs.github.com/rest/teams/discussion-comments#get-a-discussion-comment). OAuth access tokens require the `write:discussion` [scope](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). |
