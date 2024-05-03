---
title: infra_role_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - infra_role_instances
  - fabric_admin
  - azure_stack    
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
<tr><td><b>Name</b></td><td><code>infra_role_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.fabric_admin.infra_role_instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | URI of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | The region where the resource is located. |
| <CopyableCode code="properties" /> | `object` | All properties of an infrastructure role instance. |
| <CopyableCode code="tags" /> | `object` | List of key-value pairs. |
| <CopyableCode code="type" /> | `string` | Type of resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="infraRoleInstance, location, resourceGroupName, subscriptionId" /> | Return the requested infrastructure role instance. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, resourceGroupName, subscriptionId" /> | Returns a list of all infrastructure role instances at a location. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="location, resourceGroupName, subscriptionId" /> | Returns a list of all infrastructure role instances at a location. |
| <CopyableCode code="power_off" /> | `EXEC` | <CopyableCode code="infraRoleInstance, location, resourceGroupName, subscriptionId" /> | Power off an infrastructure role instance. |
| <CopyableCode code="power_on" /> | `EXEC` | <CopyableCode code="infraRoleInstance, location, resourceGroupName, subscriptionId" /> | Power on an infrastructure role instance. |
| <CopyableCode code="reboot" /> | `EXEC` | <CopyableCode code="infraRoleInstance, location, resourceGroupName, subscriptionId" /> | Reboot an infrastructure role instance. |
| <CopyableCode code="shutdown" /> | `EXEC` | <CopyableCode code="infraRoleInstance, location, resourceGroupName, subscriptionId" /> | Shut down an infrastructure role instance. |
