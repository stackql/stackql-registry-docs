---
title: watchers_flow_log_status
hide_title: false
hide_table_of_contents: false
keywords:
  - watchers_flow_log_status
  - network
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
<tr><td><b>Name</b></td><td><code>watchers_flow_log_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.watchers_flow_log_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="flowAnalyticsConfiguration" /> | `object` | Parameters that define the configuration of traffic analytics. |
| <CopyableCode code="properties" /> | `object` | Parameters that define the configuration of flow log. |
| <CopyableCode code="targetResourceId" /> | `string` | The ID of the resource to configure for flow log and traffic analytics (optional) . |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkWatcherName, resourceGroupName, subscriptionId, data__targetResourceId" /> |
