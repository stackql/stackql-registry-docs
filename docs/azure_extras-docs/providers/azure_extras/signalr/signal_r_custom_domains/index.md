---
title: signal_r_custom_domains
hide_title: false
hide_table_of_contents: false
keywords:
  - signal_r_custom_domains
  - signalr
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>signal_r_custom_domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.signalr.signal_r_custom_domains</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Properties of a custom domain. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SignalRCustomDomains_Get` | `SELECT` | `name, resourceGroupName, resourceName, subscriptionId` | Get a custom domain. |
| `SignalRCustomDomains_List` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | List all custom domains. |
| `SignalRCustomDomains_CreateOrUpdate` | `INSERT` | `name, resourceGroupName, resourceName, subscriptionId, data__properties` | Create or update a custom domain. |
| `SignalRCustomDomains_Delete` | `DELETE` | `name, resourceGroupName, resourceName, subscriptionId` | Delete a custom domain. |
