---
title: images
hide_title: false
hide_table_of_contents: false
keywords:
  - images
  - containers
  - datadog    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, monitor, and manage Datadog resources using SQL
custom_edit_url: null
image: /img/providers/datadog/stackql-datadog-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.containers.images</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Container Image ID. |
| `ContainerImageGroup_attributes` | `object` | Attributes for a Container Image Group. |
| `ContainerImageGroup_id` | `string` | Container Image Group ID. |
| `ContainerImageGroup_type` | `string` | Type of Container Image Group. |
| `attributes` | `object` | Attributes for a Container Image. |
| `relationships` | `object` | Relationships inside a Container Image Group. |
| `type` | `string` | Type of Container Image. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_container_images` | `SELECT` | `dd_site` |
| `_list_container_images` | `EXEC` | `dd_site` |
