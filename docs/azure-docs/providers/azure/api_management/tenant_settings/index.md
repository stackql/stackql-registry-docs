---
title: tenant_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - tenant_settings
  - api_management
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
<tr><td><b>Name</b></td><td><code>tenant_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.tenant_settings</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, serviceName, settingsType, subscriptionId` | Get tenant settings. |
| `list_by_service` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Public settings. |
| `_list_by_service` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Public settings. |
