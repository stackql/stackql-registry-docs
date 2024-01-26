---
title: organizations
hide_title: false
hide_table_of_contents: false
keywords:
  - organizations
  - astro
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>organizations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.astro.organizations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties specific to Data Organization resource |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `organizationName, resourceGroupName, subscriptionId` | Get a OrganizationResource |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List OrganizationResource resources by resource group |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List OrganizationResource resources by subscription ID |
| `create_or_update` | `INSERT` | `organizationName, resourceGroupName, subscriptionId` | Create a OrganizationResource |
| `delete` | `DELETE` | `organizationName, resourceGroupName, subscriptionId` | Delete a OrganizationResource |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List OrganizationResource resources by resource group |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List OrganizationResource resources by subscription ID |
| `update` | `EXEC` | `organizationName, resourceGroupName, subscriptionId` | Update a OrganizationResource |
