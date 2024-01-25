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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificate_orders_diagnostics_app_service_certificate_order_detector_response</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_service.certificate_orders_diagnostics_app_service_certificate_order_detector_response</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource Name. |
| `kind` | `string` | Kind of resource. |
| `properties` | `object` | DetectorResponse resource specific properties |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `certificateOrderName, detectorName, resourceGroupName, subscriptionId` | Description for Microsoft.CertificateRegistration call to get a detector response from App Lens. |
| `list` | `SELECT` | `certificateOrderName, resourceGroupName, subscriptionId` | Description for Microsoft.CertificateRegistration to get the list of detectors for this RP. |
| `_list` | `EXEC` | `certificateOrderName, resourceGroupName, subscriptionId` | Description for Microsoft.CertificateRegistration to get the list of detectors for this RP. |
