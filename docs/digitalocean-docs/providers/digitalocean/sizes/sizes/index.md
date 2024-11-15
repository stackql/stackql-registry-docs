---
title: sizes
hide_title: false
hide_table_of_contents: false
keywords:
  - sizes
  - sizes
  - digitalocean
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage digitalocean resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>sizes</code> resource.

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
| <CopyableCode code="disk_info" /> | `array` | An array of objects containing information about the disks available to Droplets created with this size. |
| <CopyableCode code="gpu_info" /> | `object` | An object containing information about the GPU capabilities of Droplets created with this size. |
| <CopyableCode code="memory" /> | `integer` | The amount of RAM allocated to Droplets created of this size. The value is represented in megabytes. |
| <CopyableCode code="price_hourly" /> | `number` | This describes the price of the Droplet size as measured hourly. The value is measured in US dollars. |
| <CopyableCode code="price_monthly" /> | `number` | This attribute describes the monthly cost of this Droplet size if the Droplet is kept for an entire month. The value is measured in US dollars. |
| <CopyableCode code="regions" /> | `array` | An array containing the region slugs where this size is available for Droplet creates. |
| <CopyableCode code="slug" /> | `string` | A human-readable string that is used to uniquely identify each size. |
| <CopyableCode code="transfer" /> | `number` | The amount of transfer bandwidth that is available for Droplets created in this size. This only counts traffic on the public interface. The value is given in terabytes. |
| <CopyableCode code="vcpus" /> | `integer` | The number of CPUs allocated to Droplets of this size. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="sizes_list" /> | `SELECT` | <CopyableCode code="" /> | To list all of available Droplet sizes, send a GET request to `/v2/sizes`. The response will be a JSON object with a key called `sizes`. The value of this will be an array of `size` objects each of which contain the standard size attributes. |

## `SELECT` examples

To list all of available Droplet sizes, send a GET request to `/v2/sizes`. The response will be a JSON object with a key called `sizes`. The value of this will be an array of `size` objects each of which contain the standard size attributes.


```sql
SELECT
description,
available,
disk,
disk_info,
gpu_info,
memory,
price_hourly,
price_monthly,
regions,
slug,
transfer,
vcpus
FROM digitalocean.sizes.sizes
;
```