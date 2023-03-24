---
title: backups
hide_title: false
hide_table_of_contents: false
keywords:
  - backups
  - droplets
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
<tr><td><b>Name</b></td><td><code>backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.droplets.backups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | The unique identifier for the snapshot or backup. |
| `name` | `string` | A human-readable name for the snapshot. |
| `size_gigabytes` | `number` | The billable size of the snapshot in gigabytes. |
| `created_at` | `string` | A time value given in ISO8601 combined date and time format that represents when the snapshot was created. |
| `min_disk_size` | `integer` | The minimum size in GB required for a volume or Droplet to use this snapshot. |
| `type` | `string` | Describes the kind of image. It may be one of `snapshot` or `backup`. This specifies whether an image is a user-generated Droplet snapshot or automatically created Droplet backup. |
| `regions` | `array` | An array of the regions that the snapshot is available in. The regions are represented by their identifying slug values. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_backups` | `SELECT` | `droplet_id` |
| `_list_backups` | `EXEC` | `droplet_id` |
