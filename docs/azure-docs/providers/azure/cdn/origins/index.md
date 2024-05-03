---
title: origins
hide_title: false
hide_table_of_contents: false
keywords:
  - origins
  - cdn
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
<tr><td><b>Name</b></td><td><code>origins</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.origins" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="endpointName, originName, profileName, resourceGroupName, subscriptionId" /> | Gets an existing origin within an endpoint. |
| <CopyableCode code="list_by_endpoint" /> | `SELECT` | <CopyableCode code="endpointName, profileName, resourceGroupName, subscriptionId" /> | Lists all of the existing origins within an endpoint. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="endpointName, originName, profileName, resourceGroupName, subscriptionId" /> | Creates a new origin within the specified endpoint. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="endpointName, originName, profileName, resourceGroupName, subscriptionId" /> | Deletes an existing origin within an endpoint. |
| <CopyableCode code="_list_by_endpoint" /> | `EXEC` | <CopyableCode code="endpointName, profileName, resourceGroupName, subscriptionId" /> | Lists all of the existing origins within an endpoint. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="endpointName, originName, profileName, resourceGroupName, subscriptionId" /> | Updates an existing origin within an endpoint. |
