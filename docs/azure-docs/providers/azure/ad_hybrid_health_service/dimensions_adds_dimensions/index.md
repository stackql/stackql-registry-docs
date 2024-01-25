---
title: dimensions_adds_dimensions
hide_title: false
hide_table_of_contents: false
keywords:
  - dimensions_adds_dimensions
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
<tr><td><b>Name</b></td><td><code>dimensions_adds_dimensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.ad_hybrid_health_service.dimensions_adds_dimensions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `activeAlerts` | `integer` | The count of alerts that are currently active for the service. |
| `additionalInformation` | `string` | The additional information related to the service. |
| `displayName` | `string` | The display name of the service. |
| `health` | `string` | The health status for the domain controller. |
| `lastUpdated` | `string` | The date or time , in UTC, when the service properties were last updated. |
| `resolvedAlerts` | `integer` | The total count of alerts that has been resolved for the service. |
| `signature` | `string` | The signature of the service. |
| `simpleProperties` | `object` | List of service specific configuration properties. |
| `type` | `string` | The service type for the services onboarded to Azure Active Directory Connect Health. Depending on whether the service is monitoring, ADFS, Sync or ADDS roles, the service type can either be AdFederationService or AadSyncService or AdDomainService. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `dimension, serviceName` |
| `_list` | `EXEC` | `dimension, serviceName` |
