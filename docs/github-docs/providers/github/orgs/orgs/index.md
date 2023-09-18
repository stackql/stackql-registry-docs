---
title: orgs
hide_title: false
hide_table_of_contents: false
keywords:
  - orgs
  - orgs
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
<tr><td><b>Name</b></td><td><code>orgs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.orgs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `integer` |
| `description` | `string` |
| `members_url` | `string` |
| `repos_url` | `string` |
| `hooks_url` | `string` |
| `url` | `string` |
| `public_members_url` | `string` |
| `events_url` | `string` |
| `login` | `string` |
| `avatar_url` | `string` |
| `issues_url` | `string` |
| `node_id` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` |  | Lists all organizations, in the order that they were created on GitHub.<br /><br />**Note:** Pagination is powered exclusively by the `since` parameter. Use the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers) to get the URL for the next page of organizations. |
| `list_for_user` | `SELECT` | `username` | List [public organization memberships](https://docs.github.com/articles/publicizing-or-concealing-organization-membership) for the specified user.<br /><br />This method only lists _public_ memberships, regardless of authentication. If you need to fetch all of the organization memberships (public and private) for the authenticated user, use the [List organizations for the authenticated user](https://docs.github.com/rest/orgs/orgs#list-organizations-for-the-authenticated-user) API instead. |
| `delete` | `DELETE` | `org` | Deletes an organization and all its repositories.<br /><br />The organization login will be unavailable for 90 days after deletion.<br /><br />Please review the Terms of Service regarding account deletion before using this endpoint:<br /><br />https://docs.github.com/site-policy/github-terms/github-terms-of-service |
| `enable_or_disable_security_product_on_all_org_repos` | `EXEC` | `enablement, org, security_product` | Enables or disables the specified security feature for all eligible repositories in an organization.<br /><br />To use this endpoint, you must be an organization owner or be member of a team with the security manager role.<br />A token with the 'write:org' scope is also required.<br /><br />GitHub Apps must have the `organization_administration:write` permission to use this endpoint.<br /><br />For more information, see "[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)." |
| `update` | `EXEC` | `org` | **Parameter Deprecation Notice:** GitHub will replace and discontinue `members_allowed_repository_creation_type` in favor of more granular permissions. The new input parameters are `members_can_create_public_repositories`, `members_can_create_private_repositories` for all organizations and `members_can_create_internal_repositories` for organizations associated with an enterprise account using GitHub Enterprise Cloud or GitHub Enterprise Server 2.20+. For more information, see the [blog post](https://developer.github.com/changes/2019-12-03-internal-visibility-changes).<br /><br />Enables an authenticated organization owner with the `admin:org` scope or the `repo` scope to update the organization's profile and member privileges. |
