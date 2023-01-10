---
title: partners
hide_title: false
hide_table_of_contents: false
keywords:
  - partners
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
<tr><td><b>Name</b></td><td><code>partners</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.management_partner.partners</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Identifier of the partner |
| `name` | `string` | Name of the partner |
| `type` | `string` | Type of resource. "Microsoft.ManagementPartner/partners" |
| `etag` | `integer` | Type of the partner |
| `properties` | `object` | this is the management partner properties |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Partners_Get` | `SELECT` |  |
