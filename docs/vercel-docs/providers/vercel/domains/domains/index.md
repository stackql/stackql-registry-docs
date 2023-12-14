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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>vercel.domains.domains</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The unique identifier of the domain. |
| `name` | `string` | The domain name. |
| `boughtAt` | `number` | If it was purchased through Vercel, the timestamp in milliseconds when it was purchased. |
| `createdAt` | `number` | Timestamp in milliseconds when the domain was created in the registry. |
| `creator` | `object` | An object containing information of the domain creator, including the user's id, username, and email. |
| `customNameservers` | `array` | A list of custom nameservers for the domain to point to. Only applies to domains purchased with Vercel. |
| `expiresAt` | `number` | Timestamp in milliseconds at which the domain is set to expire. `null` if not bought with Vercel. |
| `intendedNameservers` | `array` | A list of the intended nameservers for the domain to point to Vercel DNS. |
| `nameservers` | `array` | A list of the current nameservers of the domain. |
| `orderedAt` | `number` | Timestamp in milliseconds at which the domain was ordered. |
| `renew` | `boolean` | Indicates whether the domain is set to automatically renew. |
| `serviceType` | `string` | The type of service the domain is handled by. `external` if the DNS is externally handled, `zeit.world` if handled with Vercel, or `na` if the service is not available. |
| `suffix` | `boolean` |  |
| `transferStartedAt` | `number` | If transferred into Vercel, timestamp in milliseconds when the domain transfer was initiated. |
| `transferredAt` | `number` | Timestamp in milliseconds at which the domain was successfully transferred into Vercel. `null` if the transfer is still processing or was never transferred in. |
| `verified` | `boolean` | If the domain has the ownership verified. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_domain` | `SELECT` | `domain, teamId` | Get information for a single domain in an account or team. |
| `get_domains` | `SELECT` | `teamId` | Retrieves a list of domains registered for the authenticated user or team. By default it returns the last 20 domains if no limit is provided. |
| `create_or_transfer_domain` | `INSERT` | `teamId` | This endpoint is used for adding a new apex domain name with Vercel for the authenticating user. Can also be used for initiating a domain transfer request from an external Registrar to Vercel. |
| `delete_domain` | `DELETE` | `domain, teamId` | Delete a previously registered domain name from Vercel. Deleting a domain will automatically remove any associated aliases. |
| `_get_domain` | `EXEC` | `domain, teamId` | Get information for a single domain in an account or team. |
| `_get_domains` | `EXEC` | `teamId` | Retrieves a list of domains registered for the authenticated user or team. By default it returns the last 20 domains if no limit is provided. |
| `buy_domain` | `EXEC` | `teamId, data__name` | Allows to purchase the specified domain. |
| `patch_domain` | `EXEC` | `domain, teamId` | Update or move apex domain. |
