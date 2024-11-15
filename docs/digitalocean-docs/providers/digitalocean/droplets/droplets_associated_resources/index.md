---
title: droplets_associated_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - droplets_associated_resources
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

Creates, updates, deletes, gets or lists a <code>droplets_associated_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>droplets_associated_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.droplets.droplets_associated_resources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="floating_ips" /> | `array` |  |
| <CopyableCode code="reserved_ips" /> | `array` |  |
| <CopyableCode code="snapshots" /> | `array` |  |
| <CopyableCode code="volume_snapshots" /> | `array` |  |
| <CopyableCode code="volumes" /> | `array` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="droplets_list_associated_resources" /> | `SELECT` | <CopyableCode code="droplet_id" /> | To list the associated billable resources that can be destroyed along with a Droplet, send a GET request to the `/v2/droplets/$DROPLET_ID/destroy_with_associated_resources` endpoint. The response will be a JSON object containing `snapshots`, `volumes`, and `volume_snapshots` keys. Each will be set to an array of objects containing information about the associated resources. |

## `SELECT` examples

To list the associated billable resources that can be destroyed along with a Droplet, send a GET request to the `/v2/droplets/$DROPLET_ID/destroy_with_associated_resources` endpoint. The response will be a JSON object containing `snapshots`, `volumes`, and `volume_snapshots` keys. Each will be set to an array of objects containing information about the associated resources.


```sql
SELECT
floating_ips,
reserved_ips,
snapshots,
volume_snapshots,
volumes
FROM digitalocean.droplets.droplets_associated_resources
WHERE droplet_id = '{{ droplet_id }}';
```