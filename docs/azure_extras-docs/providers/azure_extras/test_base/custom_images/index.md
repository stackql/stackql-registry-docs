---
title: custom_images
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_images
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

Creates, updates, deletes, gets or lists a <code>custom_images</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.test_base.custom_images" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_custom_images', value: 'view', },
        { label: 'custom_images', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="creation_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="customImageName" /> | `text` | field from the `properties` object |
| <CopyableCode code="definition_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_disk_image_size_in_gb" /> | `text` | field from the `properties` object |
| <CopyableCode code="product" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="release" /> | `text` | field from the `properties` object |
| <CopyableCode code="release_version_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="source" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="testBaseAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="validation_results" /> | `text` | field from the `properties` object |
| <CopyableCode code="version_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="vhd_file_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="vhd_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of the test base custom image. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="customImageName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Gets a test base custom image. |
| <CopyableCode code="list_by_test_base_account" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, testBaseAccountName" /> | Lists all the custom images under a test base account. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="customImageName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Creates a test base custom image. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="customImageName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Deletes a test base custom image. |
| <CopyableCode code="check_image_name_availability" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, testBaseAccountName, data__definitionName, data__versionName" /> | Checks that the test vase custom image generated from VHD resource has valid and unique definition and version, return architecture and OS state of potential existing image definition. |

## `SELECT` examples

Lists all the custom images under a test base account.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_custom_images', value: 'view', },
        { label: 'custom_images', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
creation_time,
customImageName,
definition_name,
os_disk_image_size_in_gb,
product,
provisioning_state,
release,
release_version_date,
resourceGroupName,
source,
status,
subscriptionId,
testBaseAccountName,
validation_results,
version_name,
vhd_file_name,
vhd_id
FROM azure_extras.test_base.vw_custom_images
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_extras.test_base.custom_images
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>custom_images</code> resource.

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
INSERT INTO azure_extras.test_base.custom_images (
customImageName,
resourceGroupName,
subscriptionId,
testBaseAccountName,
properties
)
SELECT 
'{{ customImageName }}',
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
        - name: vhdId
          value: string
        - name: definitionName
          value: string
        - name: versionName
          value: string
        - name: source
          value: string
        - name: product
          value: string
        - name: release
          value: string
        - name: status
          value: string
        - name: creationTime
          value: string
        - name: validationResults
          value:
            - name: results
              value:
                - - name: verificationName
                    value: string
                  - name: result
                    value: string
                  - name: message
                    value: string
        - name: osDiskImageSizeInGB
          value: integer
        - name: releaseVersionDate
          value: string
        - name: vhdFileName
          value: string
        - name: provisioningState
          value: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>custom_images</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.test_base.custom_images
WHERE customImageName = '{{ customImageName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```
