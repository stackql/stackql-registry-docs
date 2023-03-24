---
title: resources
hide_title: false
hide_table_of_contents: false
keywords:
  - resources
  - tags
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
<tr><td><b>Name</b></td><td><code>resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.tags.resources</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `assign_resources` | `EXEC` | `tag_id, data__resources` | Resources can be tagged by sending a POST request to `/v2/tags/$TAG_NAME/resources` with an array of json objects containing `resource_id` and `resource_type` attributes.<br />Currently only tagging of Droplets, Databases, Images, Volumes, and Volume Snapshots is supported. `resource_type` is expected to be the string `droplet`, `database`, `image`, `volume` or `volume_snapshot`. `resource_id` is expected to be the ID of the resource as a string. |
| `unassign_resources` | `EXEC` | `tag_id, data__resources` | Resources can be untagged by sending a DELETE request to `/v2/tags/$TAG_NAME/resources` with an array of json objects containing `resource_id` and `resource_type` attributes.<br />Currently only untagging of Droplets, Databases, Images, Volumes, and Volume Snapshots is supported. `resource_type` is expected to be the string `droplet`, `database`, `image`, `volume` or `volume_snapshot`. `resource_id` is expected to be the ID of the resource as a string. |
