---
title: api_wiki
hide_title: false
hide_table_of_contents: false
keywords:
  - api_wiki
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
<tr><td><b>Name</b></td><td><code>api_wiki</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.api_wiki" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="apiId, resourceGroupName, serviceName, subscriptionId" /> | Gets the details of the Wiki for an API specified by its identifier. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="apiId, resourceGroupName, serviceName, subscriptionId" /> | Creates a new Wiki for an API or updates an existing one. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, apiId, resourceGroupName, serviceName, subscriptionId" /> | Deletes the specified Wiki from an API. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="If-Match, apiId, resourceGroupName, serviceName, subscriptionId" /> | Updates the details of the Wiki for an API specified by its identifier. |
