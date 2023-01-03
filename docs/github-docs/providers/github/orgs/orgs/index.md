---
title: orgs
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
<tr><td><b>Name</b></td><td><code>orgs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.orgs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `integer` |
| `name` | `string` |
| `description` | `string` |
| `node_id` | `string` |
| `members_can_create_public_pages` | `boolean` |
| `following` | `integer` |
| `plan` | `object` |
| `html_url` | `string` |
| `has_repository_projects` | `boolean` |
| `url` | `string` |
| `repos_url` | `string` |
| `billing_email` | `string` |
| `twitter_username` | `string` |
| `total_private_repos` | `integer` |
| `email` | `string` |
| `members_allowed_repository_creation_type` | `string` |
| `default_repository_permission` | `string` |
| `members_can_create_private_repositories` | `boolean` |
| `members_can_create_private_pages` | `boolean` |
| `collaborators` | `integer` |
| `disk_usage` | `integer` |
| `owned_private_repos` | `integer` |
| `members_can_create_internal_repositories` | `boolean` |
| `company` | `string` |
| `members_can_create_public_repositories` | `boolean` |
| `members_can_create_repositories` | `boolean` |
| `login` | `string` |
| `hooks_url` | `string` |
| `public_members_url` | `string` |
| `is_verified` | `boolean` |
| `type` | `string` |
| `avatar_url` | `string` |
| `two_factor_requirement_enabled` | `boolean` |
| `members_url` | `string` |
| `public_repos` | `integer` |
| `location` | `string` |
| `events_url` | `string` |
| `created_at` | `string` |
| `issues_url` | `string` |
| `private_gists` | `integer` |
| `has_organization_projects` | `boolean` |
| `blog` | `string` |
| `members_can_fork_private_repositories` | `boolean` |
| `members_can_create_pages` | `boolean` |
| `public_gists` | `integer` |
| `followers` | `integer` |
| `updated_at` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `org` | To see many of the organization response values, you need to be an authenticated organization owner with the `admin:org` scope. When the value of `two_factor_requirement_enabled` is `true`, the organization requires all members, billing managers, and outside collaborators to enable [two-factor authentication](https://docs.github.com/articles/securing-your-account-with-two-factor-authentication-2fa/).<br /><br />GitHub Apps with the `Organization plan` permission can use this endpoint to retrieve information about an organization's GitHub plan. See "[Authenticating with GitHub Apps](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/)" for details. For an example response, see 'Response with GitHub plan information' below." |
| `list` | `SELECT` |  | Lists all organizations, in the order that they were created on GitHub.<br /><br />**Note:** Pagination is powered exclusively by the `since` parameter. Use the [Link header](https://docs.github.com/rest/overview/resources-in-the-rest-api#link-header) to get the URL for the next page of organizations. |
| `list_for_user` | `SELECT` | `username` | List [public organization memberships](https://docs.github.com/articles/publicizing-or-concealing-organization-membership) for the specified user.<br /><br />This method only lists _public_ memberships, regardless of authentication. If you need to fetch all of the organization memberships (public and private) for the authenticated user, use the [List organizations for the authenticated user](https://docs.github.com/rest/reference/orgs#list-organizations-for-the-authenticated-user) API instead. |
| `list_for_authenticated_user` | `EXEC` |  | List organizations for the authenticated user.<br /><br />**OAuth scope requirements**<br /><br />This only lists organizations that your authorization allows you to operate on in some way (e.g., you can list teams with `read:org` scope, you can publicize your organization membership with `user` scope, etc.). Therefore, this API requires at least `user` or `read:org` scope. OAuth requests with insufficient scope receive a `403 Forbidden` response. |
| `update` | `EXEC` | `org` | **Parameter Deprecation Notice:** GitHub will replace and discontinue `members_allowed_repository_creation_type` in favor of more granular permissions. The new input parameters are `members_can_create_public_repositories`, `members_can_create_private_repositories` for all organizations and `members_can_create_internal_repositories` for organizations associated with an enterprise account using GitHub Enterprise Cloud or GitHub Enterprise Server 2.20+. For more information, see the [blog post](https://developer.github.com/changes/2019-12-03-internal-visibility-changes).<br /><br />Enables an authenticated organization owner with the `admin:org` scope to update the organization's profile and member privileges. |
