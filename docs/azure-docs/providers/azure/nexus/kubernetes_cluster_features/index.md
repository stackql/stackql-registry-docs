---
title: kubernetes_cluster_features
hide_title: false
hide_table_of_contents: false
keywords:
  - kubernetes_cluster_features
  - nexus
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

Creates, updates, deletes, gets or lists a <code>kubernetes_cluster_features</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>kubernetes_cluster_features</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.nexus.kubernetes_cluster_features" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_kubernetes_cluster_features', value: 'view', },
        { label: 'kubernetes_cluster_features', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="availability_lifecycle" /> | `text` | field from the `properties` object |
| <CopyableCode code="detailed_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="detailed_status_message" /> | `text` | field from the `properties` object |
| <CopyableCode code="featureName" /> | `text` | field from the `properties` object |
| <CopyableCode code="kubernetesClusterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="options" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="required" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="featureName, kubernetesClusterName, resourceGroupName, subscriptionId" /> | Get properties of the provided the Kubernetes cluster feature. |
| <CopyableCode code="list_by_kubernetes_cluster" /> | `SELECT` | <CopyableCode code="kubernetesClusterName, resourceGroupName, subscriptionId" /> | Get a list of features for the provided Kubernetes cluster. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="featureName, kubernetesClusterName, resourceGroupName, subscriptionId" /> | Create a new Kubernetes cluster feature or update properties of the Kubernetes cluster feature if it exists. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="featureName, kubernetesClusterName, resourceGroupName, subscriptionId" /> | Delete the provided Kubernetes cluster feature. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="featureName, kubernetesClusterName, resourceGroupName, subscriptionId" /> | Patch properties of the provided Kubernetes cluster feature. |

## `SELECT` examples

Get a list of features for the provided Kubernetes cluster.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_kubernetes_cluster_features', value: 'view', },
        { label: 'kubernetes_cluster_features', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
availability_lifecycle,
detailed_status,
detailed_status_message,
featureName,
kubernetesClusterName,
location,
options,
provisioning_state,
required,
resourceGroupName,
subscriptionId,
tags,
version
FROM azure.nexus.vw_kubernetes_cluster_features
WHERE kubernetesClusterName = '{{ kubernetesClusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.nexus.kubernetes_cluster_features
WHERE kubernetesClusterName = '{{ kubernetesClusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>kubernetes_cluster_features</code> resource.

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
INSERT INTO azure.nexus.kubernetes_cluster_features (
featureName,
kubernetesClusterName,
resourceGroupName,
subscriptionId,
properties,
tags,
location
)
SELECT 
'{{ featureName }}',
'{{ kubernetesClusterName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
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
        - name: availabilityLifecycle
          value: string
        - name: detailedStatus
          value: string
        - name: detailedStatusMessage
          value: string
        - name: options
          value:
            - - name: key
                value: string
              - name: value
                value: string
        - name: provisioningState
          value: string
        - name: required
          value: string
        - name: version
          value: string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>kubernetes_cluster_features</code> resource.

```sql
/*+ update */
UPDATE azure.nexus.kubernetes_cluster_features
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
featureName = '{{ featureName }}'
AND kubernetesClusterName = '{{ kubernetesClusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>kubernetes_cluster_features</code> resource.

```sql
/*+ delete */
DELETE FROM azure.nexus.kubernetes_cluster_features
WHERE featureName = '{{ featureName }}'
AND kubernetesClusterName = '{{ kubernetesClusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
