---
title: virtual_machine_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_templates
  - vmware_cloud_simple
  - azure_extras    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_machine_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.vmware_cloud_simple.virtual_machine_templates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | virtual machine template id (privateCloudId:vsphereId) |
| `name` | `string` | &#123;virtualMachineTemplateName&#125; |
| `properties` | `object` | Properties of virtual machine template |
| `type` | `string` | &#123;resourceProviderNamespace&#125;/&#123;resourceType&#125; |
| `location` | `string` | Azure region |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualMachineTemplates_Get` | `SELECT` | `api-version, pcName, regionId, subscriptionId, virtualMachineTemplateName` | Returns virtual machine templates by its name |
| `VirtualMachineTemplates_List` | `SELECT` | `api-version, pcName, regionId, resourcePoolName, subscriptionId` | Returns list of virtual machine templates in region for private cloud |
