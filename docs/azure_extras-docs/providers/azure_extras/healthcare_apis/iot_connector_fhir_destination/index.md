---
title: iot_connector_fhir_destination
hide_title: false
hide_table_of_contents: false
keywords:
  - iot_connector_fhir_destination
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
<tr><td><b>Name</b></td><td><code>iot_connector_fhir_destination</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.healthcare_apis.iot_connector_fhir_destination</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The resource location. |
| `properties` | `object` | IoT Connector destination properties for an Azure FHIR service. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `IotConnectorFhirDestination_Get` | `SELECT` | `api-version, fhirDestinationName, iotConnectorName, resourceGroupName, subscriptionId, workspaceName` | Gets the properties of the specified Iot Connector FHIR destination. |
| `IotConnectorFhirDestination_CreateOrUpdate` | `INSERT` | `api-version, fhirDestinationName, iotConnectorName, resourceGroupName, subscriptionId, workspaceName, data__properties` | Creates or updates an IoT Connector FHIR destination resource with the specified parameters. |
| `IotConnectorFhirDestination_Delete` | `DELETE` | `api-version, fhirDestinationName, iotConnectorName, resourceGroupName, subscriptionId, workspaceName` | Deletes an IoT Connector FHIR destination. |
