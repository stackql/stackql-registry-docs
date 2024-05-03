---
title: domains
hide_title: false
hide_table_of_contents: false
keywords:
  - domains
  - domains
  - vercel    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage Vercel resources using SQL
custom_edit_url: null
image: /img/providers/vercel/stackql-vercel-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="vercel.domains.domains" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique identifier of the domain. |
| <CopyableCode code="name" /> | `string` | The domain name. |
| <CopyableCode code="boughtAt" /> | `number` | If it was purchased through Vercel, the timestamp in milliseconds when it was purchased. |
| <CopyableCode code="createdAt" /> | `number` | Timestamp in milliseconds when the domain was created in the registry. |
| <CopyableCode code="creator" /> | `object` | An object containing information of the domain creator, including the user's id, username, and email. |
| <CopyableCode code="customNameservers" /> | `array` | A list of custom nameservers for the domain to point to. Only applies to domains purchased with Vercel. |
| <CopyableCode code="expiresAt" /> | `number` | Timestamp in milliseconds at which the domain is set to expire. `null` if not bought with Vercel. |
| <CopyableCode code="intendedNameservers" /> | `array` | A list of the intended nameservers for the domain to point to Vercel DNS. |
| <CopyableCode code="nameservers" /> | `array` | A list of the current nameservers of the domain. |
| <CopyableCode code="orderedAt" /> | `number` | Timestamp in milliseconds at which the domain was ordered. |
| <CopyableCode code="renew" /> | `boolean` | Indicates whether the domain is set to automatically renew. |
| <CopyableCode code="serviceType" /> | `string` | The type of service the domain is handled by. `external` if the DNS is externally handled, `zeit.world` if handled with Vercel, or `na` if the service is not available. |
| <CopyableCode code="suffix" /> | `boolean` |  |
| <CopyableCode code="transferStartedAt" /> | `number` | If transferred into Vercel, timestamp in milliseconds when the domain transfer was initiated. |
| <CopyableCode code="transferredAt" /> | `number` | Timestamp in milliseconds at which the domain was successfully transferred into Vercel. `null` if the transfer is still processing or was never transferred in. |
| <CopyableCode code="verified" /> | `boolean` | If the domain has the ownership verified. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_domain" /> | `SELECT` | <CopyableCode code="domain, teamId" /> | Get information for a single domain in an account or team. |
| <CopyableCode code="get_domains" /> | `SELECT` | <CopyableCode code="teamId" /> | Retrieves a list of domains registered for the authenticated user or team. By default it returns the last 20 domains if no limit is provided. |
| <CopyableCode code="create_or_transfer_domain" /> | `INSERT` | <CopyableCode code="teamId" /> | This endpoint is used for adding a new apex domain name with Vercel for the authenticating user. Can also be used for initiating a domain transfer request from an external Registrar to Vercel. |
| <CopyableCode code="delete_domain" /> | `DELETE` | <CopyableCode code="domain, teamId" /> | Delete a previously registered domain name from Vercel. Deleting a domain will automatically remove any associated aliases. |
| <CopyableCode code="_get_domain" /> | `EXEC` | <CopyableCode code="domain, teamId" /> | Get information for a single domain in an account or team. |
| <CopyableCode code="_get_domains" /> | `EXEC` | <CopyableCode code="teamId" /> | Retrieves a list of domains registered for the authenticated user or team. By default it returns the last 20 domains if no limit is provided. |
| <CopyableCode code="buy_domain" /> | `EXEC` | <CopyableCode code="teamId, data__name" /> | Allows to purchase the specified domain. |
| <CopyableCode code="patch_domain" /> | `EXEC` | <CopyableCode code="domain, teamId" /> | Update or move apex domain. |
