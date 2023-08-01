---
title: certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - certificates
  - web_apps
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
<tr><td><b>Name</b></td><td><code>certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.web_apps.certificates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource Name. |
| `kind` | `string` | Kind of resource. |
| `location` | `string` | Resource Location. |
| `properties` | `object` | Certificate resource specific properties |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Certificates_Get` | `SELECT` | `name, resourceGroupName, subscriptionId` | Description for Get a certificate. |
| `Certificates_List` | `SELECT` | `subscriptionId` | Description for Get all certificates for a subscription. |
| `Certificates_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Description for Get all certificates in a resource group. |
| `Certificates_CreateOrUpdate` | `INSERT` | `name, resourceGroupName, subscriptionId` | Description for Create or update a certificate. |
| `Certificates_Delete` | `DELETE` | `name, resourceGroupName, subscriptionId` | Description for Delete a certificate. |
| `Certificates_Update` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Create or update a certificate. |
