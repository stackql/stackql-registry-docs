---
title: fhir_destinations
hide_title: false
hide_table_of_contents: false
keywords:
  - fhir_destinations
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
<tr><td><b>Name</b></td><td><code>fhir_destinations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.healthcare_apis.fhir_destinations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The resource location. |
| `properties` | `object` | IoT Connector destination properties for an Azure FHIR service. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `FhirDestinations_ListByIotConnector` | `SELECT` | `api-version, iotConnectorName, resourceGroupName, subscriptionId, workspaceName` |
