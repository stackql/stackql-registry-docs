---
title: containers
hide_title: false
hide_table_of_contents: false
keywords:
  - containers
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
<tr><td><b>Name</b></td><td><code>containers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.containers.containers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Container ID. |
| `ContainerGroup_attributes` | `object` | Attributes for a container group. |
| `ContainerGroup_id` | `string` | Container Group ID. |
| `ContainerGroup_type` | `string` | Type of container group. |
| `attributes` | `object` | Attributes for a container. |
| `relationships` | `object` | Relationships to containers inside a container group. |
| `type` | `string` | Type of container. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_containers` | `SELECT` | `dd_site` |
| `_list_containers` | `EXEC` | `dd_site` |
