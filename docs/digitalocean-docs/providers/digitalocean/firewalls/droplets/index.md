---
title: droplets
hide_title: false
hide_table_of_contents: false
keywords:
  - droplets
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
<tr><td><b>Name</b></td><td><code>droplets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.firewalls.droplets</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `delete_droplets` | `DELETE` | `firewall_id, data__droplet_ids` | To remove a Droplet from a firewall, send a DELETE request to<br />`/v2/firewalls/$FIREWALL_ID/droplets`. In the body of the request, there should<br />be a `droplet_ids` attribute containing a list of Droplet IDs.<br /><br />No response body will be sent back, but the response code will indicate<br />success. Specifically, the response code will be a 204, which means that the<br />action was successful with no returned body data.<br /> |
| `assign_droplets` | `EXEC` | `firewall_id, data__droplet_ids` | To assign a Droplet to a firewall, send a POST request to<br />`/v2/firewalls/$FIREWALL_ID/droplets`. In the body of the request, there<br />should be a `droplet_ids` attribute containing a list of Droplet IDs.<br /><br />No response body will be sent back, but the response code will indicate<br />success. Specifically, the response code will be a 204, which means that the<br />action was successful with no returned body data.<br /> |
