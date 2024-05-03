---
title: workbook_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - workbook_templates
  - application_insights
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
<tr><td><b>Name</b></td><td><code>workbook_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.application_insights.workbook_templates" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Azure resource Id |
| <CopyableCode code="name" /> | `string` | Azure resource name. |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | Properties that contain a workbook template. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Azure resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Get a single workbook template by its resourceName. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get all Workbook templates defined within a specified resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Create a new workbook template. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Delete a workbook template. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get all Workbook templates defined within a specified resource group. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Updates a workbook template that has already been added. |
