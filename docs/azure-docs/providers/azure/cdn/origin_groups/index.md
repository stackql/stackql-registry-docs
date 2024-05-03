---
title: origin_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - origin_groups
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
<tr><td><b>Name</b></td><td><code>origin_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.origin_groups" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="endpointName, originGroupName, profileName, resourceGroupName, subscriptionId" /> | Gets an existing origin group within an endpoint. |
| <CopyableCode code="list_by_endpoint" /> | `SELECT` | <CopyableCode code="endpointName, profileName, resourceGroupName, subscriptionId" /> | Lists all of the existing origin groups within an endpoint. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="endpointName, originGroupName, profileName, resourceGroupName, subscriptionId" /> | Creates a new origin group within the specified endpoint. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="endpointName, originGroupName, profileName, resourceGroupName, subscriptionId" /> | Deletes an existing origin group within an endpoint. |
| <CopyableCode code="_list_by_endpoint" /> | `EXEC` | <CopyableCode code="endpointName, profileName, resourceGroupName, subscriptionId" /> | Lists all of the existing origin groups within an endpoint. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="endpointName, originGroupName, profileName, resourceGroupName, subscriptionId" /> | Updates an existing origin group within an endpoint. |
