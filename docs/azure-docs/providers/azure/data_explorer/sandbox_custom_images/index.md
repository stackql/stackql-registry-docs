---
title: sandbox_custom_images
hide_title: false
hide_table_of_contents: false
keywords:
  - sandbox_custom_images
  - data_explorer
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

Creates, updates, deletes, gets or lists a <code>sandbox_custom_images</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sandbox_custom_images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_explorer.sandbox_custom_images" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sandbox_custom_images', value: 'view', },
        { label: 'sandbox_custom_images', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="clusterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="language" /> | `text` | field from the `properties` object |
| <CopyableCode code="language_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="requirements_file_content" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sandboxCustomImageName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | A class representing the properties of a sandbox custom image object. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, sandboxCustomImageName, subscriptionId" /> | Returns a sandbox custom image |
| <CopyableCode code="list_by_cluster" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Returns the list of the existing sandbox custom images of the given Kusto cluster. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="clusterName, resourceGroupName, sandboxCustomImageName, subscriptionId" /> | Creates or updates a sandbox custom image. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, resourceGroupName, sandboxCustomImageName, subscriptionId" /> | Deletes a sandbox custom image. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="clusterName, resourceGroupName, sandboxCustomImageName, subscriptionId" /> | Updates a sandbox custom image. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId, data__name, data__type" /> | Checks that the sandbox custom image resource name is valid and is not already in use. |

## `SELECT` examples

Returns the list of the existing sandbox custom images of the given Kusto cluster.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sandbox_custom_images', value: 'view', },
        { label: 'sandbox_custom_images', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
clusterName,
language,
language_version,
provisioning_state,
requirements_file_content,
resourceGroupName,
sandboxCustomImageName,
subscriptionId
FROM azure.data_explorer.vw_sandbox_custom_images
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.data_explorer.sandbox_custom_images
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sandbox_custom_images</code> resource.

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
INSERT INTO azure.data_explorer.sandbox_custom_images (
clusterName,
resourceGroupName,
sandboxCustomImageName,
subscriptionId,
properties
)
SELECT 
'{{ clusterName }}',
'{{ resourceGroupName }}',
'{{ sandboxCustomImageName }}',
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
        - name: language
          value: string
        - name: languageVersion
          value: string
        - name: requirementsFileContent
          value: string
        - name: provisioningState
          value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>sandbox_custom_images</code> resource.

```sql
/*+ update */
UPDATE azure.data_explorer.sandbox_custom_images
SET 
properties = '{{ properties }}'
WHERE 
clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND sandboxCustomImageName = '{{ sandboxCustomImageName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>sandbox_custom_images</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_explorer.sandbox_custom_images
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND sandboxCustomImageName = '{{ sandboxCustomImageName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
