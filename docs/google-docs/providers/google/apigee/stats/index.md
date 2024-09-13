---
title: stats
hide_title: false
hide_table_of_contents: false
keywords:
  - stats
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

Creates, updates, deletes, gets or lists a <code>stats</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stats</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.stats" /></td></tr>
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
| <CopyableCode code="organizations_environments_stats_get" /> | `SELECT` | <CopyableCode code="environmentsId, organizationsId, statsId" /> | Retrieve metrics grouped by dimensions. The types of metrics you can retrieve include traffic, message counts, API call latency, response size, and cache hits and counts. Dimensions let you view metrics in meaningful groups. You can optionally pass dimensions as path parameters to the `stats` API. If dimensions are not specified, the metrics are computed on the entire set of data for the given time range. |

## `SELECT` examples

Retrieve metrics grouped by dimensions. The types of metrics you can retrieve include traffic, message counts, API call latency, response size, and cache hits and counts. Dimensions let you view metrics in meaningful groups. You can optionally pass dimensions as path parameters to the `stats` API. If dimensions are not specified, the metrics are computed on the entire set of data for the given time range.

```sql
SELECT
environments,
hosts,
metaData
FROM google.apigee.stats
WHERE environmentsId = '{{ environmentsId }}'
AND organizationsId = '{{ organizationsId }}'
AND statsId = '{{ statsId }}'; 
```
