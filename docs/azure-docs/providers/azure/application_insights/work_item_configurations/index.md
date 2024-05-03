---
title: work_item_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - work_item_configurations
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
<tr><td><b>Name</b></td><td><code>work_item_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.application_insights.work_item_configurations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="ConfigDisplayName" /> | `string` | Configuration friendly name |
| <CopyableCode code="ConfigProperties" /> | `string` | Serialized JSON object for detailed properties |
| <CopyableCode code="ConnectorId" /> | `string` | Connector identifier where work item is created |
| <CopyableCode code="Id" /> | `string` | Unique Id for work item |
| <CopyableCode code="IsDefault" /> | `boolean` | Boolean value indicating whether configuration is default |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Gets the list work item configurations that exist for the application |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Create a work item configuration for an Application Insights component. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId, workItemConfigId" /> | Delete a work item configuration of an Application Insights component. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Gets the list work item configurations that exist for the application |
