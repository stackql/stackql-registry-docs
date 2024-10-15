---
title: experimentation_workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - experimentation_workspaces
  - split
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

Creates, updates, deletes, gets or lists a <code>experimentation_workspaces</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>experimentation_workspaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.split.experimentation_workspaces" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_experimentation_workspaces', value: 'view', },
        { label: 'experimentation_workspaces', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="access_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_source" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The resource model definition representing SKU |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of the experimentation workspace |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Get a ExperimentationWorkspace |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List ExperimentationWorkspace resources by resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List ExperimentationWorkspace resources by subscription ID |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Create a ExperimentationWorkspace |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Delete a ExperimentationWorkspace |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Update a ExperimentationWorkspace |

## `SELECT` examples

List ExperimentationWorkspace resources by subscription ID

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_experimentation_workspaces', value: 'view', },
        { label: 'experimentation_workspaces', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
access_policy,
data_source,
identity,
location,
provisioning_state,
resourceGroupName,
sku,
subscriptionId,
tags,
workspaceName
FROM azure_isv.split.vw_experimentation_workspaces
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
location,
properties,
sku,
tags
FROM azure_isv.split.experimentation_workspaces
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>experimentation_workspaces</code> resource.

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
INSERT INTO azure_isv.split.experimentation_workspaces (
resourceGroupName,
subscriptionId,
workspaceName,
properties,
sku,
identity,
tags,
location
)
SELECT 
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
'{{ properties }}',
'{{ sku }}',
'{{ identity }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: provisioningState
          value: []
        - name: accessPolicy
          value:
            - name: applicationId
              value: string
            - name: defaultRole
              value: []
            - name: dataPlaneEndpoint
              value: string
        - name: dataSource
          value:
            - name: logAnalytics
              value:
                - name: resourceId
                  value: []
                - name: storageAccountResourceId
                  value: []
                - name: enabled
                  value: boolean
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: []
        - name: size
          value: string
        - name: family
          value: string
        - name: capacity
          value: integer
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: []
        - name: userAssignedIdentities
          value: []
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>experimentation_workspaces</code> resource.

```sql
/*+ update */
UPDATE azure_isv.split.experimentation_workspaces
SET 
properties = '{{ properties }}',
sku = '{{ sku }}',
identity = '{{ identity }}',
tags = '{{ tags }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```

## `DELETE` example

Deletes the specified <code>experimentation_workspaces</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.split.experimentation_workspaces
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
