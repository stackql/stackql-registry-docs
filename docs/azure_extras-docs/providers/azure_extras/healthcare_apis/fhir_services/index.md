---
title: fhir_services
hide_title: false
hide_table_of_contents: false
keywords:
  - fhir_services
  - healthcare_apis
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
<tr><td><b>Id</b></td><td><code>azure_extras.healthcare_apis.fhir_services</code></td></tr>
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
| `FhirServices_Get` | `SELECT` | `api-version, fhirServiceName, resourceGroupName, subscriptionId, workspaceName` | Gets the properties of the specified FHIR Service. |
| `FhirServices_ListByWorkspace` | `SELECT` | `api-version, resourceGroupName, subscriptionId, workspaceName` | Lists all FHIR Services for the given workspace |
| `FhirServices_CreateOrUpdate` | `INSERT` | `api-version, fhirServiceName, resourceGroupName, subscriptionId, workspaceName` | Creates or updates a FHIR Service resource with the specified parameters. |
| `FhirServices_Delete` | `DELETE` | `api-version, fhirServiceName, resourceGroupName, subscriptionId, workspaceName` | Deletes a FHIR Service. |
| `FhirServices_Update` | `EXEC` | `api-version, fhirServiceName, resourceGroupName, subscriptionId, workspaceName` | Patch FHIR Service details. |
