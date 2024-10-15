---
title: archive_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - archive_versions
  - container_registry
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

Creates, updates, deletes, gets or lists a <code>archive_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>archive_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_registry.archive_versions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_archive_versions', value: 'view', },
        { label: 'archive_versions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="archiveName" /> | `text` | field from the `properties` object |
| <CopyableCode code="archiveVersionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="archive_version_error_message" /> | `text` | field from the `properties` object |
| <CopyableCode code="packageType" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="registryName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of an export pipeline. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="archiveName, archiveVersionName, packageType, registryName, resourceGroupName, subscriptionId" /> | Gets the properties of the archive version. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="archiveName, packageType, registryName, resourceGroupName, subscriptionId" /> | Lists all archive versions for the specified container registry, repository type and archive name. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="archiveName, archiveVersionName, packageType, registryName, resourceGroupName, subscriptionId" /> | Creates a archive for a container registry with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="archiveName, archiveVersionName, packageType, registryName, resourceGroupName, subscriptionId" /> | Deletes a archive version from a container registry. |

## `SELECT` examples

Lists all archive versions for the specified container registry, repository type and archive name.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_archive_versions', value: 'view', },
        { label: 'archive_versions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
archiveName,
archiveVersionName,
archive_version_error_message,
packageType,
provisioning_state,
registryName,
resourceGroupName,
subscriptionId
FROM azure.container_registry.vw_archive_versions
WHERE archiveName = '{{ archiveName }}'
AND packageType = '{{ packageType }}'
AND registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.container_registry.archive_versions
WHERE archiveName = '{{ archiveName }}'
AND packageType = '{{ packageType }}'
AND registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>archive_versions</code> resource.

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
INSERT INTO azure.container_registry.archive_versions (
archiveName,
archiveVersionName,
packageType,
registryName,
resourceGroupName,
subscriptionId
)
SELECT 
'{{ archiveName }}',
'{{ archiveVersionName }}',
'{{ packageType }}',
'{{ registryName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>archive_versions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.container_registry.archive_versions
WHERE archiveName = '{{ archiveName }}'
AND archiveVersionName = '{{ archiveVersionName }}'
AND packageType = '{{ packageType }}'
AND registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
