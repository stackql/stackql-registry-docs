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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>regions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.regions.regions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique ID of this Region. |
| <CopyableCode code="capabilities" /> | `array` | A list of capabilities of this region.<br /> |
| <CopyableCode code="country" /> | `string` | The country where this Region resides. |
| <CopyableCode code="label" /> | `string` | Detailed location information for this Region, including city, state or region, and country. |
| <CopyableCode code="resolvers" /> | `object` |  |
| <CopyableCode code="status" /> | `string` | This region's current operational status.<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getRegion" /> | `SELECT` | <CopyableCode code="regionId" /> | Returns a single Region.<br /> |
| <CopyableCode code="getRegions" /> | `SELECT` |  | Lists the Regions available for Linode services. Not all services are guaranteed to be<br />available in all Regions.<br /> |
| <CopyableCode code="_getRegion" /> | `EXEC` | <CopyableCode code="regionId" /> | Returns a single Region.<br /> |
| <CopyableCode code="_getRegions" /> | `EXEC` |  | Lists the Regions available for Linode services. Not all services are guaranteed to be<br />available in all Regions.<br /> |
