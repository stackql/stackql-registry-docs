---
title: org_restrictions
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - github
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>org_restrictions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.interactions.org_restrictions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `origin` | `string` |  |
| `expires_at` | `string` |  |
| `limit` | `string` | The type of GitHub user that can comment, open issues, or create pull requests while the interaction limit is in effect. Can be one of: `existing_users`, `contributors_only`, `collaborators_only`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_restrictions_for_org` | `SELECT` | `org` | Shows which type of GitHub user can interact with this organization and when the restriction expires. If there is no restrictions, you will see an empty response. |
| `remove_restrictions_for_org` | `DELETE` | `org` | Removes all interaction restrictions from public repositories in the given organization. You must be an organization owner to remove restrictions. |
| `set_restrictions_for_org` | `EXEC` | `org, data__limit` | Temporarily restricts interactions to a certain type of GitHub user in any public repository in the given organization. You must be an organization owner to set these restrictions. Setting the interaction limit at the organization level will overwrite any interaction limits that are set for individual repositories owned by the organization. |
