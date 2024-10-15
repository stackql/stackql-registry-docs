---
title: configuration_profiles_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_profiles_versions
  - automanage
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

Creates, updates, deletes, gets or lists a <code>configuration_profiles_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration_profiles_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automanage.configuration_profiles_versions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_configuration_profiles_versions', value: 'view', },
        { label: 'configuration_profiles_versions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="configurationProfileName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="versionName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Automanage configuration profile properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="configurationProfileName, resourceGroupName, subscriptionId, versionName" /> | Get information about a configuration profile version |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="configurationProfileName, resourceGroupName, subscriptionId, versionName" /> | Creates a configuration profile version |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="configurationProfileName, resourceGroupName, subscriptionId, versionName" /> | Delete a configuration profile version |

## `SELECT` examples

Get information about a configuration profile version

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_configuration_profiles_versions', value: 'view', },
        { label: 'configuration_profiles_versions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
configuration,
configurationProfileName,
location,
resourceGroupName,
subscriptionId,
system_data,
tags,
versionName
FROM azure.automanage.vw_configuration_profiles_versions
WHERE configurationProfileName = '{{ configurationProfileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND versionName = '{{ versionName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
systemData,
tags
FROM azure.automanage.configuration_profiles_versions
WHERE configurationProfileName = '{{ configurationProfileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND versionName = '{{ versionName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>configuration_profiles_versions</code> resource.

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
INSERT INTO azure.automanage.configuration_profiles_versions (
configurationProfileName,
resourceGroupName,
subscriptionId,
versionName,
properties,
tags,
location
)
SELECT 
'{{ configurationProfileName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ versionName }}',
'{{ properties }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: configuration
          value: []
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
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>configuration_profiles_versions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.automanage.configuration_profiles_versions
WHERE configurationProfileName = '{{ configurationProfileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND versionName = '{{ versionName }}';
```
