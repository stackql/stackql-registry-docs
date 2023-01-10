---
title: provider_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - provider_instances
  - hana_on_azure
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
<tr><td><b>Name</b></td><td><code>provider_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.hana_on_azure.provider_instances</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ProviderInstances_Get` | `SELECT` | `providerInstanceName, resourceGroupName, sapMonitorName, subscriptionId` | Gets properties of a provider instance for the specified subscription, resource group, SapMonitor name, and resource name. |
| `ProviderInstances_List` | `SELECT` | `resourceGroupName, sapMonitorName, subscriptionId` | Gets a list of provider instances in the specified SAP monitor. The operations returns various properties of each provider instances. |
| `ProviderInstances_Create` | `INSERT` | `providerInstanceName, resourceGroupName, sapMonitorName, subscriptionId` | Creates a provider instance for the specified subscription, resource group, SapMonitor name, and resource name. |
| `ProviderInstances_Delete` | `DELETE` | `providerInstanceName, resourceGroupName, sapMonitorName, subscriptionId` | Deletes a provider instance for the specified subscription, resource group, SapMonitor name, and resource name. |
