---
title: ciam_tenants
hide_title: false
hide_table_of_contents: false
keywords:
  - ciam_tenants
  - aad_b2c
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
<tr><td><b>Name</b></td><td><code>ciam_tenants</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.aad_b2c.ciam_tenants</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | An identifier that represents the Azure AD for customers tenant resource. |
| `name` | `string` | The name of the Azure AD for customers tenant resource. |
| `location` | `string` | The location in which the resource is hosted and data resides. Can be one of 'United States', 'Europe', 'Asia Pacific', or 'Australia'. Refer to [this documentation](https://aka.ms/ciam-data-location) for more information. |
| `properties` | `object` | Properties of the Azure AD for customers tenant Azure resource. |
| `sku` | `object` | SKU properties of the Azure AD for customers tenant. Learn more about Azure AD for customers billing at [https://aka.ms/ciambilling](https://aka.ms/ciambilling). |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource Tags |
| `type` | `string` | The type of the Azure AD for customers tenant resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | Get the Azure AD for customers tenant resource. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Get all the Azure AD for customers tenants resources in a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Get all the Azure AD for customers tenant resources in a subscription. |
| `create` | `INSERT` | `resourceGroupName, resourceName, subscriptionId, data__location, data__properties, data__sku` | Initiates an async request to create both the Azure AD for customers tenant and the corresponding Azure resource linked to a subscription. Note: Please check name availability before creating a new tenant |
| `delete` | `DELETE` | `resourceGroupName, resourceName, subscriptionId` | Initiates an async operation to delete the Azure AD for customers tenant and Azure resource. The resource deletion can only happen as the last step in [the tenant deletion process](https://aka.ms/delete-ciam-tenant).  |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Get all the Azure AD for customers tenants resources in a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Get all the Azure AD for customers tenant resources in a subscription. |
| `update` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Update the Azure AD for customers tenant resource. |
