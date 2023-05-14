---
title: regions
hide_title: false
hide_table_of_contents: false
keywords:
  - regions
  - regions
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
<tr><td><b>Name</b></td><td><code>regions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.regions.regions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The unique ID of this Region. |
| `country` | `string` | The country where this Region resides. |
| `label` | `string` | Detailed location information for this Region, including city, state or region, and country. |
| `resolvers` | `object` |  |
| `status` | `string` | This region's current operational status.<br /> |
| `capabilities` | `array` | A list of capabilities of this region.<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getRegion` | `SELECT` | `regionId` | Returns a single Region.<br /> |
| `getRegions` | `SELECT` |  | Lists the Regions available for Linode services. Not all services are guaranteed to be<br />available in all Regions.<br /> |
| `_getRegion` | `EXEC` | `regionId` | Returns a single Region.<br /> |
| `_getRegions` | `EXEC` |  | Lists the Regions available for Linode services. Not all services are guaranteed to be<br />available in all Regions.<br /> |
