---
title: on_premise_sensors
hide_title: false
hide_table_of_contents: false
keywords:
  - on_premise_sensors
  - iot_security
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
<tr><td><b>Name</b></td><td><code>on_premise_sensors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.iot_security.on_premise_sensors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | On-premise IoT sensor properties |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `OnPremiseSensors_Get` | `SELECT` | `onPremiseSensorName, subscriptionId` | Get on-premise IoT sensor |
| `OnPremiseSensors_List` | `SELECT` | `subscriptionId` | List on-premise IoT sensors |
| `OnPremiseSensors_CreateOrUpdate` | `INSERT` | `onPremiseSensorName, subscriptionId` | Create or update on-premise IoT sensor |
| `OnPremiseSensors_Delete` | `DELETE` | `onPremiseSensorName, subscriptionId` | Delete on-premise IoT sensor |
| `OnPremiseSensors_DownloadActivation` | `EXEC` | `onPremiseSensorName, subscriptionId` | Download sensor activation file |
| `OnPremiseSensors_DownloadResetPassword` | `EXEC` | `onPremiseSensorName, subscriptionId` | Download file for reset password of the sensor |
