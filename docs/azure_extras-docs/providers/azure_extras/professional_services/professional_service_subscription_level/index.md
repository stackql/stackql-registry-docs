---
title: professional_service_subscription_level
hide_title: false
hide_table_of_contents: false
keywords:
  - professional_service_subscription_level
  - professional_services
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
<tr><td><b>Name</b></td><td><code>professional_service_subscription_level</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.professional_services.professional_service_subscription_level</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource uri |
| `name` | `string` | The name of the resource |
| `properties` | `object` | professionalService properties |
| `tags` | `object` | the resource tags. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | Gets information about the specified Subscription Level ProfessionalService. |
| `list_by_azure_subscription` | `SELECT` | `subscriptionId` | Gets information about all the Subscription Level ProfessionalService in a certain Azure subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Gets information about all the Subscription Level ProfessionalService in a certain resource group. |
| `create_or_update` | `INSERT` | `resourceGroupName, resourceName, subscriptionId` | Creates or updates a ProfessionalService resource. |
| `delete` | `DELETE` | `resourceGroupName, resourceName, subscriptionId` | Deletes the specified ProfessionalService. |
| `_list_by_azure_subscription` | `EXEC` | `subscriptionId` | Gets information about all the Subscription Level ProfessionalService in a certain Azure subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Gets information about all the Subscription Level ProfessionalService in a certain resource group. |
