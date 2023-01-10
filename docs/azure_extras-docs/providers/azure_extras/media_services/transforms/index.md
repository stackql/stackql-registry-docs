---
title: transforms
hide_title: false
hide_table_of_contents: false
keywords:
  - transforms
  - media_services
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
<tr><td><b>Name</b></td><td><code>transforms</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.media_services.transforms</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | A Transform. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Transforms_Get` | `SELECT` | `accountName, api-version, resourceGroupName, subscriptionId, transformName` | Gets a Transform. |
| `Transforms_List` | `SELECT` | `accountName, api-version, resourceGroupName, subscriptionId` | Lists the Transforms in the account. |
| `Transforms_CreateOrUpdate` | `INSERT` | `accountName, api-version, resourceGroupName, subscriptionId, transformName` | Creates or updates a new Transform. |
| `Transforms_Delete` | `DELETE` | `accountName, api-version, resourceGroupName, subscriptionId, transformName` | Deletes a Transform. |
| `Transforms_Update` | `EXEC` | `accountName, api-version, resourceGroupName, subscriptionId, transformName` | Updates a Transform. |
