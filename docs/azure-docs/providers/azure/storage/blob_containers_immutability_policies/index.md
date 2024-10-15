---
title: blob_containers_immutability_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - blob_containers_immutability_policies
  - storage
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

Creates, updates, deletes, gets or lists a <code>blob_containers_immutability_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>blob_containers_immutability_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage.blob_containers_immutability_policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_blob_containers_immutability_policies', value: 'view', },
        { label: 'blob_containers_immutability_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="allow_protected_append_writes" /> | `text` | field from the `properties` object |
| <CopyableCode code="allow_protected_append_writes_all" /> | `text` | field from the `properties` object |
| <CopyableCode code="containerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Resource Etag. |
| <CopyableCode code="immutabilityPolicyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="immutability_period_since_creation_in_days" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Resource Etag. |
| <CopyableCode code="properties" /> | `object` | The properties of an ImmutabilityPolicy of a blob container. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, containerName, immutabilityPolicyName, resourceGroupName, subscriptionId" /> | Gets the existing immutability policy along with the corresponding ETag in response headers and body. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, containerName, immutabilityPolicyName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates an unlocked immutability policy. ETag in If-Match is honored if given but not required for this operation. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, accountName, containerName, immutabilityPolicyName, resourceGroupName, subscriptionId" /> | Aborts an unlocked immutability policy. The response of delete has immutabilityPeriodSinceCreationInDays set to 0. ETag in If-Match is required for this operation. Deleting a locked immutability policy is not allowed, the only way is to delete the container after deleting all expired blobs inside the policy locked container. |

## `SELECT` examples

Gets the existing immutability policy along with the corresponding ETag in response headers and body.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_blob_containers_immutability_policies', value: 'view', },
        { label: 'blob_containers_immutability_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
accountName,
allow_protected_append_writes,
allow_protected_append_writes_all,
containerName,
etag,
immutabilityPolicyName,
immutability_period_since_creation_in_days,
resourceGroupName,
state,
subscriptionId
FROM azure.storage.vw_blob_containers_immutability_policies
WHERE accountName = '{{ accountName }}'
AND containerName = '{{ containerName }}'
AND immutabilityPolicyName = '{{ immutabilityPolicyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
properties
FROM azure.storage.blob_containers_immutability_policies
WHERE accountName = '{{ accountName }}'
AND containerName = '{{ containerName }}'
AND immutabilityPolicyName = '{{ immutabilityPolicyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>blob_containers_immutability_policies</code> resource.

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
INSERT INTO azure.storage.blob_containers_immutability_policies (
accountName,
containerName,
immutabilityPolicyName,
resourceGroupName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ accountName }}',
'{{ containerName }}',
'{{ immutabilityPolicyName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
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
        - name: immutabilityPeriodSinceCreationInDays
          value: integer
        - name: state
          value: string
        - name: allowProtectedAppendWrites
          value: boolean
        - name: allowProtectedAppendWritesAll
          value: boolean
    - name: etag
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>blob_containers_immutability_policies</code> resource.

```sql
/*+ delete */
DELETE FROM azure.storage.blob_containers_immutability_policies
WHERE If-Match = '{{ If-Match }}'
AND accountName = '{{ accountName }}'
AND containerName = '{{ containerName }}'
AND immutabilityPolicyName = '{{ immutabilityPolicyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
