---
title: tags
hide_title: false
hide_table_of_contents: false
keywords:
  - tags
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.firewalls.tags" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="add_tags" /> | `INSERT` | <CopyableCode code="firewall_id, data__tags" /> | To assign a tag representing a group of Droplets to a firewall, send a POST<br />request to `/v2/firewalls/$FIREWALL_ID/tags`. In the body of the request,<br />there should be a `tags` attribute containing a list of tag names.<br /><br />No response body will be sent back, but the response code will indicate<br />success. Specifically, the response code will be a 204, which means that the<br />action was successful with no returned body data.<br /> |
| <CopyableCode code="delete_tags" /> | `DELETE` | <CopyableCode code="firewall_id, data__tags" /> | To remove a tag representing a group of Droplets from a firewall, send a<br />DELETE request to `/v2/firewalls/$FIREWALL_ID/tags`. In the body of the<br />request, there should be a `tags` attribute containing a list of tag names.<br /><br />No response body will be sent back, but the response code will indicate<br />success. Specifically, the response code will be a 204, which means that the<br />action was successful with no returned body data.<br /> |
