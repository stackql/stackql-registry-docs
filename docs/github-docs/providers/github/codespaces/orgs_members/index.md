---
title: orgs_members
hide_title: false
hide_table_of_contents: false
keywords:
  - orgs_members
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
<tr><td><b>Name</b></td><td><code>orgs_members</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.codespaces.orgs_members</code></td></tr>
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
| `delete_from_organization` | `DELETE` | `codespace_name, org, username` | Deletes a user's codespace.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
| `stop_in_organization` | `EXEC` | `codespace_name, org, username` | Stops a user's codespace.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
