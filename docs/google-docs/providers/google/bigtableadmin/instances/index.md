---
title: instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instances
  - bigtableadmin
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

Creates, updates, deletes, gets or lists a <code>instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.bigtableadmin.instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The unique name of the instance. Values are of the form `projects/{project}/instances/a-z+[a-z0-9]`. |
| <CopyableCode code="createTime" /> | `string` | Output only. A commit timestamp representing when this Instance was created. For instances created before this field was added (August 2021), this value is `seconds: 0, nanos: 1`. |
| <CopyableCode code="displayName" /> | `string` | Required. The descriptive name for this instance as it appears in UIs. Can be changed at any time, but should be kept globally unique to avoid confusion. |
| <CopyableCode code="labels" /> | `object` | Labels are a flexible and lightweight mechanism for organizing cloud resources into groups that reflect a customer's organizational needs and deployment strategies. They can be used to filter resources and aggregate metrics. * Label keys must be between 1 and 63 characters long and must conform to the regular expression: `\p{Ll}\p{Lo}{0,62}`. * Label values must be between 0 and 63 characters long and must conform to the regular expression: `[\p{Ll}\p{Lo}\p{N}_-]{0,63}`. * No more than 64 labels can be associated with a given resource. * Keys and values must both be under 128 bytes. |
| <CopyableCode code="satisfiesPzi" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="state" /> | `string` | Output only. The current state of the instance. |
| <CopyableCode code="type" /> | `string` | The type of the instance. Defaults to `PRODUCTION`. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="instancesId, projectsId" /> | Gets information about an instance. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists information about instances in a project. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Create an instance within a project. Note that exactly one of Cluster.serve_nodes and Cluster.cluster_config.cluster_autoscaling_config can be set. If serve_nodes is set to non-zero, then the cluster is manually scaled. If cluster_config.cluster_autoscaling_config is non-empty, then autoscaling is enabled. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="instancesId, projectsId" /> | Delete an instance from a project. |
| <CopyableCode code="partial_update_instance" /> | `EXEC` | <CopyableCode code="instancesId, projectsId" /> | Partially updates an instance within a project. This method can modify all fields of an Instance and is the preferred way to update an Instance. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="instancesId, projectsId" /> | Updates an instance within a project. This method updates only the display name and type for an Instance. To update other Instance properties, such as labels, use PartialUpdateInstance. |

## `SELECT` examples

Lists information about instances in a project.

```sql
SELECT
name,
createTime,
displayName,
labels,
satisfiesPzi,
satisfiesPzs,
state,
type
FROM google.bigtableadmin.instances
WHERE projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>instances</code> resource.

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
INSERT INTO google.bigtableadmin.instances (
projectsId,
parent,
instanceId,
instance,
clusters
)
SELECT 
'{{ projectsId }}',
'{{ parent }}',
'{{ instanceId }}',
'{{ instance }}',
'{{ clusters }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: parent
        value: '{{ parent }}'
      - name: instanceId
        value: '{{ instanceId }}'
      - name: instance
        value: '{{ instance }}'
      - name: clusters
        value: '{{ clusters }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>instances</code> resource.

```sql
/*+ delete */
DELETE FROM google.bigtableadmin.instances
WHERE instancesId = '{{ instancesId }}'
AND projectsId = '{{ projectsId }}';
```
