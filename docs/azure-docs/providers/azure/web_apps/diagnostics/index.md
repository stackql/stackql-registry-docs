---
title: diagnostics
hide_title: false
hide_table_of_contents: false
keywords:
  - diagnostics
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
<tr><td><b>Name</b></td><td><code>diagnostics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.web_apps.diagnostics</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Diagnostics_ExecuteSiteAnalysis` | `EXEC` | `analysisName, diagnosticCategory, resourceGroupName, siteName, subscriptionId` | Description for Execute Analysis |
| `Diagnostics_ExecuteSiteAnalysisSlot` | `EXEC` | `analysisName, diagnosticCategory, resourceGroupName, siteName, slot, subscriptionId` | Description for Execute Analysis |
| `Diagnostics_ExecuteSiteDetector` | `EXEC` | `detectorName, diagnosticCategory, resourceGroupName, siteName, subscriptionId` | Description for Execute Detector |
| `Diagnostics_ExecuteSiteDetectorSlot` | `EXEC` | `detectorName, diagnosticCategory, resourceGroupName, siteName, slot, subscriptionId` | Description for Execute Detector |
| `Diagnostics_GetHostingEnvironmentDetectorResponse` | `EXEC` | `detectorName, name, resourceGroupName, subscriptionId` | Description for Get Hosting Environment Detector Response |
| `Diagnostics_GetSiteAnalysis` | `EXEC` | `analysisName, diagnosticCategory, resourceGroupName, siteName, subscriptionId` | Description for Get Site Analysis |
| `Diagnostics_GetSiteAnalysisSlot` | `EXEC` | `analysisName, diagnosticCategory, resourceGroupName, siteName, slot, subscriptionId` | Description for Get Site Analysis |
| `Diagnostics_GetSiteDetector` | `EXEC` | `detectorName, diagnosticCategory, resourceGroupName, siteName, subscriptionId` | Description for Get Detector |
| `Diagnostics_GetSiteDetectorResponse` | `EXEC` | `detectorName, resourceGroupName, siteName, subscriptionId` | Description for Get site detector response |
| `Diagnostics_GetSiteDetectorResponseSlot` | `EXEC` | `detectorName, resourceGroupName, siteName, slot, subscriptionId` | Description for Get site detector response |
| `Diagnostics_GetSiteDetectorSlot` | `EXEC` | `detectorName, diagnosticCategory, resourceGroupName, siteName, slot, subscriptionId` | Description for Get Detector |
| `Diagnostics_GetSiteDiagnosticCategory` | `EXEC` | `diagnosticCategory, resourceGroupName, siteName, subscriptionId` | Description for Get Diagnostics Category |
| `Diagnostics_GetSiteDiagnosticCategorySlot` | `EXEC` | `diagnosticCategory, resourceGroupName, siteName, slot, subscriptionId` | Description for Get Diagnostics Category |
| `Diagnostics_ListHostingEnvironmentDetectorResponses` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for List Hosting Environment Detector Responses |
| `Diagnostics_ListSiteAnalyses` | `EXEC` | `diagnosticCategory, resourceGroupName, siteName, subscriptionId` | Description for Get Site Analyses |
| `Diagnostics_ListSiteAnalysesSlot` | `EXEC` | `diagnosticCategory, resourceGroupName, siteName, slot, subscriptionId` | Description for Get Site Analyses |
| `Diagnostics_ListSiteDetectorResponses` | `EXEC` | `resourceGroupName, siteName, subscriptionId` | Description for List Site Detector Responses |
| `Diagnostics_ListSiteDetectorResponsesSlot` | `EXEC` | `resourceGroupName, siteName, slot, subscriptionId` | Description for List Site Detector Responses |
| `Diagnostics_ListSiteDetectors` | `EXEC` | `diagnosticCategory, resourceGroupName, siteName, subscriptionId` | Description for Get Detectors |
| `Diagnostics_ListSiteDetectorsSlot` | `EXEC` | `diagnosticCategory, resourceGroupName, siteName, slot, subscriptionId` | Description for Get Detectors |
| `Diagnostics_ListSiteDiagnosticCategories` | `EXEC` | `resourceGroupName, siteName, subscriptionId` | Description for Get Diagnostics Categories |
| `Diagnostics_ListSiteDiagnosticCategoriesSlot` | `EXEC` | `resourceGroupName, siteName, slot, subscriptionId` | Description for Get Diagnostics Categories |
