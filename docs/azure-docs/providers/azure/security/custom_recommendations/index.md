---
title: custom_recommendations
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_recommendations
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

Creates, updates, deletes, gets or lists a <code>custom_recommendations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_recommendations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.custom_recommendations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_custom_recommendations', value: 'view', },
        { label: 'custom_recommendations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="assessment_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="cloud_providers" /> | `text` | field from the `properties` object |
| <CopyableCode code="customRecommendationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="query" /> | `text` | field from the `properties` object |
| <CopyableCode code="remediation_description" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="security_issue" /> | `text` | field from the `properties` object |
| <CopyableCode code="severity" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="properties" /> | `object` | describes the Custom Recommendation properties |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="customRecommendationName, scope" /> | Get a specific custom recommendation for the requested scope by customRecommendationName |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="scope" /> | Get a list of all relevant custom recommendations over a scope |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="customRecommendationName, scope" /> | Creates or updates a custom recommendation over a given scope |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="customRecommendationName, scope" /> | Delete a custom recommendation over a given scope |

## `SELECT` examples

Get a list of all relevant custom recommendations over a scope

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_custom_recommendations', value: 'view', },
        { label: 'custom_recommendations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
assessment_key,
cloud_providers,
customRecommendationName,
display_name,
query,
remediation_description,
scope,
security_issue,
severity,
system_data,
type
FROM azure.security.vw_custom_recommendations
WHERE scope = '{{ scope }}';
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
FROM azure.security.custom_recommendations
WHERE scope = '{{ scope }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>custom_recommendations</code> resource.

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
INSERT INTO azure.security.custom_recommendations (
customRecommendationName,
scope,
properties
)
SELECT 
'{{ customRecommendationName }}',
'{{ scope }}',
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
        - name: query
          value: string
        - name: cloudProviders
          value:
            - []
        - name: severity
          value: string
        - name: securityIssue
          value: string
        - name: displayName
          value: string
        - name: description
          value: string
        - name: remediationDescription
          value: string
        - name: assessmentKey
          value: string
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

Deletes the specified <code>custom_recommendations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.security.custom_recommendations
WHERE customRecommendationName = '{{ customRecommendationName }}'
AND scope = '{{ scope }}';
```
