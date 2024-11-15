---
title: tiers_instance_sizes
hide_title: false
hide_table_of_contents: false
keywords:
  - tiers_instance_sizes
  - apps
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

Creates, updates, deletes, gets or lists a <code>tiers_instance_sizes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tiers_instance_sizes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.apps.tiers_instance_sizes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` |  |
| <CopyableCode code="bandwidth_allowance_gib" /> | `string` |  |
| <CopyableCode code="cpu_type" /> | `string` |  |
| <CopyableCode code="cpus" /> | `string` |  |
| <CopyableCode code="deprecation_intent" /> | `boolean` |  |
| <CopyableCode code="memory_bytes" /> | `string` |  |
| <CopyableCode code="scalable" /> | `boolean` |  |
| <CopyableCode code="single_instance_only" /> | `boolean` |  |
| <CopyableCode code="slug" /> | `string` |  |
| <CopyableCode code="tier_downgrade_to" /> | `string` |  |
| <CopyableCode code="tier_slug" /> | `string` |  |
| <CopyableCode code="tier_upgrade_to" /> | `string` |  |
| <CopyableCode code="usd_per_month" /> | `string` |  |
| <CopyableCode code="usd_per_second" /> | `string` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="apps_get_instance_size" /> | `SELECT` | <CopyableCode code="slug" /> | Retrieve information about a specific instance size for `service`, `worker`, and `job` components. |
| <CopyableCode code="apps_list_instance_sizes" /> | `SELECT` | <CopyableCode code="" /> | List all instance sizes for `service`, `worker`, and `job` components. |

## `SELECT` examples

List all instance sizes for `service`, `worker`, and `job` components.


```sql
SELECT
name,
bandwidth_allowance_gib,
cpu_type,
cpus,
deprecation_intent,
memory_bytes,
scalable,
single_instance_only,
slug,
tier_downgrade_to,
tier_slug,
tier_upgrade_to,
usd_per_month,
usd_per_second
FROM digitalocean.apps.tiers_instance_sizes
;
```