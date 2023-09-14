---
title: organizations
hide_title: false
hide_table_of_contents: false
keywords:
  - organizations
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
<tr><td><b>Name</b></td><td><code>organizations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.codespaces.organizations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `codespaces` | `array` |
| `total_count` | `integer` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_codespaces_for_user_in_org` | `SELECT` | `org, username` | Lists the codespaces that a member of an organization has for repositories in that organization.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
| `list_in_organization` | `SELECT` | `org` | Lists the codespaces associated to a specified organization.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
| `delete_codespaces_access_users` | `DELETE` | `org, data__selected_usernames` | Codespaces for the specified users will no longer be billed to the organization.<br /><br />To use this endpoint, the access settings for the organization must be set to `selected_members`.<br />For information on how to change this setting, see "[Manage access control for organization codespaces](https://docs.github.com/rest/codespaces/organizations#manage-access-control-for-organization-codespaces)."<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
| `delete_from_organization` | `DELETE` | `codespace_name, org, username` | Deletes a user's codespace.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
| `set_codespaces_access` | `EXEC` | `org, data__visibility` | Sets which users can access codespaces in an organization. This is synonymous with granting or revoking codespaces access permissions for users according to the visibility.<br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
| `set_codespaces_access_users` | `EXEC` | `org, data__selected_usernames` | Codespaces for the specified users will be billed to the organization.<br /><br />To use this endpoint, the access settings for the organization must be set to `selected_members`.<br />For information on how to change this setting, see "[Manage access control for organization codespaces](https://docs.github.com/rest/codespaces/organizations#manage-access-control-for-organization-codespaces)."<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
| `stop_in_organization` | `EXEC` | `codespace_name, org, username` | Stops a user's codespace.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
