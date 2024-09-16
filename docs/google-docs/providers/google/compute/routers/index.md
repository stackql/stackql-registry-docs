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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>routers</code> resource.

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
| <CopyableCode code="interfaces" /> | `array` | Router interfaces. To create a BGP peer that uses a router interface, the interface must have one of the following fields specified: - linkedVpnTunnel - linkedInterconnectAttachment - subnetwork You can create a router interface without any of these fields specified. However, you cannot create a BGP peer that uses that interface. |
| <CopyableCode code="kind" /> | `string` | [Output Only] Type of resource. Always compute#router for routers. |
| <CopyableCode code="md5AuthenticationKeys" /> | `array` | Keys used for MD5 authentication. |
| <CopyableCode code="nats" /> | `array` | A list of NAT services created in this router. |
| <CopyableCode code="network" /> | `string` | URI of the network to which this router belongs. |
| <CopyableCode code="region" /> | `string` | [Output Only] URI of the region where the router resides. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined URL for the resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="aggregated_list" /> | `SELECT` | <CopyableCode code="project" /> | Retrieves an aggregated list of routers. To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`. |
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="project, region, router" /> | Returns the specified Router resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project, region" /> | Retrieves a list of Router resources available to the specified project. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="project, region" /> | Creates a Router resource in the specified project and region using the data included in the request. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="project, region, router" /> | Deletes the specified Router resource. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="project, region, router" /> | Patches the specified Router resource with the data included in the request. This method supports PATCH semantics and uses JSON merge patch format and processing rules. |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="project, region, router" /> | Updates the specified Router resource with the data included in the request. This method conforms to PUT semantics, which requests that the state of the target resource be created or replaced with the state defined by the representation enclosed in the request message payload. |
| <CopyableCode code="preview" /> | `EXEC` | <CopyableCode code="project, region, router" /> | Preview fields auto-generated during router create and update operations. Calling this method does NOT create or update the router. |

## `SELECT` examples

Retrieves an aggregated list of routers. To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

```sql
SELECT
id,
name,
description,
bgp,
bgpPeers,
creationTimestamp,
encryptedInterconnectRouter,
interfaces,
kind,
md5AuthenticationKeys,
nats,
network,
region,
selfLink
FROM google.compute.routers
WHERE project = '{{ project }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>routers</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.compute.routers (
project,
region,
kind,
id,
creationTimestamp,
name,
description,
region,
network,
interfaces,
bgpPeers,
bgp,
selfLink,
nats,
encryptedInterconnectRouter,
md5AuthenticationKeys
)
SELECT 
'{{ project }}',
'{{ region }}',
'{{ kind }}',
'{{ id }}',
'{{ creationTimestamp }}',
'{{ name }}',
'{{ description }}',
'{{ region }}',
'{{ network }}',
'{{ interfaces }}',
'{{ bgpPeers }}',
'{{ bgp }}',
'{{ selfLink }}',
'{{ nats }}',
true|false,
'{{ md5AuthenticationKeys }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: kind
      value: '{{ kind }}'
    - name: id
      value: '{{ id }}'
    - name: creationTimestamp
      value: '{{ creationTimestamp }}'
    - name: name
      value: '{{ name }}'
    - name: description
      value: '{{ description }}'
    - name: region
      value: '{{ region }}'
    - name: network
      value: '{{ network }}'
    - name: interfaces
      value: '{{ interfaces }}'
    - name: bgpPeers
      value: '{{ bgpPeers }}'
    - name: bgp
      value: '{{ bgp }}'
    - name: selfLink
      value: '{{ selfLink }}'
    - name: nats
      value: '{{ nats }}'
    - name: encryptedInterconnectRouter
      value: '{{ encryptedInterconnectRouter }}'
    - name: md5AuthenticationKeys
      value: '{{ md5AuthenticationKeys }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>routers</code> resource.

```sql
/*+ update */
UPDATE google.compute.routers
SET 
kind = '{{ kind }}',
id = '{{ id }}',
creationTimestamp = '{{ creationTimestamp }}',
name = '{{ name }}',
description = '{{ description }}',
region = '{{ region }}',
network = '{{ network }}',
interfaces = '{{ interfaces }}',
bgpPeers = '{{ bgpPeers }}',
bgp = '{{ bgp }}',
selfLink = '{{ selfLink }}',
nats = '{{ nats }}',
encryptedInterconnectRouter = true|false,
md5AuthenticationKeys = '{{ md5AuthenticationKeys }}'
WHERE 
project = '{{ project }}'
AND region = '{{ region }}'
AND router = '{{ router }}';
```

## `REPLACE` example

Replaces all fields in the specified <code>routers</code> resource.

```sql
/*+ update */
REPLACE google.compute.routers
SET 
kind = '{{ kind }}',
id = '{{ id }}',
creationTimestamp = '{{ creationTimestamp }}',
name = '{{ name }}',
description = '{{ description }}',
region = '{{ region }}',
network = '{{ network }}',
interfaces = '{{ interfaces }}',
bgpPeers = '{{ bgpPeers }}',
bgp = '{{ bgp }}',
selfLink = '{{ selfLink }}',
nats = '{{ nats }}',
encryptedInterconnectRouter = true|false,
md5AuthenticationKeys = '{{ md5AuthenticationKeys }}'
WHERE 
project = '{{ project }}'
AND region = '{{ region }}'
AND router = '{{ router }}';
```

## `DELETE` example

Deletes the specified <code>routers</code> resource.

```sql
/*+ delete */
DELETE FROM google.compute.routers
WHERE project = '{{ project }}'
AND region = '{{ region }}'
AND router = '{{ router }}';
```
