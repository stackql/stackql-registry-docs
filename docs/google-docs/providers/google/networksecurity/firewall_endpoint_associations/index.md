---
title: firewall_endpoint_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_endpoint_associations
  - networksecurity
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

Creates, updates, deletes, gets or lists a <code>firewall_endpoint_associations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>firewall_endpoint_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.networksecurity.firewall_endpoint_associations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. Identifier. name of resource |
| <CopyableCode code="createTime" /> | `string` | Output only. Create time stamp |
| <CopyableCode code="disabled" /> | `boolean` | Optional. Whether the association is disabled. True indicates that traffic won't be intercepted |
| <CopyableCode code="firewallEndpoint" /> | `string` | Required. The URL of the FirewallEndpoint that is being associated. |
| <CopyableCode code="labels" /> | `object` | Optional. Labels as key value pairs |
| <CopyableCode code="network" /> | `string` | Required. The URL of the network that is being associated. |
| <CopyableCode code="reconciling" /> | `boolean` | Output only. Whether reconciling is in progress, recommended per https://google.aip.dev/128. |
| <CopyableCode code="state" /> | `string` | Output only. Current state of the association. |
| <CopyableCode code="tlsInspectionPolicy" /> | `string` | Optional. The URL of the TlsInspectionPolicy that is being associated. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Update time stamp |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_firewall_endpoint_associations_get" /> | `SELECT` | <CopyableCode code="firewallEndpointAssociationsId, locationsId, projectsId" /> | Gets details of a single FirewallEndpointAssociation. |
| <CopyableCode code="projects_locations_firewall_endpoint_associations_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists Associations in a given project and location. |
| <CopyableCode code="projects_locations_firewall_endpoint_associations_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new FirewallEndpointAssociation in a given project and location. |
| <CopyableCode code="projects_locations_firewall_endpoint_associations_delete" /> | `DELETE` | <CopyableCode code="firewallEndpointAssociationsId, locationsId, projectsId" /> | Deletes a single FirewallEndpointAssociation. |
| <CopyableCode code="projects_locations_firewall_endpoint_associations_patch" /> | `UPDATE` | <CopyableCode code="firewallEndpointAssociationsId, locationsId, projectsId" /> | Update a single FirewallEndpointAssociation. |

## `SELECT` examples

Lists Associations in a given project and location.

```sql
SELECT
name,
createTime,
disabled,
firewallEndpoint,
labels,
network,
reconciling,
state,
tlsInspectionPolicy,
updateTime
FROM google.networksecurity.firewall_endpoint_associations
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>firewall_endpoint_associations</code> resource.

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
INSERT INTO google.networksecurity.firewall_endpoint_associations (
locationsId,
projectsId,
name,
createTime,
updateTime,
labels,
state,
network,
firewallEndpoint,
tlsInspectionPolicy,
reconciling,
disabled
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ labels }}',
'{{ state }}',
'{{ network }}',
'{{ firewallEndpoint }}',
'{{ tlsInspectionPolicy }}',
true|false,
true|false
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: createTime
      value: '{{ createTime }}'
    - name: updateTime
      value: '{{ updateTime }}'
    - name: labels
      value: '{{ labels }}'
    - name: state
      value: '{{ state }}'
    - name: network
      value: '{{ network }}'
    - name: firewallEndpoint
      value: '{{ firewallEndpoint }}'
    - name: tlsInspectionPolicy
      value: '{{ tlsInspectionPolicy }}'
    - name: reconciling
      value: '{{ reconciling }}'
    - name: disabled
      value: '{{ disabled }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>firewall_endpoint_associations</code> resource.

```sql
/*+ update */
UPDATE google.networksecurity.firewall_endpoint_associations
SET 
name = '{{ name }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
labels = '{{ labels }}',
state = '{{ state }}',
network = '{{ network }}',
firewallEndpoint = '{{ firewallEndpoint }}',
tlsInspectionPolicy = '{{ tlsInspectionPolicy }}',
reconciling = true|false,
disabled = true|false
WHERE 
firewallEndpointAssociationsId = '{{ firewallEndpointAssociationsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>firewall_endpoint_associations</code> resource.

```sql
/*+ delete */
DELETE FROM google.networksecurity.firewall_endpoint_associations
WHERE firewallEndpointAssociationsId = '{{ firewallEndpointAssociationsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
