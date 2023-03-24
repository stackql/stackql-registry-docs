---
title: history
hide_title: false
hide_table_of_contents: false
keywords:
  - history
  - billing
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
<tr><td><b>Name</b></td><td><code>history</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.billing.history</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `links` | `object` |  |
| `meta` | `object` | Information about the response itself. |
| `billing_history` | `array` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `billingHistory_list` | `SELECT` |  |
