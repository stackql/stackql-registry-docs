---
title: log_analytics_log_analytics_rankings
hide_title: false
hide_table_of_contents: false
keywords:
  - log_analytics_log_analytics_rankings
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

Creates, updates, deletes, gets or lists a <code>log_analytics_log_analytics_rankings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>log_analytics_log_analytics_rankings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.log_analytics_log_analytics_rankings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="dateTimeBegin" /> | `string` |  |
| <CopyableCode code="dateTimeEnd" /> | `string` |  |
| <CopyableCode code="tables" /> | `array` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dateTimeBegin, dateTimeEnd, maxRanking, metrics, profileName, rankings, resourceGroupName, subscriptionId" /> | Get log analytics ranking report for AFD profile |

## `SELECT` examples

Get log analytics ranking report for AFD profile


```sql
SELECT
dateTimeBegin,
dateTimeEnd,
tables
FROM azure.cdn.log_analytics_log_analytics_rankings
WHERE dateTimeBegin = '{{ dateTimeBegin }}'
AND dateTimeEnd = '{{ dateTimeEnd }}'
AND maxRanking = '{{ maxRanking }}'
AND metrics = '{{ metrics }}'
AND profileName = '{{ profileName }}'
AND rankings = '{{ rankings }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```