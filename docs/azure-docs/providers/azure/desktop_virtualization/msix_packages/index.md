---
title: msix_packages
hide_title: false
hide_table_of_contents: false
keywords:
  - msix_packages
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

Creates, updates, deletes, gets or lists a <code>msix_packages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>msix_packages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.desktop_virtualization.msix_packages" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_msix_packages', value: 'view', },
        { label: 'msix_packages', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="hostPoolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="image_path" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_active" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_regular_registration" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_updated" /> | `text` | field from the `properties` object |
| <CopyableCode code="msixPackageFullName" /> | `text` | field from the `properties` object |
| <CopyableCode code="package_applications" /> | `text` | field from the `properties` object |
| <CopyableCode code="package_dependencies" /> | `text` | field from the `properties` object |
| <CopyableCode code="package_family_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="package_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="package_relative_path" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Schema for MSIX Package properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hostPoolName, msixPackageFullName, resourceGroupName, subscriptionId" /> | Get a msixpackage. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="hostPoolName, resourceGroupName, subscriptionId" /> | List MSIX packages in hostpool. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="hostPoolName, msixPackageFullName, resourceGroupName, subscriptionId, data__properties" /> | Create or update a MSIX package. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="hostPoolName, msixPackageFullName, resourceGroupName, subscriptionId" /> | Remove an MSIX Package. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="hostPoolName, msixPackageFullName, resourceGroupName, subscriptionId" /> | Update an  MSIX Package. |

## `SELECT` examples

List MSIX packages in hostpool.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_msix_packages', value: 'view', },
        { label: 'msix_packages', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
display_name,
hostPoolName,
image_path,
is_active,
is_regular_registration,
last_updated,
msixPackageFullName,
package_applications,
package_dependencies,
package_family_name,
package_name,
package_relative_path,
resourceGroupName,
subscriptionId,
system_data,
type,
version
FROM azure.desktop_virtualization.vw_msix_packages
WHERE hostPoolName = '{{ hostPoolName }}'
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
FROM azure.desktop_virtualization.msix_packages
WHERE hostPoolName = '{{ hostPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>msix_packages</code> resource.

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
INSERT INTO azure.desktop_virtualization.msix_packages (
hostPoolName,
msixPackageFullName,
resourceGroupName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ hostPoolName }}',
'{{ msixPackageFullName }}',
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
        - name: imagePath
          value: string
        - name: packageName
          value: string
        - name: packageFamilyName
          value: string
        - name: displayName
          value: string
        - name: packageRelativePath
          value: string
        - name: isRegularRegistration
          value: boolean
        - name: isActive
          value: boolean
        - name: packageDependencies
          value:
            - - name: dependencyName
                value: string
              - name: publisher
                value: string
              - name: minVersion
                value: string
        - name: version
          value: string
        - name: lastUpdated
          value: string
        - name: packageApplications
          value:
            - - name: appId
                value: string
              - name: description
                value: string
              - name: appUserModelID
                value: string
              - name: friendlyName
                value: string
              - name: iconImageName
                value: string
              - name: rawIcon
                value: string
              - name: rawPng
                value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>msix_packages</code> resource.

```sql
/*+ update */
UPDATE azure.desktop_virtualization.msix_packages
SET 
properties = '{{ properties }}'
WHERE 
hostPoolName = '{{ hostPoolName }}'
AND msixPackageFullName = '{{ msixPackageFullName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>msix_packages</code> resource.

```sql
/*+ delete */
DELETE FROM azure.desktop_virtualization.msix_packages
WHERE hostPoolName = '{{ hostPoolName }}'
AND msixPackageFullName = '{{ msixPackageFullName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
