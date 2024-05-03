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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>org</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.orgs.org" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` |  |
| <CopyableCode code="name" /> | `string` |  |
| <CopyableCode code="description" /> | `string` |  |
| <CopyableCode code="advanced_security_enabled_for_new_repositories" /> | `boolean` | Whether GitHub Advanced Security is enabled for new repositories and repositories transferred to this organization.<br /><br />This field is only visible to organization owners or members of a team with the security manager role. |
| <CopyableCode code="archived_at" /> | `string` |  |
| <CopyableCode code="avatar_url" /> | `string` |  |
| <CopyableCode code="billing_email" /> | `string` |  |
| <CopyableCode code="blog" /> | `string` |  |
| <CopyableCode code="collaborators" /> | `integer` |  |
| <CopyableCode code="company" /> | `string` |  |
| <CopyableCode code="created_at" /> | `string` |  |
| <CopyableCode code="default_repository_permission" /> | `string` |  |
| <CopyableCode code="dependabot_alerts_enabled_for_new_repositories" /> | `boolean` | Whether GitHub Advanced Security is automatically enabled for new repositories and repositories transferred to<br />this organization.<br /><br />This field is only visible to organization owners or members of a team with the security manager role. |
| <CopyableCode code="dependabot_security_updates_enabled_for_new_repositories" /> | `boolean` | Whether dependabot security updates are automatically enabled for new repositories and repositories transferred<br />to this organization.<br /><br />This field is only visible to organization owners or members of a team with the security manager role. |
| <CopyableCode code="dependency_graph_enabled_for_new_repositories" /> | `boolean` | Whether dependency graph is automatically enabled for new repositories and repositories transferred to this<br />organization.<br /><br />This field is only visible to organization owners or members of a team with the security manager role. |
| <CopyableCode code="disk_usage" /> | `integer` |  |
| <CopyableCode code="email" /> | `string` |  |
| <CopyableCode code="events_url" /> | `string` |  |
| <CopyableCode code="followers" /> | `integer` |  |
| <CopyableCode code="following" /> | `integer` |  |
| <CopyableCode code="has_organization_projects" /> | `boolean` |  |
| <CopyableCode code="has_repository_projects" /> | `boolean` |  |
| <CopyableCode code="hooks_url" /> | `string` |  |
| <CopyableCode code="html_url" /> | `string` |  |
| <CopyableCode code="is_verified" /> | `boolean` |  |
| <CopyableCode code="issues_url" /> | `string` |  |
| <CopyableCode code="location" /> | `string` |  |
| <CopyableCode code="login" /> | `string` |  |
| <CopyableCode code="members_allowed_repository_creation_type" /> | `string` |  |
| <CopyableCode code="members_can_create_internal_repositories" /> | `boolean` |  |
| <CopyableCode code="members_can_create_pages" /> | `boolean` |  |
| <CopyableCode code="members_can_create_private_pages" /> | `boolean` |  |
| <CopyableCode code="members_can_create_private_repositories" /> | `boolean` |  |
| <CopyableCode code="members_can_create_public_pages" /> | `boolean` |  |
| <CopyableCode code="members_can_create_public_repositories" /> | `boolean` |  |
| <CopyableCode code="members_can_create_repositories" /> | `boolean` |  |
| <CopyableCode code="members_can_fork_private_repositories" /> | `boolean` |  |
| <CopyableCode code="members_url" /> | `string` |  |
| <CopyableCode code="node_id" /> | `string` |  |
| <CopyableCode code="owned_private_repos" /> | `integer` |  |
| <CopyableCode code="plan" /> | `object` |  |
| <CopyableCode code="private_gists" /> | `integer` |  |
| <CopyableCode code="public_gists" /> | `integer` |  |
| <CopyableCode code="public_members_url" /> | `string` |  |
| <CopyableCode code="public_repos" /> | `integer` |  |
| <CopyableCode code="repos_url" /> | `string` |  |
| <CopyableCode code="secret_scanning_enabled_for_new_repositories" /> | `boolean` | Whether secret scanning is automatically enabled for new repositories and repositories transferred to this<br />organization.<br /><br />This field is only visible to organization owners or members of a team with the security manager role. |
| <CopyableCode code="secret_scanning_push_protection_custom_link" /> | `string` | An optional URL string to display to contributors who are blocked from pushing a secret. |
| <CopyableCode code="secret_scanning_push_protection_custom_link_enabled" /> | `boolean` | Whether a custom link is shown to contributors who are blocked from pushing a secret by push protection. |
| <CopyableCode code="secret_scanning_push_protection_enabled_for_new_repositories" /> | `boolean` | Whether secret scanning push protection is automatically enabled for new repositories and repositories<br />transferred to this organization.<br /><br />This field is only visible to organization owners or members of a team with the security manager role. |
| <CopyableCode code="total_private_repos" /> | `integer` |  |
| <CopyableCode code="twitter_username" /> | `string` |  |
| <CopyableCode code="two_factor_requirement_enabled" /> | `boolean` |  |
| <CopyableCode code="type" /> | `string` |  |
| <CopyableCode code="updated_at" /> | `string` |  |
| <CopyableCode code="url" /> | `string` |  |
| <CopyableCode code="web_commit_signoff_required" /> | `boolean` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="org" /> |
