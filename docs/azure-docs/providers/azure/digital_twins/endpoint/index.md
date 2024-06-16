---
title: endpoint
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoint
  - digital_twins
  - azure    
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
<tr><td><b>Name</b></td><td><code>endpoint</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.digital_twins.endpoint" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource identifier. |
| <CopyableCode code="name" /> | `string` | Extension resource name. |
| <CopyableCode code="properties" /> | `object` | Properties related to Digital Twins Endpoint |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, endpointName, resourceGroupName, resourceName, subscriptionId" /> | Get DigitalTwinsInstances Endpoint. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, resourceName, subscriptionId" /> | Get DigitalTwinsInstance Endpoints. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="api-version, endpointName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | Create or update DigitalTwinsInstance endpoint. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, endpointName, resourceGroupName, resourceName, subscriptionId" /> | Delete a DigitalTwinsInstance endpoint. |
