---
title: log_drains
hide_title: false
hide_table_of_contents: false
keywords:
  - log_drains
  - log_drains
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
<tr><td><b>Name</b></td><td><code>log_drains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>vercel.log_drains.log_drains</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `branch` | `string` |
| `clientId` | `string` |
| `configurationId` | `string` |
| `createdAt` | `number` |
| `createdFrom` | `string` |
| `deliveryFormat` | `string` |
| `disabledAt` | `number` |
| `disabledBy` | `string` |
| `disabledReason` | `string` |
| `environment` | `string` |
| `firstErrorTimestamp` | `number` |
| `headers` | `object` |
| `ownerId` | `string` |
| `projectIds` | `array` |
| `secret` | `string` |
| `sources` | `array` |
| `status` | `string` |
| `teamId` | `string` |
| `url` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_configurable_log_drain` | `SELECT` | `id, teamId` | Retrieves a Configurable Log Drain. This endpoint must be called with a team AccessToken (integration OAuth2 clients are not allowed). Only log drains owned by the authenticated team can be accessed. |
| `get_configurable_log_drains` | `SELECT` | `teamId` | Retrieves a list of Configurable Log Drains. This endpoint must be called with a team AccessToken (integration OAuth2 clients are not allowed). Only log drains owned by the authenticated team can be accessed. |
| `create_configurable_log_drain` | `INSERT` | `teamId, data__deliveryFormat, data__sources, data__url` | Creates a configurable log drain. This endpoint must be called with a team AccessToken (integration OAuth2 clients are not allowed) |
| `delete_configurable_log_drain` | `DELETE` | `id, teamId` | Deletes a Configurable Log Drain. This endpoint must be called with a team AccessToken (integration OAuth2 clients are not allowed). Only log drains owned by the authenticated team can be deleted. |
