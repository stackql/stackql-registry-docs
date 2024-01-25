---
title: assessment_options_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - assessment_options_operations
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
<tr><td><b>Name</b></td><td><code>assessment_options_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.migrate.assessment_options_operations</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `assessmentOptionsName, projectName, resourceGroupName, subscriptionId` | Get a AssessmentOptions |
| `list_by_assessment_project` | `SELECT` | `projectName, resourceGroupName, subscriptionId` | List AssessmentOptions resources by AssessmentProject |
| `_list_by_assessment_project` | `EXEC` | `projectName, resourceGroupName, subscriptionId` | List AssessmentOptions resources by AssessmentProject |
