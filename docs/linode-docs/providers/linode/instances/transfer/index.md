---
title: transfer
hide_title: false
hide_table_of_contents: false
keywords:
  - transfer
  - instances
  - linode    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Linode resources using SQL
custom_edit_url: null
image: /img/providers/linode/stackql-linode-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transfer</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.instances.transfer</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `quota` | `integer` | The amount of network transfer this Linode adds to your transfer pool, in GB, for the current month's billing cycle.<br /> |
| `used` | `integer` | The amount of network transfer used by this Linode, in bytes, for the current month's billing cycle.<br /> |
| `billable` | `integer` | The amount of network transfer this Linode has used, in GB, past your monthly quota.<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getLinodeTransfer` | `SELECT` | `linodeId` | Returns a Linode's network transfer pool statistics for the current month.<br /> |
| `getLinodeTransferByYearMonth` | `SELECT` | `linodeId, month, year` | Returns a Linode's network transfer statistics for a specific month. The year/month values must be either a date in the past, or the current month.<br /> |
| `_getLinodeTransfer` | `EXEC` | `linodeId` | Returns a Linode's network transfer pool statistics for the current month.<br /> |
| `_getLinodeTransferByYearMonth` | `EXEC` | `linodeId, month, year` | Returns a Linode's network transfer statistics for a specific month. The year/month values must be either a date in the past, or the current month.<br /> |
