---
title: instance_group_manager_resize_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_group_manager_resize_requests
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

Creates, updates, deletes or gets an <code>instance_group_manager_resize_request</code> resource or lists <code>instance_group_manager_resize_requests</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instance_group_manager_resize_requests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.instance_group_manager_resize_requests" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] A unique identifier for this resource type. The server generates this identifier. |
| <CopyableCode code="name" /> | `string` | The name of this resize request. The name must be 1-63 characters long, and comply with RFC1035. |
| <CopyableCode code="description" /> | `string` | An optional description of this resource. |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] The creation timestamp for this resize request in RFC3339 text format. |
| <CopyableCode code="kind" /> | `string` | [Output Only] The resource type, which is always compute#instanceGroupManagerResizeRequest for resize requests. |
| <CopyableCode code="requestedRunDuration" /> | `object` | A Duration represents a fixed-length span of time represented as a count of seconds and fractions of seconds at nanosecond resolution. It is independent of any calendar and concepts like "day" or "month". Range is approximately 10,000 years. |
| <CopyableCode code="resizeBy" /> | `integer` | The number of instances to be created by this resize request. The group's target size will be increased by this number. This field cannot be used together with 'instances'. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] The URL for this resize request. The server defines this URL. |
| <CopyableCode code="selfLinkWithId" /> | `string` | [Output Only] Server-defined URL for this resource with the resource id. |
| <CopyableCode code="state" /> | `string` | [Output only] Current state of the request. |
| <CopyableCode code="status" /> | `object` |  |
| <CopyableCode code="zone" /> | `string` | [Output Only] The URL of a zone where the resize request is located. Populated only for zonal resize requests. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="instanceGroupManager, project, resizeRequest, zone" /> | Returns all of the details about the specified resize request. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="instanceGroupManager, project, zone" /> | Retrieves a list of resize requests that are contained in the managed instance group. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="instanceGroupManager, project, zone" /> | Creates a new resize request that starts provisioning VMs immediately or queues VM creation. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="instanceGroupManager, project, resizeRequest, zone" /> | Deletes the specified, inactive resize request. Requests that are still active cannot be deleted. Deleting request does not delete instances that were provisioned previously. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="instanceGroupManager, project, resizeRequest, zone" /> | Cancels the specified resize request and removes it from the queue. Cancelled resize request does no longer wait for the resources to be provisioned. Cancel is only possible for requests that are accepted in the queue. |

## `SELECT` examples

Retrieves a list of resize requests that are contained in the managed instance group.

```sql
SELECT
id,
name,
description,
creationTimestamp,
kind,
requestedRunDuration,
resizeBy,
selfLink,
selfLinkWithId,
state,
status,
zone
FROM google.compute.instance_group_manager_resize_requests
WHERE instanceGroupManager = '{{ instanceGroupManager }}'
AND project = '{{ project }}'
AND zone = '{{ zone }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>instance_group_manager_resize_requests</code> resource.

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
INSERT INTO google.compute.instance_group_manager_resize_requests (
instanceGroupManager,
project,
zone,
kind,
id,
creationTimestamp,
name,
description,
zone,
resizeBy,
requestedRunDuration,
state,
status,
selfLink,
selfLinkWithId
)
SELECT 
'{{ instanceGroupManager }}',
'{{ project }}',
'{{ zone }}',
'{{ kind }}',
'{{ id }}',
'{{ creationTimestamp }}',
'{{ name }}',
'{{ description }}',
'{{ zone }}',
'{{ resizeBy }}',
'{{ requestedRunDuration }}',
'{{ state }}',
'{{ status }}',
'{{ selfLink }}',
'{{ selfLinkWithId }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
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
      - name: zone
        value: '{{ zone }}'
      - name: resizeBy
        value: '{{ resizeBy }}'
      - name: requestedRunDuration
        value: '{{ requestedRunDuration }}'
      - name: state
        value: '{{ state }}'
      - name: status
        value: '{{ status }}'
      - name: selfLink
        value: '{{ selfLink }}'
      - name: selfLinkWithId
        value: '{{ selfLinkWithId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified instance_group_manager_resize_request resource.

```sql
DELETE FROM google.compute.instance_group_manager_resize_requests
WHERE instanceGroupManager = '{{ instanceGroupManager }}'
AND project = '{{ project }}'
AND resizeRequest = '{{ resizeRequest }}'
AND zone = '{{ zone }}';
```
