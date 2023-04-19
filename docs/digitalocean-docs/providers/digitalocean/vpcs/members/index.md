---
title: members
hide_title: false
hide_table_of_contents: false
keywords:
  - members
  - vpcs
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
<tr><td><b>Name</b></td><td><code>members</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.vpcs.members</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the resource. |
| `urn` | `string` | The uniform resource name (URN) for the resource in the format do:resource_type:resource_id. |
| `created_at` | `string` | A time value given in ISO8601 combined date and time format that represents when the resource was created. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_members` | `SELECT` | `vpc_id` |
| `_list_members` | `EXEC` | `vpc_id` |
