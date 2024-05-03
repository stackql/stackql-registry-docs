---
title: security_managers
hide_title: false
hide_table_of_contents: false
keywords:
  - security_managers
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
<tr><td><b>Name</b></td><td><code>security_managers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.orgs.security_managers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | Unique identifier of the team |
| <CopyableCode code="name" /> | `string` | Name of the team |
| <CopyableCode code="description" /> | `string` | Description of the team |
| <CopyableCode code="html_url" /> | `string` |  |
| <CopyableCode code="ldap_dn" /> | `string` | Distinguished Name (DN) that team maps to within LDAP environment |
| <CopyableCode code="members_url" /> | `string` |  |
| <CopyableCode code="node_id" /> | `string` |  |
| <CopyableCode code="notification_setting" /> | `string` | The notification setting the team has set |
| <CopyableCode code="permission" /> | `string` | Permission that the team will have for its repositories |
| <CopyableCode code="privacy" /> | `string` | The level of privacy this team should have |
| <CopyableCode code="repositories_url" /> | `string` |  |
| <CopyableCode code="slug" /> | `string` |  |
| <CopyableCode code="url" /> | `string` | URL for the team |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_security_manager_teams" /> | `SELECT` | <CopyableCode code="org" /> | Lists teams that are security managers for an organization. For more information, see "[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)."<br /><br />To use this endpoint, you must be an administrator or security manager for the organization, and you must use an access token with the `read:org` scope.<br /><br />GitHub Apps must have the `administration` organization read permission to use this endpoint. |
| <CopyableCode code="remove_security_manager_team" /> | `DELETE` | <CopyableCode code="org, team_slug" /> | Removes the security manager role from a team for an organization. For more information, see "[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization) team from an organization."<br /><br />To use this endpoint, you must be an administrator for the organization, and you must use an access token with the `admin:org` scope.<br /><br />GitHub Apps must have the `administration` organization read-write permission to use this endpoint. |
| <CopyableCode code="add_security_manager_team" /> | `EXEC` | <CopyableCode code="org, team_slug" /> | Adds a team as a security manager for an organization. For more information, see "[Managing security for an organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization) for an organization."<br /><br />To use this endpoint, you must be an administrator for the organization, and you must use an access token with the `write:org` scope.<br /><br />GitHub Apps must have the `administration` organization read-write permission to use this endpoint. |
