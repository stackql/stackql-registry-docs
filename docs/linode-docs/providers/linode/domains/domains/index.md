---
title: domains
hide_title: false
hide_table_of_contents: false
keywords:
  - domains
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.domains.domains" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | This Domain's unique ID |
| <CopyableCode code="description" /> | `string` | A description for this Domain. This is for display purposes only.<br /> |
| <CopyableCode code="axfr_ips" /> | `array` | The list of IPs that may perform a zone transfer for this Domain. The total combined length of all data within this array cannot exceed 1000 characters.<br /><br />**Note**: This is potentially dangerous, and should be set to an empty list unless you intend to use it.<br /> |
| <CopyableCode code="domain" /> | `string` | The domain this Domain represents. Domain labels cannot be longer than 63 characters and must conform to [RFC1035](https://tools.ietf.org/html/rfc1035). Domains must be unique on Linode's platform, including across different Linode accounts; there cannot be two Domains representing the same domain.<br /> |
| <CopyableCode code="expire_sec" /> | `integer` | The amount of time in seconds that may pass before this Domain is no longer<br />authoritative.<br /><br />* Valid values are<br />0, 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200.<br /><br />* Any other value is rounded up to the nearest valid value.<br /><br />* A value of 0 is equivalent to the default value of 1209600.<br /> |
| <CopyableCode code="group" /> | `string` | The group this Domain belongs to.  This is for display purposes only.<br /> |
| <CopyableCode code="master_ips" /> | `array` | The IP addresses representing the master DNS for this Domain. At least one value is required for `type` slave Domains. The total combined length of all data within this array cannot exceed 1000 characters.<br /> |
| <CopyableCode code="refresh_sec" /> | `integer` | The amount of time in seconds before this Domain should be refreshed.<br /><br />* Valid values are<br />0, 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200.<br /><br />* Any other value is rounded up to the nearest valid value.<br /><br />* A value of 0 is equivalent to the default value of 14400.<br /> |
| <CopyableCode code="retry_sec" /> | `integer` | The interval, in seconds, at which a failed refresh should be retried.<br /><br />* Valid values are<br />0, 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200.<br /><br />* Any other value is rounded up to the nearest valid value.<br /><br />* A value of 0 is equivalent to the default value of 14400.<br /> |
| <CopyableCode code="soa_email" /> | `string` | Start of Authority email address. This is required for `type` master Domains.<br /> |
| <CopyableCode code="status" /> | `string` | Used to control whether this Domain is currently being rendered.<br /> |
| <CopyableCode code="tags" /> | `array` | An array of tags applied to this object.  Tags are for organizational purposes only.<br /> |
| <CopyableCode code="ttl_sec" /> | `integer` | "Time to Live" - the amount of time in seconds that this Domain's records may be cached by resolvers or other domain servers.<br />* Valid values are 0, 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200.<br />* Any other value is rounded up to the nearest valid value.<br />* A value of 0 is equivalent to the default value of 86400.<br /> |
| <CopyableCode code="type" /> | `string` | Whether this Domain represents the authoritative source of information for the domain it describes ("master"), or whether it is a read-only copy of a master ("slave").<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getDomain" /> | `SELECT` | <CopyableCode code="domainId" /> | This is a single Domain that you have registered in Linode's DNS Manager. Linode is not a registrar, and in order for this Domain record to work you must own the domain and point your registrar at Linode's nameservers.<br /> |
| <CopyableCode code="getDomains" /> | `SELECT` |  | This is a collection of Domains that you have registered in Linode's DNS Manager.  Linode is not a registrar, and in order for these to work you must own the domains and point your registrar at Linode's nameservers.<br /> |
| <CopyableCode code="createDomain" /> | `INSERT` | <CopyableCode code="data__domain, data__type" /> | Adds a new Domain to Linode's DNS Manager. Linode is not a registrar, and you must own the domain before adding it here. Be sure to point your registrar to Linode's nameservers so that the records hosted here are used.<br /> |
| <CopyableCode code="deleteDomain" /> | `DELETE` | <CopyableCode code="domainId" /> | Deletes a Domain from Linode's DNS Manager. The Domain will be removed from Linode's nameservers shortly after this operation completes. This also deletes all associated Domain Records.<br /> |
| <CopyableCode code="_getDomain" /> | `EXEC` | <CopyableCode code="domainId" /> | This is a single Domain that you have registered in Linode's DNS Manager. Linode is not a registrar, and in order for this Domain record to work you must own the domain and point your registrar at Linode's nameservers.<br /> |
| <CopyableCode code="_getDomains" /> | `EXEC` |  | This is a collection of Domains that you have registered in Linode's DNS Manager.  Linode is not a registrar, and in order for these to work you must own the domains and point your registrar at Linode's nameservers.<br /> |
| <CopyableCode code="cloneDomain" /> | `EXEC` | <CopyableCode code="domainId, data__domain" /> | Clones a Domain and all associated DNS records from a Domain that is registered in Linode's DNS manager.<br /> |
| <CopyableCode code="importDomain" /> | `EXEC` | <CopyableCode code="data__domain, data__remote_nameserver" /> | Imports a domain zone from a remote nameserver.<br />Your nameserver must allow zone transfers (AXFR) from the following IPs:<br /><br />  - 96.126.114.97<br />  - 96.126.114.98<br />  - 2600:3c00::5e<br />  - 2600:3c00::5f<br /> |
| <CopyableCode code="updateDomain" /> | `EXEC` | <CopyableCode code="domainId" /> | Update information about a Domain in Linode's DNS Manager.<br /> |
