---
title: apis
hide_title: false
hide_table_of_contents: false
keywords:
  - apis
  - api_center
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

Creates, updates, deletes, gets or lists a <code>apis</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>apis</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_center.apis" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_apis', value: 'view', },
        { label: 'apis', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="apiName" /> | `text` | field from the `properties` object |
| <CopyableCode code="contacts" /> | `text` | field from the `properties` object |
| <CopyableCode code="custom_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="external_documentation" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | field from the `properties` object |
| <CopyableCode code="license" /> | `text` | field from the `properties` object |
| <CopyableCode code="lifecycle_stage" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="summary" /> | `text` | field from the `properties` object |
| <CopyableCode code="terms_of_service" /> | `text` | field from the `properties` object |
| <CopyableCode code="title" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | API properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="apiName, resourceGroupName, serviceName, subscriptionId, workspaceName" /> | Returns details of the API. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, workspaceName" /> | Returns a collection of APIs. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="apiName, resourceGroupName, serviceName, subscriptionId, workspaceName" /> | Creates new or updates existing API. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="apiName, resourceGroupName, serviceName, subscriptionId, workspaceName" /> | Deletes specified API. |

## `SELECT` examples

Returns a collection of APIs.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_apis', value: 'view', },
        { label: 'apis', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
apiName,
contacts,
custom_properties,
external_documentation,
kind,
license,
lifecycle_stage,
resourceGroupName,
serviceName,
subscriptionId,
summary,
terms_of_service,
title,
workspaceName
FROM azure.api_center.vw_apis
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.api_center.apis
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>apis</code> resource.

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
INSERT INTO azure.api_center.apis (
apiName,
resourceGroupName,
serviceName,
subscriptionId,
workspaceName,
properties
)
SELECT 
'{{ apiName }}',
'{{ resourceGroupName }}',
'{{ serviceName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
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
        - name: title
          value: string
        - name: kind
          value: []
        - name: description
          value: string
        - name: summary
          value: string
        - name: lifecycleStage
          value: []
        - name: termsOfService
          value:
            - name: url
              value: string
        - name: externalDocumentation
          value:
            - - name: title
                value: string
              - name: description
                value: string
              - name: url
                value: string
        - name: contacts
          value:
            - - name: name
                value: string
              - name: url
                value: string
              - name: email
                value: string
        - name: license
          value:
            - name: name
              value: string
            - name: url
              value: string
            - name: identifier
              value: string
        - name: customProperties
          value: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>apis</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_center.apis
WHERE apiName = '{{ apiName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
