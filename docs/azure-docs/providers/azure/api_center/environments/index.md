---
title: environments
hide_title: false
hide_table_of_contents: false
keywords:
  - environments
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

Creates, updates, deletes, gets or lists a <code>environments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_center.environments" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_environments', value: 'view', },
        { label: 'environments', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="custom_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="environmentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | field from the `properties` object |
| <CopyableCode code="onboarding" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="server" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="title" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Environment properties entity. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="environmentName, resourceGroupName, serviceName, subscriptionId, workspaceName" /> | Returns details of the environment. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, workspaceName" /> | Returns a collection of environments. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="environmentName, resourceGroupName, serviceName, subscriptionId, workspaceName" /> | Creates new or updates existing environment. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="environmentName, resourceGroupName, serviceName, subscriptionId, workspaceName" /> | Deletes the environment. |

## `SELECT` examples

Returns a collection of environments.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_environments', value: 'view', },
        { label: 'environments', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
custom_properties,
environmentName,
kind,
onboarding,
resourceGroupName,
server,
serviceName,
subscriptionId,
title,
workspaceName
FROM azure.api_center.vw_environments
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
FROM azure.api_center.environments
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>environments</code> resource.

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
INSERT INTO azure.api_center.environments (
environmentName,
resourceGroupName,
serviceName,
subscriptionId,
workspaceName,
properties
)
SELECT 
'{{ environmentName }}',
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
        - name: description
          value: string
        - name: kind
          value: []
        - name: server
          value:
            - name: type
              value: []
            - name: managementPortalUri
              value:
                - string
        - name: onboarding
          value:
            - name: instructions
              value: string
            - name: developerPortalUri
              value:
                - string
        - name: customProperties
          value: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>environments</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_center.environments
WHERE environmentName = '{{ environmentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
