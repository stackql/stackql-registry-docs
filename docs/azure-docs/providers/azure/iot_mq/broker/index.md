---
title: broker
hide_title: false
hide_table_of_contents: false
keywords:
  - broker
  - iot_mq
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
<tr><td><b>Name</b></td><td><code>broker</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.iot_mq.broker</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `extendedLocation` | `object` | ExtendedLocation properties |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Broker Resource properties |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `brokerName, mqName, resourceGroupName, subscriptionId` | Get a BrokerResource |
| `list_by_mq_resource` | `SELECT` | `mqName, resourceGroupName, subscriptionId` | List BrokerResource resources by MqResource |
| `create_or_update` | `INSERT` | `brokerName, mqName, resourceGroupName, subscriptionId, data__extendedLocation` | Create a BrokerResource |
| `delete` | `DELETE` | `brokerName, mqName, resourceGroupName, subscriptionId` | Delete a BrokerResource |
| `_list_by_mq_resource` | `EXEC` | `mqName, resourceGroupName, subscriptionId` | List BrokerResource resources by MqResource |
| `update` | `EXEC` | `brokerName, mqName, resourceGroupName, subscriptionId` | Update a BrokerResource |
