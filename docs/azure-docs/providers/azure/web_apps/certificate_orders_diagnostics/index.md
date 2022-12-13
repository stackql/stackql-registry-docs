---
title: certificate_orders_diagnostics
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_orders_diagnostics
  - web_apps
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
<tr><td><b>Name</b></td><td><code>certificate_orders_diagnostics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.web_apps.certificate_orders_diagnostics</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `CertificateOrdersDiagnostics_GetAppServiceCertificateOrderDetectorResponse` | `EXEC` | `certificateOrderName, detectorName, resourceGroupName, subscriptionId` | Description for Microsoft.CertificateRegistration call to get a detector response from App Lens. |
| `CertificateOrdersDiagnostics_ListAppServiceCertificateOrderDetectorResponse` | `EXEC` | `certificateOrderName, resourceGroupName, subscriptionId` | Description for Microsoft.CertificateRegistration to get the list of detectors for this RP. |
