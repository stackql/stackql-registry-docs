---
title: rai_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - rai_policies
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

Creates, updates, deletes, gets or lists a <code>rai_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rai_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cognitive_services.rai_policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_rai_policies', value: 'view', },
        { label: 'rai_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="base_policy_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="content_filters" /> | `text` | field from the `properties` object |
| <CopyableCode code="custom_blocklists" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Resource Etag. |
| <CopyableCode code="mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="raiPolicyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="type" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Resource Etag. |
| <CopyableCode code="properties" /> | `object` | Azure OpenAI Content Filters properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, raiPolicyName, resourceGroupName, subscriptionId" /> | Gets the specified Content Filters associated with the Azure OpenAI account. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Gets the content filters associated with the Azure OpenAI account. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, raiPolicyName, resourceGroupName, subscriptionId" /> | Update the state of specified Content Filters associated with the Azure OpenAI account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, raiPolicyName, resourceGroupName, subscriptionId" /> | Deletes the specified Content Filters associated with the Azure OpenAI account. |

## `SELECT` examples

Gets the content filters associated with the Azure OpenAI account.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_rai_policies', value: 'view', },
        { label: 'rai_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
accountName,
base_policy_name,
content_filters,
custom_blocklists,
etag,
mode,
raiPolicyName,
resourceGroupName,
subscriptionId,
system_data,
tags,
type
FROM azure.cognitive_services.vw_rai_policies
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
FROM azure.cognitive_services.rai_policies
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>rai_policies</code> resource.

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
INSERT INTO azure.cognitive_services.rai_policies (
accountName,
raiPolicyName,
resourceGroupName,
subscriptionId,
tags,
properties
)
SELECT 
'{{ accountName }}',
'{{ raiPolicyName }}',
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
        - name: type
          value: string
        - name: mode
          value: string
        - name: basePolicyName
          value: string
        - name: contentFilters
          value:
            - - name: name
                value: string
              - name: enabled
                value: boolean
              - name: severityThreshold
                value: string
              - name: blocking
                value: boolean
              - name: source
                value: []
        - name: customBlocklists
          value:
            - - name: blocklistName
                value: string
              - name: blocking
                value: boolean

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>rai_policies</code> resource.

```sql
/*+ delete */
DELETE FROM azure.cognitive_services.rai_policies
WHERE accountName = '{{ accountName }}'
AND raiPolicyName = '{{ raiPolicyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
