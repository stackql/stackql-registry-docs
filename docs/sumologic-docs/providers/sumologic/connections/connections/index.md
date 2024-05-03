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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="sumologic.connections.connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Unique identifier for the connection. |
| <CopyableCode code="name" /> | `string` | Name of the connection. |
| <CopyableCode code="description" /> | `string` | Description of the connection. |
| <CopyableCode code="createdAt" /> | `string` | Creation timestamp in UTC in [RFC3339](https://tools.ietf.org/html/rfc3339) format. |
| <CopyableCode code="createdBy" /> | `string` | Identifier of the user who created the resource. |
| <CopyableCode code="modifiedAt" /> | `string` | Last modification timestamp in UTC. |
| <CopyableCode code="modifiedBy" /> | `string` | Identifier of the user who last modified the resource. |
| <CopyableCode code="type" /> | `string` | Type of connection. Valid values are `WebhookConnection`, `ServiceNowConnection`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getConnection" /> | `SELECT` | <CopyableCode code="id, type, region" /> | Get a connection with the given identifier. |
| <CopyableCode code="listConnections" /> | `SELECT` | <CopyableCode code="region" /> | Get a list of all connections in the organization. The response is paginated with a default limit of 100 connections per page. |
| <CopyableCode code="createConnection" /> | `INSERT` | <CopyableCode code="data__name, data__type, region" /> | Create a new connection in the organization. |
| <CopyableCode code="deleteConnection" /> | `DELETE` | <CopyableCode code="id, type, region" /> | Delete a connection with the given identifier. |
| <CopyableCode code="updateConnection" /> | `EXEC` | <CopyableCode code="id, data__name, data__type, region" /> | Update an existing connection. |
