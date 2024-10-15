---
title: afd_origin_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - afd_origin_groups
  - cdn
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

Creates, updates, deletes, gets or lists a <code>afd_origin_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>afd_origin_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.afd_origin_groups" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_afd_origin_groups', value: 'view', },
        { label: 'afd_origin_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="deployment_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="health_probe_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="load_balancing_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="originGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="profileName" /> | `text` | field from the `properties` object |
| <CopyableCode code="profile_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="session_affinity_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="traffic_restoration_time_to_healed_or_new_endpoints_in_minutes" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The JSON object that contains the properties of the origin group. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="originGroupName, profileName, resourceGroupName, subscriptionId" /> | Gets an existing origin group within a profile. |
| <CopyableCode code="list_by_profile" /> | `SELECT` | <CopyableCode code="profileName, resourceGroupName, subscriptionId" /> | Lists all of the existing origin groups within a profile. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="originGroupName, profileName, resourceGroupName, subscriptionId" /> | Creates a new origin group within the specified profile. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="originGroupName, profileName, resourceGroupName, subscriptionId" /> | Deletes an existing origin group within a profile. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="originGroupName, profileName, resourceGroupName, subscriptionId" /> | Updates an existing origin group within a profile. |

## `SELECT` examples

Lists all of the existing origin groups within a profile.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_afd_origin_groups', value: 'view', },
        { label: 'afd_origin_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
deployment_status,
health_probe_settings,
load_balancing_settings,
originGroupName,
profileName,
profile_name,
provisioning_state,
resourceGroupName,
session_affinity_state,
subscriptionId,
traffic_restoration_time_to_healed_or_new_endpoints_in_minutes
FROM azure.cdn.vw_afd_origin_groups
WHERE profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.cdn.afd_origin_groups
WHERE profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>afd_origin_groups</code> resource.

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
INSERT INTO azure.cdn.afd_origin_groups (
originGroupName,
profileName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ originGroupName }}',
'{{ profileName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: profileName
          value: string
        - name: loadBalancingSettings
          value:
            - name: sampleSize
              value: integer
            - name: successfulSamplesRequired
              value: integer
            - name: additionalLatencyInMilliseconds
              value: integer
        - name: healthProbeSettings
          value:
            - name: probePath
              value: string
            - name: probeRequestType
              value: string
            - name: probeProtocol
              value: string
            - name: probeIntervalInSeconds
              value: integer
        - name: trafficRestorationTimeToHealedOrNewEndpointsInMinutes
          value: integer
        - name: sessionAffinityState
          value: string
        - name: provisioningState
          value: string
        - name: deploymentStatus
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>afd_origin_groups</code> resource.

```sql
/*+ update */
UPDATE azure.cdn.afd_origin_groups
SET 
properties = '{{ properties }}'
WHERE 
originGroupName = '{{ originGroupName }}'
AND profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>afd_origin_groups</code> resource.

```sql
/*+ delete */
DELETE FROM azure.cdn.afd_origin_groups
WHERE originGroupName = '{{ originGroupName }}'
AND profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
