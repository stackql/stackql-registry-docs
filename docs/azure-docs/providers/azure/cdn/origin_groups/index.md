---
title: origin_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - origin_groups
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

Creates, updates, deletes, gets or lists a <code>origin_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>origin_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.origin_groups" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_origin_groups', value: 'view', },
        { label: 'origin_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="endpointName" /> | `text` | field from the `properties` object |
| <CopyableCode code="health_probe_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="originGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="origins" /> | `text` | field from the `properties` object |
| <CopyableCode code="profileName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="response_based_origin_error_detection_settings" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="endpointName, originGroupName, profileName, resourceGroupName, subscriptionId" /> | Gets an existing origin group within an endpoint. |
| <CopyableCode code="list_by_endpoint" /> | `SELECT` | <CopyableCode code="endpointName, profileName, resourceGroupName, subscriptionId" /> | Lists all of the existing origin groups within an endpoint. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="endpointName, originGroupName, profileName, resourceGroupName, subscriptionId" /> | Creates a new origin group within the specified endpoint. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="endpointName, originGroupName, profileName, resourceGroupName, subscriptionId" /> | Deletes an existing origin group within an endpoint. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="endpointName, originGroupName, profileName, resourceGroupName, subscriptionId" /> | Updates an existing origin group within an endpoint. |

## `SELECT` examples

Lists all of the existing origin groups within an endpoint.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_origin_groups', value: 'view', },
        { label: 'origin_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
endpointName,
health_probe_settings,
originGroupName,
origins,
profileName,
provisioning_state,
resourceGroupName,
resource_state,
response_based_origin_error_detection_settings,
subscriptionId,
traffic_restoration_time_to_healed_or_new_endpoints_in_minutes
FROM azure.cdn.vw_origin_groups
WHERE endpointName = '{{ endpointName }}'
AND profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.cdn.origin_groups
WHERE endpointName = '{{ endpointName }}'
AND profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>origin_groups</code> resource.

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
INSERT INTO azure.cdn.origin_groups (
endpointName,
originGroupName,
profileName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ endpointName }}',
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
        - name: origins
          value:
            - - name: id
                value: string
        - name: trafficRestorationTimeToHealedOrNewEndpointsInMinutes
          value: integer
        - name: responseBasedOriginErrorDetectionSettings
          value:
            - name: responseBasedDetectedErrorTypes
              value: string
            - name: responseBasedFailoverThresholdPercentage
              value: integer
            - name: httpErrorRanges
              value:
                - - name: begin
                    value: integer
                  - name: end
                    value: integer
        - name: resourceState
          value: string
        - name: provisioningState
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>origin_groups</code> resource.

```sql
/*+ update */
UPDATE azure.cdn.origin_groups
SET 
properties = '{{ properties }}'
WHERE 
endpointName = '{{ endpointName }}'
AND originGroupName = '{{ originGroupName }}'
AND profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>origin_groups</code> resource.

```sql
/*+ delete */
DELETE FROM azure.cdn.origin_groups
WHERE endpointName = '{{ endpointName }}'
AND originGroupName = '{{ originGroupName }}'
AND profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
