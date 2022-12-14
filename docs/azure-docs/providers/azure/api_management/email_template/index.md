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
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Email Template Contract properties. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `EmailTemplate_Get` | `SELECT` | `resourceGroupName, serviceName, subscriptionId, templateName` | Gets the details of the email template specified by its identifier. |
| `EmailTemplate_ListByService` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Gets all email templates |
| `EmailTemplate_CreateOrUpdate` | `INSERT` | `resourceGroupName, serviceName, subscriptionId, templateName` | Updates an Email Template. |
| `EmailTemplate_Delete` | `DELETE` | `If-Match, resourceGroupName, serviceName, subscriptionId, templateName` | Reset the Email Template to default template provided by the API Management service instance. |
| `EmailTemplate_GetEntityTag` | `EXEC` | `resourceGroupName, serviceName, subscriptionId, templateName` | Gets the entity state (Etag) version of the email template specified by its identifier. |
| `EmailTemplate_Update` | `EXEC` | `If-Match, resourceGroupName, serviceName, subscriptionId, templateName` | Updates API Management email template |
