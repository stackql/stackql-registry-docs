---
title: secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - secrets
  - openshift_clusters
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

Creates, updates, deletes, gets or lists a <code>secrets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.openshift_clusters.secrets" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_secrets', value: 'view', },
        { label: 'secrets', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="childResourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="secret_resources" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | SecretProperties represents the properties of a Secret |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="childResourceName, resourceGroupName, resourceName, subscriptionId" /> | The operation returns properties of a Secret. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | The operation returns properties of each Secret. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="childResourceName, resourceGroupName, resourceName, subscriptionId" /> | The operation returns properties of a Secret. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="childResourceName, resourceGroupName, resourceName, subscriptionId" /> | The operation returns nothing. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="childResourceName, resourceGroupName, resourceName, subscriptionId" /> | The operation returns properties of a Secret. |

## `SELECT` examples

The operation returns properties of each Secret.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_secrets', value: 'view', },
        { label: 'secrets', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
childResourceName,
resourceGroupName,
resourceName,
secret_resources,
subscriptionId,
system_data
FROM azure_isv.openshift_clusters.vw_secrets
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
systemData
FROM azure_isv.openshift_clusters.secrets
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>secrets</code> resource.

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
INSERT INTO azure_isv.openshift_clusters.secrets (
childResourceName,
resourceGroupName,
resourceName,
subscriptionId,
properties
)
SELECT 
'{{ childResourceName }}',
'{{ resourceGroupName }}',
'{{ resourceName }}',
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
        - name: secretResources
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

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>secrets</code> resource.

```sql
/*+ update */
UPDATE azure_isv.openshift_clusters.secrets
SET 
properties = '{{ properties }}'
WHERE 
childResourceName = '{{ childResourceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>secrets</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.openshift_clusters.secrets
WHERE childResourceName = '{{ childResourceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
