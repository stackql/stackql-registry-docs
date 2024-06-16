---
title: dns_resolvers
hide_title: false
hide_table_of_contents: false
keywords:
  - dns_resolvers
  - dns_resolver
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
<tr><td><b>Name</b></td><td><code>dns_resolvers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dns_resolver.dns_resolvers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | ETag of the DNS resolver. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Represents the properties of a DNS resolver. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dnsResolverName, resourceGroupName, subscriptionId" /> | Gets properties of a DNS resolver. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists DNS resolvers in all resource groups of a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists DNS resolvers within a resource group. |
| <CopyableCode code="list_by_virtual_network" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkName" /> | Lists DNS resolver resource IDs linked to a virtual network. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="dnsResolverName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates a DNS resolver. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dnsResolverName, resourceGroupName, subscriptionId" /> | Deletes a DNS resolver. WARNING: This operation cannot be undone. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="dnsResolverName, resourceGroupName, subscriptionId" /> | Updates a DNS resolver. |
