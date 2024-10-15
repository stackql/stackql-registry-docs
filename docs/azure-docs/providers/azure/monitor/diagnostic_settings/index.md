---
title: diagnostic_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - diagnostic_settings
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

Creates, updates, deletes, gets or lists a <code>diagnostic_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>diagnostic_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.diagnostic_settings" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_diagnostic_settings', value: 'view', },
        { label: 'diagnostic_settings', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Azure resource Id |
| <CopyableCode code="name" /> | `text` | Azure resource name |
| <CopyableCode code="event_hub_authorization_rule_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="event_hub_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location |
| <CopyableCode code="log_analytics_destination_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="logs" /> | `text` | field from the `properties` object |
| <CopyableCode code="marketplace_partner_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="metrics" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceUri" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_bus_rule_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_account_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Gets or sets a list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater in length than 128 characters and a value no greater in length than 256 characters. |
| <CopyableCode code="type" /> | `text` | Azure resource type |
| <CopyableCode code="workspace_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Azure resource Id |
| <CopyableCode code="name" /> | `string` | Azure resource name |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | The diagnostic settings. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Gets or sets a list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater in length than 128 characters and a value no greater in length than 256 characters. |
| <CopyableCode code="type" /> | `string` | Azure resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, resourceUri" /> | Gets the active diagnostic settings for the specified resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceUri" /> | Gets the active diagnostic settings list for the specified resource. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="name, resourceUri" /> | Creates or updates diagnostic settings for the specified resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, resourceUri" /> | Deletes existing diagnostic settings for the specified resource. |

## `SELECT` examples

Gets the active diagnostic settings list for the specified resource.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_diagnostic_settings', value: 'view', },
        { label: 'diagnostic_settings', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
event_hub_authorization_rule_id,
event_hub_name,
location,
log_analytics_destination_type,
logs,
marketplace_partner_id,
metrics,
resourceUri,
service_bus_rule_id,
storage_account_id,
system_data,
tags,
type,
workspace_id
FROM azure.monitor.vw_diagnostic_settings
WHERE resourceUri = '{{ resourceUri }}';
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
FROM azure.monitor.diagnostic_settings
WHERE resourceUri = '{{ resourceUri }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>diagnostic_settings</code> resource.

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
INSERT INTO azure.monitor.diagnostic_settings (
name,
resourceUri,
location,
tags,
properties
)
SELECT 
'{{ name }}',
'{{ resourceUri }}',
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
        - name: storageAccountId
          value: string
        - name: serviceBusRuleId
          value: string
        - name: eventHubAuthorizationRuleId
          value: string
        - name: eventHubName
          value: string
        - name: metrics
          value:
            - - name: timeGrain
                value: string
              - name: category
                value: string
              - name: enabled
                value: boolean
              - name: retentionPolicy
                value:
                  - name: enabled
                    value: boolean
                  - name: days
                    value: integer
        - name: logs
          value:
            - - name: category
                value: string
              - name: categoryGroup
                value: string
              - name: enabled
                value: boolean
        - name: workspaceId
          value: string
        - name: marketplacePartnerId
          value: string
        - name: logAnalyticsDestinationType
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>diagnostic_settings</code> resource.

```sql
/*+ delete */
DELETE FROM azure.monitor.diagnostic_settings
WHERE name = '{{ name }}'
AND resourceUri = '{{ resourceUri }}';
```
