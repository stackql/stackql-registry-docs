---
title: security_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - security_rules
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
<tr><td><b>Name</b></td><td><code>security_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.security_rules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Security rule resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkSecurityGroupName, resourceGroupName, securityRuleName, subscriptionId" /> | Get the specified network security rule. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="networkSecurityGroupName, resourceGroupName, subscriptionId" /> | Gets all security rules in a network security group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="networkSecurityGroupName, resourceGroupName, securityRuleName, subscriptionId" /> | Creates or updates a security rule in the specified network security group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkSecurityGroupName, resourceGroupName, securityRuleName, subscriptionId" /> | Deletes the specified network security rule. |
