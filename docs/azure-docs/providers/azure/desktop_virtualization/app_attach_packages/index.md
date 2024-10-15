---
title: app_attach_packages
hide_title: false
hide_table_of_contents: false
keywords:
  - app_attach_packages
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

Creates, updates, deletes, gets or lists a <code>app_attach_packages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>app_attach_packages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.desktop_virtualization.app_attach_packages" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_app_attach_packages', value: 'view', },
        { label: 'app_attach_packages', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="appAttachPackageName" /> | `text` | field from the `properties` object |
| <CopyableCode code="custom_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="fail_health_check_on_staging_failure" /> | `text` | field from the `properties` object |
| <CopyableCode code="host_pool_references" /> | `text` | field from the `properties` object |
| <CopyableCode code="image" /> | `text` | field from the `properties` object |
| <CopyableCode code="key_vault_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="package_lookback_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="package_owner_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Schema for App Attach Package properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="appAttachPackageName, resourceGroupName, subscriptionId" /> | Get an app attach package. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List App Attach packages in resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List App Attach packages in subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="appAttachPackageName, resourceGroupName, subscriptionId, data__properties" /> | Create or update an App Attach package. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="appAttachPackageName, resourceGroupName, subscriptionId" /> | Remove an App Attach Package. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="appAttachPackageName, resourceGroupName, subscriptionId" /> | Update an App Attach Package |
| <CopyableCode code="import_info" /> | `EXEC` | <CopyableCode code="hostPoolName, resourceGroupName, subscriptionId" /> | Gets information from a package given the path to the package. |

## `SELECT` examples

List App Attach packages in subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_app_attach_packages', value: 'view', },
        { label: 'app_attach_packages', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
appAttachPackageName,
custom_data,
fail_health_check_on_staging_failure,
host_pool_references,
image,
key_vault_url,
location,
package_lookback_url,
package_owner_name,
provisioning_state,
resourceGroupName,
subscriptionId,
tags
FROM azure.desktop_virtualization.vw_app_attach_packages
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.desktop_virtualization.app_attach_packages
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>app_attach_packages</code> resource.

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
INSERT INTO azure.desktop_virtualization.app_attach_packages (
appAttachPackageName,
resourceGroupName,
subscriptionId,
data__properties,
tags,
location,
properties
)
SELECT 
'{{ appAttachPackageName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ tags }}',
'{{ location }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: tags
      value: object
    - name: location
      value: string
    - name: properties
      value:
        - name: provisioningState
          value: []
        - name: image
          value:
            - name: packageAlias
              value: string
            - name: imagePath
              value: string
            - name: packageName
              value: string
            - name: packageFamilyName
              value: string
            - name: packageFullName
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
            - name: certificateName
              value: string
            - name: certificateExpiry
              value: string
            - name: isPackageTimestamped
              value: string
        - name: hostPoolReferences
          value:
            - string
        - name: keyVaultURL
          value: string
        - name: failHealthCheckOnStagingFailure
          value: []
        - name: packageOwnerName
          value: string
        - name: packageLookbackUrl
          value: string
        - name: customData
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>app_attach_packages</code> resource.

```sql
/*+ update */
UPDATE azure.desktop_virtualization.app_attach_packages
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
appAttachPackageName = '{{ appAttachPackageName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>app_attach_packages</code> resource.

```sql
/*+ delete */
DELETE FROM azure.desktop_virtualization.app_attach_packages
WHERE appAttachPackageName = '{{ appAttachPackageName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
