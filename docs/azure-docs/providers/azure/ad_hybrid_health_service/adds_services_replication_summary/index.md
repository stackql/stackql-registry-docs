---
title: adds_services_replication_summary
hide_title: false
hide_table_of_contents: false
keywords:
  - adds_services_replication_summary
  - ad_hybrid_health_service
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
<tr><td><b>Name</b></td><td><code>adds_services_replication_summary</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ad_hybrid_health_service.adds_services_replication_summary" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="domain" /> | `string` | The domain name for a given domain controller. |
| <CopyableCode code="inboundNeighborCollection" /> | `array` | List of individual domain controller neighbor's inbound replication status. |
| <CopyableCode code="lastAttemptedSync" /> | `string` | The last time when a sync was attempted for a given domain controller. |
| <CopyableCode code="lastSuccessfulSync" /> | `string` | The time when the last successful sync happened for a given domain controller. |
| <CopyableCode code="site" /> | `string` | The site name for a given domain controller. |
| <CopyableCode code="status" /> | `integer` | The health status for a domain controller. |
| <CopyableCode code="targetServer" /> | `string` | The domain controller name. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="isGroupbySite, nextPartitionKey, nextRowKey, query, serviceName" /> |
