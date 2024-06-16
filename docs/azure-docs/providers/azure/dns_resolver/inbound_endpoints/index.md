---
title: inbound_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - inbound_endpoints
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
<tr><td><b>Name</b></td><td><code>inbound_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dns_resolver.inbound_endpoints" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | ETag of the inbound endpoint. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Represents the properties of an inbound endpoint for a DNS resolver. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dnsResolverName, inboundEndpointName, resourceGroupName, subscriptionId" /> | Gets properties of an inbound endpoint for a DNS resolver. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="dnsResolverName, resourceGroupName, subscriptionId" /> | Lists inbound endpoints for a DNS resolver. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="dnsResolverName, inboundEndpointName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates an inbound endpoint for a DNS resolver. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dnsResolverName, inboundEndpointName, resourceGroupName, subscriptionId" /> | Deletes an inbound endpoint for a DNS resolver. WARNING: This operation cannot be undone. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="dnsResolverName, inboundEndpointName, resourceGroupName, subscriptionId" /> | Updates an inbound endpoint for a DNS resolver. |
