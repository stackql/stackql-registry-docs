---
title: partner
hide_title: false
hide_table_of_contents: false
keywords:
  - partner
  - management_partner
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
<tr><td><b>Name</b></td><td><code>partner</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.management_partner.partner</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Identifier of the partner |
| `name` | `string` | Name of the partner |
| `etag` | `integer` | Type of the partner |
| `properties` | `object` | this is the management partner properties |
| `type` | `string` | Type of resource. "Microsoft.ManagementPartner/partners" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `partnerId` | Get the management partner using the partnerId, objectId and tenantId. |
| `create` | `INSERT` | `partnerId` | Create a management partner for the objectId and tenantId. |
| `delete` | `DELETE` | `partnerId` | Delete the management partner for the objectId and tenantId. |
| `update` | `EXEC` | `partnerId` | Update the management partner for the objectId and tenantId. |
