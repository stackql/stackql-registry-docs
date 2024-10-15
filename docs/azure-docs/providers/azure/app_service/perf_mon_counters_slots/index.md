---
title: perf_mon_counters_slots
hide_title: false
hide_table_of_contents: false
keywords:
  - perf_mon_counters_slots
  - app_service
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>perf_mon_counters_slots</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>perf_mon_counters_slots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.perf_mon_counters_slots" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="code" /> | `string` | The response code. |
| <CopyableCode code="data" /> | `object` | Metric information. |
| <CopyableCode code="message" /> | `string` | The message. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Gets perfmon counters for web app. |

## `SELECT` examples

Description for Gets perfmon counters for web app.


```sql
SELECT
code,
data,
message
FROM azure.app_service.perf_mon_counters_slots
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND slot = '{{ slot }}'
AND subscriptionId = '{{ subscriptionId }}';
```