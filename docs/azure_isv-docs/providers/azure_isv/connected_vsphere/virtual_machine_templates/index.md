---
title: virtual_machine_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_templates
  - connected_vsphere
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>virtual_machine_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.connected_vsphere.virtual_machine_templates" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets or sets the Id. |
| <CopyableCode code="name" /> | `string` | Gets or sets the name. |
| <CopyableCode code="extendedLocation" /> | `object` | The extended location. |
| <CopyableCode code="kind" /> | `string` | Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value. |
| <CopyableCode code="location" /> | `string` | Gets or sets the location. |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a Virtual Machine Template. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Gets or sets the Resource tags. |
| <CopyableCode code="type" /> | `string` | Gets or sets the type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, subscriptionId, virtualMachineTemplateName" /> | Implements virtual machine template GET method. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, subscriptionId" /> | List of virtualMachineTemplates in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, subscriptionId" /> | List of virtualMachineTemplates in a resource group. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="api-version, resourceGroupName, subscriptionId, virtualMachineTemplateName, data__location, data__properties" /> | Create Or Update virtual machine template. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, resourceGroupName, subscriptionId, virtualMachineTemplateName" /> | Implements virtual machine template DELETE method. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, subscriptionId, virtualMachineTemplateName" /> | API to update certain properties of the virtual machine template resource. |
