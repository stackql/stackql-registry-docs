---
title: configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - configurations
  - nginx
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

Creates, updates, deletes, gets or lists a <code>configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.nginx.configurations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_configurations', value: 'view', },
        { label: 'configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | field from the `properties` object |
| <CopyableCode code="name" /> | `text` | field from the `properties` object |
| <CopyableCode code="configurationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="deploymentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="files" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | field from the `properties` object |
| <CopyableCode code="package" /> | `text` | field from the `properties` object |
| <CopyableCode code="protected_files" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="root_file" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="name" /> | `string` |  |
| <CopyableCode code="location" /> | `string` |  |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` |  |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="configurationName, deploymentName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deploymentName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="configurationName, deploymentName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="configurationName, deploymentName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="analysis" /> | `EXEC` | <CopyableCode code="configurationName, deploymentName, resourceGroupName, subscriptionId, data__config" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_configurations', value: 'view', },
        { label: 'configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
configurationName,
deploymentName,
files,
location,
package,
protected_files,
provisioning_state,
resourceGroupName,
root_file,
subscriptionId,
system_data,
type
FROM azure_isv.nginx.vw_configurations
WHERE deploymentName = '{{ deploymentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
systemData,
type
FROM azure_isv.nginx.configurations
WHERE deploymentName = '{{ deploymentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>configurations</code> resource.

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
INSERT INTO azure_isv.nginx.configurations (
configurationName,
deploymentName,
resourceGroupName,
subscriptionId,
properties,
location
)
SELECT 
'{{ configurationName }}',
'{{ deploymentName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ location }}'
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
        - name: provisioningState
          value: []
        - name: files
          value:
            - - name: content
                value: string
              - name: virtualPath
                value: string
        - name: protectedFiles
          value:
            - - name: content
                value: string
              - name: virtualPath
                value: string
        - name: package
          value:
            - name: data
              value: string
            - name: protectedFiles
              value:
                - string
        - name: rootFile
          value: string
    - name: location
      value: string
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>configurations</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.nginx.configurations
WHERE configurationName = '{{ configurationName }}'
AND deploymentName = '{{ deploymentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
