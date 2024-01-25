---
title: b2c_tenants
hide_title: false
hide_table_of_contents: false
keywords:
  - b2c_tenants
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
<tr><td><b>Name</b></td><td><code>b2c_tenants</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.aad_b2c.b2c_tenants</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | An identifier that represents the Azure AD B2C tenant resource. |
| `name` | `string` | The name of the Azure AD B2C tenant resource. |
| `location` | `string` | The location in which the resource is hosted and data resides. Can be one of 'United States', 'Europe', 'Asia Pacific', or 'Australia'. Refer to [this documentation](https://aka.ms/B2CDataResidency) for more information. |
| `properties` | `object` | Properties of the Azure AD B2C tenant Azure resource. |
| `sku` | `object` | SKU properties of the Azure AD B2C tenant. Learn more about Azure AD B2C billing at [aka.ms/b2cBilling](https://aka.ms/b2cBilling). |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource Tags |
| `type` | `string` | The type of the B2C tenant resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | Get the Azure AD B2C tenant resource. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Get all the Azure AD B2C tenant resources in a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Get all the Azure AD B2C tenant resources in a subscription. |
| `create` | `INSERT` | `resourceGroupName, resourceName, subscriptionId, data__location, data__properties, data__sku` | Initiates an async request to create both the Azure AD B2C tenant and the corresponding Azure resource linked to a subscription. Note: Please check name availability before creating a new tenant. |
| `delete` | `DELETE` | `resourceGroupName, resourceName, subscriptionId` | Initiates an async operation to delete the Azure AD B2C tenant and Azure resource. The resource deletion can only happen as the last step in [the tenant deletion process](https://aka.ms/deleteB2Ctenant).  |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Get all the Azure AD B2C tenant resources in a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Get all the Azure AD B2C tenant resources in a subscription. |
| `b2c_tenants` | `EXEC` | `subscriptionId, data__countryCode, data__name` | Checks the availability and validity of a domain name for the tenant. |
| `update` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Update the Azure AD B2C tenant resource. |
