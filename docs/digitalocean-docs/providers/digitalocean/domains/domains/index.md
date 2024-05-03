---
title: domains
hide_title: false
hide_table_of_contents: false
keywords:
  - domains
  - domains
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
<tr><td><b>Name</b></td><td><code>domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.domains.domains" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the domain itself. This should follow the standard domain format of domain.TLD. For instance, `example.com` is a valid domain name. |
| <CopyableCode code="ip_address" /> | `string` | This optional attribute may contain an IP address. When provided, an A record will be automatically created pointing to the apex domain. |
| <CopyableCode code="ttl" /> | `integer` | This value is the time to live for the records on this domain, in seconds. This defines the time frame that clients can cache queried information before a refresh should be requested. |
| <CopyableCode code="zone_file" /> | `string` | This attribute contains the complete contents of the zone file for the selected domain. Individual domain record resources should be used to get more granular control over records. However, this attribute can also be used to get information about the SOA record, which is created automatically and is not accessible as an individual record resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="domain_name" /> | To get details about a specific domain, send a GET request to `/v2/domains/$DOMAIN_NAME`. |
| <CopyableCode code="list" /> | `SELECT` |  | To retrieve a list of all of the domains in your account, send a GET request to `/v2/domains`. |
| <CopyableCode code="create" /> | `INSERT` |  | To create a new domain, send a POST request to `/v2/domains`. Set the "name"<br />attribute to the domain name you are adding. Optionally, you may set the<br />"ip_address" attribute, and an A record will be automatically created pointing<br />to the apex domain.<br /> |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="domain_name" /> | To delete a domain, send a DELETE request to `/v2/domains/$DOMAIN_NAME`.<br /> |
| <CopyableCode code="_get" /> | `EXEC` | <CopyableCode code="domain_name" /> | To get details about a specific domain, send a GET request to `/v2/domains/$DOMAIN_NAME`. |
| <CopyableCode code="_list" /> | `EXEC` |  | To retrieve a list of all of the domains in your account, send a GET request to `/v2/domains`. |
