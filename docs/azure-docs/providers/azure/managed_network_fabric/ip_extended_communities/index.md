---
title: ip_extended_communities
hide_title: false
hide_table_of_contents: false
keywords:
  - ip_extended_communities
  - managed_network_fabric
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
<tr><td><b>Name</b></td><td><code>ip_extended_communities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network_fabric.ip_extended_communities" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | IP Extended Community Properties defines the resource properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="ipExtendedCommunityName, resourceGroupName, subscriptionId" /> | Implements IP Extended Community GET method. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Implements IpExtendedCommunities list by resource group GET method. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Implements IpExtendedCommunities list by subscription GET method. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="ipExtendedCommunityName, resourceGroupName, subscriptionId, data__properties" /> | Implements IP Extended Community PUT method. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="ipExtendedCommunityName, resourceGroupName, subscriptionId" /> | Implements IP Extended Community DELETE method. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Implements IpExtendedCommunities list by resource group GET method. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Implements IpExtendedCommunities list by subscription GET method. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="ipExtendedCommunityName, resourceGroupName, subscriptionId" /> | API to update certain properties of the IP Extended Community resource. |
