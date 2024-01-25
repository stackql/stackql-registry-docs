---
title: api_tag_description
hide_title: false
hide_table_of_contents: false
keywords:
  - api_tag_description
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
<tr><td><b>Name</b></td><td><code>api_tag_description</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.api_tag_description</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `apiId, resourceGroupName, serviceName, subscriptionId, tagDescriptionId` | Get Tag description in scope of API |
| `list_by_service` | `SELECT` | `apiId, resourceGroupName, serviceName, subscriptionId` | Lists all Tags descriptions in scope of API. Model similar to swagger - tagDescription is defined on API level but tag may be assigned to the Operations |
| `create_or_update` | `INSERT` | `apiId, resourceGroupName, serviceName, subscriptionId, tagDescriptionId` | Create/Update tag description in scope of the Api. |
| `delete` | `DELETE` | `If-Match, apiId, resourceGroupName, serviceName, subscriptionId, tagDescriptionId` | Delete tag description for the Api. |
| `_list_by_service` | `EXEC` | `apiId, resourceGroupName, serviceName, subscriptionId` | Lists all Tags descriptions in scope of API. Model similar to swagger - tagDescription is defined on API level but tag may be assigned to the Operations |
