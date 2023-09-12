---
title: repos_secrets_public_key
hide_title: false
hide_table_of_contents: false
keywords:
  - repos_secrets_public_key
  - dependabot
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
<tr><td><b>Name</b></td><td><code>repos_secrets_public_key</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.dependabot.repos_secrets_public_key</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `key` | `string` | The Base64 encoded public key. |
| `key_id` | `string` | The identifier for the key. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_repo_public_key` | `SELECT` | `owner, repo` |
