
---
title: peerings
hide_title: false
hide_table_of_contents: false
keywords:
  - peerings
  - managedidentities
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

Creates, updates, deletes or gets an <code>peering</code> resource or lists <code>peerings</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>peerings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.managedidentities.peerings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Unique name of the peering in this scope including projects and location using the form: `projects/{project_id}/locations/global/peerings/{peering_id}`. |
| <CopyableCode code="authorizedNetwork" /> | `string` | Required. The full names of the Google Compute Engine [networks](/compute/docs/networks-and-firewalls#networks) to which the instance is connected. Caller needs to make sure that CIDR subnets do not overlap between networks, else peering creation will fail. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time the instance was created. |
| <CopyableCode code="domainResource" /> | `string` | Required. Full domain resource path for the Managed AD Domain involved in peering. The resource path should be in the form: `projects/{project_id}/locations/global/domains/{domain_name}` |
| <CopyableCode code="labels" /> | `object` | Optional. Resource labels to represent user-provided metadata. |
| <CopyableCode code="state" /> | `string` | Output only. The current state of this Peering. |
| <CopyableCode code="statusMessage" /> | `string` | Output only. Additional information about the current status of this peering, if available. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Last update time. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="peeringsId, projectsId" /> | Gets details of a single Peering. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists Peerings in a given project. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates a Peering for Managed AD instance. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="peeringsId, projectsId" /> | Deletes identified Peering. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="peeringsId, projectsId" /> | Updates the labels for specified Peering. |

## `SELECT` examples

Lists Peerings in a given project.

```sql
SELECT
name,
authorizedNetwork,
createTime,
domainResource,
labels,
state,
statusMessage,
updateTime
FROM google.managedidentities.peerings
WHERE projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>peerings</code> resource.

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
INSERT INTO google.managedidentities.peerings (
projectsId,
name,
labels,
authorizedNetwork,
domainResource,
createTime,
updateTime,
state,
statusMessage
)
SELECT 
'{{ projectsId }}',
'{{ name }}',
'{{ labels }}',
'{{ authorizedNetwork }}',
'{{ domainResource }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ state }}',
'{{ statusMessage }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: labels
        value: '{{ labels }}'
      - name: authorizedNetwork
        value: '{{ authorizedNetwork }}'
      - name: domainResource
        value: '{{ domainResource }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: state
        value: '{{ state }}'
      - name: statusMessage
        value: '{{ statusMessage }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a peering only if the necessary resources are available.

```sql
UPDATE google.managedidentities.peerings
SET 
name = '{{ name }}',
labels = '{{ labels }}',
authorizedNetwork = '{{ authorizedNetwork }}',
domainResource = '{{ domainResource }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
state = '{{ state }}',
statusMessage = '{{ statusMessage }}'
WHERE 
peeringsId = '{{ peeringsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified peering resource.

```sql
DELETE FROM google.managedidentities.peerings
WHERE peeringsId = '{{ peeringsId }}'
AND projectsId = '{{ projectsId }}';
```
