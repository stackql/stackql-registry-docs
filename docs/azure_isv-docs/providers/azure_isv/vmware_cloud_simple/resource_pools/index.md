---
title: resource_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_pools
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
<tr><td><b>Name</b></td><td><code>resource_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.vmware_cloud_simple.resource_pools" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | resource pool id (privateCloudId:vsphereId) |
| <CopyableCode code="name" /> | `string` | &#123;ResourcePoolName&#125; |
| <CopyableCode code="location" /> | `string` | Azure region |
| <CopyableCode code="privateCloudId" /> | `string` | The Private Cloud Id |
| <CopyableCode code="properties" /> | `object` | Properties of resource pool |
| <CopyableCode code="type" /> | `string` | &#123;resourceProviderNamespace&#125;/&#123;resourceType&#125; |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, pcName, regionId, resourcePoolName, subscriptionId" /> | Returns resource pool templates by its name |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, pcName, regionId, subscriptionId" /> | Returns list of resource pools in region for private cloud |
