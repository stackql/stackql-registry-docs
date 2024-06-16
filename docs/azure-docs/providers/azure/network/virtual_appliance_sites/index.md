---
title: virtual_appliance_sites
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_appliance_sites
  - network
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
<tr><td><b>Name</b></td><td><code>virtual_appliance_sites</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.virtual_appliance_sites" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Name of the virtual appliance site. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Properties of the rule group. |
| <CopyableCode code="type" /> | `string` | Site type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkVirtualApplianceName, resourceGroupName, siteName, subscriptionId" /> | Gets the specified Virtual Appliance Site. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="networkVirtualApplianceName, resourceGroupName, subscriptionId" /> | Lists all Network Virtual Appliance Sites in a Network Virtual Appliance resource. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="networkVirtualApplianceName, resourceGroupName, siteName, subscriptionId" /> | Creates or updates the specified Network Virtual Appliance Site. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkVirtualApplianceName, resourceGroupName, siteName, subscriptionId" /> | Deletes the specified site from a Virtual Appliance. |
