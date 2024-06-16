---
title: live_outputs
hide_title: false
hide_table_of_contents: false
keywords:
  - live_outputs
  - media_services
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
<tr><td><b>Name</b></td><td><code>live_outputs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.media_services.live_outputs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The JSON object that contains the properties required to create a live output. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, api-version, liveEventName, liveOutputName, resourceGroupName, subscriptionId" /> | Gets a live output. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, api-version, liveEventName, resourceGroupName, subscriptionId" /> | Lists the live outputs of a live event. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, api-version, liveEventName, liveOutputName, resourceGroupName, subscriptionId" /> | Creates a new live output. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, api-version, liveEventName, liveOutputName, resourceGroupName, subscriptionId" /> | Deletes a live output. Deleting a live output does not delete the asset the live output is writing to. |
| <CopyableCode code="async_operation" /> | `EXEC` | <CopyableCode code="accountName, api-version, operationId, resourceGroupName, subscriptionId" /> | Get a Live Output operation status. |
| <CopyableCode code="operation_location" /> | `EXEC` | <CopyableCode code="accountName, api-version, liveEventName, liveOutputName, operationId, resourceGroupName, subscriptionId" /> | Get a Live Output operation status. |
