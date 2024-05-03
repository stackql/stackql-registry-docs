---
title: live_events
hide_title: false
hide_table_of_contents: false
keywords:
  - live_events
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
<tr><td><b>Name</b></td><td><code>live_events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.media_services.live_events" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The live event properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, api-version, liveEventName, resourceGroupName, subscriptionId" /> | Gets properties of a live event. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, api-version, resourceGroupName, subscriptionId" /> | Lists all the live events in the account. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, api-version, liveEventName, resourceGroupName, subscriptionId" /> | Creates a new live event. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, api-version, liveEventName, resourceGroupName, subscriptionId" /> | Deletes a live event. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="accountName, api-version, resourceGroupName, subscriptionId" /> | Lists all the live events in the account. |
| <CopyableCode code="allocate" /> | `EXEC` | <CopyableCode code="accountName, api-version, liveEventName, resourceGroupName, subscriptionId" /> | A live event is in StandBy state after allocation completes, and is ready to start. |
| <CopyableCode code="async_operation" /> | `EXEC` | <CopyableCode code="accountName, api-version, operationId, resourceGroupName, subscriptionId" /> | Get a live event operation status. |
| <CopyableCode code="operation_location" /> | `EXEC` | <CopyableCode code="accountName, api-version, liveEventName, operationId, resourceGroupName, subscriptionId" /> | Get a live event operation status. |
| <CopyableCode code="reset" /> | `EXEC` | <CopyableCode code="accountName, api-version, liveEventName, resourceGroupName, subscriptionId" /> | Resets an existing live event. All live outputs for the live event are deleted and the live event is stopped and will be started again. All assets used by the live outputs and streaming locators created on these assets are unaffected.  |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="accountName, api-version, liveEventName, resourceGroupName, subscriptionId" /> | A live event in Stopped or StandBy state will be in Running state after the start operation completes. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="accountName, api-version, liveEventName, resourceGroupName, subscriptionId" /> | Stops a running live event. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="accountName, api-version, liveEventName, resourceGroupName, subscriptionId" /> | Updates settings on an existing live event. |
