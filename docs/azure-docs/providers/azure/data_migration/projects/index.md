---
title: projects
hide_title: false
hide_table_of_contents: false
keywords:
  - projects
  - data_migration
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

Creates, updates, deletes, gets or lists a <code>projects</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_migration.projects" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_projects', value: 'view', },
        { label: 'projects', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | field from the `properties` object |
| <CopyableCode code="name" /> | `text` | field from the `properties` object |
| <CopyableCode code="azure_authentication_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="databases_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | HTTP strong entity tag value. This is ignored if submitted. |
| <CopyableCode code="groupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | field from the `properties` object |
| <CopyableCode code="projectName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_connection_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_platform" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_connection_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_platform" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="name" /> | `string` |  |
| <CopyableCode code="etag" /> | `string` | HTTP strong entity tag value. This is ignored if submitted. |
| <CopyableCode code="location" /> | `string` |  |
| <CopyableCode code="properties" /> | `object` | Project-specific properties |
| <CopyableCode code="systemData" /> | `object` |  |
| <CopyableCode code="tags" /> | `object` |  |
| <CopyableCode code="type" /> | `string` |  |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="groupName, projectName, serviceName, subscriptionId" /> | The project resource is a nested resource representing a stored migration project. The GET method retrieves information about a project. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="groupName, serviceName, subscriptionId" /> | The project resource is a nested resource representing a stored migration project. This method returns a list of projects owned by a service resource. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="groupName, projectName, serviceName, subscriptionId" /> | The project resource is a nested resource representing a stored migration project. The PUT method creates a new project or updates an existing one. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="groupName, projectName, serviceName, subscriptionId" /> | The project resource is a nested resource representing a stored migration project. The DELETE method deletes a project. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="groupName, projectName, serviceName, subscriptionId" /> | The project resource is a nested resource representing a stored migration project. The PATCH method updates an existing project. |

## `SELECT` examples

The project resource is a nested resource representing a stored migration project. This method returns a list of projects owned by a service resource.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_projects', value: 'view', },
        { label: 'projects', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
azure_authentication_info,
creation_time,
databases_info,
etag,
groupName,
location,
projectName,
provisioning_state,
serviceName,
source_connection_info,
source_platform,
subscriptionId,
system_data,
tags,
target_connection_info,
target_platform,
type
FROM azure.data_migration.vw_projects
WHERE groupName = '{{ groupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
location,
properties,
systemData,
tags,
type
FROM azure.data_migration.projects
WHERE groupName = '{{ groupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>projects</code> resource.

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
INSERT INTO azure.data_migration.projects (
groupName,
projectName,
serviceName,
subscriptionId,
properties,
etag,
location,
tags
)
SELECT 
'{{ groupName }}',
'{{ projectName }}',
'{{ serviceName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ etag }}',
'{{ location }}',
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
        - name: sourcePlatform
          value: []
        - name: azureAuthenticationInfo
          value:
            - name: applicationId
              value: string
            - name: appKey
              value: string
            - name: tenantId
              value: string
            - name: ignoreAzurePermissions
              value: boolean
        - name: targetPlatform
          value: []
        - name: creationTime
          value: string
        - name: sourceConnectionInfo
          value:
            - name: type
              value: string
            - name: userName
              value: string
            - name: password
              value: string
        - name: databasesInfo
          value:
            - - name: sourceDatabaseName
                value: string
        - name: provisioningState
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
    - name: etag
      value: string
    - name: location
      value: string
    - name: tags
      value: object
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>projects</code> resource.

```sql
/*+ update */
UPDATE azure.data_migration.projects
SET 
properties = '{{ properties }}',
etag = '{{ etag }}',
location = '{{ location }}',
tags = '{{ tags }}'
WHERE 
groupName = '{{ groupName }}'
AND projectName = '{{ projectName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>projects</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_migration.projects
WHERE groupName = '{{ groupName }}'
AND projectName = '{{ projectName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
