---
title: host_stats
hide_title: false
hide_table_of_contents: false
keywords:
  - host_stats
  - apigee
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

Creates, updates, deletes or gets an <code>host_stat</code> resource or lists <code>host_stats</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>host_stats</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.host_stats" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="environments" /> | `array` | List of query results on the environment level. |
| <CopyableCode code="hosts" /> | `array` | List of query results grouped by host. |
| <CopyableCode code="metaData" /> | `object` | Encapsulates additional information about query execution. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_host_stats_get" /> | `SELECT` | <CopyableCode code="hostStatsId, organizationsId" /> | Retrieve metrics grouped by dimensions in host level. The types of metrics you can retrieve include traffic, message counts, API call latency, response size, and cache hits and counts. Dimensions let you view metrics in meaningful groups. You can optionally pass dimensions as path parameters to the `stats` API. If dimensions are not specified, the metrics are computed on the entire set of data for the given time range. |

## `SELECT` examples

Retrieve metrics grouped by dimensions in host level. The types of metrics you can retrieve include traffic, message counts, API call latency, response size, and cache hits and counts. Dimensions let you view metrics in meaningful groups. You can optionally pass dimensions as path parameters to the `stats` API. If dimensions are not specified, the metrics are computed on the entire set of data for the given time range.

```sql
SELECT
environments,
hosts,
metaData
FROM google.apigee.host_stats
WHERE hostStatsId = '{{ hostStatsId }}'
AND organizationsId = '{{ organizationsId }}'; 
```
