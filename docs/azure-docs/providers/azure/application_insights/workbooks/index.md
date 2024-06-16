---
title: workbooks
hide_title: false
hide_table_of_contents: false
keywords:
  - workbooks
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
<tr><td><b>Name</b></td><td><code>workbooks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.application_insights.workbooks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Resource etag |
| <CopyableCode code="identity" /> | `object` | Identity used for BYOS |
| <CopyableCode code="kind" /> | `string` | The kind of workbook. Only valid value is shared. |
| <CopyableCode code="properties" /> | `object` | Properties that contain a workbook. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Get a single workbook by its resourceName. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="category, resourceGroupName, subscriptionId" /> | Get all Workbooks defined within a specified resource group and category. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="category, subscriptionId" /> | Get all Workbooks defined within a specified subscription and category. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Create a new workbook. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Delete a workbook. |
| <CopyableCode code="revision_get" /> | `EXEC` | <CopyableCode code="resourceGroupName, resourceName, revisionId, subscriptionId" /> | Get a single workbook revision defined by its revisionId. |
| <CopyableCode code="revisions_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Get the revisions for the workbook defined by its resourceName. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Updates a workbook that has already been added. |
