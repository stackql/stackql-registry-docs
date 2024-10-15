---
title: defender_for_ai_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - defender_for_ai_settings
  - cognitive_services
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

Creates, updates, deletes, gets or lists a <code>defender_for_ai_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>defender_for_ai_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cognitive_services.defender_for_ai_settings" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_defender_for_ai_settings', value: 'view', },
        { label: 'defender_for_ai_settings', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="defenderForAISettingName" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Resource Etag. |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Resource Etag. |
| <CopyableCode code="properties" /> | `object` | The Defender for AI resource properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, defenderForAISettingName, resourceGroupName, subscriptionId" /> | Gets the specified Defender for AI setting by name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Lists the Defender for AI settings. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, defenderForAISettingName, resourceGroupName, subscriptionId" /> | Creates or Updates the specified Defender for AI setting. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountName, defenderForAISettingName, resourceGroupName, subscriptionId" /> | Updates the specified Defender for AI setting. |

## `SELECT` examples

Lists the Defender for AI settings.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_defender_for_ai_settings', value: 'view', },
        { label: 'defender_for_ai_settings', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
accountName,
defenderForAISettingName,
etag,
resourceGroupName,
state,
subscriptionId,
system_data,
tags
FROM azure.cognitive_services.vw_defender_for_ai_settings
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
properties,
systemData,
tags
FROM azure.cognitive_services.defender_for_ai_settings
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>defender_for_ai_settings</code> resource.

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
INSERT INTO azure.cognitive_services.defender_for_ai_settings (
accountName,
defenderForAISettingName,
resourceGroupName,
subscriptionId,
tags,
properties
)
SELECT 
'{{ accountName }}',
'{{ defenderForAISettingName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ tags }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
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
    - name: etag
      value: string
    - name: tags
      value: object
    - name: properties
      value:
        - name: state
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>defender_for_ai_settings</code> resource.

```sql
/*+ update */
UPDATE azure.cognitive_services.defender_for_ai_settings
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
accountName = '{{ accountName }}'
AND defenderForAISettingName = '{{ defenderForAISettingName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
