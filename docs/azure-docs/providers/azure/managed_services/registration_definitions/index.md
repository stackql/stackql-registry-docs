---
title: registration_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - registration_definitions
  - managed_services
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
<tr><td><b>Name</b></td><td><code>registration_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.managed_services.registration_definitions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The fully qualified path of the registration definition. |
| `name` | `string` | The name of the registration definition. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the Azure resource (Microsoft.ManagedServices/registrationDefinitions). |
| `plan` | `object` | Plan for the resource. |
| `properties` | `object` | The properties of a registration definition. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `RegistrationDefinitions_Get` | `SELECT` | `registrationDefinitionId, scope` | Gets the registration definition details. |
| `RegistrationDefinitions_List` | `SELECT` | `scope` | Gets a list of the registration definitions. |
| `RegistrationDefinitions_CreateOrUpdate` | `INSERT` | `registrationDefinitionId, scope` | Creates or updates a registration definition. |
| `RegistrationDefinitions_Delete` | `DELETE` | `registrationDefinitionId, scope` | Deletes the registration definition. |
