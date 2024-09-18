---
title: profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - profiles
  - cloudprofiler
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

Creates, updates, deletes, gets or lists a <code>profiles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudprofiler.profiles" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Opaque, server-assigned, unique ID for this profile. |
| <CopyableCode code="deployment" /> | `object` | Deployment contains the deployment identification information. |
| <CopyableCode code="duration" /> | `string` | Duration of the profiling session. Input (for the offline mode) or output (for the online mode). The field represents requested profiling duration. It may slightly differ from the effective profiling duration, which is recorded in the profile data, in case the profiling can't be stopped immediately (e.g. in case stopping the profiling is handled asynchronously). |
| <CopyableCode code="labels" /> | `object` | Input only. Labels associated to this specific profile. These labels will get merged with the deployment labels for the final data set. See documentation on deployment labels for validation rules and limits. |
| <CopyableCode code="profileBytes" /> | `string` | Input only. Profile bytes, as a gzip compressed serialized proto, the format is https://github.com/google/pprof/blob/master/proto/profile.proto. |
| <CopyableCode code="profileType" /> | `string` | Type of profile. For offline mode, this must be specified when creating the profile. For online mode it is assigned and returned by the server. |
| <CopyableCode code="startTime" /> | `string` | Output only. Start time for the profile. This output is only present in response from the ListProfiles method. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists profiles which have been collected so far and for which the caller has permission to view. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="projectsId" /> | CreateProfile creates a new profile resource in the online mode. _Direct use of this API is discouraged, please use a [supported profiler agent](https://cloud.google.com/profiler/docs/about-profiler#profiling_agent) instead for profile collection._ The server ensures that the new profiles are created at a constant rate per deployment, so the creation request may hang for some time until the next profile session is available. The request may fail with ABORTED error if the creation is not available within ~1m, the response will indicate the duration of the backoff the client should take before attempting creating a profile again. The backoff duration is returned in google.rpc.RetryInfo extension on the response status. To a gRPC client, the extension will be return as a binary-serialized proto in the trailing metadata item named "google.rpc.retryinfo-bin".  |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="profilesId, projectsId" /> | UpdateProfile updates the profile bytes and labels on the profile resource created in the online mode. Updating the bytes for profiles created in the offline mode is currently not supported: the profile content must be provided at the time of the profile creation. _Direct use of this API is discouraged, please use a [supported profiler agent](https://cloud.google.com/profiler/docs/about-profiler#profiling_agent) instead for profile collection._ |

## `SELECT` examples

Lists profiles which have been collected so far and for which the caller has permission to view.

```sql
SELECT
name,
deployment,
duration,
labels,
profileBytes,
profileType,
startTime
FROM google.cloudprofiler.profiles
WHERE projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>profiles</code> resource.

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
INSERT INTO google.cloudprofiler.profiles (
projectsId,
deployment,
profileType
)
SELECT 
'{{ projectsId }}',
'{{ deployment }}',
'{{ profileType }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
deployment:
  projectId: string
  target: string
  labels: object
profileType:
  - type: string
    enumDescriptions: string
    enum: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>profiles</code> resource.

```sql
/*+ update */
UPDATE google.cloudprofiler.profiles
SET 
profileType = '{{ profileType }}',
deployment = '{{ deployment }}',
duration = '{{ duration }}',
profileBytes = '{{ profileBytes }}',
labels = '{{ labels }}'
WHERE 
profilesId = '{{ profilesId }}'
AND projectsId = '{{ projectsId }}';
```
