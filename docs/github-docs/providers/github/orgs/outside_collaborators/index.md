---
title: outside_collaborators
hide_title: false
hide_table_of_contents: false
keywords:
  - outside_collaborators
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
<tr><td><b>Name</b></td><td><code>outside_collaborators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.orgs.outside_collaborators" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `integer` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="avatar_url" /> | `string` |
| <CopyableCode code="email" /> | `string` |
| <CopyableCode code="events_url" /> | `string` |
| <CopyableCode code="followers_url" /> | `string` |
| <CopyableCode code="following_url" /> | `string` |
| <CopyableCode code="gists_url" /> | `string` |
| <CopyableCode code="gravatar_id" /> | `string` |
| <CopyableCode code="html_url" /> | `string` |
| <CopyableCode code="login" /> | `string` |
| <CopyableCode code="node_id" /> | `string` |
| <CopyableCode code="organizations_url" /> | `string` |
| <CopyableCode code="received_events_url" /> | `string` |
| <CopyableCode code="repos_url" /> | `string` |
| <CopyableCode code="site_admin" /> | `boolean` |
| <CopyableCode code="starred_at" /> | `string` |
| <CopyableCode code="starred_url" /> | `string` |
| <CopyableCode code="subscriptions_url" /> | `string` |
| <CopyableCode code="type" /> | `string` |
| <CopyableCode code="url" /> | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_outside_collaborators" /> | `SELECT` | <CopyableCode code="org" /> | List all users who are outside collaborators of an organization. |
| <CopyableCode code="remove_outside_collaborator" /> | `DELETE` | <CopyableCode code="org, username" /> | Removing a user from this list will remove them from all the organization's repositories. |
| <CopyableCode code="convert_member_to_outside_collaborator" /> | `EXEC` | <CopyableCode code="org, username" /> | When an organization member is converted to an outside collaborator, they'll only have access to the repositories that their current team membership allows. The user will no longer be a member of the organization. For more information, see "[Converting an organization member to an outside collaborator](https://docs.github.com/articles/converting-an-organization-member-to-an-outside-collaborator/)". Converting an organization member to an outside collaborator may be restricted by enterprise administrators. For more information, see "[Enforcing repository management policies in your enterprise](https://docs.github.com/admin/policies/enforcing-policies-for-your-enterprise/enforcing-repository-management-policies-in-your-enterprise#enforcing-a-policy-for-inviting-outside-collaborators-to-repositories)." |
