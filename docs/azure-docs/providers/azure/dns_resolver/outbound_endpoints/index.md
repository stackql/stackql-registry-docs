---
title: outbound_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - outbound_endpoints
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
<tr><td><b>Name</b></td><td><code>outbound_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dns_resolver.outbound_endpoints" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | ETag of the outbound endpoint. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Represents the properties of an outbound endpoint for a DNS resolver. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dnsResolverName, outboundEndpointName, resourceGroupName, subscriptionId" /> | Gets properties of an outbound endpoint for a DNS resolver. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="dnsResolverName, resourceGroupName, subscriptionId" /> | Lists outbound endpoints for a DNS resolver. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="dnsResolverName, outboundEndpointName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates an outbound endpoint for a DNS resolver. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dnsResolverName, outboundEndpointName, resourceGroupName, subscriptionId" /> | Deletes an outbound endpoint for a DNS resolver. WARNING: This operation cannot be undone. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="dnsResolverName, outboundEndpointName, resourceGroupName, subscriptionId" /> | Updates an outbound endpoint for a DNS resolver. |
