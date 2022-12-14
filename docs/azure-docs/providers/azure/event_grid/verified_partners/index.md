---
title: verified_partners
hide_title: false
hide_table_of_contents: false
keywords:
  - verified_partners
  - event_grid
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
<tr><td><b>Name</b></td><td><code>verified_partners</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.event_grid.verified_partners</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified identifier of the resource. |
| `name` | `string` | Name of the resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | Type of the resource. |
| `properties` | `object` | Properties of the verified partner. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VerifiedPartners_Get` | `SELECT` | `verifiedPartnerName` | Get properties of a verified partner. |
| `VerifiedPartners_List` | `SELECT` |  | Get a list of all verified partners. |
