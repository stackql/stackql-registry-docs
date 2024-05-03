---
title: collection_partition_region_metrics
hide_title: false
hide_table_of_contents: false
keywords:
  - collection_partition_region_metrics
  - cosmos_db
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>collection_partition_region_metrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.collection_partition_region_metrics" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `object` | A metric name. |
| <CopyableCode code="endTime" /> | `string` | The end time for the metric (ISO-8601 format). |
| <CopyableCode code="metricValues" /> | `array` | The metric values for the specified time window and timestep. |
| <CopyableCode code="partitionId" /> | `string` | The partition id (GUID identifier) of the metric values. |
| <CopyableCode code="partitionKeyRangeId" /> | `string` | The partition key range id (integer identifier) of the metric values. |
| <CopyableCode code="startTime" /> | `string` | The start time for the metric (ISO-8601 format). |
| <CopyableCode code="timeGrain" /> | `string` | The time grain to be used to summarize the metric values. |
| <CopyableCode code="unit" /> | `string` | The unit of the metric. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="$filter, accountName, collectionRid, databaseRid, region, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="$filter, accountName, collectionRid, databaseRid, region, resourceGroupName, subscriptionId" /> |
