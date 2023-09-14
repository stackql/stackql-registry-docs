---
title: org
hide_title: false
hide_table_of_contents: false
keywords:
  - org
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
<tr><td><b>Name</b></td><td><code>org</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.org</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `collaborators` | `integer` |  |
| `members_can_create_private_repositories` | `boolean` |  |
| `issues_url` | `string` |  |
| `following` | `integer` |  |
| `hooks_url` | `string` |  |
| `company` | `string` |  |
| `dependabot_security_updates_enabled_for_new_repositories` | `boolean` | Whether dependabot security updates are automatically enabled for new repositories and repositories transferred<br />to this organization.<br /><br />This field is only visible to organization owners or members of a team with the security manager role. |
| `followers` | `integer` |  |
| `owned_private_repos` | `integer` |  |
| `dependency_graph_enabled_for_new_repositories` | `boolean` | Whether dependency graph is automatically enabled for new repositories and repositories transferred to this<br />organization.<br /><br />This field is only visible to organization owners or members of a team with the security manager role. |
| `twitter_username` | `string` |  |
| `two_factor_requirement_enabled` | `boolean` |  |
| `members_can_create_private_pages` | `boolean` |  |
| `members_can_create_public_repositories` | `boolean` |  |
| `public_members_url` | `string` |  |
| `is_verified` | `boolean` |  |
| `has_repository_projects` | `boolean` |  |
| `dependabot_alerts_enabled_for_new_repositories` | `boolean` | Whether GitHub Advanced Security is automatically enabled for new repositories and repositories transferred to<br />this organization.<br /><br />This field is only visible to organization owners or members of a team with the security manager role. |
| `private_gists` | `integer` |  |
| `public_gists` | `integer` |  |
| `repos_url` | `string` |  |
| `events_url` | `string` |  |
| `members_allowed_repository_creation_type` | `string` |  |
| `archived_at` | `string` |  |
| `disk_usage` | `integer` |  |
| `members_can_create_public_pages` | `boolean` |  |
| `plan` | `object` |  |
| `type` | `string` |  |
| `email` | `string` |  |
| `created_at` | `string` |  |
| `location` | `string` |  |
| `has_organization_projects` | `boolean` |  |
| `members_can_create_pages` | `boolean` |  |
| `members_can_fork_private_repositories` | `boolean` |  |
| `secret_scanning_enabled_for_new_repositories` | `boolean` | Whether secret scanning is automatically enabled for new repositories and repositories transferred to this<br />organization.<br /><br />This field is only visible to organization owners or members of a team with the security manager role. |
| `default_repository_permission` | `string` |  |
| `html_url` | `string` |  |
| `billing_email` | `string` |  |
| `blog` | `string` |  |
| `secret_scanning_push_protection_enabled_for_new_repositories` | `boolean` | Whether secret scanning push protection is automatically enabled for new repositories and repositories<br />transferred to this organization.<br /><br />This field is only visible to organization owners or members of a team with the security manager role. |
| `secret_scanning_push_protection_custom_link` | `string` | An optional URL string to display to contributors who are blocked from pushing a secret. |
| `web_commit_signoff_required` | `boolean` |  |
| `public_repos` | `integer` |  |
| `updated_at` | `string` |  |
| `members_can_create_repositories` | `boolean` |  |
| `node_id` | `string` |  |
| `total_private_repos` | `integer` |  |
| `url` | `string` |  |
| `secret_scanning_push_protection_custom_link_enabled` | `boolean` | Whether a custom link is shown to contributors who are blocked from pushing a secret by push protection. |
| `login` | `string` |  |
| `members_can_create_internal_repositories` | `boolean` |  |
| `advanced_security_enabled_for_new_repositories` | `boolean` | Whether GitHub Advanced Security is enabled for new repositories and repositories transferred to this organization.<br /><br />This field is only visible to organization owners or members of a team with the security manager role. |
| `avatar_url` | `string` |  |
| `members_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `org` |
