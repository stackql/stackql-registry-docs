---
title: fhir_destinations
hide_title: false
hide_table_of_contents: false
keywords:
  - fhir_destinations
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
<tr><td><b>Name</b></td><td><code>fhir_destinations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.healthcare.fhir_destinations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The resource location. |
| <CopyableCode code="properties" /> | `object` | IoT Connector destination properties for an Azure FHIR service. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_by_iot_connector" /> | `SELECT` | <CopyableCode code="iotConnectorName, resourceGroupName, subscriptionId, workspaceName" /> |
| <CopyableCode code="_list_by_iot_connector" /> | `EXEC` | <CopyableCode code="iotConnectorName, resourceGroupName, subscriptionId, workspaceName" /> |
