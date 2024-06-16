---
title: api_tag_description
hide_title: false
hide_table_of_contents: false
keywords:
  - api_tag_description
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
<tr><td><b>Name</b></td><td><code>api_tag_description</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.api_tag_description" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="apiId, resourceGroupName, serviceName, subscriptionId, tagDescriptionId" /> | Get Tag description in scope of API |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="apiId, resourceGroupName, serviceName, subscriptionId" /> | Lists all Tags descriptions in scope of API. Model similar to swagger - tagDescription is defined on API level but tag may be assigned to the Operations |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="apiId, resourceGroupName, serviceName, subscriptionId, tagDescriptionId" /> | Create/Update tag description in scope of the Api. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, apiId, resourceGroupName, serviceName, subscriptionId, tagDescriptionId" /> | Delete tag description for the Api. |
