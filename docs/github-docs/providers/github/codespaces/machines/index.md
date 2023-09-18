---
title: machines
hide_title: false
hide_table_of_contents: false
keywords:
  - machines
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
<tr><td><b>Name</b></td><td><code>machines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.codespaces.machines</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `machines` | `array` |
| `total_count` | `integer` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `codespace_machines_for_authenticated_user` | `SELECT` | `codespace_name` | List the machine types a codespace can transition to use.<br /><br />You must authenticate using an access token with the `codespace` scope to use this endpoint.<br /><br />GitHub Apps must have read access to the `codespaces_metadata` repository permission to use this endpoint. |
| `repo_machines_for_authenticated_user` | `SELECT` | `owner, repo` | List the machine types available for a given repository based on its configuration.<br /><br />You must authenticate using an access token with the `codespace` scope to use this endpoint.<br /><br />GitHub Apps must have write access to the `codespaces_metadata` repository permission to use this endpoint. |
