---
title: monitored_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - monitored_subscriptions
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
<tr><td><b>Name</b></td><td><code>monitored_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.newrelic.monitored_subscriptions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The id of the monitored subscription resource. |
| `name` | `string` | Name of the monitored subscription resource. |
| `properties` | `object` | The request to update subscriptions needed to be monitored by the NewRelic monitor resource. |
| `type` | `string` | The type of the monitored subscription resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `configurationName, monitorName, resourceGroupName, subscriptionId` |
| `list` | `SELECT` | `monitorName, resourceGroupName, subscriptionId` |
| `delete` | `DELETE` | `configurationName, monitorName, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `monitorName, resourceGroupName, subscriptionId` |
| `createor_update` | `EXEC` | `configurationName, monitorName, resourceGroupName, subscriptionId` |
| `update` | `EXEC` | `configurationName, monitorName, resourceGroupName, subscriptionId` |
