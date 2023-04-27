---
title: saml_ids
hide_title: false
hide_table_of_contents: false
keywords:
  - saml_ids
  - scim
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
<tr><td><b>Name</b></td><td><code>saml_ids</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.scim.saml_ids</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `scimIdentity` | `object` |
| `user` | `object` |
| `guid` | `string` |
| `samlIdentity` | `object` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_saml_identities` | `SELECT` | `org` |
