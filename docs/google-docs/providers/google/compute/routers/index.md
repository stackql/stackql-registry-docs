---
title: routers
hide_title: false
hide_table_of_contents: false
keywords:
  - routers
  - compute
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
<tr><td><b>Name</b></td><td><code>routers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.routers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| <CopyableCode code="name" /> | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| <CopyableCode code="description" /> | `string` | An optional description of this resource. Provide this property when you create the resource. |
| <CopyableCode code="bgp" /> | `object` |  |
| <CopyableCode code="bgpPeers" /> | `array` | BGP information that must be configured into the routing stack to establish BGP peering. This information must specify the peer ASN and either the interface name, IP address, or peer IP address. Please refer to RFC4273. |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| <CopyableCode code="encryptedInterconnectRouter" /> | `boolean` | Indicates if a router is dedicated for use with encrypted VLAN attachments (interconnectAttachments). |
| <CopyableCode code="interfaces" /> | `array` | Router interfaces. Each interface requires either one linked resource, (for example, linkedVpnTunnel), or IP address and IP address range (for example, ipRange), or both. |
| <CopyableCode code="kind" /> | `string` | [Output Only] Type of resource. Always compute#router for routers. |
| <CopyableCode code="md5AuthenticationKeys" /> | `array` | Keys used for MD5 authentication. |
| <CopyableCode code="nats" /> | `array` | A list of NAT services created in this router. |
| <CopyableCode code="network" /> | `string` | URI of the network to which this router belongs. |
| <CopyableCode code="region" /> | `string` | [Output Only] URI of the region where the router resides. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined URL for the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="aggregated_list" /> | `SELECT` | <CopyableCode code="project" /> | Retrieves an aggregated list of routers. |
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="project, region, router" /> | Returns the specified Router resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project, region" /> | Retrieves a list of Router resources available to the specified project. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="project, region" /> | Creates a Router resource in the specified project and region using the data included in the request. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="project, region, router" /> | Deletes the specified Router resource. |
| <CopyableCode code="_aggregated_list" /> | `EXEC` | <CopyableCode code="project" /> | Retrieves an aggregated list of routers. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="project, region, router" /> | Patches the specified Router resource with the data included in the request. This method supports PATCH semantics and uses JSON merge patch format and processing rules. |
| <CopyableCode code="preview" /> | `EXEC` | <CopyableCode code="project, region, router" /> | Preview fields auto-generated during router create and update operations. Calling this method does NOT create or update the router. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="project, region, router" /> | Updates the specified Router resource with the data included in the request. This method conforms to PUT semantics, which requests that the state of the target resource be created or replaced with the state defined by the representation enclosed in the request message payload. |
