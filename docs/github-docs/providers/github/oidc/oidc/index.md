---
title: oidc
hide_title: false
hide_table_of_contents: false
keywords:
  - oidc
  - oidc
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
<tr><td><b>Name</b></td><td><code>oidc</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.oidc.oidc</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_oidc_custom_sub_template_for_org` | `SELECT` | `org` | Gets the customization template for an OpenID Connect (OIDC) subject claim.<br />You must authenticate using an access token with the `read:org` scope to use this endpoint.<br />GitHub Apps must have the `organization_administration:write` permission to use this endpoint. |
| `update_oidc_custom_sub_template_for_org` | `EXEC` | `org, data__include_claim_keys` | Creates or updates the customization template for an OpenID Connect (OIDC) subject claim.<br />You must authenticate using an access token with the `write:org` scope to use this endpoint.<br />GitHub Apps must have the `admin:org` permission to use this endpoint. |
