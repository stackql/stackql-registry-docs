---
title: node_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - node_groups
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

Creates, updates, deletes, gets or lists a <code>node_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>node_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.node_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| <CopyableCode code="name" /> | `string` | The name of the resource, provided by the client when initially creating the resource. The resource name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| <CopyableCode code="description" /> | `string` | An optional description of this resource. Provide this property when you create the resource. |
| <CopyableCode code="autoscalingPolicy" /> | `object` |  |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| <CopyableCode code="fingerprint" /> | `string` |  |
| <CopyableCode code="kind" /> | `string` | [Output Only] The type of the resource. Always compute#nodeGroup for node group. |
| <CopyableCode code="locationHint" /> | `string` | An opaque location hint used to place the Node close to other resources. This field is for use by internal tools that use the public API. The location hint here on the NodeGroup overrides any location_hint present in the NodeTemplate. |
| <CopyableCode code="maintenanceInterval" /> | `string` | Specifies the frequency of planned maintenance events. The accepted values are: `AS_NEEDED` and `RECURRENT`. |
| <CopyableCode code="maintenancePolicy" /> | `string` | Specifies how to handle instances when a node in the group undergoes maintenance. Set to one of: DEFAULT, RESTART_IN_PLACE, or MIGRATE_WITHIN_NODE_GROUP. The default value is DEFAULT. For more information, see Maintenance policies. |
| <CopyableCode code="maintenanceWindow" /> | `object` | Time window specified for daily maintenance operations. GCE's internal maintenance will be performed within this window. |
| <CopyableCode code="nodeTemplate" /> | `string` | URL of the node template to create the node group from. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined URL for the resource. |
| <CopyableCode code="shareSettings" /> | `object` | The share setting for reservations and sole tenancy node groups. |
| <CopyableCode code="size" /> | `integer` | [Output Only] The total number of nodes in the node group. |
| <CopyableCode code="status" /> | `string` |  |
| <CopyableCode code="zone" /> | `string` | [Output Only] The name of the zone where the node group resides, such as us-central1-a. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="aggregated_list" /> | `SELECT` | <CopyableCode code="project" /> | Retrieves an aggregated list of node groups. Note: use nodeGroups.listNodes for more details about each group. To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`. |
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="nodeGroup, project, zone" /> | Returns the specified NodeGroup. Get a list of available NodeGroups by making a list() request. Note: the "nodes" field should not be used. Use nodeGroups.listNodes instead. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project, zone" /> | Retrieves a list of node groups available to the specified project. Note: use nodeGroups.listNodes for more details about each group. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="initialNodeCount, project, zone" /> | Creates a NodeGroup resource in the specified project using the data included in the request. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="nodeGroup, project, zone" /> | Deletes the specified NodeGroup resource. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="nodeGroup, project, zone" /> | Updates the specified node group. |
| <CopyableCode code="perform_maintenance" /> | `EXEC` | <CopyableCode code="nodeGroup, project, zone" /> | Perform maintenance on a subset of nodes in the node group. |
| <CopyableCode code="set_node_template" /> | `EXEC` | <CopyableCode code="nodeGroup, project, zone" /> | Updates the node template of the node group. |
| <CopyableCode code="simulate_maintenance_event" /> | `EXEC` | <CopyableCode code="nodeGroup, project, zone" /> | Simulates maintenance event on specified nodes from the node group. |

## `SELECT` examples

Retrieves an aggregated list of node groups. Note: use nodeGroups.listNodes for more details about each group. To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

```sql
SELECT
id,
name,
description,
autoscalingPolicy,
creationTimestamp,
fingerprint,
kind,
locationHint,
maintenanceInterval,
maintenancePolicy,
maintenanceWindow,
nodeTemplate,
selfLink,
shareSettings,
size,
status,
zone
FROM google.compute.node_groups
WHERE project = '{{ project }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>node_groups</code> resource.

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
INSERT INTO google.compute.node_groups (
initialNodeCount,
project,
zone,
name,
description,
nodeTemplate,
zone,
status,
size,
autoscalingPolicy,
maintenancePolicy,
locationHint,
fingerprint,
maintenanceWindow,
shareSettings,
maintenanceInterval
)
SELECT 
'{{ initialNodeCount }}',
'{{ project }}',
'{{ zone }}',
'{{ name }}',
'{{ description }}',
'{{ nodeTemplate }}',
'{{ zone }}',
'{{ status }}',
'{{ size }}',
'{{ autoscalingPolicy }}',
'{{ maintenancePolicy }}',
'{{ locationHint }}',
'{{ fingerprint }}',
'{{ maintenanceWindow }}',
'{{ shareSettings }}',
'{{ maintenanceInterval }}'
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
    - name: nodeTemplate
      value: '{{ nodeTemplate }}'
    - name: zone
      value: '{{ zone }}'
    - name: status
      value: '{{ status }}'
    - name: size
      value: '{{ size }}'
    - name: autoscalingPolicy
      value:
        - name: mode
          value: '{{ mode }}'
        - name: minNodes
          value: '{{ minNodes }}'
        - name: maxNodes
          value: '{{ maxNodes }}'
    - name: maintenancePolicy
      value: '{{ maintenancePolicy }}'
    - name: locationHint
      value: '{{ locationHint }}'
    - name: fingerprint
      value: '{{ fingerprint }}'
    - name: maintenanceWindow
      value:
        - name: startTime
          value: '{{ startTime }}'
        - name: maintenanceDuration
          value:
            - name: seconds
              value: '{{ seconds }}'
            - name: nanos
              value: '{{ nanos }}'
    - name: shareSettings
      value:
        - name: shareType
          value: '{{ shareType }}'
        - name: projectMap
          value: '{{ projectMap }}'
    - name: maintenanceInterval
      value: '{{ maintenanceInterval }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>node_groups</code> resource.

```sql
/*+ update */
UPDATE google.compute.node_groups
SET 
name = '{{ name }}',
description = '{{ description }}',
nodeTemplate = '{{ nodeTemplate }}',
zone = '{{ zone }}',
status = '{{ status }}',
size = '{{ size }}',
autoscalingPolicy = '{{ autoscalingPolicy }}',
maintenancePolicy = '{{ maintenancePolicy }}',
locationHint = '{{ locationHint }}',
fingerprint = '{{ fingerprint }}',
maintenanceWindow = '{{ maintenanceWindow }}',
shareSettings = '{{ shareSettings }}',
maintenanceInterval = '{{ maintenanceInterval }}'
WHERE 
nodeGroup = '{{ nodeGroup }}'
AND project = '{{ project }}'
AND zone = '{{ zone }}';
```

## `DELETE` example

Deletes the specified <code>node_groups</code> resource.

```sql
/*+ delete */
DELETE FROM google.compute.node_groups
WHERE nodeGroup = '{{ nodeGroup }}'
AND project = '{{ project }}'
AND zone = '{{ zone }}';
```
