---
title: firewalls
hide_title: false
hide_table_of_contents: false
keywords:
  - firewalls
  - droplets
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
<tr><td><b>Name</b></td><td><code>firewalls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.droplets.firewalls</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | A unique ID that can be used to identify and reference a firewall. |
| `name` | `string` | A human-readable name for a firewall. The name must begin with an alphanumeric character. Subsequent characters must either be alphanumeric characters, a period (.), or a dash (-). |
| `inbound_rules` | `array` |  |
| `pending_changes` | `array` | An array of objects each containing the fields "droplet_id", "removing", and "status". It is provided to detail exactly which Droplets are having their security policies updated. When empty, all changes have been successfully applied. |
| `status` | `string` | A status string indicating the current state of the firewall. This can be "waiting", "succeeded", or "failed". |
| `tags` | `array` | A flat array of tag names as strings to be applied to the resource. Tag names may be for either existing or new tags. |
| `created_at` | `string` | A time value given in ISO8601 combined date and time format that represents when the firewall was created. |
| `droplet_ids` | `array` | An array containing the IDs of the Droplets assigned to the firewall. |
| `outbound_rules` | `array` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_firewalls` | `SELECT` | `droplet_id` |
| `_list_firewalls` | `EXEC` | `droplet_id` |
