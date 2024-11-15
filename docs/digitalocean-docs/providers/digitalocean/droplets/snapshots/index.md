---
title: snapshots
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshots
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

Creates, updates, deletes, gets or lists a <code>snapshots</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>snapshots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.droplets.snapshots" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | The unique identifier for the snapshot or backup. |
| <CopyableCode code="name" /> | `string` | A human-readable name for the snapshot. |
| <CopyableCode code="created_at" /> | `string` | A time value given in ISO8601 combined date and time format that represents when the snapshot was created. |
| <CopyableCode code="min_disk_size" /> | `integer` | The minimum size in GB required for a volume or Droplet to use this snapshot. |
| <CopyableCode code="regions" /> | `array` | An array of the regions that the snapshot is available in. The regions are represented by their identifying slug values. |
| <CopyableCode code="size_gigabytes" /> | `number` | The billable size of the snapshot in gigabytes. |
| <CopyableCode code="type" /> | `string` | Describes the kind of image. It may be one of `snapshot` or `backup`. This specifies whether an image is a user-generated Droplet snapshot or automatically created Droplet backup. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="droplets_list_snapshots" /> | `SELECT` | <CopyableCode code="droplet_id" /> | To retrieve the snapshots that have been created from a Droplet, send a GET request to `/v2/droplets/$DROPLET_ID/snapshots`. You will get back a JSON object that has a `snapshots` key. This will be set to an array of snapshot objects, each of which contain the standard Droplet snapshot attributes. |

## `SELECT` examples

To retrieve the snapshots that have been created from a Droplet, send a GET request to `/v2/droplets/$DROPLET_ID/snapshots`. You will get back a JSON object that has a `snapshots` key. This will be set to an array of snapshot objects, each of which contain the standard Droplet snapshot attributes.


```sql
SELECT
id,
name,
created_at,
min_disk_size,
regions,
size_gigabytes,
type
FROM digitalocean.droplets.snapshots
WHERE droplet_id = '{{ droplet_id }}';
```