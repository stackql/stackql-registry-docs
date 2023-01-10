---
title: configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - configurations
  - advisor
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
<tr><td><b>Name</b></td><td><code>configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.advisor.configurations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource ID. |
| `name` | `string` | The name of the resource. |
| `properties` | `object` | Configuration data properties |
| `type` | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Configurations_ListByResourceGroup` | `SELECT` | `resourceGroup, subscriptionId` |  |
| `Configurations_ListBySubscription` | `SELECT` | `subscriptionId` | Retrieve Azure Advisor configurations and also retrieve configurations of contained resource groups. |
| `Configurations_CreateInResourceGroup` | `EXEC` | `configurationName, resourceGroup, subscriptionId` |  |
| `Configurations_CreateInSubscription` | `EXEC` | `configurationName, subscriptionId` | Create/Overwrite Azure Advisor configuration and also delete all configurations of contained resource groups. |
