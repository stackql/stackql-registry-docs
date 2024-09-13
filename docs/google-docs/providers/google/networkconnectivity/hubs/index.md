
---
title: hubs
hide_title: false
hide_table_of_contents: false
keywords:
  - hubs
  - networkconnectivity
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

Creates, updates, deletes or gets an <code>hub</code> resource or lists <code>hubs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hubs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.networkconnectivity.hubs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The name of the hub. Hub names must be unique. They use the following form: `projects/{project_number}/locations/global/hubs/{hub_id}` |
| <CopyableCode code="description" /> | `string` | An optional description of the hub. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time the hub was created. |
| <CopyableCode code="exportPsc" /> | `boolean` | Optional. Whether Private Service Connect transitivity is enabled for the hub. If true, Private Service Connect endpoints in VPC spokes attached to the hub are made accessible to other VPC spokes attached to the hub. The default value is false. |
| <CopyableCode code="labels" /> | `object` | Optional labels in key-value pair format. For more information about labels, see [Requirements for labels](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements). |
| <CopyableCode code="policyMode" /> | `string` | Optional. The policy mode of this hub. This field can be either PRESET or CUSTOM. If unspecified, the policy_mode defaults to PRESET. |
| <CopyableCode code="presetTopology" /> | `string` | Optional. The topology implemented in this hub. Currently, this field is only used when policy_mode = PRESET. The available preset topologies are MESH and STAR. If preset_topology is unspecified and policy_mode = PRESET, the preset_topology defaults to MESH. When policy_mode = CUSTOM, the preset_topology is set to PRESET_TOPOLOGY_UNSPECIFIED. |
| <CopyableCode code="routeTables" /> | `array` | Output only. The route tables that belong to this hub. They use the following form: `projects/{project_number}/locations/global/hubs/{hub_id}/routeTables/{route_table_id}` This field is read-only. Network Connectivity Center automatically populates it based on the route tables nested under the hub. |
| <CopyableCode code="routingVpcs" /> | `array` | The VPC networks associated with this hub's spokes. This field is read-only. Network Connectivity Center automatically populates it based on the set of spokes attached to the hub. |
| <CopyableCode code="spokeSummary" /> | `object` | Summarizes information about the spokes associated with a hub. The summary includes a count of spokes according to type and according to state. If any spokes are inactive, the summary also lists the reasons they are inactive, including a count for each reason. |
| <CopyableCode code="state" /> | `string` | Output only. The current lifecycle state of this hub. |
| <CopyableCode code="uniqueId" /> | `string` | Output only. The Google-generated UUID for the hub. This value is unique across all hub resources. If a hub is deleted and another with the same name is created, the new hub is assigned a different unique_id. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time the hub was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hubsId, projectsId" /> | Gets details about a Network Connectivity Center hub. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists the Network Connectivity Center hubs associated with a given project. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates a new Network Connectivity Center hub in the specified project. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="hubsId, projectsId" /> | Deletes a Network Connectivity Center hub. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="hubsId, projectsId" /> | Updates the description and/or labels of a Network Connectivity Center hub. |
| <CopyableCode code="accept_spoke" /> | `EXEC` | <CopyableCode code="hubsId, projectsId" /> | Accepts a proposal to attach a Network Connectivity Center spoke to a hub. |
| <CopyableCode code="reject_spoke" /> | `EXEC` | <CopyableCode code="hubsId, projectsId" /> | Rejects a Network Connectivity Center spoke from being attached to a hub. If the spoke was previously in the `ACTIVE` state, it transitions to the `INACTIVE` state and is no longer able to connect to other spokes that are attached to the hub. |

## `SELECT` examples

Lists the Network Connectivity Center hubs associated with a given project.

```sql
SELECT
name,
description,
createTime,
exportPsc,
labels,
policyMode,
presetTopology,
routeTables,
routingVpcs,
spokeSummary,
state,
uniqueId,
updateTime
FROM google.networkconnectivity.hubs
WHERE projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>hubs</code> resource.

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
INSERT INTO google.networkconnectivity.hubs (
projectsId,
name,
createTime,
updateTime,
labels,
description,
uniqueId,
state,
routingVpcs,
routeTables,
spokeSummary,
policyMode,
presetTopology,
exportPsc
)
SELECT 
'{{ projectsId }}',
'{{ name }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ labels }}',
'{{ description }}',
'{{ uniqueId }}',
'{{ state }}',
'{{ routingVpcs }}',
'{{ routeTables }}',
'{{ spokeSummary }}',
'{{ policyMode }}',
'{{ presetTopology }}',
true|false
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
      - name: createTime
        value: '{{ createTime }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: labels
        value: '{{ labels }}'
      - name: description
        value: '{{ description }}'
      - name: uniqueId
        value: '{{ uniqueId }}'
      - name: state
        value: '{{ state }}'
      - name: routingVpcs
        value: '{{ routingVpcs }}'
      - name: routeTables
        value: '{{ routeTables }}'
      - name: spokeSummary
        value: '{{ spokeSummary }}'
      - name: policyMode
        value: '{{ policyMode }}'
      - name: presetTopology
        value: '{{ presetTopology }}'
      - name: exportPsc
        value: '{{ exportPsc }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a hub only if the necessary resources are available.

```sql
UPDATE google.networkconnectivity.hubs
SET 
name = '{{ name }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
labels = '{{ labels }}',
description = '{{ description }}',
uniqueId = '{{ uniqueId }}',
state = '{{ state }}',
routingVpcs = '{{ routingVpcs }}',
routeTables = '{{ routeTables }}',
spokeSummary = '{{ spokeSummary }}',
policyMode = '{{ policyMode }}',
presetTopology = '{{ presetTopology }}',
exportPsc = true|false
WHERE 
hubsId = '{{ hubsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified hub resource.

```sql
DELETE FROM google.networkconnectivity.hubs
WHERE hubsId = '{{ hubsId }}'
AND projectsId = '{{ projectsId }}';
```
