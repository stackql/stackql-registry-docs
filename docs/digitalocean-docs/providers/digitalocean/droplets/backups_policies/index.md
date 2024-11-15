---
title: backups_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - backups_policies
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

Creates, updates, deletes, gets or lists a <code>backups_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backups_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.droplets.backups_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="column_anon" /> | `` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="droplets_get_backup_policy" /> | `SELECT` | <CopyableCode code="droplet_id" /> | To show information about an individual Droplet's backup policy, send a GET request to `/v2/droplets/$DROPLET_ID/backups/policy`. |
| <CopyableCode code="droplets_list_backup_policies" /> | `SELECT` | <CopyableCode code="" /> | To list information about the backup policies for all Droplets in the account, send a GET request to `/v2/droplets/backups/policies`. |

## `SELECT` examples

To list information about the backup policies for all Droplets in the account, send a GET request to `/v2/droplets/backups/policies`.


```sql
SELECT
column_anon
FROM digitalocean.droplets.backups_policies
;
```