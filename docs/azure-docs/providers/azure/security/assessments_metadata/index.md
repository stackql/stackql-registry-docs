---
title: assessments_metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - assessments_metadata
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

Creates, updates, deletes, gets or lists a <code>assessments_metadata</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assessments_metadata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.assessments_metadata" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_assessments_metadata', value: 'view', },
        { label: 'assessments_metadata', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="assessmentMetadataName" /> | `text` | field from the `properties` object |
| <CopyableCode code="assessment_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="categories" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="implementation_effort" /> | `text` | field from the `properties` object |
| <CopyableCode code="partner_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="planned_deprecation_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="policy_definition_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="preview" /> | `text` | field from the `properties` object |
| <CopyableCode code="publish_dates" /> | `text` | field from the `properties` object |
| <CopyableCode code="remediation_description" /> | `text` | field from the `properties` object |
| <CopyableCode code="severity" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tactics" /> | `text` | field from the `properties` object |
| <CopyableCode code="techniques" /> | `text` | field from the `properties` object |
| <CopyableCode code="threats" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
| <CopyableCode code="user_impact" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="properties" /> | `object` | Describes properties of an assessment metadata response. |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="assessmentMetadataName" /> | Get metadata information on an assessment type |
| <CopyableCode code="get_in_subscription" /> | `SELECT` | <CopyableCode code="assessmentMetadataName, subscriptionId" /> | Get metadata information on an assessment type in a specific subscription |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Get metadata information on all assessment types |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get metadata information on all assessment types in a specific subscription |
| <CopyableCode code="create_in_subscription" /> | `INSERT` | <CopyableCode code="assessmentMetadataName, subscriptionId" /> | Create metadata information on an assessment type in a specific subscription |
| <CopyableCode code="delete_in_subscription" /> | `DELETE` | <CopyableCode code="assessmentMetadataName, subscriptionId" /> | Delete metadata information on an assessment type in a specific subscription, will cause the deletion of all the assessments of that type in that subscription |

## `SELECT` examples

Get metadata information on all assessment types

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_assessments_metadata', value: 'view', },
        { label: 'assessments_metadata', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
assessmentMetadataName,
assessment_type,
categories,
display_name,
implementation_effort,
partner_data,
planned_deprecation_date,
policy_definition_id,
preview,
publish_dates,
remediation_description,
severity,
subscriptionId,
tactics,
techniques,
threats,
type,
user_impact
FROM azure.security.vw_assessments_metadata
;
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.security.assessments_metadata
;
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>assessments_metadata</code> resource.

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
INSERT INTO azure.security.assessments_metadata (
assessmentMetadataName,
subscriptionId,
properties
)
SELECT 
'{{ assessmentMetadataName }}',
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
        - name: publishDates
          value:
            - name: GA
              value: string
            - name: public
              value: string
        - name: plannedDeprecationDate
          value: string
        - name: tactics
          value:
            - string
        - name: techniques
          value:
            - string
        - name: displayName
          value: string
        - name: policyDefinitionId
          value: string
        - name: description
          value: string
        - name: remediationDescription
          value: string
        - name: categories
          value:
            - string
        - name: severity
          value: string
        - name: userImpact
          value: string
        - name: implementationEffort
          value: string
        - name: threats
          value:
            - string
        - name: preview
          value: boolean
        - name: assessmentType
          value: string
        - name: partnerData
          value:
            - name: partnerName
              value: string
            - name: productName
              value: string
            - name: secret
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

Deletes the specified <code>assessments_metadata</code> resource.

```sql
/*+ delete */
DELETE FROM azure.security.assessments_metadata
WHERE assessmentMetadataName = '{{ assessmentMetadataName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
