---
title: sql_assessment_v2_summary_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_assessment_v2_summary_operations
  - migrate
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
<tr><td><b>Name</b></td><td><code>sql_assessment_v2_summary_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.migrate.sql_assessment_v2_summary_operations</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `assessmentName, groupName, projectName, resourceGroupName, subscriptionId, summaryName` | Get a SqlAssessmentV2Summary |
| `list_by_sql_assessment_v2` | `SELECT` | `assessmentName, groupName, projectName, resourceGroupName, subscriptionId` | List SqlAssessmentV2Summary resources by SqlAssessmentV2 |
| `_list_by_sql_assessment_v2` | `EXEC` | `assessmentName, groupName, projectName, resourceGroupName, subscriptionId` | List SqlAssessmentV2Summary resources by SqlAssessmentV2 |
