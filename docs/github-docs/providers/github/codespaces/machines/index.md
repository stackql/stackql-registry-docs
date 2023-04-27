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
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the machine. |
| `memory_in_bytes` | `integer` | How much memory is available to the codespace. |
| `operating_system` | `string` | The operating system of the machine. |
| `prebuild_availability` | `string` | Whether a prebuild is currently available when creating a codespace for this machine and repository. If a branch was not specified as a ref, the default branch will be assumed. Value will be "null" if prebuilds are not supported or prebuild availability could not be determined. Value is the type of prebuild available, or "none" if none are available. |
| `storage_in_bytes` | `integer` | How much storage is available to the codespace. |
| `cpus` | `integer` | How many cores are available to the codespace. |
| `display_name` | `string` | The display name of the machine includes cores, memory, and storage. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `codespace_machines_for_authenticated_user` | `SELECT` | `codespace_name` | List the machine types a codespace can transition to use.<br /><br />You must authenticate using an access token with the `codespace` scope to use this endpoint. |
| `repo_machines_for_authenticated_user` | `SELECT` | `location, owner, repo` | List the machine types available for a given repository based on its configuration.<br /><br />Location is required.<br /><br />You must authenticate using an access token with the `codespace` scope to use this endpoint. |
