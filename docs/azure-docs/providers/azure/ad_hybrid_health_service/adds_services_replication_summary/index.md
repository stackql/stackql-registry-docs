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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>adds_services_replication_summary</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.ad_hybrid_health_service.adds_services_replication_summary</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `domain` | `string` | The domain name for a given domain controller. |
| `inboundNeighborCollection` | `array` | List of individual domain controller neighbor's inbound replication status. |
| `lastAttemptedSync` | `string` | The last time when a sync was attempted for a given domain controller. |
| `lastSuccessfulSync` | `string` | The time when the last successful sync happened for a given domain controller. |
| `site` | `string` | The site name for a given domain controller. |
| `status` | `integer` | The health status for a domain controller. |
| `targetServer` | `string` | The domain controller name. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `isGroupbySite, nextPartitionKey, nextRowKey, query, serviceName` |
| `_list` | `EXEC` | `isGroupbySite, nextPartitionKey, nextRowKey, query, serviceName` |
