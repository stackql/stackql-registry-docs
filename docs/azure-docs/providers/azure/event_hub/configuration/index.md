---
title: configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration
  - event_hub
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
<tr><td><b>Name</b></td><td><code>configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.event_hub.configuration</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Configuration_Get` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Get all Event Hubs Cluster settings - a collection of key/value pairs which represent the quotas and settings imposed on the cluster. |
| `Configuration_Patch` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Replace all specified Event Hubs Cluster settings with those contained in the request body. Leaves the settings not specified in the request body unmodified. |
