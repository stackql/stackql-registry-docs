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
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `has_organization_projects` | `boolean` |  |
| `created_at` | `string` |  |
| `url` | `string` |  |
| `email` | `string` |  |
| `billing_email` | `string` |  |
| `updated_at` | `string` |  |
| `dependabot_security_updates_enabled_for_new_repositories` | `boolean` | Whether dependabot security updates are automatically enabled for new repositories and repositories transferred<br />to this organization.<br /><br />This field is only visible to organization owners or members of a team with the security manager role. |
| `plan` | `object` |  |
| `has_repository_projects` | `boolean` |  |
| `private_gists` | `integer` |  |
| `hooks_url` | `string` |  |
| `avatar_url` | `string` |  |
| `two_factor_requirement_enabled` | `boolean` |  |
| `node_id` | `string` |  |
| `members_can_create_public_repositories` | `boolean` |  |
| `members_can_create_public_pages` | `boolean` |  |
| `secret_scanning_push_protection_custom_link` | `string` | An optional URL string to display to contributors who are blocked from pushing a secret. |
| `total_private_repos` | `integer` |  |
| `secret_scanning_enabled_for_new_repositories` | `boolean` | Whether secret scanning is automatically enabled for new repositories and repositories transferred to this<br />organization.<br /><br />This field is only visible to organization owners or members of a team with the security manager role. |
| `secret_scanning_push_protection_enabled_for_new_repositories` | `boolean` | Whether secret scanning push protection is automatically enabled for new repositories and repositories<br />transferred to this organization.<br /><br />This field is only visible to organization owners or members of a team with the security manager role. |
| `repos_url` | `string` |  |
| `html_url` | `string` |  |
| `blog` | `string` |  |
| `members_can_create_private_pages` | `boolean` |  |
| `events_url` | `string` |  |
| `members_can_create_private_repositories` | `boolean` |  |
| `owned_private_repos` | `integer` |  |
| `login` | `string` |  |
| `dependabot_alerts_enabled_for_new_repositories` | `boolean` | Whether GitHub Advanced Security is automatically enabled for new repositories and repositories transferred to<br />this organization.<br /><br />This field is only visible to organization owners or members of a team with the security manager role. |
| `collaborators` | `integer` |  |
| `members_allowed_repository_creation_type` | `string` |  |
| `disk_usage` | `integer` |  |
| `secret_scanning_push_protection_custom_link_enabled` | `boolean` | Whether a custom link is shown to contributors who are blocked from pushing a secret by push protection. |
| `location` | `string` |  |
| `type` | `string` |  |
| `following` | `integer` |  |
| `archived_at` | `string` |  |
| `members_can_create_internal_repositories` | `boolean` |  |
| `issues_url` | `string` |  |
| `followers` | `integer` |  |
| `members_url` | `string` |  |
| `default_repository_permission` | `string` |  |
| `advanced_security_enabled_for_new_repositories` | `boolean` | Whether GitHub Advanced Security is enabled for new repositories and repositories transferred to this organization.<br /><br />This field is only visible to organization owners or members of a team with the security manager role. |
| `public_gists` | `integer` |  |
| `members_can_create_repositories` | `boolean` |  |
| `twitter_username` | `string` |  |
| `is_verified` | `boolean` |  |
| `members_can_fork_private_repositories` | `boolean` |  |
| `members_can_create_pages` | `boolean` |  |
| `company` | `string` |  |
| `dependency_graph_enabled_for_new_repositories` | `boolean` | Whether dependency graph is automatically enabled for new repositories and repositories transferred to this<br />organization.<br /><br />This field is only visible to organization owners or members of a team with the security manager role. |
| `public_repos` | `integer` |  |
| `web_commit_signoff_required` | `boolean` |  |
| `public_members_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `org` | To see many of the organization response values, you need to be an authenticated organization owner with the `admin:org` scope. When the value of `two_factor_requirement_enabled` is `true`, the organization requires all members, billing managers, and outside collaborators to enable [two-factor authentication](https://docs.github.com/articles/securing-your-account-with-two-factor-authentication-2fa/).<br /><br />GitHub Apps with the `Organization plan` permission can use this endpoint to retrieve information about an organization's GitHub plan. See "[Authenticating with GitHub Apps](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/)" for details. For an example response, see 'Response with GitHub plan information' below." |
| `delete` | `DELETE` | `org` | Deletes an organization and all its repositories.<br /><br />The organization login will be unavailable for 90 days after deletion.<br /><br />Please review the Terms of Service regarding account deletion before using this endpoint:<br /><br />https://docs.github.com/site-policy/github-terms/github-terms-of-service |
| `enable_or_disable_security_product_on_all_org_repos` | `EXEC` | `enablement, org, security_product` | Enables or disables the specified security feature for all eligible repositories in an organization.<br /><br />To use this endpoint, you must be an organization owner or be member of a team with the security manager role.<br />A token with the 'write:org' scope is also required.<br /><br />GitHub Apps must have the `organization_administration:write` permission to use this endpoint.<br /><br />For more information, see "[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)." |
| `update` | `EXEC` | `org` | **Parameter Deprecation Notice:** GitHub will replace and discontinue `members_allowed_repository_creation_type` in favor of more granular permissions. The new input parameters are `members_can_create_public_repositories`, `members_can_create_private_repositories` for all organizations and `members_can_create_internal_repositories` for organizations associated with an enterprise account using GitHub Enterprise Cloud or GitHub Enterprise Server 2.20+. For more information, see the [blog post](https://developer.github.com/changes/2019-12-03-internal-visibility-changes).<br /><br />Enables an authenticated organization owner with the `admin:org` scope or the `repo` scope to update the organization's profile and member privileges. |
