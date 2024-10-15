---
title: resource_quota_metrics
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_quota_metrics
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

Creates, updates, deletes, gets or lists a <code>resource_quota_metrics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_quota_metrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_hub.resource_quota_metrics" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the quota metric. |
| <CopyableCode code="currentValue" /> | `integer` | The current value for the quota metric. |
| <CopyableCode code="maxValue" /> | `integer` | The maximum value of the quota metric. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Get the quota metrics for an IoT hub. |

## `SELECT` examples

Get the quota metrics for an IoT hub.


```sql
SELECT
name,
currentValue,
maxValue
FROM azure.iot_hub.resource_quota_metrics
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```