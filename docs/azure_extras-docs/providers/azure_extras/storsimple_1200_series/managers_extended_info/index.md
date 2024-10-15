---
title: managers_extended_info
hide_title: false
hide_table_of_contents: false
keywords:
  - managers_extended_info
  - storsimple_1200_series
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

Creates, updates, deletes, gets or lists a <code>managers_extended_info</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managers_extended_info</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_1200_series.managers_extended_info" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managers_extended_info', value: 'view', },
        { label: 'managers_extended_info', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The identifier. |
| <CopyableCode code="name" /> | `text` | The name. |
| <CopyableCode code="algorithm" /> | `text` | field from the `properties` object |
| <CopyableCode code="encryption_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="encryption_key_thumbprint" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | ETag of the Resource |
| <CopyableCode code="integrity_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="managerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="portal_certificate_thumbprint" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type. |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier. |
| <CopyableCode code="name" /> | `string` | The name. |
| <CopyableCode code="etag" /> | `string` | ETag of the Resource |
| <CopyableCode code="properties" /> | `object` | Properties of the ManagerExtendedInfo |
| <CopyableCode code="type" /> | `string` | The type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="managerName, resourceGroupName, subscriptionId" /> | Returns the extended information of the specified manager name. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="managerName, resourceGroupName, subscriptionId, data__properties" /> | Creates the extended info of the manager. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="managerName, resourceGroupName, subscriptionId" /> | Deletes the extended info of the manager. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="If-Match, managerName, resourceGroupName, subscriptionId, data__properties" /> | Updates the extended info of the manager. |

## `SELECT` examples

Returns the extended information of the specified manager name.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managers_extended_info', value: 'view', },
        { label: 'managers_extended_info', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
algorithm,
encryption_key,
encryption_key_thumbprint,
etag,
integrity_key,
managerName,
portal_certificate_thumbprint,
resourceGroupName,
subscriptionId,
type,
version
FROM azure_extras.storsimple_1200_series.vw_managers_extended_info
WHERE managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
properties,
type
FROM azure_extras.storsimple_1200_series.managers_extended_info
WHERE managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>managers_extended_info</code> resource.

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
INSERT INTO azure_extras.storsimple_1200_series.managers_extended_info (
managerName,
resourceGroupName,
subscriptionId,
data__properties,
properties,
etag
)
SELECT 
'{{ managerName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}',
'{{ etag }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: properties
      value:
        - name: version
          value: string
        - name: integrityKey
          value: string
        - name: encryptionKey
          value: string
        - name: encryptionKeyThumbprint
          value: string
        - name: portalCertificateThumbprint
          value: string
        - name: algorithm
          value: string
    - name: etag
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>managers_extended_info</code> resource.

```sql
/*+ update */
UPDATE azure_extras.storsimple_1200_series.managers_extended_info
SET 
properties = '{{ properties }}',
etag = '{{ etag }}'
WHERE 
If-Match = '{{ If-Match }}'
AND managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND data__properties = '{{ data__properties }}';
```

## `DELETE` example

Deletes the specified <code>managers_extended_info</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.storsimple_1200_series.managers_extended_info
WHERE managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
