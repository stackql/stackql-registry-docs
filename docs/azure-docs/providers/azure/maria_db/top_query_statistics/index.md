---
title: top_query_statistics
hide_title: false
hide_table_of_contents: false
keywords:
  - top_query_statistics
  - maria_db
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
<tr><td><b>Name</b></td><td><code>top_query_statistics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.maria_db.top_query_statistics" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="queryStatisticId, resourceGroupName, serverName, subscriptionId" /> | Retrieve the query statistic for specified identifier. |
| <CopyableCode code="list_by_server" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId, data__properties" /> | Retrieve the Query-Store top queries for specified metric and aggregation. |
| <CopyableCode code="_list_by_server" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverName, subscriptionId, data__properties" /> | Retrieve the Query-Store top queries for specified metric and aggregation. |
