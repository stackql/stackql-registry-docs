---
title: connections
hide_title: false
hide_table_of_contents: false
keywords:
  - connections
  - connectors
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="connectors.connections" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="check_readiness" /> | `EXEC` | <CopyableCode code="connectionsId, locationsId, projectsId" /> | Reports readiness status of the connector. Similar logic to GetStatus but modified for kubernetes health check to understand. |
| <CopyableCode code="check_status" /> | `EXEC` | <CopyableCode code="connectionsId, locationsId, projectsId" /> | Reports the status of the connection. Note that when the connection is in a state that is not ACTIVE, the implementation of this RPC method must return a Status with the corresponding State instead of returning a gRPC status code that is not "OK", which indicates that ConnectionStatus itself, not the connection, failed. |
| <CopyableCode code="exchange_auth_code" /> | `EXEC` | <CopyableCode code="connectionsId, locationsId, projectsId" /> | ExchangeAuthCode exchanges the OAuth authorization code (and other necessary data) for an access token (and associated credentials). |
| <CopyableCode code="execute_sql_query" /> | `EXEC` | <CopyableCode code="connectionsId, locationsId, projectsId" /> | Executes a SQL statement specified in the body of the request. An example of this SQL statement in the case of Salesforce connector would be 'select * from Account a, Order o where a.Id = o.AccountId'. |
| <CopyableCode code="refresh_access_token" /> | `EXEC` | <CopyableCode code="connectionsId, locationsId, projectsId" /> | RefreshAccessToken exchanges the OAuth refresh token (and other necessary data) for a new access token (and new associated credentials). |
