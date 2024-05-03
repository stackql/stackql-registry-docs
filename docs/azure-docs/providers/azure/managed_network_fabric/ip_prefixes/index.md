---
title: ip_prefixes
hide_title: false
hide_table_of_contents: false
keywords:
  - ip_prefixes
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
<tr><td><b>Name</b></td><td><code>ip_prefixes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network_fabric.ip_prefixes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | IP Prefix Properties defines the properties of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="ipPrefixName, resourceGroupName, subscriptionId" /> | Implements IP Prefix GET method. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Implements IpPrefixes list by resource group GET method. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Implements IpPrefixes list by subscription GET method. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="ipPrefixName, resourceGroupName, subscriptionId, data__location, data__properties" /> | Implements IP Prefix PUT method. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="ipPrefixName, resourceGroupName, subscriptionId" /> | Implements IP Prefix DELETE method. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Implements IpPrefixes list by resource group GET method. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Implements IpPrefixes list by subscription GET method. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="ipPrefixName, resourceGroupName, subscriptionId" /> | API to update certain properties of the IP Prefix resource. |
