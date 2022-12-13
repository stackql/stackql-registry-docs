---
title: user_metrics_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - user_metrics_keys
  - traffic_manager
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
<tr><td><b>Name</b></td><td><code>user_metrics_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.traffic_manager.user_metrics_keys</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `TrafficManagerUserMetricsKeys_Get` | `SELECT` | `subscriptionId` | Get the subscription-level key used for Real User Metrics collection. |
| `TrafficManagerUserMetricsKeys_CreateOrUpdate` | `INSERT` | `subscriptionId` | Create or update a subscription-level key used for Real User Metrics collection. |
| `TrafficManagerUserMetricsKeys_Delete` | `DELETE` | `subscriptionId` | Delete a subscription-level key used for Real User Metrics collection. |
