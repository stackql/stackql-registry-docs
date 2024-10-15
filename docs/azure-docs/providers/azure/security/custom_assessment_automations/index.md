---
title: custom_assessment_automations
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_assessment_automations
  - security
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

Creates, updates, deletes, gets or lists a <code>custom_assessment_automations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_assessment_automations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.custom_assessment_automations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_custom_assessment_automations', value: 'view', },
        { label: 'custom_assessment_automations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="assessment_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="compressed_query" /> | `text` | field from the `properties` object |
| <CopyableCode code="customAssessmentAutomationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="remediation_description" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="severity" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="supported_cloud" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="properties" /> | `object` | describes the Custom Assessment Automation properties |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="customAssessmentAutomationName, resourceGroupName, subscriptionId" /> | Gets a single custom assessment automation by name for the provided subscription and resource group. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List custom assessment automations by provided subscription and resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List custom assessment automations by provided subscription |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="customAssessmentAutomationName, resourceGroupName, subscriptionId" /> | Creates or updates a custom assessment automation for the provided subscription. Please note that providing an existing custom assessment automation will replace the existing record. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="customAssessmentAutomationName, resourceGroupName, subscriptionId" /> | Deletes a custom assessment automation by name for a provided subscription |

## `SELECT` examples

List custom assessment automations by provided subscription

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_custom_assessment_automations', value: 'view', },
        { label: 'custom_assessment_automations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
assessment_key,
compressed_query,
customAssessmentAutomationName,
display_name,
remediation_description,
resourceGroupName,
severity,
subscriptionId,
supported_cloud,
system_data,
type
FROM azure.security.vw_custom_assessment_automations
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure.security.custom_assessment_automations
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>custom_assessment_automations</code> resource.

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
INSERT INTO azure.security.custom_assessment_automations (
customAssessmentAutomationName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ customAssessmentAutomationName }}',
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
        - name: compressedQuery
          value: string
        - name: supportedCloud
          value: string
        - name: severity
          value: string
        - name: displayName
          value: string
        - name: description
          value: string
        - name: remediationDescription
          value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>custom_assessment_automations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.security.custom_assessment_automations
WHERE customAssessmentAutomationName = '{{ customAssessmentAutomationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
