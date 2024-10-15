---
title: archives
hide_title: false
hide_table_of_contents: false
keywords:
  - archives
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

Creates, updates, deletes, gets or lists a <code>archives</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>archives</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_registry.archives" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_archives', value: 'view', },
        { label: 'archives', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="archiveName" /> | `text` | field from the `properties` object |
| <CopyableCode code="packageType" /> | `text` | field from the `properties` object |
| <CopyableCode code="package_source" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="published_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="registryName" /> | `text` | field from the `properties` object |
| <CopyableCode code="repository_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="repository_endpoint_prefix" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of a archive. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="archiveName, packageType, registryName, resourceGroupName, subscriptionId" /> | Gets the properties of the archive. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="packageType, registryName, resourceGroupName, subscriptionId" /> | Lists all archives for the specified container registry and package type. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="archiveName, packageType, registryName, resourceGroupName, subscriptionId" /> | Creates a archive for a container registry with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="archiveName, packageType, registryName, resourceGroupName, subscriptionId" /> | Deletes a archive from a container registry. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="archiveName, packageType, registryName, resourceGroupName, subscriptionId" /> | Updates a archive for a container registry with the specified parameters. |

## `SELECT` examples

Lists all archives for the specified container registry and package type.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_archives', value: 'view', },
        { label: 'archives', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
archiveName,
packageType,
package_source,
provisioning_state,
published_version,
registryName,
repository_endpoint,
repository_endpoint_prefix,
resourceGroupName,
subscriptionId
FROM azure.container_registry.vw_archives
WHERE packageType = '{{ packageType }}'
AND registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.container_registry.archives
WHERE packageType = '{{ packageType }}'
AND registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>archives</code> resource.

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
INSERT INTO azure.container_registry.archives (
archiveName,
packageType,
registryName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ archiveName }}',
'{{ packageType }}',
'{{ registryName }}',
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
        - name: packageSource
          value:
            - name: type
              value: string
            - name: url
              value: string
        - name: publishedVersion
          value: string
        - name: repositoryEndpointPrefix
          value: string
        - name: repositoryEndpoint
          value: string
        - name: provisioningState
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>archives</code> resource.

```sql
/*+ update */
UPDATE azure.container_registry.archives
SET 
properties = '{{ properties }}'
WHERE 
archiveName = '{{ archiveName }}'
AND packageType = '{{ packageType }}'
AND registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>archives</code> resource.

```sql
/*+ delete */
DELETE FROM azure.container_registry.archives
WHERE archiveName = '{{ archiveName }}'
AND packageType = '{{ packageType }}'
AND registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
