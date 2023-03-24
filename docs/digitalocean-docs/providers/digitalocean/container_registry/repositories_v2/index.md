---
title: repositories_v2
hide_title: false
hide_table_of_contents: false
keywords:
  - repositories_v2
  - container_registry
  - digitalocean    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>repositories_v2</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.container_registry.repositories_v2</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the repository. |
| `tag_count` | `integer` | The number of tags in the repository. |
| `latest_manifest` | `object` |  |
| `manifest_count` | `integer` | The number of manifests in the repository. |
| `registry_name` | `string` | The name of the container registry. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `registry_list_repositoriesV2` | `SELECT` | `registry_name` |
| `_registry_list_repositoriesV2` | `EXEC` | `registry_name` |
