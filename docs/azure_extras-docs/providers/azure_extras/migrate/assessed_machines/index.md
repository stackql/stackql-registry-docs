---
title: assessed_machines
hide_title: false
hide_table_of_contents: false
keywords:
  - assessed_machines
  - migrate
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
<tr><td><b>Name</b></td><td><code>assessed_machines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.migrate.assessed_machines</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Path reference to this assessed machine. /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.Migrate/assessmentProjects/&#123;projectName&#125;/groups/&#123;groupName&#125;/assessments/&#123;assessmentName&#125;/assessedMachines/&#123;assessedMachineName&#125; |
| `name` | `string` | Name of the machine. |
| `type` | `string` | Type of the object = [Microsoft.Migrate/assessmentProjects/groups/assessments/assessedMachines]. |
| `eTag` | `string` | For optimistic concurrency control. |
| `properties` | `object` | Properties of an assessed machine. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AssessedMachines_Get` | `SELECT` | `api-version, assessedMachineName, assessmentName, groupName, projectName, resourceGroupName, subscriptionId` | Get an assessed machine with its size & cost estimate that was evaluated in the specified assessment. |
| `AssessedMachines_ListByAssessment` | `SELECT` | `api-version, assessmentName, groupName, projectName, resourceGroupName, subscriptionId` | Get list of machines that assessed as part of the specified assessment. Returns a json array of objects of type 'assessedMachine' as specified in the Models section.<br /><br />Whenever an assessment is created or updated, it goes under computation. During this phase, the 'status' field of Assessment object reports 'Computing'.<br />During the period when the assessment is under computation, the list of assessed machines is empty and no assessed machines are returned by this call.<br /> |
