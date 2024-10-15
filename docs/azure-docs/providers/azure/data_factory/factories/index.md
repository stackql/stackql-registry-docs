---
title: factories
hide_title: false
hide_table_of_contents: false
keywords:
  - factories
  - data_factory
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

Creates, updates, deletes, gets or lists a <code>factories</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>factories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_factory.factories" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_factories', value: 'view', },
        { label: 'factories', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource identifier. |
| <CopyableCode code="name" /> | `text` | The resource name. |
| <CopyableCode code="create_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="e_tag" /> | `text` | field from the `properties` object |
| <CopyableCode code="encryption" /> | `text` | field from the `properties` object |
| <CopyableCode code="factoryName" /> | `text` | field from the `properties` object |
| <CopyableCode code="global_parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Identity properties of the factory resource. |
| <CopyableCode code="location" /> | `text` | The resource location. |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="purview_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="repo_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | The resource tags. |
| <CopyableCode code="type" /> | `text` | The resource type. |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource identifier. |
| <CopyableCode code="name" /> | `string` | The resource name. |
| <CopyableCode code="eTag" /> | `string` | Etag identifies change in the resource. |
| <CopyableCode code="identity" /> | `object` | Identity properties of the factory resource. |
| <CopyableCode code="location" /> | `string` | The resource location. |
| <CopyableCode code="properties" /> | `object` | Factory resource properties. |
| <CopyableCode code="tags" /> | `object` | The resource tags. |
| <CopyableCode code="type" /> | `string` | The resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="factoryName, resourceGroupName, subscriptionId" /> | Gets a factory. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists factories under the specified subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists factories. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="factoryName, resourceGroupName, subscriptionId" /> | Creates or updates a factory. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="factoryName, resourceGroupName, subscriptionId" /> | Deletes a factory. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="factoryName, resourceGroupName, subscriptionId" /> | Updates a factory. |
| <CopyableCode code="configure_factory_repo" /> | `EXEC` | <CopyableCode code="locationId, subscriptionId" /> | Updates a factory's repo information. |

## `SELECT` examples

Lists factories under the specified subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_factories', value: 'view', },
        { label: 'factories', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
create_time,
e_tag,
encryption,
factoryName,
global_parameters,
identity,
location,
provisioning_state,
public_network_access,
purview_configuration,
repo_configuration,
resourceGroupName,
subscriptionId,
tags,
type,
version
FROM azure.data_factory.vw_factories
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
eTag,
identity,
location,
properties,
tags,
type
FROM azure.data_factory.factories
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>factories</code> resource.

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
INSERT INTO azure.data_factory.factories (
factoryName,
resourceGroupName,
subscriptionId,
location,
tags,
identity,
properties
)
SELECT 
'{{ factoryName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ location }}',
'{{ tags }}',
'{{ identity }}',
'{{ properties }}'
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
    - name: location
      value: string
    - name: tags
      value: object
    - name: eTag
      value: string
    - name: identity
      value:
        - name: type
          value: string
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: userAssignedIdentities
          value: []
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: createTime
          value: string
        - name: version
          value: string
        - name: purviewConfiguration
          value:
            - name: purviewResourceId
              value: string
        - name: repoConfiguration
          value:
            - name: type
              value: string
            - name: accountName
              value: string
            - name: repositoryName
              value: string
            - name: collaborationBranch
              value: string
            - name: rootFolder
              value: string
            - name: lastCommitId
              value: string
            - name: disablePublish
              value: boolean
        - name: globalParameters
          value: []
        - name: encryption
          value:
            - name: keyName
              value: string
            - name: vaultBaseUrl
              value: string
            - name: keyVersion
              value: string
            - name: identity
              value:
                - name: userAssignedIdentity
                  value: string
        - name: publicNetworkAccess
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>factories</code> resource.

```sql
/*+ update */
UPDATE azure.data_factory.factories
SET 
tags = '{{ tags }}',
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
factoryName = '{{ factoryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>factories</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_factory.factories
WHERE factoryName = '{{ factoryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
