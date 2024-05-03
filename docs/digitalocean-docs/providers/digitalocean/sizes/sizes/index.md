---
title: sizes
hide_title: false
hide_table_of_contents: false
keywords:
  - sizes
  - sizes
  - digitalocean    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sizes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.sizes.sizes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `string` | A string describing the class of Droplets created from this size. For example: Basic, General Purpose, CPU-Optimized, Memory-Optimized, or Storage-Optimized. |
| <CopyableCode code="available" /> | `boolean` | This is a boolean value that represents whether new Droplets can be created with this size. |
| <CopyableCode code="disk" /> | `integer` | The amount of disk space set aside for Droplets of this size. The value is represented in gigabytes. |
| <CopyableCode code="memory" /> | `integer` | The amount of RAM allocated to Droplets created of this size. The value is represented in megabytes. |
| <CopyableCode code="price_hourly" /> | `number` | This describes the price of the Droplet size as measured hourly. The value is measured in US dollars. |
| <CopyableCode code="price_monthly" /> | `number` | This attribute describes the monthly cost of this Droplet size if the Droplet is kept for an entire month. The value is measured in US dollars. |
| <CopyableCode code="regions" /> | `array` | An array containing the region slugs where this size is available for Droplet creates. |
| <CopyableCode code="slug" /> | `string` | A human-readable string that is used to uniquely identify each size. |
| <CopyableCode code="transfer" /> | `number` | The amount of transfer bandwidth that is available for Droplets created in this size. This only counts traffic on the public interface. The value is given in terabytes. |
| <CopyableCode code="vcpus" /> | `integer` | The integer of number CPUs allocated to Droplets of this size. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` |  |
| <CopyableCode code="_list" /> | `EXEC` |  |
