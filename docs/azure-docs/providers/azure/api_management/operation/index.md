---
title: operation
hide_title: false
hide_table_of_contents: false
keywords:
  - operation
  - api_management
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
<tr><td><b>Name</b></td><td><code>operation</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.operation" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="api" /> | `object` | API contract properties for the Tag Resources. |
| <CopyableCode code="operation" /> | `object` | Operation Entity contract Properties. |
| <CopyableCode code="product" /> | `object` | Product profile. |
| <CopyableCode code="tag" /> | `object` | Contract defining the Tag property in the Tag Resource Contract |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_by_tags" /> | `SELECT` | <CopyableCode code="apiId, resourceGroupName, serviceName, subscriptionId" /> |
| <CopyableCode code="_list_by_tags" /> | `EXEC` | <CopyableCode code="apiId, resourceGroupName, serviceName, subscriptionId" /> |
