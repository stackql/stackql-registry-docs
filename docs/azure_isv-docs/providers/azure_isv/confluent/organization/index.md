---
title: organization
hide_title: false
hide_table_of_contents: false
keywords:
  - organization
  - confluent
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>organization</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.confluent.organization" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ARM id of the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="location" /> | `string` | Location of Organization resource |
| <CopyableCode code="properties" /> | `object` | Organization resource property |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Organization resource tags |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="organizationName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="organizationName, resourceGroupName, subscriptionId, data__properties" /> |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="organizationName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="organizationName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="validate_organization" /> | `EXEC` | <CopyableCode code="organizationName, resourceGroupName, subscriptionId, data__properties" /> |
| <CopyableCode code="validate_organization_v2" /> | `EXEC` | <CopyableCode code="organizationName, resourceGroupName, subscriptionId, data__properties" /> |
