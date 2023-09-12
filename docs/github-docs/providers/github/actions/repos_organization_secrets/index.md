---
title: repos_organization_secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - repos_organization_secrets
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
<tr><td><b>Name</b></td><td><code>repos_organization_secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.actions.repos_organization_secrets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `secrets` | `array` |
| `total_count` | `integer` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_repo_organization_secrets` | `SELECT` | `owner, repo` |
