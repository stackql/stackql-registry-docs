---
title: records
hide_title: false
hide_table_of_contents: false
keywords:
  - records
  - domains
  - linode    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Linode resources using SQL
custom_edit_url: null
image: /img/providers/linode/stackql-linode-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>records</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.domains.records</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | This Record's unique ID. |
| `name` | `string` | The name of this Record. For requests, this property's actual usage and whether it is required depends<br />on the type of record this represents:<br /><br />`A` and `AAAA`: The hostname or FQDN of the Record.<br /><br />`NS`: The subdomain, if any, to use with the Domain of the Record. Wildcard NS records (`*`) are not supported.<br /><br />`MX`: The mail subdomain. For example, `sub` for the address `user@sub.example.com` under the `example.com`<br />Domain. Must be an empty string (`""`) for a Null MX Record.<br /><br />`CNAME`: The hostname. Must be unique. Required.<br /><br />`TXT`: The hostname.<br /><br />`SRV`: Unused. Use the `service` property to set the service name for this record.<br /><br />`CAA`: The subdomain. Omit or enter an empty string (`""`) to apply to the entire Domain.<br /><br />`PTR`: See our guide on how to [Configure Your Linode for Reverse DNS<br />(rDNS)](/docs/guides/configure-rdns/).<br /> |
| `updated` | `string` | When this Domain Record was last updated. |
| `port` | `integer` | The port this Record points to. Only valid and required for SRV record requests.<br /> |
| `ttl_sec` | `integer` | "Time to Live" - the amount of time in seconds that this Domain's records may be cached by resolvers or other domain servers. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.<br /> |
| `priority` | `integer` | The priority of the target host for this Record. Lower values are preferred. Only valid for<br />MX and SRV record requests. Required for SRV record requests.<br /><br />Defaults to `0` for MX record requests. Must be `0` for Null MX records.<br /> |
| `weight` | `integer` | The relative weight of this Record used in the case of identical priority. Higher values are preferred. Only valid and required for SRV record requests.<br /> |
| `type` | `string` | The type of Record this is in the DNS system. For example, A records associate a domain name with an IPv4 address, and AAAA records associate a domain name with an IPv6 address. For more information, see the guides on [DNS Record Types](/docs/products/networking/dns-manager/guides/#dns-record-types).<br /> |
| `protocol` | `string` | The protocol this Record's service communicates with. An underscore (`_`) is prepended automatically to the submitted value for this property. Only valid for SRV record requests.<br /> |
| `service` | `string` | The name of the service. An underscore (`_`) is prepended and a period (`.`) is appended automatically to the submitted value for this property. Only valid and required for SRV record requests.<br /> |
| `target` | `string` | The target for this Record. For requests, this property's actual usage and whether it is required depends<br />on the type of record this represents:<br /><br />`A` and `AAAA`: The IP address. Use `[remote_addr]` to submit the IPv4 address of the request. Required.<br /><br />`NS`: The name server. Must be a valid domain. Required.<br /><br />`MX`: The mail server. Must be a valid domain unless creating a Null MX Record. To create a<br />[Null MX Record](https://datatracker.ietf.org/doc/html/rfc7505), first<br />[remove](/docs/api/domains/#domain-record-delete) any additional MX records, create an MX record with empty strings<br />(`""`) for the `target` and `name`. If a Domain has a Null MX record, new MX records cannot be created. Required.<br /><br />`CNAME`: The alias. Must be a valid domain. Required.<br /><br />`TXT`: The value. Required.<br /><br />`SRV`: The target domain or subdomain. If a subdomain is entered, it is automatically used with the Domain.<br />To configure for a different domain, enter a valid FQDN. For example, the value `www` with a Domain for<br />`example.com` results in a target set to `www.example.com`, whereas the value `sample.com` results in a<br />target set to `sample.com`. Required.<br /><br />`CAA`: The value. For `issue` or `issuewild` tags, the domain of your certificate issuer. For the `iodef`<br />tag, a contact or submission URL (domain, http, https, or mailto). Requirements depend on the tag for this record:<br />  * `issue`: The domain of your certificate issuer. Must be a valid domain.<br />  * `issuewild`: The domain of your wildcard certificate issuer. Must be a valid domain and must not start with an asterisk (`*`).<br />  * `iodef`: Must be either (1) a valid domain, (2) a valid domain prepended with `http://` or `https://`, or (3) a valid email address prepended with `mailto:`.<br /><br />`PTR`: Required. See our guide on how to [Configure Your Linode for Reverse DNS<br />(rDNS)](/docs/guides/configure-rdns/).<br /><br />With the exception of A, AAAA, and CAA records, this field accepts a trailing period.<br /> |
| `created` | `string` | When this Domain Record was created. |
| `tag` | `string` | The tag portion of a CAA record. Only valid and required for CAA record requests.<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getDomainRecord` | `SELECT` | `domainId, recordId` | View a single Record on this Domain.<br /> |
| `getDomainRecords` | `SELECT` | `domainId` | Returns a paginated list of Records configured on a Domain in Linode's<br />DNS Manager.<br /> |
| `createDomainRecord` | `INSERT` | `domainId, data__type` | Adds a new Domain Record to the zonefile this Domain represents.<br /><br />Each domain can have up to 12,000 active records.<br /> |
| `deleteDomainRecord` | `DELETE` | `domainId, recordId` | Deletes a Record on this Domain.<br /> |
| `_getDomainRecord` | `EXEC` | `domainId, recordId` | View a single Record on this Domain.<br /> |
| `_getDomainRecords` | `EXEC` | `domainId` | Returns a paginated list of Records configured on a Domain in Linode's<br />DNS Manager.<br /> |
| `updateDomainRecord` | `EXEC` | `domainId, recordId` | Updates a single Record on this Domain.<br /> |
