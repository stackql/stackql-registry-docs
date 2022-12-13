---
title: contacts
hide_title: false
hide_table_of_contents: false
keywords:
  - contacts
  - security
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
<tr><td><b>Name</b></td><td><code>contacts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.contacts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Describes security contact properties |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SecurityContacts_Get` | `SELECT` | `api-version, securityContactName, subscriptionId` | Get Default Security contact configurations for the subscription |
| `SecurityContacts_List` | `SELECT` | `api-version, subscriptionId` | List all security contact configurations for the subscription |
| `SecurityContacts_Create` | `INSERT` | `api-version, securityContactName, subscriptionId` | Create security contact configurations for the subscription |
| `SecurityContacts_Delete` | `DELETE` | `api-version, securityContactName, subscriptionId` | Delete security contact configurations for the subscription |
