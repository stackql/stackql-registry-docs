---
title: app_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - app_profiles
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

Creates, updates, deletes, gets or lists a <code>app_profiles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>app_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.bigtableadmin.app_profiles" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The unique name of the app profile. Values are of the form `projects/{project}/instances/{instance}/appProfiles/_a-zA-Z0-9*`. |
| <CopyableCode code="description" /> | `string` | Long form description of the use case for this AppProfile. |
| <CopyableCode code="dataBoostIsolationReadOnly" /> | `object` | Data Boost is a serverless compute capability that lets you run high-throughput read jobs and queries on your Bigtable data, without impacting the performance of the clusters that handle your application traffic. Data Boost supports read-only use cases with single-cluster routing. |
| <CopyableCode code="etag" /> | `string` | Strongly validated etag for optimistic concurrency control. Preserve the value returned from `GetAppProfile` when calling `UpdateAppProfile` to fail the request if there has been a modification in the mean time. The `update_mask` of the request need not include `etag` for this protection to apply. See [Wikipedia](https://en.wikipedia.org/wiki/HTTP_ETag) and [RFC 7232](https://tools.ietf.org/html/rfc7232#section-2.3) for more details. |
| <CopyableCode code="multiClusterRoutingUseAny" /> | `object` | Read/write requests are routed to the nearest cluster in the instance, and will fail over to the nearest cluster that is available in the event of transient errors or delays. Clusters in a region are considered equidistant. Choosing this option sacrifices read-your-writes consistency to improve availability. |
| <CopyableCode code="priority" /> | `string` | This field has been deprecated in favor of `standard_isolation.priority`. If you set this field, `standard_isolation.priority` will be set instead. The priority of requests sent using this app profile. |
| <CopyableCode code="singleClusterRouting" /> | `object` | Unconditionally routes all read/write requests to a specific cluster. This option preserves read-your-writes consistency but does not improve availability. |
| <CopyableCode code="standardIsolation" /> | `object` | Standard options for isolating this app profile's traffic from other use cases. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="appProfilesId, instancesId, projectsId" /> | Gets information about an app profile. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="instancesId, projectsId" /> | Lists information about app profiles in an instance. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="instancesId, projectsId" /> | Creates an app profile within an instance. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="appProfilesId, instancesId, projectsId" /> | Deletes an app profile from an instance. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="appProfilesId, instancesId, projectsId" /> | Updates an app profile within an instance. |

## `SELECT` examples

Lists information about app profiles in an instance.

```sql
SELECT
name,
description,
dataBoostIsolationReadOnly,
etag,
multiClusterRoutingUseAny,
priority,
singleClusterRouting,
standardIsolation
FROM google.bigtableadmin.app_profiles
WHERE instancesId = '{{ instancesId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>app_profiles</code> resource.

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
INSERT INTO google.bigtableadmin.app_profiles (
instancesId,
projectsId,
name,
etag,
description,
multiClusterRoutingUseAny,
singleClusterRouting,
priority,
standardIsolation,
dataBoostIsolationReadOnly
)
SELECT 
'{{ instancesId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ etag }}',
'{{ description }}',
'{{ multiClusterRoutingUseAny }}',
'{{ singleClusterRouting }}',
'{{ priority }}',
'{{ standardIsolation }}',
'{{ dataBoostIsolationReadOnly }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
etag: string
description: string
multiClusterRoutingUseAny:
  clusterIds:
    - type: string
singleClusterRouting:
  clusterId: string
  allowTransactionalWrites: boolean
priority: string
standardIsolation:
  priority: string
dataBoostIsolationReadOnly:
  computeBillingOwner: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>app_profiles</code> resource.

```sql
/*+ update */
UPDATE google.bigtableadmin.app_profiles
SET 
name = '{{ name }}',
etag = '{{ etag }}',
description = '{{ description }}',
multiClusterRoutingUseAny = '{{ multiClusterRoutingUseAny }}',
singleClusterRouting = '{{ singleClusterRouting }}',
priority = '{{ priority }}',
standardIsolation = '{{ standardIsolation }}',
dataBoostIsolationReadOnly = '{{ dataBoostIsolationReadOnly }}'
WHERE 
appProfilesId = '{{ appProfilesId }}'
AND instancesId = '{{ instancesId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>app_profiles</code> resource.

```sql
/*+ delete */
DELETE FROM google.bigtableadmin.app_profiles
WHERE appProfilesId = '{{ appProfilesId }}'
AND instancesId = '{{ instancesId }}'
AND projectsId = '{{ projectsId }}';
```
