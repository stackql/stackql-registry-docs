---
title: firewalls
hide_title: false
hide_table_of_contents: false
keywords:
  - firewalls
  - firewalls
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
<tr><td><b>Id</b></td><td><code>digitalocean.firewalls.firewalls</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | A unique ID that can be used to identify and reference a firewall. |
| `name` | `string` | A human-readable name for a firewall. The name must begin with an alphanumeric character. Subsequent characters must either be alphanumeric characters, a period (.), or a dash (-). |
| `pending_changes` | `array` | An array of objects each containing the fields "droplet_id", "removing", and "status". It is provided to detail exactly which Droplets are having their security policies updated. When empty, all changes have been successfully applied. |
| `outbound_rules` | `array` |  |
| `droplet_ids` | `array` | An array containing the IDs of the Droplets assigned to the firewall. |
| `status` | `string` | A status string indicating the current state of the firewall. This can be "waiting", "succeeded", or "failed". |
| `tags` | `array` | A flat array of tag names as strings to be applied to the resource. Tag names may be for either existing or new tags. |
| `created_at` | `string` | A time value given in ISO8601 combined date and time format that represents when the firewall was created. |
| `inbound_rules` | `array` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `firewall_id` | To show information about an existing firewall, send a GET request to `/v2/firewalls/$FIREWALL_ID`. |
| `list` | `SELECT` |  | To list all of the firewalls available on your account, send a GET request to `/v2/firewalls`. |
| `create` | `INSERT` |  | To create a new firewall, send a POST request to `/v2/firewalls`. The request<br />must contain at least one inbound or outbound access rule.<br /> |
| `delete` | `DELETE` | `firewall_id` | To delete a firewall send a DELETE request to `/v2/firewalls/$FIREWALL_ID`.<br /><br />No response body will be sent back, but the response code will indicate<br />success. Specifically, the response code will be a 204, which means that the<br />action was successful with no returned body data.<br /> |
| `_get` | `EXEC` | `firewall_id` | To show information about an existing firewall, send a GET request to `/v2/firewalls/$FIREWALL_ID`. |
| `_list` | `EXEC` |  | To list all of the firewalls available on your account, send a GET request to `/v2/firewalls`. |
| `update` | `EXEC` | `firewall_id, data__name` | To update the configuration of an existing firewall, send a PUT request to<br />`/v2/firewalls/$FIREWALL_ID`. The request should contain a full representation<br />of the firewall including existing attributes. **Note that any attributes that<br />are not provided will be reset to their default values.**<br /> |
