---
title: instance_groups_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_groups_instances
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

Creates, updates, deletes, gets or lists a <code>instance_groups_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instance_groups_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.instance_groups_instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="instance" /> | `string` | [Output Only] The URL of the instance. |
| <CopyableCode code="namedPorts" /> | `array` | [Output Only] The named ports that belong to this instance group. |
| <CopyableCode code="status" /> | `string` | [Output Only] The status of the instance. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_instances" /> | `SELECT` | <CopyableCode code="instanceGroup, project, zone" /> | Lists the instances in the specified instance group. The orderBy query parameter is not supported. The filter query parameter is supported, but only for expressions that use `eq` (equal) or `ne` (not equal) operators. |
| <CopyableCode code="add_instances" /> | `INSERT` | <CopyableCode code="instanceGroup, project, zone" /> | Adds a list of instances to the specified instance group. All of the instances in the instance group must be in the same network/subnetwork. Read Adding instances for more information. |
| <CopyableCode code="remove_instances" /> | `DELETE` | <CopyableCode code="instanceGroup, project, zone" /> | Removes one or more instances from the specified instance group, but does not delete those instances. If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration before the VM instance is removed or deleted. |

## `SELECT` examples

Lists the instances in the specified instance group. The orderBy query parameter is not supported. The filter query parameter is supported, but only for expressions that use `eq` (equal) or `ne` (not equal) operators.

```sql
SELECT
instance,
namedPorts,
status
FROM google.compute.instance_groups_instances
WHERE instanceGroup = '{{ instanceGroup }}'
AND project = '{{ project }}'
AND zone = '{{ zone }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>instance_groups_instances</code> resource.

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
INSERT INTO google.compute.instance_groups_instances (
instanceGroup,
project,
zone,
instances
)
SELECT 
'{{ instanceGroup }}',
'{{ project }}',
'{{ zone }}',
'{{ instances }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: instances
      value: '{{ instances }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>instance_groups_instances</code> resource.

```sql
/*+ delete */
DELETE FROM google.compute.instance_groups_instances
WHERE instanceGroup = '{{ instanceGroup }}'
AND project = '{{ project }}'
AND zone = '{{ zone }}';
```
