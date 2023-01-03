---
title: instances_effective_firewalls
hide_title: false
hide_table_of_contents: false
keywords:
  - instances_effective_firewalls
  - compute
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instances_effective_firewalls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.instances_effective_firewalls</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `firewallPolicys` | `array` | Effective firewalls from firewall policies. |
| `firewalls` | `array` | Effective firewalls on the instance. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `instances_getEffectiveFirewalls` | `SELECT` | `instance, networkInterface, project, zone` |
