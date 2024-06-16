---
title: collection_metric_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - collection_metric_definitions
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
<tr><td><b>Name</b></td><td><code>collection_metric_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.collection_metric_definitions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `object` | A metric name. |
| <CopyableCode code="metricAvailabilities" /> | `array` | The list of metric availabilities for the account. |
| <CopyableCode code="primaryAggregationType" /> | `string` | The primary aggregation type of the metric. |
| <CopyableCode code="resourceUri" /> | `string` | The resource uri of the database. |
| <CopyableCode code="unit" /> | `string` | The unit of the metric. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, collectionRid, databaseRid, resourceGroupName, subscriptionId" /> |
