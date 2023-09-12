---
title: security_managers_teams
hide_title: false
hide_table_of_contents: false
keywords:
  - security_managers_teams
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
<tr><td><b>Name</b></td><td><code>security_managers_teams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.security_managers_teams</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `remove_security_manager_team` | `DELETE` | `org, team_slug` | Removes the security manager role from a team for an organization. For more information, see "[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization) team from an organization."<br /><br />To use this endpoint, you must be an administrator for the organization, and you must use an access token with the `admin:org` scope.<br /><br />GitHub Apps must have the `administration` organization read-write permission to use this endpoint. |
| `add_security_manager_team` | `EXEC` | `org, team_slug` | Adds a team as a security manager for an organization. For more information, see "[Managing security for an organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization) for an organization."<br /><br />To use this endpoint, you must be an administrator for the organization, and you must use an access token with the `write:org` scope.<br /><br />GitHub Apps must have the `administration` organization read-write permission to use this endpoint. |
