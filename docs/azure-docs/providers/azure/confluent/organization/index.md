---
title: organization
hide_title: false
hide_table_of_contents: false
keywords:
  - organization
  - confluent
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
<tr><td><b>Name</b></td><td><code>organization</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.confluent.organization</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ARM id of the resource. |
| `name` | `string` | The name of the resource. |
| `location` | `string` | Location of Organization resource |
| `properties` | `object` | Organization resource property |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Organization resource tags |
| `type` | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Organization_Get` | `SELECT` | `organizationName, resourceGroupName, subscriptionId` |
| `Organization_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` |
| `Organization_ListBySubscription` | `SELECT` | `subscriptionId` |
| `Organization_Create` | `INSERT` | `organizationName, resourceGroupName, subscriptionId, data__properties` |
| `Organization_Delete` | `DELETE` | `organizationName, resourceGroupName, subscriptionId` |
| `Organization_Update` | `EXEC` | `organizationName, resourceGroupName, subscriptionId` |
