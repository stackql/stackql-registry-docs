---
title: resource_endpoint_health
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_endpoint_health
  - iot_hub
  - azure    
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
<tr><td><b>Name</b></td><td><code>resource_endpoint_health</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.iot_hub.resource_endpoint_health</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `endpointId` | `string` | Id of the endpoint |
| `healthStatus` | `string` | Health statuses have following meanings. The 'healthy' status shows that the endpoint is accepting messages as expected. The 'unhealthy' status shows that the endpoint is not accepting messages as expected and IoT Hub is retrying to send data to this endpoint. The status of an unhealthy endpoint will be updated to healthy when IoT Hub has established an eventually consistent state of health. The 'dead' status shows that the endpoint is not accepting messages, after IoT Hub retried sending messages for the retrial period. See IoT Hub metrics to identify errors and monitor issues with endpoints. The 'unknown' status shows that the IoT Hub has not established a connection with the endpoint. No messages have been delivered to or rejected from this endpoint |
| `lastKnownError` | `string` | Last error obtained when a message failed to be delivered to iot hub |
| `lastKnownErrorTime` | `string` | Time at which the last known error occurred |
| `lastSendAttemptTime` | `string` | Last time iot hub tried to send a message to the endpoint |
| `lastSuccessfulSendAttemptTime` | `string` | Last time iot hub successfully sent a message to the endpoint |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `api-version, iotHubName, resourceGroupName, subscriptionId` |
| `_get` | `EXEC` | `api-version, iotHubName, resourceGroupName, subscriptionId` |
