---
title: change_data_capture
hide_title: false
hide_table_of_contents: false
keywords:
  - change_data_capture
  - data_factory
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
<tr><td><b>Name</b></td><td><code>change_data_capture</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_factory.change_data_capture" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource identifier. |
| <CopyableCode code="name" /> | `string` | The resource name. |
| <CopyableCode code="etag" /> | `string` | Etag identifies change in the resource. |
| <CopyableCode code="properties" /> | `object` | A Azure Data Factory object which automatically detects data changes at the source and then sends the updated data to the destination. |
| <CopyableCode code="type" /> | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, changeDataCaptureName, factoryName, resourceGroupName, subscriptionId" /> | Gets a change data capture. |
| <CopyableCode code="list_by_factory" /> | `SELECT` | <CopyableCode code="api-version, factoryName, resourceGroupName, subscriptionId" /> | Lists all resources of type change data capture. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="api-version, changeDataCaptureName, factoryName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates a change data capture resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, changeDataCaptureName, factoryName, resourceGroupName, subscriptionId" /> | Deletes a change data capture. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="api-version, changeDataCaptureName, factoryName, resourceGroupName, subscriptionId" /> | Starts a change data capture. |
| <CopyableCode code="status" /> | `EXEC` | <CopyableCode code="api-version, changeDataCaptureName, factoryName, resourceGroupName, subscriptionId" /> | Gets the current status for the change data capture resource. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="api-version, changeDataCaptureName, factoryName, resourceGroupName, subscriptionId" /> | Stops a change data capture. |
