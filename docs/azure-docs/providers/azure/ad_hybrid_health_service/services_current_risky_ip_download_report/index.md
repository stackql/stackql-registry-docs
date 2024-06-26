---
title: services_current_risky_ip_download_report
hide_title: false
hide_table_of_contents: false
keywords:
  - services_current_risky_ip_download_report
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
<tr><td><b>Name</b></td><td><code>services_current_risky_ip_download_report</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ad_hybrid_health_service.services_current_risky_ip_download_report" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="blobCreateDateTime" /> | `string` | Time at which the new Risky IP report was requested. |
| <CopyableCode code="jobCompletionTime" /> | `string` | Time at which the blob creation job for the new Risky IP report was completed. |
| <CopyableCode code="resultSasUri" /> | `string` | The blob uri for the report. |
| <CopyableCode code="serviceId" /> | `string` | The service id for whom the report belongs to. |
| <CopyableCode code="status" /> | `string` | Status of the Risky IP report generation. |
| <CopyableCode code="tenantId" /> | `string` | The tenant id for whom the report belongs to. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="serviceName" /> |
