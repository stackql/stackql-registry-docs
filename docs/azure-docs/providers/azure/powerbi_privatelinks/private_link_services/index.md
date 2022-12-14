---
title: private_link_services
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_services
  - powerbi_privatelinks
  - azure    
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
<tr><td><b>Name</b></td><td><code>private_link_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.powerbi_privatelinks.private_link_services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Specifies the resource identifier of the resource. |
| `name` | `string` | Specifies the name of the resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Specifies the tags of the resource. |
| `type` | `string` | Specifies the type of the resource. |
| `location` | `string` | Specifies the location of the resource. |
| `properties` | `object` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `PrivateLinkServices_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` |
