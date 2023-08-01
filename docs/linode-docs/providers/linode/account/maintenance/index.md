---
title: maintenance
hide_title: false
hide_table_of_contents: false
keywords:
  - maintenance
  - account
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
<tr><td><b>Name</b></td><td><code>maintenance</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.account.maintenance</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `reason` | `string` | The reason maintenance is being performed.<br /> |
| `status` | `string` | The maintenance status.<br /><br />Maintenance progresses in the following sequence: pending, started, then completed.<br /> |
| `type` | `string` | The type of maintenance.<br /> |
| `when` | `string` | When the maintenance will begin.<br /><br />[Filterable](/docs/api/#filtering-and-sorting) with the following parameters:<br /><br />* A single value in date-time string format ("%Y-%m-%dT%H:%M:%S"), which returns only matches to that value.<br /><br />* A dictionary containing pairs of inequality operator string keys ("+or", "+gt", "+gte", "+lt", "+lte",<br />or "+neq") and single date-time string format values ("%Y-%m-%dT%H:%M:%S"). "+or" accepts an array of values that<br />may consist of single date-time strings or dictionaries of inequality operator pairs.<br /> |
| `entity` | `object` | The entity being affected by maintenance.<br /> |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getMaintenance` | `SELECT` |  |
| `_getMaintenance` | `EXEC` |  |
