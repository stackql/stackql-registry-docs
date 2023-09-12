---
title: repos_oidc_customization_sub
hide_title: false
hide_table_of_contents: false
keywords:
  - repos_oidc_customization_sub
  - actions
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
<tr><td><b>Name</b></td><td><code>repos_oidc_customization_sub</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.actions.repos_oidc_customization_sub</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `include_claim_keys` | `array` | Array of unique strings. Each claim key can only contain alphanumeric characters and underscores. |
| `use_default` | `boolean` | Whether to use the default template or not. If `true`, the `include_claim_keys` field is ignored. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_custom_oidc_sub_claim_for_repo` | `SELECT` | `owner, repo` | Gets the customization template for an OpenID Connect (OIDC) subject claim.<br />You must authenticate using an access token with the `repo` scope to use this<br />endpoint. GitHub Apps must have the `organization_administration:read` permission to use this endpoint. |
| `set_custom_oidc_sub_claim_for_repo` | `EXEC` | `owner, repo, data__use_default` | Sets the customization template and `opt-in` or `opt-out` flag for an OpenID Connect (OIDC) subject claim for a repository.<br />You must authenticate using an access token with the `repo` scope to use this<br />endpoint. GitHub Apps must have the `actions:write` permission to use this endpoint. |
