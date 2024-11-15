---
title: neighbors
hide_title: false
hide_table_of_contents: false
keywords:
  - neighbors
  - droplets
  - digitalocean
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage digitalocean resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>neighbors</code> resource.

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
| <CopyableCode code="backup_ids" /> | `array` | An array of backup IDs of any backups that have been taken of the Droplet instance. Droplet backups are enabled at the time of the instance creation. |
| <CopyableCode code="created_at" /> | `string` | A time value given in ISO8601 combined date and time format that represents when the Droplet was created. |
| <CopyableCode code="disk" /> | `integer` | The size of the Droplet's disk in gigabytes. |
| <CopyableCode code="disk_info" /> | `array` | An array of objects containing information about the disks available to the Droplet. |
| <CopyableCode code="features" /> | `array` | An array of features enabled on this Droplet. |
| <CopyableCode code="gpu_info" /> | `object` | An object containing information about the GPU capabilities of Droplets created with this size. |
| <CopyableCode code="image" /> | `object` |  |
| <CopyableCode code="kernel" /> | `object` | **Note**: All Droplets created after March 2017 use internal kernels by default. These Droplets will have this attribute set to `null`. The current [kernel](https://docs.digitalocean.com/products/droplets/how-to/kernel/) for Droplets with externally managed kernels. This will initially be set to the kernel of the base image when the Droplet is created. |
| <CopyableCode code="locked" /> | `boolean` | A boolean value indicating whether the Droplet has been locked, preventing actions by users. |
| <CopyableCode code="memory" /> | `integer` | Memory of the Droplet in megabytes. |
| <CopyableCode code="networks" /> | `object` | The details of the network that are configured for the Droplet instance. This is an object that contains keys for IPv4 and IPv6. The value of each of these is an array that contains objects describing an individual IP resource allocated to the Droplet. These will define attributes like the IP address, netmask, and gateway of the specific network depending on the type of network it is. |
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
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="droplets_list_neighbors" /> | `SELECT` | <CopyableCode code="droplet_id" /> | To retrieve a list of any "neighbors" (i.e. Droplets that are co-located on the same physical hardware) for a specific Droplet, send a GET request to `/v2/droplets/$DROPLET_ID/neighbors`. The results will be returned as a JSON object with a key of `droplets`. This will be set to an array containing objects representing any other Droplets that share the same physical hardware. An empty array indicates that the Droplet is not co-located any other Droplets associated with your account. |

## `SELECT` examples

To retrieve a list of any "neighbors" (i.e. Droplets that are co-located on the same physical hardware) for a specific Droplet, send a GET request to `/v2/droplets/$DROPLET_ID/neighbors`. The results will be returned as a JSON object with a key of `droplets`. This will be set to an array containing objects representing any other Droplets that share the same physical hardware. An empty array indicates that the Droplet is not co-located any other Droplets associated with your account.


```sql
SELECT
id,
name,
backup_ids,
created_at,
disk,
disk_info,
features,
gpu_info,
image,
kernel,
locked,
memory,
networks,
next_backup_window,
region,
size,
size_slug,
snapshot_ids,
status,
tags,
vcpus,
volume_ids,
vpc_uuid
FROM digitalocean.droplets.neighbors
WHERE droplet_id = '{{ droplet_id }}';
```