---
title: streaming_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - streaming_endpoints
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
<tr><td><b>Name</b></td><td><code>streaming_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.media_services.streaming_endpoints" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The streaming endpoint properties. |
| <CopyableCode code="sku" /> | `object` | The streaming endpoint current sku. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, api-version, resourceGroupName, streamingEndpointName, subscriptionId" /> | Gets a streaming endpoint. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, api-version, resourceGroupName, subscriptionId" /> | Lists the streaming endpoints in the account. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, api-version, resourceGroupName, streamingEndpointName, subscriptionId" /> | Creates a streaming endpoint. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, api-version, resourceGroupName, streamingEndpointName, subscriptionId" /> | Deletes a streaming endpoint. |
| <CopyableCode code="async_operation" /> | `EXEC` | <CopyableCode code="accountName, api-version, operationId, resourceGroupName, subscriptionId" /> | Get a streaming endpoint operation status. |
| <CopyableCode code="operation_location" /> | `EXEC` | <CopyableCode code="accountName, api-version, operationId, resourceGroupName, streamingEndpointName, subscriptionId" /> | Get a streaming endpoint operation status. |
| <CopyableCode code="scale" /> | `EXEC` | <CopyableCode code="accountName, api-version, resourceGroupName, streamingEndpointName, subscriptionId" /> | Scales an existing streaming endpoint. |
| <CopyableCode code="skus" /> | `EXEC` | <CopyableCode code="accountName, api-version, resourceGroupName, streamingEndpointName, subscriptionId" /> | List streaming endpoint supported skus. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="accountName, api-version, resourceGroupName, streamingEndpointName, subscriptionId" /> | Starts an existing streaming endpoint. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="accountName, api-version, resourceGroupName, streamingEndpointName, subscriptionId" /> | Stops an existing streaming endpoint. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="accountName, api-version, resourceGroupName, streamingEndpointName, subscriptionId" /> | Updates a existing streaming endpoint. |
