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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sizes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.sizes.sizes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | A string describing the class of Droplets created from this size. For example: Basic, General Purpose, CPU-Optimized, Memory-Optimized, or Storage-Optimized. |
| `regions` | `array` | An array containing the region slugs where this size is available for Droplet creates. |
| `disk` | `integer` | The amount of disk space set aside for Droplets of this size. The value is represented in gigabytes. |
| `transfer` | `number` | The amount of transfer bandwidth that is available for Droplets created in this size. This only counts traffic on the public interface. The value is given in terabytes. |
| `price_monthly` | `number` | This attribute describes the monthly cost of this Droplet size if the Droplet is kept for an entire month. The value is measured in US dollars. |
| `slug` | `string` | A human-readable string that is used to uniquely identify each size. |
| `price_hourly` | `number` | This describes the price of the Droplet size as measured hourly. The value is measured in US dollars. |
| `vcpus` | `integer` | The integer of number CPUs allocated to Droplets of this size. |
| `memory` | `integer` | The amount of RAM allocated to Droplets created of this size. The value is represented in megabytes. |
| `available` | `boolean` | This is a boolean value that represents whether new Droplets can be created with this size. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` |  |
| `_list` | `EXEC` |  |
