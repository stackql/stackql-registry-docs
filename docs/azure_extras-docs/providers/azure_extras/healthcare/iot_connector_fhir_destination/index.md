---
title: iot_connector_fhir_destination
hide_title: false
hide_table_of_contents: false
keywords:
  - iot_connector_fhir_destination
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>iot_connector_fhir_destination</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.healthcare.iot_connector_fhir_destination" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The resource location. |
| <CopyableCode code="properties" /> | `object` | IoT Connector destination properties for an Azure FHIR service. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="fhirDestinationName, iotConnectorName, resourceGroupName, subscriptionId, workspaceName" /> | Gets the properties of the specified Iot Connector FHIR destination. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="fhirDestinationName, iotConnectorName, resourceGroupName, subscriptionId, workspaceName, data__properties" /> | Creates or updates an IoT Connector FHIR destination resource with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="fhirDestinationName, iotConnectorName, resourceGroupName, subscriptionId, workspaceName" /> | Deletes an IoT Connector FHIR destination. |
