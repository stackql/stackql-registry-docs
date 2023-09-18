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
| `advanced_security_enabled_for_new_repositories` | `boolean` | Whether GitHub Advanced Security is enabled for new repositories and repositories transferred to this organization.<br /><br />This field is only visible to organization owners or members of a team with the security manager role. |
| `total_private_repos` | `integer` |  |
| `created_at` | `string` |  |
| `html_url` | `string` |  |
| `members_url` | `string` |  |
| `twitter_username` | `string` |  |
| `node_id` | `string` |  |
| `location` | `string` |  |
| `members_can_create_public_repositories` | `boolean` |  |
| `members_can_fork_private_repositories` | `boolean` |  |
| `owned_private_repos` | `integer` |  |
| `disk_usage` | `integer` |  |
| `public_repos` | `integer` |  |
| `dependabot_security_updates_enabled_for_new_repositories` | `boolean` | Whether dependabot security updates are automatically enabled for new repositories and repositories transferred<br />to this organization.<br /><br />This field is only visible to organization owners or members of a team with the security manager role. |
| `events_url` | `string` |  |
| `company` | `string` |  |
| `default_repository_permission` | `string` |  |
| `archived_at` | `string` |  |
| `dependency_graph_enabled_for_new_repositories` | `boolean` | Whether dependency graph is automatically enabled for new repositories and repositories transferred to this<br />organization.<br /><br />This field is only visible to organization owners or members of a team with the security manager role. |
| `secret_scanning_push_protection_enabled_for_new_repositories` | `boolean` | Whether secret scanning push protection is automatically enabled for new repositories and repositories<br />transferred to this organization.<br /><br />This field is only visible to organization owners or members of a team with the security manager role. |
| `issues_url` | `string` |  |
| `members_can_create_private_repositories` | `boolean` |  |
| `followers` | `integer` |  |
| `dependabot_alerts_enabled_for_new_repositories` | `boolean` | Whether GitHub Advanced Security is automatically enabled for new repositories and repositories transferred to<br />this organization.<br /><br />This field is only visible to organization owners or members of a team with the security manager role. |
| `following` | `integer` |  |
| `plan` | `object` |  |
| `collaborators` | `integer` |  |
| `private_gists` | `integer` |  |
| `login` | `string` |  |
| `has_repository_projects` | `boolean` |  |
| `url` | `string` |  |
| `two_factor_requirement_enabled` | `boolean` |  |
| `members_can_create_private_pages` | `boolean` |  |
| `members_can_create_repositories` | `boolean` |  |
| `email` | `string` |  |
| `has_organization_projects` | `boolean` |  |
| `web_commit_signoff_required` | `boolean` |  |
| `avatar_url` | `string` |  |
| `hooks_url` | `string` |  |
| `members_can_create_public_pages` | `boolean` |  |
| `secret_scanning_enabled_for_new_repositories` | `boolean` | Whether secret scanning is automatically enabled for new repositories and repositories transferred to this<br />organization.<br /><br />This field is only visible to organization owners or members of a team with the security manager role. |
| `members_can_create_pages` | `boolean` |  |
| `type` | `string` |  |
| `blog` | `string` |  |
| `members_can_create_internal_repositories` | `boolean` |  |
| `secret_scanning_push_protection_custom_link` | `string` | An optional URL string to display to contributors who are blocked from pushing a secret. |
| `is_verified` | `boolean` |  |
| `repos_url` | `string` |  |
| `members_allowed_repository_creation_type` | `string` |  |
| `secret_scanning_push_protection_custom_link_enabled` | `boolean` | Whether a custom link is shown to contributors who are blocked from pushing a secret by push protection. |
| `public_gists` | `integer` |  |
| `public_members_url` | `string` |  |
| `updated_at` | `string` |  |
| `billing_email` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `org` |
