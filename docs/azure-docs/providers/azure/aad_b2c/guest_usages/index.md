---
title: guest_usages
hide_title: false
hide_table_of_contents: false
keywords:
  - guest_usages
  - aad_b2c
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
<tr><td><b>Name</b></td><td><code>guest_usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.aad_b2c.guest_usages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | An identifier that represents the Guest Usages resource. |
| <CopyableCode code="name" /> | `string` | The name of the Guest Usages resource. |
| <CopyableCode code="location" /> | `string` | Location of the Guest Usages resource. |
| <CopyableCode code="properties" /> | `object` | Guest Usages Resource Properties |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Key-value pairs of additional resource provisioning properties. |
| <CopyableCode code="type" /> | `string` | The type of the Guest Usages resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Gets a Guest Usages resource for the Microsoft.AzureActiveDirectory resource provider |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets Guest Usages resources under a resource group for the Microsoft.AzureActiveDirectory resource provider |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets Guest Usages resources under a subscription for the Microsoft.AzureActiveDirectory resource provider |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Creates a Guest Usages resource, which is used to linking a subscription to an instance of Azure AD External Identities. [Learn more](https://aka.ms/extidbilling). |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Deletes a Guest Usages resource for the Microsoft.AzureActiveDirectory resource provider |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Updates a Guest Usages resource for the Microsoft.AzureActiveDirectory resource provider |
