---
title: monitors
hide_title: false
hide_table_of_contents: false
keywords:
  - monitors
  - newrelic
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>monitors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.newrelic.monitors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties specific to the NewRelic Monitor resource |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `monitorName, resourceGroupName, subscriptionId` | Get a NewRelicMonitorResource |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List NewRelicMonitorResource resources by resource group |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List NewRelicMonitorResource resources by subscription ID |
| `create_or_update` | `INSERT` | `monitorName, resourceGroupName, subscriptionId, data__properties` | Create a NewRelicMonitorResource |
| `delete` | `DELETE` | `monitorName, resourceGroupName, subscriptionId, userEmail` | Delete a NewRelicMonitorResource |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List NewRelicMonitorResource resources by resource group |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List NewRelicMonitorResource resources by subscription ID |
| `switch_billing` | `EXEC` | `monitorName, resourceGroupName, subscriptionId, data__userEmail` | Switches the billing for NewRelic monitor resource. |
| `update` | `EXEC` | `monitorName, resourceGroupName, subscriptionId` | Update a NewRelicMonitorResource |
| `vm_host_payload` | `EXEC` | `monitorName, resourceGroupName, subscriptionId` | Returns the payload that needs to be passed in the request body for installing NewRelic agent on a VM. |
