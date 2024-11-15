---
title: backups_supported_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - backups_supported_policies
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

Creates, updates, deletes, gets or lists a <code>backups_supported_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backups_supported_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.droplets.backups_supported_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the Droplet backup plan. |
| <CopyableCode code="possible_days" /> | `array` | The day of the week the backup will occur. |
| <CopyableCode code="possible_window_starts" /> | `array` | An array of integers representing the hours of the day that a backup can start. |
| <CopyableCode code="retention_period_days" /> | `integer` | The number of days that a backup will be kept. |
| <CopyableCode code="window_length_hours" /> | `integer` | The number of hours that a backup window is open. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="droplets_list_supported_backup_policies" /> | `SELECT` | <CopyableCode code="" /> | To retrieve a list of all supported Droplet backup policies, send a GET request to `/v2/droplets/backups/supported_policies`. |

## `SELECT` examples

To retrieve a list of all supported Droplet backup policies, send a GET request to `/v2/droplets/backups/supported_policies`.


```sql
SELECT
name,
possible_days,
possible_window_starts,
retention_period_days,
window_length_hours
FROM digitalocean.droplets.backups_supported_policies
;
```