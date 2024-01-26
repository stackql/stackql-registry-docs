---
title: customization_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - customization_policies
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>customization_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.vmware_cloud_simple.customization_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Customization policy azure id |
| `name` | `string` | Customization policy name |
| `location` | `string` | Azure region |
| `properties` | `object` | The properties of Customization policy |
| `type` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, customizationPolicyName, pcName, regionId, subscriptionId` | Returns customization policy by its name |
| `list` | `SELECT` | `api-version, pcName, regionId, subscriptionId` | Returns list of customization policies in region for private cloud |
| `_list` | `EXEC` | `api-version, pcName, regionId, subscriptionId` | Returns list of customization policies in region for private cloud |
