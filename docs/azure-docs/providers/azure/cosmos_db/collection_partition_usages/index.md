---
title: collection_partition_usages
hide_title: false
hide_table_of_contents: false
keywords:
  - collection_partition_usages
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
<tr><td><b>Name</b></td><td><code>collection_partition_usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.collection_partition_usages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `object` | A metric name. |
| <CopyableCode code="currentValue" /> | `integer` | Current value for this metric |
| <CopyableCode code="limit" /> | `integer` | Maximum value for this metric |
| <CopyableCode code="partitionId" /> | `string` | The partition id (GUID identifier) of the usages. |
| <CopyableCode code="partitionKeyRangeId" /> | `string` | The partition key range id (integer identifier) of the usages. |
| <CopyableCode code="quotaPeriod" /> | `string` | The quota period used to summarize the usage values. |
| <CopyableCode code="unit" /> | `string` | The unit of the metric. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, collectionRid, databaseRid, resourceGroupName, subscriptionId" /> |
