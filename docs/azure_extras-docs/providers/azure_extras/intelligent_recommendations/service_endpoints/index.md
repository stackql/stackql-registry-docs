---
title: service_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - service_endpoints
  - intelligent_recommendations
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
<tr><td><b>Name</b></td><td><code>service_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.intelligent_recommendations.service_endpoints" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | ServiceEndpoint resource properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, serviceEndpointName, subscriptionId" /> | Returns ServiceEndpoint resources for a given name. |
| <CopyableCode code="list_by_account_resource" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Returns list of ServiceEndpoint resources for a given Account name. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, resourceGroupName, serviceEndpointName, subscriptionId" /> | Creates or updates ServiceEndpoint resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, resourceGroupName, serviceEndpointName, subscriptionId" /> | Deletes ServiceEndpoint resources of a given name. |
| <CopyableCode code="_list_by_account_resource" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Returns list of ServiceEndpoint resources for a given Account name. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, serviceEndpointName, subscriptionId" /> | Updates ServiceEndpoint resource details. |
