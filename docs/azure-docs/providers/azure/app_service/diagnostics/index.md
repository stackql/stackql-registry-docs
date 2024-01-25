---
title: diagnostics
hide_title: false
hide_table_of_contents: false
keywords:
  - diagnostics
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
<tr><td><b>Name</b></td><td><code>diagnostics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_service.diagnostics</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `execute_site_analysis` | `EXEC` | `analysisName, diagnosticCategory, resourceGroupName, siteName, subscriptionId` | Description for Execute Analysis |
| `execute_site_analysis_slot` | `EXEC` | `analysisName, diagnosticCategory, resourceGroupName, siteName, slot, subscriptionId` | Description for Execute Analysis |
| `execute_site_detector` | `EXEC` | `detectorName, diagnosticCategory, resourceGroupName, siteName, subscriptionId` | Description for Execute Detector |
| `execute_site_detector_slot` | `EXEC` | `detectorName, diagnosticCategory, resourceGroupName, siteName, slot, subscriptionId` | Description for Execute Detector |
