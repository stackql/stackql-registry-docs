---
title: services_all_risky_ip_download_report
hide_title: false
hide_table_of_contents: false
keywords:
  - services_all_risky_ip_download_report
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
<tr><td><b>Name</b></td><td><code>services_all_risky_ip_download_report</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.ad_hybrid_health_service.services_all_risky_ip_download_report</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `blobCreateDateTime` | `string` | Time at which the new Risky IP report was requested. |
| `jobCompletionTime` | `string` | Time at which the blob creation job for the new Risky IP report was completed. |
| `resultSasUri` | `string` | The blob uri for the report. |
| `serviceId` | `string` | The service id for whom the report belongs to. |
| `status` | `string` | Status of the Risky IP report generation. |
| `tenantId` | `string` | The tenant id for whom the report belongs to. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `serviceName` |
| `_list` | `EXEC` | `serviceName` |
