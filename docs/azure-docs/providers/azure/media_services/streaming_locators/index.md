---
title: streaming_locators
hide_title: false
hide_table_of_contents: false
keywords:
  - streaming_locators
  - media_services
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

Creates, updates, deletes, gets or lists a <code>streaming_locators</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>streaming_locators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.media_services.streaming_locators" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_streaming_locators', value: 'view', },
        { label: 'streaming_locators', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="alternative_media_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="asset_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="content_keys" /> | `text` | field from the `properties` object |
| <CopyableCode code="created" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_content_key_policy_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="filters" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="streamingLocatorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="streaming_locator_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="streaming_policy_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of the Streaming Locator. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, streamingLocatorName, subscriptionId" /> | Get the details of a Streaming Locator in the Media Services account |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Lists the Streaming Locators in the account |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, resourceGroupName, streamingLocatorName, subscriptionId" /> | Create a Streaming Locator in the Media Services account |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, resourceGroupName, streamingLocatorName, subscriptionId" /> | Deletes a Streaming Locator in the Media Services account |

## `SELECT` examples

Lists the Streaming Locators in the account

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_streaming_locators', value: 'view', },
        { label: 'streaming_locators', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
accountName,
alternative_media_id,
asset_name,
content_keys,
created,
default_content_key_policy_name,
end_time,
filters,
resourceGroupName,
start_time,
streamingLocatorName,
streaming_locator_id,
streaming_policy_name,
subscriptionId,
system_data
FROM azure.media_services.vw_streaming_locators
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
systemData
FROM azure.media_services.streaming_locators
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>streaming_locators</code> resource.

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
INSERT INTO azure.media_services.streaming_locators (
accountName,
resourceGroupName,
streamingLocatorName,
subscriptionId,
properties
)
SELECT 
'{{ accountName }}',
'{{ resourceGroupName }}',
'{{ streamingLocatorName }}',
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
        - name: assetName
          value: string
        - name: created
          value: string
        - name: startTime
          value: string
        - name: endTime
          value: string
        - name: streamingLocatorId
          value: string
        - name: streamingPolicyName
          value: string
        - name: defaultContentKeyPolicyName
          value: string
        - name: contentKeys
          value:
            - - name: id
                value: string
              - name: type
                value: string
              - name: labelReferenceInStreamingPolicy
                value: string
              - name: value
                value: string
              - name: policyName
                value: string
              - name: tracks
                value:
                  - - name: trackSelections
                      value:
                        - - name: property
                            value: string
                          - name: operation
                            value: string
                          - name: value
                            value: string
        - name: alternativeMediaId
          value: string
        - name: filters
          value:
            - string
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

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>streaming_locators</code> resource.

```sql
/*+ delete */
DELETE FROM azure.media_services.streaming_locators
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND streamingLocatorName = '{{ streamingLocatorName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
