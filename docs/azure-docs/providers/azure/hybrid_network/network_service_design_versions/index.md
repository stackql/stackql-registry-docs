---
title: network_service_design_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - network_service_design_versions
  - hybrid_network
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
<tr><td><b>Name</b></td><td><code>network_service_design_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_network.network_service_design_versions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | network service design version properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkServiceDesignGroupName, networkServiceDesignVersionName, publisherName, resourceGroupName, subscriptionId" /> | Gets information about a network service design version. |
| <CopyableCode code="list_by_network_service_design_group" /> | `SELECT` | <CopyableCode code="networkServiceDesignGroupName, publisherName, resourceGroupName, subscriptionId" /> | Gets information about a list of network service design versions under a network service design group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="networkServiceDesignGroupName, networkServiceDesignVersionName, publisherName, resourceGroupName, subscriptionId" /> | Creates or updates a network service design version. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkServiceDesignGroupName, networkServiceDesignVersionName, publisherName, resourceGroupName, subscriptionId" /> | Deletes the specified network service design version. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="networkServiceDesignGroupName, networkServiceDesignVersionName, publisherName, resourceGroupName, subscriptionId" /> | Updates a network service design version resource. |
