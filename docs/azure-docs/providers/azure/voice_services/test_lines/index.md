---
title: test_lines
hide_title: false
hide_table_of_contents: false
keywords:
  - test_lines
  - voice_services
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
<tr><td><b>Name</b></td><td><code>test_lines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.voice_services.test_lines</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Details of the TestLine resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `communicationsGatewayName, resourceGroupName, subscriptionId, testLineName` | Get a TestLine |
| `list_by_communications_gateway` | `SELECT` | `communicationsGatewayName, resourceGroupName, subscriptionId` | List TestLine resources by CommunicationsGateway |
| `create_or_update` | `INSERT` | `communicationsGatewayName, resourceGroupName, subscriptionId, testLineName` | Create a TestLine |
| `delete` | `DELETE` | `communicationsGatewayName, resourceGroupName, subscriptionId, testLineName` | Delete a TestLine |
| `_list_by_communications_gateway` | `EXEC` | `communicationsGatewayName, resourceGroupName, subscriptionId` | List TestLine resources by CommunicationsGateway |
| `update` | `EXEC` | `communicationsGatewayName, resourceGroupName, subscriptionId, testLineName` | Update a TestLine |
