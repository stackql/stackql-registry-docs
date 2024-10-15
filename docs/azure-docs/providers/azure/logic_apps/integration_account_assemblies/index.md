---
title: integration_account_assemblies
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_account_assemblies
  - logic_apps
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

Creates, updates, deletes, gets or lists a <code>integration_account_assemblies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integration_account_assemblies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.logic_apps.integration_account_assemblies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_integration_account_assemblies', value: 'view', },
        { label: 'integration_account_assemblies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource id. |
| <CopyableCode code="name" /> | `text` | Gets the resource name. |
| <CopyableCode code="assemblyArtifactName" /> | `text` | field from the `properties` object |
| <CopyableCode code="assembly_culture" /> | `text` | field from the `properties` object |
| <CopyableCode code="assembly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="assembly_public_key_token" /> | `text` | field from the `properties` object |
| <CopyableCode code="assembly_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="content" /> | `text` | field from the `properties` object |
| <CopyableCode code="content_link" /> | `text` | field from the `properties` object |
| <CopyableCode code="content_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="integrationAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The resource location. |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | The resource tags. |
| <CopyableCode code="type" /> | `text` | Gets the resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource id. |
| <CopyableCode code="name" /> | `string` | Gets the resource name. |
| <CopyableCode code="location" /> | `string` | The resource location. |
| <CopyableCode code="properties" /> | `object` | The assembly properties definition. |
| <CopyableCode code="tags" /> | `object` | The resource tags. |
| <CopyableCode code="type" /> | `string` | Gets the resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="assemblyArtifactName, integrationAccountName, resourceGroupName, subscriptionId" /> | Get an assembly for an integration account. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="integrationAccountName, resourceGroupName, subscriptionId" /> | List the assemblies for an integration account. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="assemblyArtifactName, integrationAccountName, resourceGroupName, subscriptionId, data__properties" /> | Create or update an assembly for an integration account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="assemblyArtifactName, integrationAccountName, resourceGroupName, subscriptionId" /> | Delete an assembly for an integration account. |

## `SELECT` examples

List the assemblies for an integration account.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_integration_account_assemblies', value: 'view', },
        { label: 'integration_account_assemblies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
assemblyArtifactName,
assembly_culture,
assembly_name,
assembly_public_key_token,
assembly_version,
content,
content_link,
content_type,
integrationAccountName,
location,
resourceGroupName,
subscriptionId,
tags,
type
FROM azure.logic_apps.vw_integration_account_assemblies
WHERE integrationAccountName = '{{ integrationAccountName }}'
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
tags,
type
FROM azure.logic_apps.integration_account_assemblies
WHERE integrationAccountName = '{{ integrationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>integration_account_assemblies</code> resource.

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
INSERT INTO azure.logic_apps.integration_account_assemblies (
assemblyArtifactName,
integrationAccountName,
resourceGroupName,
subscriptionId,
data__properties,
properties,
location,
tags
)
SELECT 
'{{ assemblyArtifactName }}',
'{{ integrationAccountName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}',
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
        - name: assemblyName
          value: string
        - name: assemblyVersion
          value: string
        - name: assemblyCulture
          value: string
        - name: assemblyPublicKeyToken
          value: string
        - name: content
          value: string
        - name: contentType
          value: string
        - name: contentLink
          value:
            - name: uri
              value: string
            - name: contentVersion
              value: string
            - name: contentSize
              value: integer
            - name: contentHash
              value:
                - name: algorithm
                  value: string
                - name: value
                  value: string
            - name: metadata
              value: []
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

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>integration_account_assemblies</code> resource.

```sql
/*+ delete */
DELETE FROM azure.logic_apps.integration_account_assemblies
WHERE assemblyArtifactName = '{{ assemblyArtifactName }}'
AND integrationAccountName = '{{ integrationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
