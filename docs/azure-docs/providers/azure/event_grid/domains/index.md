---
title: domains
hide_title: false
hide_table_of_contents: false
keywords:
  - domains
  - event_grid
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
<tr><td><b>Name</b></td><td><code>domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.event_grid.domains" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | The identity information for the resource. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of the Event Grid Domain Resource. |
| <CopyableCode code="sku" /> | `object` | Describes an EventGrid Resource Sku. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="domainName, resourceGroupName, subscriptionId" /> | Get properties of a domain. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all the domains under a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List all the domains under an Azure subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="domainName, resourceGroupName, subscriptionId" /> | Asynchronously creates or updates a new domain with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="domainName, resourceGroupName, subscriptionId" /> | Delete existing domain. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all the domains under a resource group. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | List all the domains under an Azure subscription. |
| <CopyableCode code="regenerate_key" /> | `EXEC` | <CopyableCode code="domainName, resourceGroupName, subscriptionId, data__keyName" /> | Regenerate a shared access key for a domain. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="domainName, resourceGroupName, subscriptionId" /> | Asynchronously updates a domain with the specified parameters. |
