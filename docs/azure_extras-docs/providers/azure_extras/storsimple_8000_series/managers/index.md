---
title: managers
hide_title: false
hide_table_of_contents: false
keywords:
  - managers
  - storsimple_8000_series
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>managers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_8000_series.managers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource ID. |
| <CopyableCode code="name" /> | `string` | The resource name. |
| <CopyableCode code="etag" /> | `string` | The etag of the manager. |
| <CopyableCode code="location" /> | `string` | The geo location of the resource. |
| <CopyableCode code="properties" /> | `object` | The properties of the StorSimple Manager. |
| <CopyableCode code="tags" /> | `object` | The tags attached to the resource. |
| <CopyableCode code="type" /> | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="managerName, resourceGroupName, subscriptionId" /> | Returns the properties of the specified manager name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Retrieves all the managers in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Retrieves all the managers in a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="managerName, resourceGroupName, subscriptionId" /> | Creates or updates the manager. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="managerName, resourceGroupName, subscriptionId" /> | Deletes the manager. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Retrieves all the managers in a subscription. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Retrieves all the managers in a resource group. |
| <CopyableCode code="regenerate_activation_key" /> | `EXEC` | <CopyableCode code="managerName, resourceGroupName, subscriptionId" /> | Re-generates and returns the activation key of the manager. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="managerName, resourceGroupName, subscriptionId" /> | Updates the StorSimple Manager. |
