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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.domains.domains</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the domain itself. This should follow the standard domain format of domain.TLD. For instance, `example.com` is a valid domain name. |
| `zone_file` | `string` | This attribute contains the complete contents of the zone file for the selected domain. Individual domain record resources should be used to get more granular control over records. However, this attribute can also be used to get information about the SOA record, which is created automatically and is not accessible as an individual record resource. |
| `ip_address` | `string` | This optional attribute may contain an IP address. When provided, an A record will be automatically created pointing to the apex domain. |
| `ttl` | `integer` | This value is the time to live for the records on this domain, in seconds. This defines the time frame that clients can cache queried information before a refresh should be requested. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `domain_name` | To get details about a specific domain, send a GET request to `/v2/domains/$DOMAIN_NAME`. |
| `list` | `SELECT` |  | To retrieve a list of all of the domains in your account, send a GET request to `/v2/domains`. |
| `create` | `INSERT` |  | To create a new domain, send a POST request to `/v2/domains`. Set the "name"<br />attribute to the domain name you are adding. Optionally, you may set the<br />"ip_address" attribute, and an A record will be automatically created pointing<br />to the apex domain.<br /> |
| `delete` | `DELETE` | `domain_name` | To delete a domain, send a DELETE request to `/v2/domains/$DOMAIN_NAME`.<br /> |
| `_get` | `EXEC` | `domain_name` | To get details about a specific domain, send a GET request to `/v2/domains/$DOMAIN_NAME`. |
| `_list` | `EXEC` |  | To retrieve a list of all of the domains in your account, send a GET request to `/v2/domains`. |
