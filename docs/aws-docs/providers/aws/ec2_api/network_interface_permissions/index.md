---
title: network_interface_permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - network_interface_permissions
  - ec2_api
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_interface_permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.network_interface_permissions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="awsAccountId" /> | `string` | The Amazon Web Services account ID. |
| <CopyableCode code="awsService" /> | `string` | The Amazon Web Service. |
| <CopyableCode code="networkInterfaceId" /> | `string` | The ID of the network interface. |
| <CopyableCode code="networkInterfacePermissionId" /> | `string` | The ID of the network interface permission. |
| <CopyableCode code="permission" /> | `string` | The type of permission. |
| <CopyableCode code="permissionState" /> | `object` | Describes the state of a network interface permission. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="network_interface_permissions_Describe" /> | `SELECT` | <CopyableCode code="region" /> | Describes the permissions for your network interfaces.  |
| <CopyableCode code="network_interface_permission_Create" /> | `INSERT` | <CopyableCode code="NetworkInterfaceId, Permission, region" /> | &lt;p&gt;Grants an Amazon Web Services-authorized account permission to attach the specified network interface to an instance in their account.&lt;/p&gt; &lt;p&gt;You can grant permission to a single Amazon Web Services account only, and only one account at a time.&lt;/p&gt; |
| <CopyableCode code="network_interface_permission_Delete" /> | `DELETE` | <CopyableCode code="NetworkInterfacePermissionId, region" /> | Deletes a permission for a network interface. By default, you cannot delete the permission if the account for which you're removing the permission has attached the network interface to an instance. However, you can force delete the permission, regardless of any attachment. |
