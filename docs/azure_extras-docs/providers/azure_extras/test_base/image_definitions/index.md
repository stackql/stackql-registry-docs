---
title: image_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - image_definitions
  - test_base
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

Creates, updates, deletes, gets or lists a <code>image_definitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>image_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.test_base.image_definitions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_image_definitions', value: 'view', },
        { label: 'image_definitions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="architecture" /> | `text` | field from the `properties` object |
| <CopyableCode code="imageDefinitionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="security_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="testBaseAccountName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The image properties under the image definition name. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="imageDefinitionName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Get image properties under the image definition name created by test base custom image which derived from 'VHD' source. |
| <CopyableCode code="list_by_test_base_account" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, testBaseAccountName" /> | List all image definition properties created by test base custom images which are derived from 'VHD' source. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="imageDefinitionName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Create image definition for test base custom images which are derived from 'VHD' source. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="imageDefinitionName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Delete a test base image definition resource. |

## `SELECT` examples

List all image definition properties created by test base custom images which are derived from 'VHD' source.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_image_definitions', value: 'view', },
        { label: 'image_definitions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
architecture,
imageDefinitionName,
os_state,
provisioning_state,
resourceGroupName,
security_type,
subscriptionId,
testBaseAccountName
FROM azure_extras.test_base.vw_image_definitions
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_extras.test_base.image_definitions
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>image_definitions</code> resource.

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
INSERT INTO azure_extras.test_base.image_definitions (
imageDefinitionName,
resourceGroupName,
subscriptionId,
testBaseAccountName,
properties
)
SELECT 
'{{ imageDefinitionName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ testBaseAccountName }}',
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
        - name: architecture
          value: string
        - name: osState
          value: string
        - name: securityType
          value: string
        - name: provisioningState
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>image_definitions</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.test_base.image_definitions
WHERE imageDefinitionName = '{{ imageDefinitionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```
