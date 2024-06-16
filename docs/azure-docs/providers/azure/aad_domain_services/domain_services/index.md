---
title: domain_services
hide_title: false
hide_table_of_contents: false
keywords:
  - domain_services
  - aad_domain_services
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
<tr><td><b>Name</b></td><td><code>domain_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.aad_domain_services.domain_services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="etag" /> | `string` | Resource etag |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | Properties of the Domain Service. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="domainServiceName, resourceGroupName, subscriptionId" /> | The Get Domain Service operation retrieves a json representation of the Domain Service. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | The List Domain Services in Subscription operation lists all the domain services available under the given subscription (and across all resource groups within that subscription). |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | The List Domain Services in Resource Group operation lists all the domain services available under the given resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="domainServiceName, resourceGroupName, subscriptionId" /> | The Create Domain Service operation creates a new domain service with the specified parameters. If the specific service already exists, then any patchable properties will be updated and any immutable properties will remain unchanged. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="domainServiceName, resourceGroupName, subscriptionId" /> | The Delete Domain Service operation deletes an existing Domain Service. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="domainServiceName, resourceGroupName, subscriptionId" /> | The Update Domain Service operation can be used to update the existing deployment. The update call only supports the properties listed in the PATCH body. |
