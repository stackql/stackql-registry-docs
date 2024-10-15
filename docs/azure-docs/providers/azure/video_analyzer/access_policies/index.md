---
title: access_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - access_policies
  - video_analyzer
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

Creates, updates, deletes, gets or lists a <code>access_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.video_analyzer.access_policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_access_policies', value: 'view', },
        { label: 'access_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accessPolicyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="authentication" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="role" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Application level properties for the access policy resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accessPolicyName, accountName, resourceGroupName, subscriptionId" /> | Retrieves an existing access policy resource with the given name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Retrieves all existing access policy resources, along with their JSON representations. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accessPolicyName, accountName, resourceGroupName, subscriptionId" /> | Creates a new access policy resource or updates an existing one with the given name. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accessPolicyName, accountName, resourceGroupName, subscriptionId" /> | Deletes an existing access policy resource with the given name. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accessPolicyName, accountName, resourceGroupName, subscriptionId" /> | Updates individual properties of an existing access policy resource with the given name. |

## `SELECT` examples

Retrieves all existing access policy resources, along with their JSON representations.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_access_policies', value: 'view', },
        { label: 'access_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
accessPolicyName,
accountName,
authentication,
resourceGroupName,
role,
subscriptionId
FROM azure.video_analyzer.vw_access_policies
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.video_analyzer.access_policies
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>access_policies</code> resource.

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
INSERT INTO azure.video_analyzer.access_policies (
accessPolicyName,
accountName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ accessPolicyName }}',
'{{ accountName }}',
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
        - name: role
          value: string
        - name: authentication
          value:
            - name: '@type'
              value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>access_policies</code> resource.

```sql
/*+ update */
UPDATE azure.video_analyzer.access_policies
SET 
properties = '{{ properties }}'
WHERE 
accessPolicyName = '{{ accessPolicyName }}'
AND accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>access_policies</code> resource.

```sql
/*+ delete */
DELETE FROM azure.video_analyzer.access_policies
WHERE accessPolicyName = '{{ accessPolicyName }}'
AND accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
