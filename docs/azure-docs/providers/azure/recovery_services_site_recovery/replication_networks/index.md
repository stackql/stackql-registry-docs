---
title: replication_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_networks
  - recovery_services_site_recovery
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
<tr><td><b>Name</b></td><td><code>replication_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_site_recovery.replication_networks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource Name |
| <CopyableCode code="location" /> | `string` | Resource Location |
| <CopyableCode code="properties" /> | `object` | Network Properties. |
| <CopyableCode code="type" /> | `string` | Resource Type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, fabricName, networkName, resourceGroupName, resourceName, subscriptionId" /> | Gets the details of a network. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, resourceName, subscriptionId" /> | Lists the networks available in a vault. |
| <CopyableCode code="list_by_replication_fabrics" /> | `SELECT` | <CopyableCode code="api-version, fabricName, resourceGroupName, resourceName, subscriptionId" /> | Lists the networks available for a fabric. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, resourceName, subscriptionId" /> | Lists the networks available in a vault. |
| <CopyableCode code="_list_by_replication_fabrics" /> | `EXEC` | <CopyableCode code="api-version, fabricName, resourceGroupName, resourceName, subscriptionId" /> | Lists the networks available for a fabric. |
