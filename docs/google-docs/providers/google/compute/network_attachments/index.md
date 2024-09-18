---
title: network_attachments
hide_title: false
hide_table_of_contents: false
keywords:
  - network_attachments
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

Creates, updates, deletes, gets or lists a <code>network_attachments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.network_attachments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] The unique identifier for the resource type. The server generates this identifier. |
| <CopyableCode code="name" /> | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| <CopyableCode code="description" /> | `string` | An optional description of this resource. Provide this property when you create the resource. |
| <CopyableCode code="connectionEndpoints" /> | `array` | [Output Only] An array of connections for all the producers connected to this network attachment. |
| <CopyableCode code="connectionPreference" /> | `string` |  |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| <CopyableCode code="fingerprint" /> | `string` | Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking. An up-to-date fingerprint must be provided in order to patch. |
| <CopyableCode code="kind" /> | `string` | [Output Only] Type of the resource. |
| <CopyableCode code="network" /> | `string` | [Output Only] The URL of the network which the Network Attachment belongs to. Practically it is inferred by fetching the network of the first subnetwork associated. Because it is required that all the subnetworks must be from the same network, it is assured that the Network Attachment belongs to the same network as all the subnetworks. |
| <CopyableCode code="producerAcceptLists" /> | `array` | Projects that are allowed to connect to this network attachment. The project can be specified using its id or number. |
| <CopyableCode code="producerRejectLists" /> | `array` | Projects that are not allowed to connect to this network attachment. The project can be specified using its id or number. |
| <CopyableCode code="region" /> | `string` | [Output Only] URL of the region where the network attachment resides. This field applies only to the region resource. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined URL for the resource. |
| <CopyableCode code="selfLinkWithId" /> | `string` | [Output Only] Server-defined URL for this resource's resource id. |
| <CopyableCode code="subnetworks" /> | `array` | An array of URLs where each entry is the URL of a subnet provided by the service consumer to use for endpoints in the producers that connect to this network attachment. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="aggregated_list" /> | `SELECT` | <CopyableCode code="project" /> | Retrieves the list of all NetworkAttachment resources, regional and global, available to the specified project. To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`. |
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkAttachment, project, region" /> | Returns the specified NetworkAttachment resource in the given scope. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project, region" /> | Lists the NetworkAttachments for a project in the given scope. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="project, region" /> | Creates a NetworkAttachment in the specified project in the given scope using the parameters that are included in the request. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkAttachment, project, region" /> | Deletes the specified NetworkAttachment in the given scope |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="networkAttachment, project, region" /> | Patches the specified NetworkAttachment resource with the data included in the request. This method supports PATCH semantics and uses JSON merge patch format and processing rules. |

## `SELECT` examples

Retrieves the list of all NetworkAttachment resources, regional and global, available to the specified project. To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

```sql
SELECT
id,
name,
description,
connectionEndpoints,
connectionPreference,
creationTimestamp,
fingerprint,
kind,
network,
producerAcceptLists,
producerRejectLists,
region,
selfLink,
selfLinkWithId,
subnetworks
FROM google.compute.network_attachments
WHERE project = '{{ project }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>network_attachments</code> resource.

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
INSERT INTO google.compute.network_attachments (
project,
region,
name,
description,
region,
connectionPreference,
connectionEndpoints,
subnetworks,
producerRejectLists,
producerAcceptLists,
fingerprint,
network
)
SELECT 
'{{ project }}',
'{{ region }}',
'{{ name }}',
'{{ description }}',
'{{ region }}',
'{{ connectionPreference }}',
'{{ connectionEndpoints }}',
'{{ subnetworks }}',
'{{ producerRejectLists }}',
'{{ producerAcceptLists }}',
'{{ fingerprint }}',
'{{ network }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
kind: string
id: string
creationTimestamp: string
name: string
description: string
selfLink: string
selfLinkWithId: string
region: string
connectionPreference: string
connectionEndpoints:
  - status: string
    projectIdOrNum: string
    subnetwork: string
    ipAddress: string
    ipv6Address: string
    secondaryIpCidrRanges:
      - type: string
    subnetworkCidrRange: string
subnetworks:
  - type: string
producerRejectLists:
  - type: string
producerAcceptLists:
  - type: string
fingerprint: string
network: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>network_attachments</code> resource.

```sql
/*+ update */
UPDATE google.compute.network_attachments
SET 
name = '{{ name }}',
description = '{{ description }}',
region = '{{ region }}',
connectionPreference = '{{ connectionPreference }}',
connectionEndpoints = '{{ connectionEndpoints }}',
subnetworks = '{{ subnetworks }}',
producerRejectLists = '{{ producerRejectLists }}',
producerAcceptLists = '{{ producerAcceptLists }}',
fingerprint = '{{ fingerprint }}',
network = '{{ network }}'
WHERE 
networkAttachment = '{{ networkAttachment }}'
AND project = '{{ project }}'
AND region = '{{ region }}';
```

## `DELETE` example

Deletes the specified <code>network_attachments</code> resource.

```sql
/*+ delete */
DELETE FROM google.compute.network_attachments
WHERE networkAttachment = '{{ networkAttachment }}'
AND project = '{{ project }}'
AND region = '{{ region }}';
```
