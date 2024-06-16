---
title: virtual_machine_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_templates
  - vmware_cloud_simple
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.vmware_cloud_simple.virtual_machine_templates" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | virtual machine template id (privateCloudId:vsphereId) |
| <CopyableCode code="name" /> | `string` | &#123;virtualMachineTemplateName&#125; |
| <CopyableCode code="location" /> | `string` | Azure region |
| <CopyableCode code="properties" /> | `object` | Properties of virtual machine template |
| <CopyableCode code="type" /> | `string` | &#123;resourceProviderNamespace&#125;/&#123;resourceType&#125; |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, pcName, regionId, subscriptionId, virtualMachineTemplateName" /> | Returns virtual machine templates by its name |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, pcName, regionId, resourcePoolName, subscriptionId" /> | Returns list of virtual machine templates in region for private cloud |
