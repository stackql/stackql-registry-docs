---
title: plans_web_apps_by_hybrid_connection
hide_title: false
hide_table_of_contents: false
keywords:
  - plans_web_apps_by_hybrid_connection
  - app_service
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
<tr><td><b>Name</b></td><td><code>plans_web_apps_by_hybrid_connection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_service.plans_web_apps_by_hybrid_connection</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `name, namespaceName, relayName, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `name, namespaceName, relayName, resourceGroupName, subscriptionId` |
