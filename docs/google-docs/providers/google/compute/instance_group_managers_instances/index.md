---
title: instance_group_managers_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_group_managers_instances
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

Creates, updates, deletes, gets or lists a <code>instance_group_managers_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instance_group_managers_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.instance_group_managers_instances" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create_instances" /> | `INSERT` | <CopyableCode code="instanceGroupManager, project, zone" /> | Creates instances with per-instance configurations in this managed instance group. Instances are created using the current instance template. The create instances operation is marked DONE if the createInstances request is successful. The underlying actions take additional time. You must separately verify the status of the creating or actions with the listmanagedinstances method. |
| <CopyableCode code="delete_instances" /> | `DELETE` | <CopyableCode code="instanceGroupManager, project, zone" /> | Flags the specified instances in the managed instance group for immediate deletion. The instances are also removed from any target pools of which they were a member. This method reduces the targetSize of the managed instance group by the number of instances that you delete. This operation is marked as DONE when the action is scheduled even if the instances are still being deleted. You must separately verify the status of the deleting action with the listmanagedinstances method. If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted. You can specify a maximum of 1000 instances with this method per request. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>instance_group_managers_instances</code> resource.

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
INSERT INTO google.compute.instance_group_managers_instances (
instanceGroupManager,
project,
zone,
instances
)
SELECT 
'{{ instanceGroupManager }}',
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
      value:
        - - name: name
            value: string
          - name: preservedState
            value:
              - name: disks
                value: object
              - name: metadata
                value: object
              - name: internalIPs
                value: object
              - name: externalIPs
                value: object
          - name: status
            value: string
          - name: fingerprint
            value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>instance_group_managers_instances</code> resource.

```sql
/*+ delete */
DELETE FROM google.compute.instance_group_managers_instances
WHERE instanceGroupManager = '{{ instanceGroupManager }}'
AND project = '{{ project }}'
AND zone = '{{ zone }}';
```
