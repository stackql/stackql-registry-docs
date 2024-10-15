---
title: autoscale_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - autoscale_settings
  - monitor
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

Creates, updates, deletes, gets or lists a <code>autoscale_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>autoscale_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.autoscale_settings" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_autoscale_settings', value: 'view', },
        { label: 'autoscale_settings', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Azure resource Id |
| <CopyableCode code="name" /> | `text` | Azure resource name |
| <CopyableCode code="autoscaleSettingName" /> | `text` | field from the `properties` object |
| <CopyableCode code="enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location |
| <CopyableCode code="notifications" /> | `text` | field from the `properties` object |
| <CopyableCode code="predictive_autoscale_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="profiles" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Gets or sets a list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater in length than 128 characters and a value no greater in length than 256 characters. |
| <CopyableCode code="target_resource_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_resource_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Azure resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Azure resource Id |
| <CopyableCode code="name" /> | `string` | Azure resource name |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | A setting that contains all of the configuration for the automatic scaling of a resource. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Gets or sets a list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater in length than 128 characters and a value no greater in length than 256 characters. |
| <CopyableCode code="type" /> | `string` | Azure resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="autoscaleSettingName, resourceGroupName, subscriptionId" /> | Gets an autoscale setting |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists the autoscale settings for a resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists the autoscale settings for a subscription |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="autoscaleSettingName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates an autoscale setting. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="autoscaleSettingName, resourceGroupName, subscriptionId" /> | Deletes and autoscale setting |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="autoscaleSettingName, resourceGroupName, subscriptionId" /> | Updates an existing AutoscaleSettingsResource. To update other fields use the CreateOrUpdate method. |

## `SELECT` examples

Lists the autoscale settings for a subscription

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_autoscale_settings', value: 'view', },
        { label: 'autoscale_settings', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
autoscaleSettingName,
enabled,
location,
notifications,
predictive_autoscale_policy,
profiles,
resourceGroupName,
subscriptionId,
system_data,
tags,
target_resource_location,
target_resource_uri,
type
FROM azure.monitor.vw_autoscale_settings
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
systemData,
tags,
type
FROM azure.monitor.autoscale_settings
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>autoscale_settings</code> resource.

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
INSERT INTO azure.monitor.autoscale_settings (
autoscaleSettingName,
resourceGroupName,
subscriptionId,
data__properties,
location,
tags,
properties
)
SELECT 
'{{ autoscaleSettingName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string
    - name: tags
      value: object
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string
    - name: properties
      value:
        - name: profiles
          value:
            - - name: name
                value: string
              - name: capacity
                value:
                  - name: minimum
                    value: string
                  - name: maximum
                    value: string
                  - name: default
                    value: string
              - name: rules
                value:
                  - - name: metricTrigger
                      value:
                        - name: metricName
                          value: string
                        - name: metricNamespace
                          value: string
                        - name: metricResourceUri
                          value: string
                        - name: metricResourceLocation
                          value: string
                        - name: timeGrain
                          value: string
                        - name: statistic
                          value: string
                        - name: timeWindow
                          value: string
                        - name: timeAggregation
                          value: string
                        - name: operator
                          value: string
                        - name: threshold
                          value: number
                        - name: dimensions
                          value:
                            - - name: DimensionName
                                value: string
                              - name: Operator
                                value: string
                              - name: Values
                                value:
                                  - string
                        - name: dividePerInstance
                          value: boolean
                    - name: scaleAction
                      value:
                        - name: direction
                          value: string
                        - name: type
                          value: string
                        - name: value
                          value: string
                        - name: cooldown
                          value: string
              - name: fixedDate
                value:
                  - name: timeZone
                    value: string
                  - name: start
                    value: string
                  - name: end
                    value: string
              - name: recurrence
                value:
                  - name: frequency
                    value: string
                  - name: schedule
                    value:
                      - name: timeZone
                        value: string
                      - name: days
                        value:
                          - string
                      - name: hours
                        value:
                          - integer
                      - name: minutes
                        value:
                          - integer
        - name: notifications
          value:
            - - name: operation
                value: string
              - name: email
                value:
                  - name: sendToSubscriptionAdministrator
                    value: boolean
                  - name: sendToSubscriptionCoAdministrators
                    value: boolean
                  - name: customEmails
                    value:
                      - string
              - name: webhooks
                value:
                  - - name: serviceUri
                      value: string
                    - name: properties
                      value: object
        - name: enabled
          value: boolean
        - name: predictiveAutoscalePolicy
          value:
            - name: scaleMode
              value: string
            - name: scaleLookAheadTime
              value: string
        - name: name
          value: string
        - name: targetResourceUri
          value: string
        - name: targetResourceLocation
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>autoscale_settings</code> resource.

```sql
/*+ update */
UPDATE azure.monitor.autoscale_settings
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
autoscaleSettingName = '{{ autoscaleSettingName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>autoscale_settings</code> resource.

```sql
/*+ delete */
DELETE FROM azure.monitor.autoscale_settings
WHERE autoscaleSettingName = '{{ autoscaleSettingName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
