---
title: virtual_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_networks
  - vmware_cloud_simple
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
<tr><td><b>Name</b></td><td><code>virtual_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.vmware_cloud_simple.virtual_networks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | virtual network id (privateCloudId:vsphereId) |
| <CopyableCode code="name" /> | `string` | &#123;VirtualNetworkName&#125; |
| <CopyableCode code="assignable" /> | `boolean` | can be used in vm creation/deletion |
| <CopyableCode code="location" /> | `string` | Azure region |
| <CopyableCode code="properties" /> | `object` | Properties of virtual network |
| <CopyableCode code="type" /> | `string` | &#123;resourceProviderNamespace&#125;/&#123;resourceType&#125; |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, pcName, regionId, subscriptionId, virtualNetworkName" /> | Return virtual network by its name |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, pcName, regionId, resourcePoolName, subscriptionId" /> | Return list of virtual networks in location for private cloud |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="api-version, pcName, regionId, resourcePoolName, subscriptionId" /> | Return list of virtual networks in location for private cloud |
