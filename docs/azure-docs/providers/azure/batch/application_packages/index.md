---
title: application_packages
hide_title: false
hide_table_of_contents: false
keywords:
  - application_packages
  - batch
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

Creates, updates, deletes, gets or lists a <code>application_packages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application_packages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.batch.application_packages" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_application_packages', value: 'view', },
        { label: 'application_packages', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The ID of the resource. |
| <CopyableCode code="name" /> | `text` | The name of the resource. |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="applicationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | The ETag of the resource, used for concurrency statements. |
| <CopyableCode code="format" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_activation_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_url_expiry" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | The tags of the resource. |
| <CopyableCode code="type" /> | `text` | The type of the resource. |
| <CopyableCode code="versionName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="etag" /> | `string` | The ETag of the resource, used for concurrency statements. |
| <CopyableCode code="properties" /> | `object` | Properties of an application package |
| <CopyableCode code="tags" /> | `object` | The tags of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, applicationName, resourceGroupName, subscriptionId, versionName" /> | Gets information about the specified application package. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, applicationName, resourceGroupName, subscriptionId" /> | Lists all of the application packages in the specified application. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, applicationName, resourceGroupName, subscriptionId, versionName" /> | Creates an application package record. The record contains a storageUrl where the package should be uploaded to.  Once it is uploaded the `ApplicationPackage` needs to be activated using `ApplicationPackageActive` before it can be used. If the auto storage account was configured to use storage keys, the URL returned will contain a SAS. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, applicationName, resourceGroupName, subscriptionId, versionName" /> | Deletes an application package record and its associated binary file. |
| <CopyableCode code="activate" /> | `EXEC` | <CopyableCode code="accountName, applicationName, resourceGroupName, subscriptionId, versionName, data__format" /> | Activates the specified application package. This should be done after the `ApplicationPackage` was created and uploaded. This needs to be done before an `ApplicationPackage` can be used on Pools or Tasks. |

## `SELECT` examples

Lists all of the application packages in the specified application.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_application_packages', value: 'view', },
        { label: 'application_packages', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
accountName,
applicationName,
etag,
format,
last_activation_time,
resourceGroupName,
state,
storage_url,
storage_url_expiry,
subscriptionId,
tags,
type,
versionName
FROM azure.batch.vw_application_packages
WHERE accountName = '{{ accountName }}'
AND applicationName = '{{ applicationName }}'
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
tags,
type
FROM azure.batch.application_packages
WHERE accountName = '{{ accountName }}'
AND applicationName = '{{ applicationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>application_packages</code> resource.

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
INSERT INTO azure.batch.application_packages (
accountName,
applicationName,
resourceGroupName,
subscriptionId,
versionName,
properties,
tags
)
SELECT 
'{{ accountName }}',
'{{ applicationName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ versionName }}',
'{{ properties }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: state
          value: string
        - name: format
          value: string
        - name: storageUrl
          value: string
        - name: storageUrlExpiry
          value: string
        - name: lastActivationTime
          value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: etag
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>application_packages</code> resource.

```sql
/*+ delete */
DELETE FROM azure.batch.application_packages
WHERE accountName = '{{ accountName }}'
AND applicationName = '{{ applicationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND versionName = '{{ versionName }}';
```
