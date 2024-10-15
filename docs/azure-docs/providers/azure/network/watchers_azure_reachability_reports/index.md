---
title: watchers_azure_reachability_reports
hide_title: false
hide_table_of_contents: false
keywords:
  - watchers_azure_reachability_reports
  - network
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

Creates, updates, deletes, gets or lists a <code>watchers_azure_reachability_reports</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>watchers_azure_reachability_reports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.watchers_azure_reachability_reports" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="aggregationLevel" /> | `string` | The aggregation level of Azure reachability report. Can be Country, State or City. |
| <CopyableCode code="providerLocation" /> | `object` | Parameters that define a geographic location. |
| <CopyableCode code="reachabilityReport" /> | `array` | List of Azure reachability report items. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkWatcherName, resourceGroupName, subscriptionId, data__endTime, data__providerLocation, data__startTime" /> | NOTE: This feature is currently in preview and still being tested for stability. Gets the relative latency score for internet service providers from a specified location to Azure regions. |

## `SELECT` examples

NOTE: This feature is currently in preview and still being tested for stability. Gets the relative latency score for internet service providers from a specified location to Azure regions.


```sql
SELECT
aggregationLevel,
providerLocation,
reachabilityReport
FROM azure.network.watchers_azure_reachability_reports
WHERE networkWatcherName = '{{ networkWatcherName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND data__endTime = '{{ data__endTime }}'
AND data__providerLocation = '{{ data__providerLocation }}'
AND data__startTime = '{{ data__startTime }}';
```