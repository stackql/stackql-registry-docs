---
title: analysis_results
hide_title: false
hide_table_of_contents: false
keywords:
  - analysis_results
  - test_base
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>analysis_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.test_base.analysis_results</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `properties` | `object` | The properties of Analysis Result resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AnalysisResults_Get` | `SELECT` | `analysisResultName, packageName, resourceGroupName, subscriptionId, testBaseAccountName, testResultName` | Gets an Analysis Result of a Test Result by name. |
| `AnalysisResults_List` | `SELECT` | `analysisResultType, packageName, resourceGroupName, subscriptionId, testBaseAccountName, testResultName` | Lists the Analysis Results of a Test Result. The result collection will only contain one element as all the data will be nested in a singleton object. |
