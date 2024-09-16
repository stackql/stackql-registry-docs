---
title: profiles_offline
hide_title: false
hide_table_of_contents: false
keywords:
  - profiles_offline
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

Creates, updates, deletes, gets or lists a <code>profiles_offline</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>profiles_offline</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudprofiler.profiles_offline" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create_offline" /> | `INSERT` | <CopyableCode code="projectsId" /> | CreateOfflineProfile creates a new profile resource in the offline mode. The client provides the profile to create along with the profile bytes, the server records it. _Direct use of this API is discouraged, please use a [supported profiler agent](https://cloud.google.com/profiler/docs/about-profiler#profiling_agent) instead for profile collection._ |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>profiles_offline</code> resource.

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
INSERT INTO google.cloudprofiler.profiles_offline (
projectsId,
name,
profileType,
deployment,
duration,
profileBytes,
labels,
startTime
)
SELECT 
'{{ projectsId }}',
'{{ name }}',
'{{ profileType }}',
'{{ deployment }}',
'{{ duration }}',
'{{ profileBytes }}',
'{{ labels }}',
'{{ startTime }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: profileType
      value: '{{ profileType }}'
    - name: deployment
      value: '{{ deployment }}'
    - name: duration
      value: '{{ duration }}'
    - name: profileBytes
      value: '{{ profileBytes }}'
    - name: labels
      value: '{{ labels }}'
    - name: startTime
      value: '{{ startTime }}'

```
</TabItem>
</Tabs>
