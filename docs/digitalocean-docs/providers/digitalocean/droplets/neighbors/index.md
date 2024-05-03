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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>neighbors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.droplets.neighbors" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | A unique identifier for each Droplet instance. This is automatically generated upon Droplet creation. |
| <CopyableCode code="name" /> | `string` | The human-readable name set for the Droplet instance. |
| <CopyableCode code="backup_ids" /> | `array` | An array of backup IDs of any backups that have been taken of the Droplet instance.  Droplet backups are enabled at the time of the instance creation. |
| <CopyableCode code="created_at" /> | `string` | A time value given in ISO8601 combined date and time format that represents when the Droplet was created. |
| <CopyableCode code="disk" /> | `integer` | The size of the Droplet's disk in gigabytes. |
| <CopyableCode code="features" /> | `array` | An array of features enabled on this Droplet. |
| <CopyableCode code="image" /> | `object` |  |
| <CopyableCode code="kernel" /> | `object` | **Note**: All Droplets created after March 2017 use internal kernels by default.<br />These Droplets will have this attribute set to `null`.<br /><br />The current [kernel](https://www.digitalocean.com/docs/droplets/how-to/kernel/)<br />for Droplets with externally managed kernels. This will initially be set to<br />the kernel of the base image when the Droplet is created.<br /> |
| <CopyableCode code="locked" /> | `boolean` | A boolean value indicating whether the Droplet has been locked, preventing actions by users. |
| <CopyableCode code="memory" /> | `integer` | Memory of the Droplet in megabytes. |
| <CopyableCode code="networks" /> | `object` | The details of the network that are configured for the Droplet instance.  This is an object that contains keys for IPv4 and IPv6.  The value of each of these is an array that contains objects describing an individual IP resource allocated to the Droplet.  These will define attributes like the IP address, netmask, and gateway of the specific network depending on the type of network it is. |
| <CopyableCode code="next_backup_window" /> | `object` | The details of the Droplet's backups feature, if backups are configured for the Droplet. This object contains keys for the start and end times of the window during which the backup will start. |
| <CopyableCode code="region" /> | `object` |  |
| <CopyableCode code="size" /> | `object` |  |
| <CopyableCode code="size_slug" /> | `string` | The unique slug identifier for the size of this Droplet. |
| <CopyableCode code="snapshot_ids" /> | `array` | An array of snapshot IDs of any snapshots created from the Droplet instance. |
| <CopyableCode code="status" /> | `string` | A status string indicating the state of the Droplet instance. This may be "new", "active", "off", or "archive". |
| <CopyableCode code="tags" /> | `array` | An array of Tags the Droplet has been tagged with. |
| <CopyableCode code="vcpus" /> | `integer` | The number of virtual CPUs. |
| <CopyableCode code="volume_ids" /> | `array` | A flat array including the unique identifier for each Block Storage volume attached to the Droplet. |
| <CopyableCode code="vpc_uuid" /> | `string` | A string specifying the UUID of the VPC to which the Droplet is assigned. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_neighbors" /> | `SELECT` | <CopyableCode code="droplet_id" /> |
| <CopyableCode code="_list_neighbors" /> | `EXEC` | <CopyableCode code="droplet_id" /> |
