---
title: services_export_status
hide_title: false
hide_table_of_contents: false
keywords:
  - services_export_status
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
<tr><td><b>Name</b></td><td><code>services_export_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ad_hybrid_health_service.services_export_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="endTime" /> | `string` | The date and time when the export ended. |
| <CopyableCode code="runStepResultId" /> | `string` | The run step result Id. |
| <CopyableCode code="serviceId" /> | `string` | The id of the service for whom the export status is being reported. |
| <CopyableCode code="serviceMemberId" /> | `string` | The server Id for whom the export status is being reported. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="serviceName" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="serviceName" /> |
