---
title: virtual_machine_extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_extensions
  - compute
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

Creates, updates, deletes, gets or lists a <code>virtual_machine_extensions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_machine_extensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.virtual_machine_extensions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_machine_extensions', value: 'view', },
        { label: 'virtual_machine_extensions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="auto_upgrade_minor_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_automatic_upgrade" /> | `text` | field from the `properties` object |
| <CopyableCode code="force_update_tag" /> | `text` | field from the `properties` object |
| <CopyableCode code="instance_view" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location |
| <CopyableCode code="protected_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="protected_settings_from_key_vault" /> | `text` | field from the `properties` object |
| <CopyableCode code="provision_after_extensions" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisher" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="suppress_failures" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags |
| <CopyableCode code="type" /> | `text` | Resource type |
| <CopyableCode code="type_handler_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="vmExtensionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="vmName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a Virtual Machine Extension. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vmExtensionName, vmName" /> | The operation to get the extension. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | The operation to get all extensions of a Virtual Machine. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, vmExtensionName, vmName" /> | The operation to create or update the extension. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, vmExtensionName, vmName" /> | The operation to delete the extension. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, subscriptionId, vmExtensionName, vmName" /> | The operation to update the extension. |

## `SELECT` examples

The operation to get all extensions of a Virtual Machine.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_machine_extensions', value: 'view', },
        { label: 'virtual_machine_extensions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
auto_upgrade_minor_version,
enable_automatic_upgrade,
force_update_tag,
instance_view,
location,
protected_settings,
protected_settings_from_key_vault,
provision_after_extensions,
provisioning_state,
publisher,
resourceGroupName,
settings,
subscriptionId,
suppress_failures,
tags,
type,
type_handler_version,
vmExtensionName,
vmName
FROM azure.compute.vw_virtual_machine_extensions
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vmName = '{{ vmName }}';
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
FROM azure.compute.virtual_machine_extensions
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vmName = '{{ vmName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>virtual_machine_extensions</code> resource.

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
INSERT INTO azure.compute.virtual_machine_extensions (
resourceGroupName,
subscriptionId,
vmExtensionName,
vmName,
properties,
location,
tags
)
SELECT 
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ vmExtensionName }}',
'{{ vmName }}',
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
        - name: forceUpdateTag
          value: string
        - name: publisher
          value: string
        - name: type
          value: string
        - name: typeHandlerVersion
          value: string
        - name: autoUpgradeMinorVersion
          value: boolean
        - name: enableAutomaticUpgrade
          value: boolean
        - name: settings
          value: object
        - name: protectedSettings
          value: object
        - name: provisioningState
          value: string
        - name: instanceView
          value:
            - name: name
              value: string
            - name: type
              value: string
            - name: typeHandlerVersion
              value: string
            - name: substatuses
              value:
                - - name: code
                    value: string
                  - name: level
                    value: string
                  - name: displayStatus
                    value: string
                  - name: message
                    value: string
                  - name: time
                    value: string
            - name: statuses
              value:
                - - name: code
                    value: string
                  - name: level
                    value: string
                  - name: displayStatus
                    value: string
                  - name: message
                    value: string
                  - name: time
                    value: string
        - name: suppressFailures
          value: boolean
        - name: protectedSettingsFromKeyVault
          value:
            - name: secretUrl
              value: string
            - name: sourceVault
              value:
                - name: id
                  value: string
        - name: provisionAfterExtensions
          value:
            - string
    - name: location
      value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>virtual_machine_extensions</code> resource.

```sql
/*+ update */
UPDATE azure.compute.virtual_machine_extensions
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vmExtensionName = '{{ vmExtensionName }}'
AND vmName = '{{ vmName }}';
```

## `DELETE` example

Deletes the specified <code>virtual_machine_extensions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.compute.virtual_machine_extensions
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vmExtensionName = '{{ vmExtensionName }}'
AND vmName = '{{ vmName }}';
```
