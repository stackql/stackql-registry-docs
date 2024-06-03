---
title: discovery_clients
hide_title: false
hide_table_of_contents: false
keywords:
  - discovery_clients
  - migrationcenter
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
<tr><td><b>Name</b></td><td><code>discovery_clients</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.migrationcenter.discovery_clients" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Identifier. Full name of this discovery client. |
| <CopyableCode code="description" /> | `string` | Optional. Free text description. Maximum length is 1000 characters. |
| <CopyableCode code="createTime" /> | `string` | Output only. Time when the discovery client was first created. |
| <CopyableCode code="displayName" /> | `string` | Optional. Free text display name. Maximum length is 63 characters. |
| <CopyableCode code="errors" /> | `array` | Output only. Errors affecting client functionality. |
| <CopyableCode code="expireTime" /> | `string` | Optional. Client expiration time in UTC. If specified, the backend will not accept new frames after this time. |
| <CopyableCode code="heartbeatTime" /> | `string` | Output only. Last heartbeat time. Healthy clients are expected to send heartbeats regularly (normally every few minutes). |
| <CopyableCode code="labels" /> | `object` | Optional. Labels as key value pairs. |
| <CopyableCode code="serviceAccount" /> | `string` | Required. Service account used by the discovery client for various operation. |
| <CopyableCode code="signalsEndpoint" /> | `string` | Output only. This field is intended for internal use. |
| <CopyableCode code="source" /> | `string` | Required. Immutable. Full name of the source object associated with this discovery client. |
| <CopyableCode code="state" /> | `string` | Output only. Current state of the discovery client. |
| <CopyableCode code="ttl" /> | `string` | Optional. Input only. Client time-to-live. If specified, the backend will not accept new frames after this time. This field is input only. The derived expiration time is provided as output through the `expire_time` field. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Time when the discovery client was last updated. This value is not updated by heartbeats, to view the last heartbeat time please refer to the `heartbeat_time` field. |
| <CopyableCode code="version" /> | `string` | Output only. Client version, as reported in recent heartbeat. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="discoveryClientsId, locationsId, projectsId" /> | Gets the details of a discovery client. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists all the discovery clients in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new discovery client. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="discoveryClientsId, locationsId, projectsId" /> | Deletes a discovery client. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="discoveryClientsId, locationsId, projectsId" /> | Updates a discovery client. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists all the discovery clients in a given project and location. |
| <CopyableCode code="send_heartbeat" /> | `EXEC` | <CopyableCode code="discoveryClientsId, locationsId, projectsId" /> | Sends a discovery client heartbeat. Healthy clients are expected to send heartbeats regularly (normally every few minutes). |
