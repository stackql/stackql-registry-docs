---
title: orgs_access_selected_users
hide_title: false
hide_table_of_contents: false
keywords:
  - orgs_access_selected_users
  - codespaces
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
<tr><td><b>Name</b></td><td><code>orgs_access_selected_users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.codespaces.orgs_access_selected_users</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `delete_codespaces_access_users` | `DELETE` | `org, data__selected_usernames` | Codespaces for the specified users will no longer be billed to the organization.<br /><br />To use this endpoint, the access settings for the organization must be set to `selected_members`.<br />For information on how to change this setting, see "[Manage access control for organization codespaces](https://docs.github.com/rest/codespaces/organizations#manage-access-control-for-organization-codespaces)."<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
| `set_codespaces_access_users` | `EXEC` | `org, data__selected_usernames` | Codespaces for the specified users will be billed to the organization.<br /><br />To use this endpoint, the access settings for the organization must be set to `selected_members`.<br />For information on how to change this setting, see "[Manage access control for organization codespaces](https://docs.github.com/rest/codespaces/organizations#manage-access-control-for-organization-codespaces)."<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
