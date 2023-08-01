---
title: secret
hide_title: false
hide_table_of_contents: false
keywords:
  - secret
  - service_fabric_mesh
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
<tr><td><b>Name</b></td><td><code>secret</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_fabric_mesh.secret</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Describes the properties of a secret resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Secret_Get` | `SELECT` | `api-version, resourceGroupName, secretResourceName, subscriptionId` | Gets the information about the secret resource with the given name. The information include the description and other properties of the secret. |
| `Secret_ListByResourceGroup` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | Gets the information about all secret resources in a given resource group. The information include the description and other properties of the Secret. |
| `Secret_ListBySubscription` | `SELECT` | `api-version, subscriptionId` | Gets the information about all secret resources in a given resource group. The information include the description and other properties of the secret. |
| `Secret_Create` | `INSERT` | `api-version, resourceGroupName, secretResourceName, subscriptionId, data__properties` | Creates a secret resource with the specified name, description and properties. If a secret resource with the same name exists, then it is updated with the specified description and properties. |
| `Secret_Delete` | `DELETE` | `api-version, resourceGroupName, secretResourceName, subscriptionId` | Deletes the secret resource identified by the name. |
