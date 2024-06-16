---
title: instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instances
  - scom
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
<tr><td><b>Name</b></td><td><code>instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.scom.instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Azure Active Directory identity configuration for a resource. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The properties of a SCOM instance resource |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="instanceName, resourceGroupName, subscriptionId" /> | Get SCOM managed instance details |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all SCOM managed instances in a resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all SCOM managed instances in a subscription  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="instanceName, resourceGroupName, subscriptionId" /> | Create or update SCOM managed instance |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="instanceName, resourceGroupName, subscriptionId" /> | Delete a SCOM managed instance |
| <CopyableCode code="link_log_analytics" /> | `EXEC` | <CopyableCode code="instanceName, resourceGroupName, subscriptionId" /> | Link Log Analytics workspace for SCOM monitoring instance |
| <CopyableCode code="patch_servers" /> | `EXEC` | <CopyableCode code="instanceName, resourceGroupName, subscriptionId" /> | Update SCOM servers with latest scom software. |
| <CopyableCode code="scale" /> | `EXEC` | <CopyableCode code="instanceName, resourceGroupName, subscriptionId" /> | Scaling SCOM managed instance. |
| <CopyableCode code="unlink_log_analytics" /> | `EXEC` | <CopyableCode code="instanceName, resourceGroupName, subscriptionId" /> | Unlink Log Analytics workspace for SCOM monitoring instance |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="instanceName, resourceGroupName, subscriptionId" /> | Patch SCOM managed instance |
