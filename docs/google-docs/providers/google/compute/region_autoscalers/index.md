---
title: region_autoscalers
hide_title: false
hide_table_of_contents: false
keywords:
  - region_autoscalers
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

Creates, updates, deletes, gets or lists a <code>region_autoscalers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>region_autoscalers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.region_autoscalers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| <CopyableCode code="name" /> | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| <CopyableCode code="description" /> | `string` | An optional description of this resource. Provide this property when you create the resource. |
| <CopyableCode code="autoscalingPolicy" /> | `object` | Cloud Autoscaler policy. |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| <CopyableCode code="kind" /> | `string` | [Output Only] Type of the resource. Always compute#autoscaler for autoscalers. |
| <CopyableCode code="recommendedSize" /> | `integer` | [Output Only] Target recommended MIG size (number of instances) computed by autoscaler. Autoscaler calculates the recommended MIG size even when the autoscaling policy mode is different from ON. This field is empty when autoscaler is not connected to an existing managed instance group or autoscaler did not generate its prediction. |
| <CopyableCode code="region" /> | `string` | [Output Only] URL of the region where the instance group resides (for autoscalers living in regional scope). |
| <CopyableCode code="scalingScheduleStatus" /> | `object` | [Output Only] Status information of existing scaling schedules. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined URL for the resource. |
| <CopyableCode code="status" /> | `string` | [Output Only] The status of the autoscaler configuration. Current set of possible values: - PENDING: Autoscaler backend hasn't read new/updated configuration. - DELETING: Configuration is being deleted. - ACTIVE: Configuration is acknowledged to be effective. Some warnings might be present in the statusDetails field. - ERROR: Configuration has errors. Actionable for users. Details are present in the statusDetails field. New values might be added in the future. |
| <CopyableCode code="statusDetails" /> | `array` | [Output Only] Human-readable details about the current state of the autoscaler. Read the documentation for Commonly returned status messages for examples of status messages you might encounter. |
| <CopyableCode code="target" /> | `string` | URL of the managed instance group that this autoscaler will scale. This field is required when creating an autoscaler. |
| <CopyableCode code="zone" /> | `string` | [Output Only] URL of the zone where the instance group resides (for autoscalers living in zonal scope). |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="autoscaler, project, region" /> | Returns the specified autoscaler. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project, region" /> | Retrieves a list of autoscalers contained within the specified region. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="project, region" /> | Creates an autoscaler in the specified project using the data included in the request. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="autoscaler, project, region" /> | Deletes the specified autoscaler. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="project, region" /> | Updates an autoscaler in the specified project using the data included in the request. This method supports PATCH semantics and uses the JSON merge patch format and processing rules. |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="project, region" /> | Updates an autoscaler in the specified project using the data included in the request. |

## `SELECT` examples

Retrieves a list of autoscalers contained within the specified region.

```sql
SELECT
id,
name,
description,
autoscalingPolicy,
creationTimestamp,
kind,
recommendedSize,
region,
scalingScheduleStatus,
selfLink,
status,
statusDetails,
target,
zone
FROM google.compute.region_autoscalers
WHERE project = '{{ project }}'
AND region = '{{ region }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>region_autoscalers</code> resource.

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
INSERT INTO google.compute.region_autoscalers (
project,
region,
kind,
id,
creationTimestamp,
name,
description,
target,
autoscalingPolicy,
zone,
region,
selfLink,
status,
statusDetails,
recommendedSize,
scalingScheduleStatus
)
SELECT 
'{{ project }}',
'{{ region }}',
'{{ kind }}',
'{{ id }}',
'{{ creationTimestamp }}',
'{{ name }}',
'{{ description }}',
'{{ target }}',
'{{ autoscalingPolicy }}',
'{{ zone }}',
'{{ region }}',
'{{ selfLink }}',
'{{ status }}',
'{{ statusDetails }}',
'{{ recommendedSize }}',
'{{ scalingScheduleStatus }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
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
    - name: target
      value: '{{ target }}'
    - name: autoscalingPolicy
      value: '{{ autoscalingPolicy }}'
    - name: zone
      value: '{{ zone }}'
    - name: region
      value: '{{ region }}'
    - name: selfLink
      value: '{{ selfLink }}'
    - name: status
      value: '{{ status }}'
    - name: statusDetails
      value: '{{ statusDetails }}'
    - name: recommendedSize
      value: '{{ recommendedSize }}'
    - name: scalingScheduleStatus
      value: '{{ scalingScheduleStatus }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>region_autoscalers</code> resource.

```sql
/*+ update */
UPDATE google.compute.region_autoscalers
SET 
kind = '{{ kind }}',
id = '{{ id }}',
creationTimestamp = '{{ creationTimestamp }}',
name = '{{ name }}',
description = '{{ description }}',
target = '{{ target }}',
autoscalingPolicy = '{{ autoscalingPolicy }}',
zone = '{{ zone }}',
region = '{{ region }}',
selfLink = '{{ selfLink }}',
status = '{{ status }}',
statusDetails = '{{ statusDetails }}',
recommendedSize = '{{ recommendedSize }}',
scalingScheduleStatus = '{{ scalingScheduleStatus }}'
WHERE 
project = '{{ project }}'
AND region = '{{ region }}';
```

## `UPDATE` example

Replaces all fields in the specified <code>region_autoscalers</code> resource.

```sql
/*+ update */
REPLACE google.compute.region_autoscalers
SET 
kind = '{{ kind }}',
id = '{{ id }}',
creationTimestamp = '{{ creationTimestamp }}',
name = '{{ name }}',
description = '{{ description }}',
target = '{{ target }}',
autoscalingPolicy = '{{ autoscalingPolicy }}',
zone = '{{ zone }}',
region = '{{ region }}',
selfLink = '{{ selfLink }}',
status = '{{ status }}',
statusDetails = '{{ statusDetails }}',
recommendedSize = '{{ recommendedSize }}',
scalingScheduleStatus = '{{ scalingScheduleStatus }}'
WHERE 
project = '{{ project }}'
AND region = '{{ region }}';
```

## `DELETE` example

Deletes the specified <code>region_autoscalers</code> resource.

```sql
/*+ delete */
DELETE FROM google.compute.region_autoscalers
WHERE autoscaler = '{{ autoscaler }}'
AND project = '{{ project }}'
AND region = '{{ region }}';
```
