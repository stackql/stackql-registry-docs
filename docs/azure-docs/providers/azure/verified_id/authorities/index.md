---
title: authorities
hide_title: false
hide_table_of_contents: false
keywords:
  - authorities
  - verified_id
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

Creates, updates, deletes, gets or lists a <code>authorities</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>authorities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.verified_id.authorities" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_authorities', value: 'view', },
        { label: 'authorities', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="authorityName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Details of the VerifiedId Authority. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="authorityName, resourceGroupName, subscriptionId" /> | Get a Authority |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List Authority resources by resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List Authority resources by subscription ID |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="authorityName, resourceGroupName, subscriptionId" /> | Create a Authority |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="authorityName, resourceGroupName, subscriptionId" /> | Delete a Authority |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="authorityName, resourceGroupName, subscriptionId" /> | Update a Authority |

## `SELECT` examples

List Authority resources by subscription ID

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_authorities', value: 'view', },
        { label: 'authorities', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
authorityName,
location,
provisioning_state,
resourceGroupName,
subscriptionId,
tags
FROM azure.verified_id.vw_authorities
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.verified_id.authorities
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>authorities</code> resource.

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
INSERT INTO azure.verified_id.authorities (
authorityName,
resourceGroupName,
subscriptionId,
properties,
tags,
location
)
SELECT 
'{{ authorityName }}',
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
        - name: provisioningState
          value: []
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>authorities</code> resource.

```sql
/*+ update */
UPDATE azure.verified_id.authorities
SET 
tags = '{{ tags }}'
WHERE 
authorityName = '{{ authorityName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>authorities</code> resource.

```sql
/*+ delete */
DELETE FROM azure.verified_id.authorities
WHERE authorityName = '{{ authorityName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
