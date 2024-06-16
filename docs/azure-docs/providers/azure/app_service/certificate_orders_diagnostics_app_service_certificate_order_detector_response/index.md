---
title: certificate_orders_diagnostics_app_service_certificate_order_detector_response
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_orders_diagnostics_app_service_certificate_order_detector_response
  - app_service
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
<tr><td><b>Name</b></td><td><code>certificate_orders_diagnostics_app_service_certificate_order_detector_response</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.certificate_orders_diagnostics_app_service_certificate_order_detector_response" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | DetectorResponse resource specific properties |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="certificateOrderName, detectorName, resourceGroupName, subscriptionId" /> | Description for Microsoft.CertificateRegistration call to get a detector response from App Lens. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="certificateOrderName, resourceGroupName, subscriptionId" /> | Description for Microsoft.CertificateRegistration to get the list of detectors for this RP. |
