---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - desktop_virtualization
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

Creates, updates, deletes, gets or lists a <code>applications</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.desktop_virtualization.applications" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_applications', value: 'view', },
        { label: 'applications', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="applicationGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="applicationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="application_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="command_line_arguments" /> | `text` | field from the `properties` object |
| <CopyableCode code="command_line_setting" /> | `text` | field from the `properties` object |
| <CopyableCode code="file_path" /> | `text` | field from the `properties` object |
| <CopyableCode code="friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="icon_content" /> | `text` | field from the `properties` object |
| <CopyableCode code="icon_hash" /> | `text` | field from the `properties` object |
| <CopyableCode code="icon_index" /> | `text` | field from the `properties` object |
| <CopyableCode code="icon_path" /> | `text` | field from the `properties` object |
| <CopyableCode code="msix_package_application_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="msix_package_family_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="object_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="show_in_portal" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Schema for Application properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="applicationGroupName, applicationName, resourceGroupName, subscriptionId" /> | Get an application. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="applicationGroupName, resourceGroupName, subscriptionId" /> | List applications. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="applicationGroupName, applicationName, resourceGroupName, subscriptionId, data__properties" /> | Create or update an application. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="applicationGroupName, applicationName, resourceGroupName, subscriptionId" /> | Remove an application. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="applicationGroupName, applicationName, resourceGroupName, subscriptionId" /> | Update an application. |

## `SELECT` examples

List applications.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_applications', value: 'view', },
        { label: 'applications', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
applicationGroupName,
applicationName,
application_type,
command_line_arguments,
command_line_setting,
file_path,
friendly_name,
icon_content,
icon_hash,
icon_index,
icon_path,
msix_package_application_id,
msix_package_family_name,
object_id,
resourceGroupName,
show_in_portal,
subscriptionId,
system_data,
type
FROM azure.desktop_virtualization.vw_applications
WHERE applicationGroupName = '{{ applicationGroupName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure.desktop_virtualization.applications
WHERE applicationGroupName = '{{ applicationGroupName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>applications</code> resource.

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
INSERT INTO azure.desktop_virtualization.applications (
applicationGroupName,
applicationName,
resourceGroupName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ applicationGroupName }}',
'{{ applicationName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
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
    - name: properties
      value:
        - name: objectId
          value: string
        - name: description
          value: string
        - name: friendlyName
          value: string
        - name: filePath
          value: string
        - name: msixPackageFamilyName
          value: string
        - name: msixPackageApplicationId
          value: string
        - name: applicationType
          value: string
        - name: commandLineSetting
          value: string
        - name: commandLineArguments
          value: string
        - name: showInPortal
          value: boolean
        - name: iconPath
          value: string
        - name: iconIndex
          value: integer
        - name: iconHash
          value: string
        - name: iconContent
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>applications</code> resource.

```sql
/*+ update */
UPDATE azure.desktop_virtualization.applications
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
applicationGroupName = '{{ applicationGroupName }}'
AND applicationName = '{{ applicationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>applications</code> resource.

```sql
/*+ delete */
DELETE FROM azure.desktop_virtualization.applications
WHERE applicationGroupName = '{{ applicationGroupName }}'
AND applicationName = '{{ applicationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
