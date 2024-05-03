---
title: teams_for_auth_user
hide_title: false
hide_table_of_contents: false
keywords:
  - teams_for_auth_user
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>teams_for_auth_user</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.teams.teams_for_auth_user" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | Unique identifier of the team |
| <CopyableCode code="name" /> | `string` | Name of the team |
| <CopyableCode code="description" /> | `string` |  |
| <CopyableCode code="created_at" /> | `string` |  |
| <CopyableCode code="html_url" /> | `string` |  |
| <CopyableCode code="ldap_dn" /> | `string` | Distinguished Name (DN) that team maps to within LDAP environment |
| <CopyableCode code="members_count" /> | `integer` |  |
| <CopyableCode code="members_url" /> | `string` |  |
| <CopyableCode code="node_id" /> | `string` |  |
| <CopyableCode code="notification_setting" /> | `string` | The notification setting the team has set |
| <CopyableCode code="organization" /> | `object` | Team Organization |
| <CopyableCode code="parent" /> | `object` | Groups of organization members that gives permissions on specified repositories. |
| <CopyableCode code="permission" /> | `string` | Permission that the team will have for its repositories |
| <CopyableCode code="privacy" /> | `string` | The level of privacy this team should have |
| <CopyableCode code="repos_count" /> | `integer` |  |
| <CopyableCode code="repositories_url" /> | `string` |  |
| <CopyableCode code="slug" /> | `string` |  |
| <CopyableCode code="updated_at" /> | `string` |  |
| <CopyableCode code="url" /> | `string` | URL for the team |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_for_authenticated_user" /> | `SELECT` |  |
