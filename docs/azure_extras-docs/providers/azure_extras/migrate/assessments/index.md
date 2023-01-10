---
title: assessments
hide_title: false
hide_table_of_contents: false
keywords:
  - assessments
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
<tr><td><b>Name</b></td><td><code>assessments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.migrate.assessments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Path reference to this assessment. /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.Migrate/assessmentProjects/&#123;projectName&#125;/groups/&#123;groupName&#125;/assessment/&#123;assessmentName&#125; |
| `name` | `string` | Unique name of an assessment. |
| `properties` | `object` | Properties of an assessment. |
| `type` | `string` | Type of the object = [Microsoft.Migrate/assessmentProjects/groups/assessments]. |
| `eTag` | `string` | For optimistic concurrency control. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Assessments_Get` | `SELECT` | `api-version, assessmentName, groupName, projectName, resourceGroupName, subscriptionId` | Get an existing assessment with the specified name. Returns a json object of type 'assessment' as specified in Models section. |
| `Assessments_ListByGroup` | `SELECT` | `api-version, groupName, projectName, resourceGroupName, subscriptionId` | Get all assessments created for the specified group.<br /><br />Returns a json array of objects of type 'assessment' as specified in Models section.<br /> |
| `Assessments_ListByProject` | `SELECT` | `api-version, projectName, resourceGroupName, subscriptionId` | Get all assessments created in the project.<br /><br />Returns a json array of objects of type 'assessment' as specified in Models section.<br /> |
| `Assessments_Create` | `INSERT` | `api-version, assessmentName, groupName, projectName, resourceGroupName, subscriptionId, data__properties` | Create a new assessment with the given name and the specified settings. Since name of an assessment in a project is a unique identifier, if an assessment with the name provided already exists, then the existing assessment is updated.<br /><br />Any PUT operation, resulting in either create or update on an assessment, will cause the assessment to go in a "InProgress" state. This will be indicated by the field 'computationState' on the Assessment object. During this time no other PUT operation will be allowed on that assessment object, nor will a Delete operation. Once the computation for the assessment is complete, the field 'computationState' will be updated to 'Ready', and then other PUT or DELETE operations can happen on the assessment.<br /><br />When assessment is under computation, any PUT will lead to a 400 - Bad Request error.<br /> |
| `Assessments_Delete` | `DELETE` | `api-version, assessmentName, groupName, projectName, resourceGroupName, subscriptionId` | Delete an assessment from the project. The machines remain in the assessment. Deleting a non-existent assessment results in a no-operation.<br /><br />When an assessment is under computation, as indicated by the 'computationState' field, it cannot be deleted. Any such attempt will return a 400 - Bad Request.<br /> |
| `Assessments_GetReportDownloadUrl` | `EXEC` | `api-version, assessmentName, groupName, projectName, resourceGroupName, subscriptionId` | Get the URL for downloading the assessment in a report format. |
