---
title: fhir_services
hide_title: false
hide_table_of_contents: false
keywords:
  - fhir_services
  - healthcare
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
<tr><td><b>Name</b></td><td><code>fhir_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.healthcare.fhir_services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Setting indicating whether the service has a managed identity associated with it. |
| `kind` | `string` | The kind of the service. |
| `properties` | `object` | Fhir Service properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `fhirServiceName, resourceGroupName, subscriptionId, workspaceName` | Gets the properties of the specified FHIR Service. |
| `list_by_workspace` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Lists all FHIR Services for the given workspace |
| `create_or_update` | `INSERT` | `fhirServiceName, resourceGroupName, subscriptionId, workspaceName` | Creates or updates a FHIR Service resource with the specified parameters. |
| `delete` | `DELETE` | `fhirServiceName, resourceGroupName, subscriptionId, workspaceName` | Deletes a FHIR Service. |
| `_list_by_workspace` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Lists all FHIR Services for the given workspace |
| `update` | `EXEC` | `fhirServiceName, resourceGroupName, subscriptionId, workspaceName` | Patch FHIR Service details. |
