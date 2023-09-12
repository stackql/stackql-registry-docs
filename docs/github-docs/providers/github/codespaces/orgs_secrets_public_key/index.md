---
title: orgs_secrets_public_key
hide_title: false
hide_table_of_contents: false
keywords:
  - orgs_secrets_public_key
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
<tr><td><b>Name</b></td><td><code>orgs_secrets_public_key</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.codespaces.orgs_secrets_public_key</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `key` | `string` | The Base64 encoded public key. |
| `key_id` | `string` | The identifier for the key. |
| `title` | `string` |  |
| `url` | `string` |  |
| `created_at` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_org_public_key` | `SELECT` | `org` |
