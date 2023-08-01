---
title: tiers
hide_title: false
hide_table_of_contents: false
keywords:
  - tiers
  - sqladmin
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tiers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.sqladmin.tiers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `RAM` | `string` | The maximum RAM usage of this tier in bytes. |
| `kind` | `string` | This is always `sql#tier`. |
| `region` | `array` | The applicable regions for this tier. |
| `tier` | `string` | An identifier for the machine type, for example, `db-custom-1-3840`. For related information, see [Pricing](/sql/pricing). |
| `DiskQuota` | `string` | The maximum disk size of this tier in bytes. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `project` |
