---
title: documentation
hide_title: false
hide_table_of_contents: false
keywords:
  - documentation
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
<tr><td><b>Name</b></td><td><code>documentation</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.documentation" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="documentationId, resourceGroupName, serviceName, subscriptionId" /> | Gets the details of the Documentation specified by its identifier. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Lists all Documentations of the API Management service instance. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="documentationId, resourceGroupName, serviceName, subscriptionId" /> | Creates a new Documentation or updates an existing one. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, documentationId, resourceGroupName, serviceName, subscriptionId" /> | Deletes the specified Documentation from an API. |
| <CopyableCode code="_list_by_service" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Lists all Documentations of the API Management service instance. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="If-Match, documentationId, resourceGroupName, serviceName, subscriptionId" /> | Updates the details of the Documentation for an API specified by its identifier. |
