---
title: packet_mirrorings
hide_title: false
hide_table_of_contents: false
keywords:
  - packet_mirrorings
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

Creates, updates, deletes, gets or lists a <code>packet_mirrorings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>packet_mirrorings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.packet_mirrorings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| <CopyableCode code="name" /> | `string` | Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| <CopyableCode code="description" /> | `string` | An optional description of this resource. Provide this property when you create the resource. |
| <CopyableCode code="collectorIlb" /> | `object` |  |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| <CopyableCode code="enable" /> | `string` | Indicates whether or not this packet mirroring takes effect. If set to FALSE, this packet mirroring policy will not be enforced on the network. The default is TRUE. |
| <CopyableCode code="filter" /> | `object` |  |
| <CopyableCode code="kind" /> | `string` | [Output Only] Type of the resource. Always compute#packetMirroring for packet mirrorings. |
| <CopyableCode code="mirroredResources" /> | `object` |  |
| <CopyableCode code="network" /> | `object` |  |
| <CopyableCode code="priority" /> | `integer` | The priority of applying this configuration. Priority is used to break ties in cases where there is more than one matching rule. In the case of two rules that apply for a given Instance, the one with the lowest-numbered priority value wins. Default value is 1000. Valid range is 0 through 65535. |
| <CopyableCode code="region" /> | `string` | [Output Only] URI of the region where the packetMirroring resides. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined URL for the resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="aggregated_list" /> | `SELECT` | <CopyableCode code="project" /> | Retrieves an aggregated list of packetMirrorings. To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`. |
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="packetMirroring, project, region" /> | Returns the specified PacketMirroring resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project, region" /> | Retrieves a list of PacketMirroring resources available to the specified project and region. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="project, region" /> | Creates a PacketMirroring resource in the specified project and region using the data included in the request. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="packetMirroring, project, region" /> | Deletes the specified PacketMirroring resource. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="packetMirroring, project, region" /> | Patches the specified PacketMirroring resource with the data included in the request. This method supports PATCH semantics and uses JSON merge patch format and processing rules. |

## `SELECT` examples

Retrieves an aggregated list of packetMirrorings. To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

```sql
SELECT
id,
name,
description,
collectorIlb,
creationTimestamp,
enable,
filter,
kind,
mirroredResources,
network,
priority,
region,
selfLink
FROM google.compute.packet_mirrorings
WHERE project = '{{ project }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>packet_mirrorings</code> resource.

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
INSERT INTO google.compute.packet_mirrorings (
project,
region,
name,
description,
region,
network,
priority,
collectorIlb,
mirroredResources,
filter,
enable
)
SELECT 
'{{ project }}',
'{{ region }}',
'{{ name }}',
'{{ description }}',
'{{ region }}',
'{{ network }}',
'{{ priority }}',
'{{ collectorIlb }}',
'{{ mirroredResources }}',
'{{ filter }}',
'{{ enable }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: description
      value: '{{ description }}'
    - name: region
      value: '{{ region }}'
    - name: network
      value:
        - name: url
          value: '{{ url }}'
        - name: canonicalUrl
          value: '{{ canonicalUrl }}'
    - name: priority
      value: '{{ priority }}'
    - name: collectorIlb
      value:
        - name: url
          value: '{{ url }}'
        - name: canonicalUrl
          value: '{{ canonicalUrl }}'
    - name: mirroredResources
      value:
        - name: subnetworks
          value:
            - name: $ref
              value: '{{ $ref }}'
        - name: instances
          value:
            - name: $ref
              value: '{{ $ref }}'
        - name: tags
          value:
            - name: type
              value: '{{ type }}'
    - name: filter
      value:
        - name: cidrRanges
          value:
            - name: type
              value: '{{ type }}'
        - name: IPProtocols
          value:
            - name: type
              value: '{{ type }}'
        - name: direction
          value: '{{ direction }}'
    - name: enable
      value: '{{ enable }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>packet_mirrorings</code> resource.

```sql
/*+ update */
UPDATE google.compute.packet_mirrorings
SET 
name = '{{ name }}',
description = '{{ description }}',
region = '{{ region }}',
network = '{{ network }}',
priority = '{{ priority }}',
collectorIlb = '{{ collectorIlb }}',
mirroredResources = '{{ mirroredResources }}',
filter = '{{ filter }}',
enable = '{{ enable }}'
WHERE 
packetMirroring = '{{ packetMirroring }}'
AND project = '{{ project }}'
AND region = '{{ region }}';
```

## `DELETE` example

Deletes the specified <code>packet_mirrorings</code> resource.

```sql
/*+ delete */
DELETE FROM google.compute.packet_mirrorings
WHERE packetMirroring = '{{ packetMirroring }}'
AND project = '{{ project }}'
AND region = '{{ region }}';
```
