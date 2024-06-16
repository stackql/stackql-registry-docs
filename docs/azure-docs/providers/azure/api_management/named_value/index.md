---
title: named_value
hide_title: false
hide_table_of_contents: false
keywords:
  - named_value
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
<tr><td><b>Name</b></td><td><code>named_value</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.named_value" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="namedValueId, resourceGroupName, serviceName, subscriptionId" /> | Gets the details of the named value specified by its identifier. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Lists a collection of named values defined within a service instance. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="namedValueId, resourceGroupName, serviceName, subscriptionId" /> | Creates or updates named value. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, namedValueId, resourceGroupName, serviceName, subscriptionId" /> | Deletes specific named value from the API Management service instance. |
| <CopyableCode code="refresh_secret" /> | `EXEC` | <CopyableCode code="namedValueId, resourceGroupName, serviceName, subscriptionId" /> | Refresh the secret of the named value specified by its identifier. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="If-Match, namedValueId, resourceGroupName, serviceName, subscriptionId" /> | Updates the specific named value. |
