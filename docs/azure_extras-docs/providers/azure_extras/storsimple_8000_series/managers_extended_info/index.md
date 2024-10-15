---
title: managers_extended_info
hide_title: false
hide_table_of_contents: false
keywords:
  - managers_extended_info
  - storsimple_8000_series
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_8000_series.managers_extended_info" /></td></tr>
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
| <CopyableCode code="id" /> | `text` | The path ID that uniquely identifies the object. |
| <CopyableCode code="name" /> | `text` | The name of the object. |
| <CopyableCode code="algorithm" /> | `text` | field from the `properties` object |
| <CopyableCode code="encryption_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="encryption_key_thumbprint" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | The etag of the resource. |
| <CopyableCode code="integrity_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | The Kind of the object. Currently only Series8000 is supported |
| <CopyableCode code="managerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="portal_certificate_thumbprint" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The hierarchical type of the object. |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The path ID that uniquely identifies the object. |
| <CopyableCode code="name" /> | `string` | The name of the object. |
| <CopyableCode code="etag" /> | `string` | The etag of the resource. |
| <CopyableCode code="kind" /> | `string` | The Kind of the object. Currently only Series8000 is supported |
| <CopyableCode code="properties" /> | `object` | The properties of the manager extended info. |
| <CopyableCode code="type" /> | `string` | The hierarchical type of the object. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="managerName, resourceGroupName, subscriptionId" /> | Returns the extended information of the specified manager name. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="managerName, resourceGroupName, subscriptionId" /> | Creates the extended info of the manager. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="managerName, resourceGroupName, subscriptionId" /> | Deletes the extended info of the manager. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="If-Match, managerName, resourceGroupName, subscriptionId" /> | Updates the extended info of the manager. |

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
kind,
managerName,
portal_certificate_thumbprint,
resourceGroupName,
subscriptionId,
type,
version
FROM azure_extras.storsimple_8000_series.vw_managers_extended_info
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
kind,
properties,
type
FROM azure_extras.storsimple_8000_series.managers_extended_info
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
INSERT INTO azure_extras.storsimple_8000_series.managers_extended_info (
managerName,
resourceGroupName,
subscriptionId,
kind,
properties,
etag
)
SELECT 
'{{ managerName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ kind }}',
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
    - name: kind
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
UPDATE azure_extras.storsimple_8000_series.managers_extended_info
SET 
kind = '{{ kind }}',
properties = '{{ properties }}',
etag = '{{ etag }}'
WHERE 
If-Match = '{{ If-Match }}'
AND managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>managers_extended_info</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.storsimple_8000_series.managers_extended_info
WHERE managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
