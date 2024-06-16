---
title: dedicated_cloud_nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - dedicated_cloud_nodes
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
<tr><td><b>Name</b></td><td><code>dedicated_cloud_nodes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.vmware_cloud_simple.dedicated_cloud_nodes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/dedicatedCloudNodes/&#123;dedicatedCloudNodeName&#125; |
| <CopyableCode code="name" /> | `string` | &#123;dedicatedCloudNodeName&#125; |
| <CopyableCode code="location" /> | `string` | Azure region |
| <CopyableCode code="properties" /> | `object` | Properties of dedicated cloud node |
| <CopyableCode code="sku" /> | `object` | The purchase SKU for CloudSimple paid resources |
| <CopyableCode code="tags" /> | `object` | Tags model |
| <CopyableCode code="type" /> | `string` | &#123;resourceProviderNamespace&#125;/&#123;resourceType&#125; |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, dedicatedCloudNodeName, resourceGroupName, subscriptionId" /> | Returns dedicated cloud node |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, subscriptionId" /> | Returns list of dedicate cloud nodes within resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="api-version, subscriptionId" /> | Returns list of dedicate cloud nodes within subscription |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="Referer, api-version, dedicatedCloudNodeName, resourceGroupName, subscriptionId, data__location" /> | Returns dedicated cloud node by its name |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, dedicatedCloudNodeName, resourceGroupName, subscriptionId" /> | Delete dedicated cloud node |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="api-version, dedicatedCloudNodeName, resourceGroupName, subscriptionId" /> | Patches dedicated node properties |
