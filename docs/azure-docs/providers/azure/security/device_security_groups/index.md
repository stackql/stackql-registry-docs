---
title: device_security_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - device_security_groups
  - security
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
<tr><td><b>Name</b></td><td><code>device_security_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.device_security_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | describes properties of a security group. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, deviceSecurityGroupName" /> | Use this method to get the device security group for the specified IoT Hub resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version" /> | Use this method get the list of device security groups for the specified IoT Hub resource. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="api-version, deviceSecurityGroupName" /> | Use this method to creates or updates the device security group on a specified IoT Hub resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, deviceSecurityGroupName" /> | User this method to deletes the device security group. |
