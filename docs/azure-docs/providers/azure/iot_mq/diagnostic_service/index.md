---
title: diagnostic_service
hide_title: false
hide_table_of_contents: false
keywords:
  - diagnostic_service
  - iot_mq
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
<tr><td><b>Name</b></td><td><code>diagnostic_service</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_mq.diagnostic_service" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | ExtendedLocation properties |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | MQ Diagnostic Services Resource properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="diagnosticServiceName, mqName, resourceGroupName, subscriptionId" /> | Get a DiagnosticServiceResource |
| <CopyableCode code="list_by_mq_resource" /> | `SELECT` | <CopyableCode code="mqName, resourceGroupName, subscriptionId" /> | List DiagnosticServiceResource resources by MqResource |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="diagnosticServiceName, mqName, resourceGroupName, subscriptionId, data__extendedLocation" /> | Create a DiagnosticServiceResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="diagnosticServiceName, mqName, resourceGroupName, subscriptionId" /> | Delete a DiagnosticServiceResource |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="diagnosticServiceName, mqName, resourceGroupName, subscriptionId" /> | Update a DiagnosticServiceResource |
