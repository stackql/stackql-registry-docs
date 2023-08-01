---
title: registration_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - registration_assignments
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
<tr><td><b>Name</b></td><td><code>registration_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.managed_services.registration_assignments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The fully qualified path of the registration assignment. |
| `name` | `string` | The name of the registration assignment. |
| `properties` | `object` | The properties of the registration assignment. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the Azure resource (Microsoft.ManagedServices/registrationAssignments). |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `RegistrationAssignments_Get` | `SELECT` | `registrationAssignmentId, scope` | Gets the details of the specified registration assignment. |
| `RegistrationAssignments_List` | `SELECT` | `scope` | Gets a list of the registration assignments. |
| `RegistrationAssignments_CreateOrUpdate` | `INSERT` | `registrationAssignmentId, scope` | Creates or updates a registration assignment. |
| `RegistrationAssignments_Delete` | `DELETE` | `registrationAssignmentId, scope` | Deletes the specified registration assignment. |
