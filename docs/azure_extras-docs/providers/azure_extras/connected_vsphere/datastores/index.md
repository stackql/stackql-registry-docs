---
title: datastores
hide_title: false
hide_table_of_contents: false
keywords:
  - datastores
  - connected_vsphere
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>datastores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.connected_vsphere.datastores</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Gets or sets the Id. |
| `name` | `string` | Gets or sets the name. |
| `tags` | `object` | Gets or sets the Resource tags. |
| `type` | `string` | Gets or sets the type of the resource. |
| `extendedLocation` | `object` | The extended location. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `location` | `string` | Gets or sets the location. |
| `properties` | `object` | Defines the resource properties. |
| `kind` | `string` | Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Datastores_Get` | `SELECT` | `api-version, datastoreName, resourceGroupName, subscriptionId` | Implements datastore GET method. |
| `Datastores_List` | `SELECT` | `api-version, subscriptionId` | List of datastores in a subscription. |
| `Datastores_ListByResourceGroup` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | List of datastores in a resource group. |
| `Datastores_Create` | `INSERT` | `api-version, datastoreName, resourceGroupName, subscriptionId, data__location, data__properties` | Create Or Update datastore. |
| `Datastores_Delete` | `DELETE` | `api-version, datastoreName, resourceGroupName, subscriptionId` | Implements datastore DELETE method. |
| `Datastores_Update` | `EXEC` | `api-version, datastoreName, resourceGroupName, subscriptionId` | API to update certain properties of the datastore resource. |
