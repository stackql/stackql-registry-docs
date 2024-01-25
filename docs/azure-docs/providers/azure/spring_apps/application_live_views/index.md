---
title: application_live_views
hide_title: false
hide_table_of_contents: false
keywords:
  - application_live_views
  - spring_apps
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
<tr><td><b>Name</b></td><td><code>application_live_views</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.spring_apps.application_live_views</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `applicationLiveViewName, resourceGroupName, serviceName, subscriptionId` | Get the Application Live  and its properties. |
| `list` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Handles requests to list all resources in a Service. |
| `create_or_update` | `INSERT` | `applicationLiveViewName, resourceGroupName, serviceName, subscriptionId` | Create the default Application Live View or update the existing Application Live View. |
| `delete` | `DELETE` | `applicationLiveViewName, resourceGroupName, serviceName, subscriptionId` | Disable the default Application Live View. |
| `_list` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Handles requests to list all resources in a Service. |
