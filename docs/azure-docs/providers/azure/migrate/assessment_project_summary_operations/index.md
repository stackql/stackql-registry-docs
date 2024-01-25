---
title: assessment_project_summary_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - assessment_project_summary_operations
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
<tr><td><b>Name</b></td><td><code>assessment_project_summary_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.migrate.assessment_project_summary_operations</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `projectName, projectSummaryName, resourceGroupName, subscriptionId` | Get a AssessmentProjectSummary |
| `list_by_assessment_project` | `SELECT` | `projectName, resourceGroupName, subscriptionId` | List AssessmentProjectSummary resources by AssessmentProject |
| `_list_by_assessment_project` | `EXEC` | `projectName, resourceGroupName, subscriptionId` | List AssessmentProjectSummary resources by AssessmentProject |
