---
title: device_settings_alert_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - device_settings_alert_settings
  - storsimple_8000_series
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

Creates, updates, deletes, gets or lists a <code>device_settings_alert_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>device_settings_alert_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_8000_series.device_settings_alert_settings" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_device_settings_alert_settings', value: 'view', },
        { label: 'device_settings_alert_settings', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The path ID that uniquely identifies the object. |
| <CopyableCode code="name" /> | `text` | The name of the object. |
| <CopyableCode code="additional_recipient_email_list" /> | `text` | field from the `properties` object |
| <CopyableCode code="alert_notification_culture" /> | `text` | field from the `properties` object |
| <CopyableCode code="deviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="email_notification" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | The Kind of the object. Currently only Series8000 is supported |
| <CopyableCode code="managerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="notification_to_service_owners" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The hierarchical type of the object. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The path ID that uniquely identifies the object. |
| <CopyableCode code="name" /> | `string` | The name of the object. |
| <CopyableCode code="kind" /> | `string` | The Kind of the object. Currently only Series8000 is supported |
| <CopyableCode code="properties" /> | `object` | The properties of the alert notification settings. |
| <CopyableCode code="type" /> | `string` | The hierarchical type of the object. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Gets the alert settings of the specified device. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates the alert settings of the specified device. |

## `SELECT` examples

Gets the alert settings of the specified device.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_device_settings_alert_settings', value: 'view', },
        { label: 'device_settings_alert_settings', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
additional_recipient_email_list,
alert_notification_culture,
deviceName,
email_notification,
kind,
managerName,
notification_to_service_owners,
resourceGroupName,
subscriptionId,
type
FROM azure_extras.storsimple_8000_series.vw_device_settings_alert_settings
WHERE deviceName = '{{ deviceName }}'
AND managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
kind,
properties,
type
FROM azure_extras.storsimple_8000_series.device_settings_alert_settings
WHERE deviceName = '{{ deviceName }}'
AND managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>device_settings_alert_settings</code> resource.

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
INSERT INTO azure_extras.storsimple_8000_series.device_settings_alert_settings (
deviceName,
managerName,
resourceGroupName,
subscriptionId,
data__properties,
kind,
properties
)
SELECT 
'{{ deviceName }}',
'{{ managerName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ kind }}',
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
    - name: kind
      value: string
    - name: properties
      value:
        - name: emailNotification
          value: string
        - name: alertNotificationCulture
          value: string
        - name: notificationToServiceOwners
          value: string
        - name: additionalRecipientEmailList
          value:
            - string

```
</TabItem>
</Tabs>
