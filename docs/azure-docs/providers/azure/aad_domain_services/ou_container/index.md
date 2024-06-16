---
title: ou_container
hide_title: false
hide_table_of_contents: false
keywords:
  - ou_container
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
<tr><td><b>Name</b></td><td><code>ou_container</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.aad_domain_services.ou_container" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="etag" /> | `string` | Resource etag |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | Properties of the OuContainer. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="domainServiceName, ouContainerName, resourceGroupName, subscriptionId" /> | Get OuContainer in DomainService instance. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="domainServiceName, resourceGroupName, subscriptionId" /> | The List of OuContainers in DomainService instance. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="domainServiceName, ouContainerName, resourceGroupName, subscriptionId" /> | The Create OuContainer operation creates a new OuContainer under the specified Domain Service instance. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="domainServiceName, ouContainerName, resourceGroupName, subscriptionId" /> | The Delete OuContainer operation deletes specified OuContainer. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="domainServiceName, ouContainerName, resourceGroupName, subscriptionId" /> | The Update OuContainer operation can be used to update the existing OuContainers. |
