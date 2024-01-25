---
title: sql_assessment_v2_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_assessment_v2_operations
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
<tr><td><b>Name</b></td><td><code>sql_assessment_v2_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.migrate.sql_assessment_v2_operations</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `assessmentName, groupName, projectName, resourceGroupName, subscriptionId` | Get a SqlAssessmentV2 |
| `list_by_group` | `SELECT` | `groupName, projectName, resourceGroupName, subscriptionId` | List SqlAssessmentV2 resources by Group |
| `create` | `INSERT` | `assessmentName, groupName, projectName, resourceGroupName, subscriptionId` | Create a SqlAssessmentV2 |
| `delete` | `DELETE` | `assessmentName, groupName, projectName, resourceGroupName, subscriptionId` | Delete a SqlAssessmentV2 |
| `_list_by_group` | `EXEC` | `groupName, projectName, resourceGroupName, subscriptionId` | List SqlAssessmentV2 resources by Group |
| `download_url` | `EXEC` | `assessmentName, groupName, projectName, resourceGroupName, subscriptionId` | Get the URL for downloading the assessment in a report format. |
