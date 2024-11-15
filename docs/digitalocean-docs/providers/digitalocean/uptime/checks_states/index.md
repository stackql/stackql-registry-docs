---
title: checks_states
hide_title: false
hide_table_of_contents: false
keywords:
  - checks_states
  - uptime
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

Creates, updates, deletes, gets or lists a <code>checks_states</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>checks_states</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.uptime.checks_states" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="previous_outage" /> | `object` |  |
| <CopyableCode code="regions" /> | `object` | A map of region to regional state |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="uptime_get_check_state" /> | `SELECT` | <CopyableCode code="check_id" /> | To show information about an existing check's state, send a GET request to `/v2/uptime/checks/$CHECK_ID/state`. |

## `SELECT` examples

To show information about an existing check's state, send a GET request to `/v2/uptime/checks/$CHECK_ID/state`.


```sql
SELECT
previous_outage,
regions
FROM digitalocean.uptime.checks_states
WHERE check_id = '{{ check_id }}';
```