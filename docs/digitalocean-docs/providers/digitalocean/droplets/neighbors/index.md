---
title: neighbors
hide_title: false
hide_table_of_contents: false
keywords:
  - neighbors
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
<tr><td><b>Name</b></td><td><code>neighbors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.droplets.neighbors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | A unique identifier for each Droplet instance. This is automatically generated upon Droplet creation. |
| `name` | `string` | The human-readable name set for the Droplet instance. |
| `features` | `array` | An array of features enabled on this Droplet. |
| `status` | `string` | A status string indicating the state of the Droplet instance. This may be "new", "active", "off", or "archive". |
| `created_at` | `string` | A time value given in ISO8601 combined date and time format that represents when the Droplet was created. |
| `vpc_uuid` | `string` | A string specifying the UUID of the VPC to which the Droplet is assigned. |
| `tags` | `array` | An array of Tags the Droplet has been tagged with. |
| `snapshot_ids` | `array` | An array of snapshot IDs of any snapshots created from the Droplet instance. |
| `image` | `object` |  |
| `backup_ids` | `array` | An array of backup IDs of any backups that have been taken of the Droplet instance.  Droplet backups are enabled at the time of the instance creation. |
| `size` | `object` |  |
| `disk` | `integer` | The size of the Droplet's disk in gigabytes. |
| `kernel` | `object` | **Note**: All Droplets created after March 2017 use internal kernels by default.<br />These Droplets will have this attribute set to `null`.<br /><br />The current [kernel](https://www.digitalocean.com/docs/droplets/how-to/kernel/)<br />for Droplets with externally managed kernels. This will initially be set to<br />the kernel of the base image when the Droplet is created.<br /> |
| `next_backup_window` | `object` | The details of the Droplet's backups feature, if backups are configured for the Droplet. This object contains keys for the start and end times of the window during which the backup will start. |
| `locked` | `boolean` | A boolean value indicating whether the Droplet has been locked, preventing actions by users. |
| `volume_ids` | `array` | A flat array including the unique identifier for each Block Storage volume attached to the Droplet. |
| `networks` | `object` | The details of the network that are configured for the Droplet instance.  This is an object that contains keys for IPv4 and IPv6.  The value of each of these is an array that contains objects describing an individual IP resource allocated to the Droplet.  These will define attributes like the IP address, netmask, and gateway of the specific network depending on the type of network it is. |
| `vcpus` | `integer` | The number of virtual CPUs. |
| `size_slug` | `string` | The unique slug identifier for the size of this Droplet. |
| `memory` | `integer` | Memory of the Droplet in megabytes. |
| `region` | `object` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_neighbors` | `SELECT` | `droplet_id` |
| `_list_neighbors` | `EXEC` | `droplet_id` |
