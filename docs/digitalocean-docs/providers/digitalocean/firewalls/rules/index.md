---
title: rules
hide_title: false
hide_table_of_contents: false
keywords:
  - rules
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
<tr><td><b>Name</b></td><td><code>rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.firewalls.rules</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `add_rules` | `INSERT` | `firewall_id` | To add additional access rules to a firewall, send a POST request to<br />`/v2/firewalls/$FIREWALL_ID/rules`. The body of the request may include an<br />inbound_rules and/or outbound_rules attribute containing an array of rules to<br />be added.<br /><br />No response body will be sent back, but the response code will indicate<br />success. Specifically, the response code will be a 204, which means that the<br />action was successful with no returned body data.<br /> |
| `delete_rules` | `DELETE` | `firewall_id` | To remove access rules from a firewall, send a DELETE request to<br />`/v2/firewalls/$FIREWALL_ID/rules`. The body of the request may include an<br />`inbound_rules` and/or `outbound_rules` attribute containing an array of rules<br />to be removed.<br /><br />No response body will be sent back, but the response code will indicate<br />success. Specifically, the response code will be a 204, which means that the<br />action was successful with no returned body data.<br /> |
