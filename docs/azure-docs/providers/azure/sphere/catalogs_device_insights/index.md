---
title: catalogs_device_insights
hide_title: false
hide_table_of_contents: false
keywords:
  - catalogs_device_insights
  - sphere
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

Creates, updates, deletes, gets or lists a <code>catalogs_device_insights</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>catalogs_device_insights</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sphere.catalogs_device_insights" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `string` | Event description |
| <CopyableCode code="deviceId" /> | `string` | Device ID |
| <CopyableCode code="endTimestampUtc" /> | `string` | Event end timestamp |
| <CopyableCode code="eventCategory" /> | `string` | Event category |
| <CopyableCode code="eventClass" /> | `string` | Event class |
| <CopyableCode code="eventCount" /> | `integer` | Event count |
| <CopyableCode code="eventType" /> | `string` | Event type |
| <CopyableCode code="startTimestampUtc" /> | `string` | Event start timestamp |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="catalogName, resourceGroupName, subscriptionId" /> | Lists device insights for catalog. |

## `SELECT` examples

Lists device insights for catalog.


```sql
SELECT
description,
deviceId,
endTimestampUtc,
eventCategory,
eventClass,
eventCount,
eventType,
startTimestampUtc
FROM azure.sphere.catalogs_device_insights
WHERE catalogName = '{{ catalogName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```