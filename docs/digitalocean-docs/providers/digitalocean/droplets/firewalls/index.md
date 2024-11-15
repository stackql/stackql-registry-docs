---
title: firewalls
hide_title: false
hide_table_of_contents: false
keywords:
  - firewalls
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

Creates, updates, deletes, gets or lists a <code>firewalls</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>firewalls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.droplets.firewalls" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | A unique ID that can be used to identify and reference a firewall. |
| <CopyableCode code="name" /> | `string` | A human-readable name for a firewall. The name must begin with an alphanumeric character. Subsequent characters must either be alphanumeric characters, a period (.), or a dash (-). |
| <CopyableCode code="created_at" /> | `string` | A time value given in ISO8601 combined date and time format that represents when the firewall was created. |
| <CopyableCode code="droplet_ids" /> | `array` | An array containing the IDs of the Droplets assigned to the firewall. |
| <CopyableCode code="inbound_rules" /> | `array` |  |
| <CopyableCode code="outbound_rules" /> | `array` |  |
| <CopyableCode code="pending_changes" /> | `array` | An array of objects each containing the fields "droplet_id", "removing", and "status". It is provided to detail exactly which Droplets are having their security policies updated. When empty, all changes have been successfully applied. |
| <CopyableCode code="status" /> | `string` | A status string indicating the current state of the firewall. This can be "waiting", "succeeded", or "failed". |
| <CopyableCode code="tags" /> | `array` | An array containing the names of the Tags assigned to the firewall. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="droplets_list_firewalls" /> | `SELECT` | <CopyableCode code="droplet_id" /> | To retrieve a list of all firewalls available to a Droplet, send a GET request to `/v2/droplets/$DROPLET_ID/firewalls` The response will be a JSON object that has a key called `firewalls`. This will be set to an array of `firewall` objects, each of which contain the standard `firewall` attributes. |

## `SELECT` examples

To retrieve a list of all firewalls available to a Droplet, send a GET request to `/v2/droplets/$DROPLET_ID/firewalls` The response will be a JSON object that has a key called `firewalls`. This will be set to an array of `firewall` objects, each of which contain the standard `firewall` attributes.


```sql
SELECT
id,
name,
created_at,
droplet_ids,
inbound_rules,
outbound_rules,
pending_changes,
status,
tags
FROM digitalocean.droplets.firewalls
WHERE droplet_id = '{{ droplet_id }}';
```