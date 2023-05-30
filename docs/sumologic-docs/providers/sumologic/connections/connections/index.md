---
title: connections
hide_title: false
hide_table_of_contents: false
keywords:
  - connections
  - connections
  - sumologic    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/sumologic/stackql-sumologic-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.connections.connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Unique identifier for the connection. |
| `name` | `string` | Name of the connection. |
| `description` | `string` | Description of the connection. |
| `modifiedAt` | `string` | Last modification timestamp in UTC. |
| `modifiedBy` | `string` | Identifier of the user who last modified the resource. |
| `type` | `string` | Type of connection. Valid values are `WebhookConnection`, `ServiceNowConnection`. |
| `createdAt` | `string` | Creation timestamp in UTC in [RFC3339](https://tools.ietf.org/html/rfc3339) format. |
| `createdBy` | `string` | Identifier of the user who created the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getConnection` | `SELECT` | `id, type, region` | Get a connection with the given identifier. |
| `listConnections` | `SELECT` | `region` | Get a list of all connections in the organization. The response is paginated with a default limit of 100 connections per page. |
| `createConnection` | `INSERT` | `data__name, data__type, region` | Create a new connection in the organization. |
| `deleteConnection` | `DELETE` | `id, type, region` | Delete a connection with the given identifier. |
| `updateConnection` | `EXEC` | `id, data__name, data__type, region` | Update an existing connection. |
