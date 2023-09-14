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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_managers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.security_managers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | Unique identifier of the team |
| `name` | `string` | Name of the team |
| `description` | `string` | Description of the team |
| `node_id` | `string` |  |
| `repositories_url` | `string` |  |
| `url` | `string` | URL for the team |
| `privacy` | `string` | The level of privacy this team should have |
| `slug` | `string` |  |
| `html_url` | `string` |  |
| `permission` | `string` | Permission that the team will have for its repositories |
| `members_url` | `string` |  |
| `notification_setting` | `string` | The notification setting the team has set |
| `ldap_dn` | `string` | Distinguished Name (DN) that team maps to within LDAP environment |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_security_manager_teams` | `SELECT` | `org` | Lists teams that are security managers for an organization. For more information, see "[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)."<br /><br />To use this endpoint, you must be an administrator or security manager for the organization, and you must use an access token with the `read:org` scope.<br /><br />GitHub Apps must have the `administration` organization read permission to use this endpoint. |
| `remove_security_manager_team` | `DELETE` | `org, team_slug` | Removes the security manager role from a team for an organization. For more information, see "[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization) team from an organization."<br /><br />To use this endpoint, you must be an administrator for the organization, and you must use an access token with the `admin:org` scope.<br /><br />GitHub Apps must have the `administration` organization read-write permission to use this endpoint. |
| `add_security_manager_team` | `EXEC` | `org, team_slug` | Adds a team as a security manager for an organization. For more information, see "[Managing security for an organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization) for an organization."<br /><br />To use this endpoint, you must be an administrator for the organization, and you must use an access token with the `write:org` scope.<br /><br />GitHub Apps must have the `administration` organization read-write permission to use this endpoint. |
