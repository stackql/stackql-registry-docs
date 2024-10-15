---
title: resource_stats
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_stats
  - iot_hub
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

Creates, updates, deletes, gets or lists a <code>resource_stats</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_stats</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_hub.resource_stats" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="disabledDeviceCount" /> | `integer` | The count of disabled devices in the identity registry. |
| <CopyableCode code="enabledDeviceCount" /> | `integer` | The count of enabled devices in the identity registry. |
| <CopyableCode code="totalDeviceCount" /> | `integer` | The total count of devices in the identity registry. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Get the statistics from an IoT hub. |

## `SELECT` examples

Get the statistics from an IoT hub.


```sql
SELECT
disabledDeviceCount,
enabledDeviceCount,
totalDeviceCount
FROM azure.iot_hub.resource_stats
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```