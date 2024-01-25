---
title: api_issue_comment
hide_title: false
hide_table_of_contents: false
keywords:
  - api_issue_comment
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
<tr><td><b>Name</b></td><td><code>api_issue_comment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.api_issue_comment</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `apiId, commentId, issueId, resourceGroupName, serviceName, subscriptionId` | Gets the details of the issue Comment for an API specified by its identifier. |
| `list_by_service` | `SELECT` | `apiId, issueId, resourceGroupName, serviceName, subscriptionId` | Lists all comments for the Issue associated with the specified API. |
| `create_or_update` | `INSERT` | `apiId, commentId, issueId, resourceGroupName, serviceName, subscriptionId` | Creates a new Comment for the Issue in an API or updates an existing one. |
| `delete` | `DELETE` | `If-Match, apiId, commentId, issueId, resourceGroupName, serviceName, subscriptionId` | Deletes the specified comment from an Issue. |
| `_list_by_service` | `EXEC` | `apiId, issueId, resourceGroupName, serviceName, subscriptionId` | Lists all comments for the Issue associated with the specified API. |
