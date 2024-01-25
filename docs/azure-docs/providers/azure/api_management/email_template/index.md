---
title: email_template
hide_title: false
hide_table_of_contents: false
keywords:
  - email_template
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
<tr><td><b>Name</b></td><td><code>email_template</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.email_template</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, serviceName, subscriptionId, templateName` | Gets the details of the email template specified by its identifier. |
| `list_by_service` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Gets all email templates |
| `create_or_update` | `INSERT` | `resourceGroupName, serviceName, subscriptionId, templateName` | Updates an Email Template. |
| `delete` | `DELETE` | `If-Match, resourceGroupName, serviceName, subscriptionId, templateName` | Reset the Email Template to default template provided by the API Management service instance. |
| `_list_by_service` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Gets all email templates |
| `update` | `EXEC` | `If-Match, resourceGroupName, serviceName, subscriptionId, templateName` | Updates API Management email template |
