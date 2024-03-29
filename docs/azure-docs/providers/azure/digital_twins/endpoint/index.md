---
title: endpoint
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoint
  - digital_twins
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
<tr><td><b>Name</b></td><td><code>endpoint</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.digital_twins.endpoint</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource identifier. |
| `name` | `string` | Extension resource name. |
| `properties` | `object` | Properties related to Digital Twins Endpoint |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, endpointName, resourceGroupName, resourceName, subscriptionId` | Get DigitalTwinsInstances Endpoint. |
| `list` | `SELECT` | `api-version, resourceGroupName, resourceName, subscriptionId` | Get DigitalTwinsInstance Endpoints. |
| `create_or_update` | `INSERT` | `api-version, endpointName, resourceGroupName, resourceName, subscriptionId, data__properties` | Create or update DigitalTwinsInstance endpoint. |
| `delete` | `DELETE` | `api-version, endpointName, resourceGroupName, resourceName, subscriptionId` | Delete a DigitalTwinsInstance endpoint. |
| `_list` | `EXEC` | `api-version, resourceGroupName, resourceName, subscriptionId` | Get DigitalTwinsInstance Endpoints. |
