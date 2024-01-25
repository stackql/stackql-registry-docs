---
title: api_issue
hide_title: false
hide_table_of_contents: false
keywords:
  - api_issue
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
<tr><td><b>Name</b></td><td><code>api_issue</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.api_issue</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `apiId, issueId, resourceGroupName, serviceName, subscriptionId` | Gets the details of the Issue for an API specified by its identifier. |
| `list_by_service` | `SELECT` | `apiId, resourceGroupName, serviceName, subscriptionId` | Lists all issues associated with the specified API. |
| `create_or_update` | `INSERT` | `apiId, issueId, resourceGroupName, serviceName, subscriptionId` | Creates a new Issue for an API or updates an existing one. |
| `delete` | `DELETE` | `If-Match, apiId, issueId, resourceGroupName, serviceName, subscriptionId` | Deletes the specified Issue from an API. |
| `_list_by_service` | `EXEC` | `apiId, resourceGroupName, serviceName, subscriptionId` | Lists all issues associated with the specified API. |
| `update` | `EXEC` | `If-Match, apiId, issueId, resourceGroupName, serviceName, subscriptionId` | Updates an existing issue for an API. |
