---
title: assessment_projects_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - assessment_projects_operations
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assessment_projects_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.assessment_projects_operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of a project. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="projectName, resourceGroupName, subscriptionId" /> | Get a AssessmentProject |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List AssessmentProject resources by resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List AssessmentProject resources by subscription ID |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="projectName, resourceGroupName, subscriptionId" /> | Create a AssessmentProject |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="projectName, resourceGroupName, subscriptionId" /> | Delete a AssessmentProject |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List AssessmentProject resources by resource group |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | List AssessmentProject resources by subscription ID |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="projectName, resourceGroupName, subscriptionId" /> | Update a AssessmentProject |
