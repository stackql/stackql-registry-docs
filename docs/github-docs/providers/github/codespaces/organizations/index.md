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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>organizations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.codespaces.organizations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="codespaces" /> | `array` |
| <CopyableCode code="total_count" /> | `integer` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_codespaces_for_user_in_org" /> | `SELECT` | <CopyableCode code="org, username" /> | Lists the codespaces that a member of an organization has for repositories in that organization.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
| <CopyableCode code="list_in_organization" /> | `SELECT` | <CopyableCode code="org" /> | Lists the codespaces associated to a specified organization.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
| <CopyableCode code="delete_codespaces_access_users" /> | `DELETE` | <CopyableCode code="org, data__selected_usernames" /> | Codespaces for the specified users will no longer be billed to the organization.<br /><br />To use this endpoint, the access settings for the organization must be set to `selected_members`.<br />For information on how to change this setting, see "[Manage access control for organization codespaces](https://docs.github.com/rest/codespaces/organizations#manage-access-control-for-organization-codespaces)."<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
| <CopyableCode code="delete_from_organization" /> | `DELETE` | <CopyableCode code="codespace_name, org, username" /> | Deletes a user's codespace.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
| <CopyableCode code="set_codespaces_access" /> | `EXEC` | <CopyableCode code="org, data__visibility" /> | Sets which users can access codespaces in an organization. This is synonymous with granting or revoking codespaces access permissions for users according to the visibility.<br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
| <CopyableCode code="set_codespaces_access_users" /> | `EXEC` | <CopyableCode code="org, data__selected_usernames" /> | Codespaces for the specified users will be billed to the organization.<br /><br />To use this endpoint, the access settings for the organization must be set to `selected_members`.<br />For information on how to change this setting, see "[Manage access control for organization codespaces](https://docs.github.com/rest/codespaces/organizations#manage-access-control-for-organization-codespaces)."<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
| <CopyableCode code="stop_in_organization" /> | `EXEC` | <CopyableCode code="codespace_name, org, username" /> | Stops a user's codespace.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
