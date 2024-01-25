---
title: service_members_export_status
hide_title: false
hide_table_of_contents: false
keywords:
  - service_members_export_status
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
<tr><td><b>Name</b></td><td><code>service_members_export_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.ad_hybrid_health_service.service_members_export_status</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `endTime` | `string` | The date and time when the export ended. |
| `runStepResultId` | `string` | The run step result Id. |
| `serviceId` | `string` | The id of the service for whom the export status is being reported. |
| `serviceMemberId` | `string` | The server Id for whom the export status is being reported. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `serviceMemberId, serviceName` |
| `_list` | `EXEC` | `serviceMemberId, serviceName` |
