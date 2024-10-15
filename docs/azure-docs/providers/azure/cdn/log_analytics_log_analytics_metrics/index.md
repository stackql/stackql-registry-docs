---
title: log_analytics_log_analytics_metrics
hide_title: false
hide_table_of_contents: false
keywords:
  - log_analytics_log_analytics_metrics
  - cdn
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

Creates, updates, deletes, gets or lists a <code>log_analytics_log_analytics_metrics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>log_analytics_log_analytics_metrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.log_analytics_log_analytics_metrics" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="dateTimeBegin" /> | `string` |  |
| <CopyableCode code="dateTimeEnd" /> | `string` |  |
| <CopyableCode code="granularity" /> | `string` |  |
| <CopyableCode code="series" /> | `array` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="customDomains, dateTimeBegin, dateTimeEnd, granularity, metrics, profileName, protocols, resourceGroupName, subscriptionId" /> | Get log report for AFD profile |

## `SELECT` examples

Get log report for AFD profile


```sql
SELECT
dateTimeBegin,
dateTimeEnd,
granularity,
series
FROM azure.cdn.log_analytics_log_analytics_metrics
WHERE customDomains = '{{ customDomains }}'
AND dateTimeBegin = '{{ dateTimeBegin }}'
AND dateTimeEnd = '{{ dateTimeEnd }}'
AND granularity = '{{ granularity }}'
AND metrics = '{{ metrics }}'
AND profileName = '{{ profileName }}'
AND protocols = '{{ protocols }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```