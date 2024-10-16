---
title: scaling_plans
hide_title: false
hide_table_of_contents: false
keywords:
  - scaling_plans
  - desktop_virtualization
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

Creates, updates, deletes, gets or lists a <code>scaling_plans</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scaling_plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.desktop_virtualization.scaling_plans" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_scaling_plans', value: 'view', },
        { label: 'scaling_plans', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | The etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal etag convention.  Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields. |
| <CopyableCode code="exclusion_tag" /> | `text` | field from the `properties` object |
| <CopyableCode code="friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="host_pool_references" /> | `text` | field from the `properties` object |
| <CopyableCode code="host_pool_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Identity for the resource. |
| <CopyableCode code="kind" /> | `text` | Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type. E.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value. |
| <CopyableCode code="managed_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="object_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="plan" /> | `text` | Plan for the resource. |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scalingPlanName" /> | `text` | field from the `properties` object |
| <CopyableCode code="schedules" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The resource model definition representing SKU |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_zone" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | The etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal etag convention.  Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields. |
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="kind" /> | `string` | Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type. E.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value. |
| <CopyableCode code="managedBy" /> | `string` | The fully qualified resource ID of the resource that manages this resource. Indicates if this resource is managed by another Azure resource. If this is present, complete mode deployment will not delete the resource if it is removed from the template since it is managed by another resource. |
| <CopyableCode code="plan" /> | `object` | Plan for the resource. |
| <CopyableCode code="properties" /> | `object` | Scaling plan properties. |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, scalingPlanName, subscriptionId" /> | Get a scaling plan. |
| <CopyableCode code="list_by_host_pool" /> | `SELECT` | <CopyableCode code="hostPoolName, resourceGroupName, subscriptionId" /> | List scaling plan associated with hostpool. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List scaling plans. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List scaling plans in subscription. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, scalingPlanName, subscriptionId, data__properties" /> | Create or update a scaling plan. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, scalingPlanName, subscriptionId" /> | Remove a scaling plan. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, scalingPlanName, subscriptionId" /> | Update a scaling plan. |

## `SELECT` examples

List scaling plans in subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_scaling_plans', value: 'view', },
        { label: 'scaling_plans', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
etag,
exclusion_tag,
friendly_name,
host_pool_references,
host_pool_type,
identity,
kind,
managed_by,
object_id,
plan,
resourceGroupName,
scalingPlanName,
schedules,
sku,
subscriptionId,
time_zone
FROM azure.desktop_virtualization.vw_scaling_plans
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
identity,
kind,
managedBy,
plan,
properties,
sku
FROM azure.desktop_virtualization.scaling_plans
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>scaling_plans</code> resource.

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
INSERT INTO azure.desktop_virtualization.scaling_plans (
resourceGroupName,
scalingPlanName,
subscriptionId,
data__properties,
managedBy,
kind,
identity,
sku,
plan,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ scalingPlanName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ managedBy }}',
'{{ kind }}',
'{{ identity }}',
'{{ sku }}',
'{{ plan }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: managedBy
      value: string
    - name: kind
      value: string
    - name: etag
      value: string
    - name: identity
      value: string
    - name: sku
      value: string
    - name: plan
      value: string
    - name: properties
      value:
        - name: objectId
          value: string
        - name: description
          value: string
        - name: friendlyName
          value: string
        - name: timeZone
          value: string
        - name: hostPoolType
          value: string
        - name: exclusionTag
          value: string
        - name: schedules
          value:
            - - name: name
                value: string
              - name: daysOfWeek
                value:
                  - string
              - name: rampUpStartTime
                value:
                  - name: hour
                    value: integer
                  - name: minute
                    value: integer
              - name: rampUpLoadBalancingAlgorithm
                value: string
              - name: rampUpMinimumHostsPct
                value: integer
              - name: rampUpCapacityThresholdPct
                value: integer
              - name: peakLoadBalancingAlgorithm
                value: string
              - name: rampDownLoadBalancingAlgorithm
                value: string
              - name: rampDownMinimumHostsPct
                value: integer
              - name: rampDownCapacityThresholdPct
                value: integer
              - name: rampDownForceLogoffUsers
                value: boolean
              - name: rampDownStopHostsWhen
                value: string
              - name: rampDownWaitTimeMinutes
                value: integer
              - name: rampDownNotificationMessage
                value: string
              - name: offPeakLoadBalancingAlgorithm
                value: string
        - name: hostPoolReferences
          value:
            - - name: hostPoolArmPath
                value: string
              - name: scalingPlanEnabled
                value: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>scaling_plans</code> resource.

```sql
/*+ update */
UPDATE azure.desktop_virtualization.scaling_plans
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND scalingPlanName = '{{ scalingPlanName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>scaling_plans</code> resource.

```sql
/*+ delete */
DELETE FROM azure.desktop_virtualization.scaling_plans
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND scalingPlanName = '{{ scalingPlanName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
