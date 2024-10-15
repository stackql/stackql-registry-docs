---
title: aml_filesystems
hide_title: false
hide_table_of_contents: false
keywords:
  - aml_filesystems
  - storage_cache
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

Creates, updates, deletes, gets or lists a <code>aml_filesystems</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>aml_filesystems</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_cache.aml_filesystems" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed Identity properties. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of the AML file system. |
| <CopyableCode code="sku" /> | `object` | SKU for the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="zones" /> | `array` | Availability zones for resources. This field should only contain a single element in the array. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="amlFilesystemName, resourceGroupName, subscriptionId" /> | Returns an AML file system. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Returns all AML file systems the user has access to under a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Returns all AML file systems the user has access to under a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="amlFilesystemName, resourceGroupName, subscriptionId" /> | Create or update an AML file system. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="amlFilesystemName, resourceGroupName, subscriptionId" /> | Schedules an AML file system for deletion. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="amlFilesystemName, resourceGroupName, subscriptionId" /> | Update an AML file system instance. |
| <CopyableCode code="archive" /> | `EXEC` | <CopyableCode code="amlFilesystemName, resourceGroupName, subscriptionId" /> | Archive data from the AML file system. |
| <CopyableCode code="cancel_archive" /> | `EXEC` | <CopyableCode code="amlFilesystemName, resourceGroupName, subscriptionId" /> | Cancel archiving data from the AML file system. |

## `SELECT` examples

Returns all AML file systems the user has access to under a subscription.


```sql
SELECT
identity,
location,
properties,
sku,
tags,
zones
FROM azure.storage_cache.aml_filesystems
WHERE subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>aml_filesystems</code> resource.

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
INSERT INTO azure.storage_cache.aml_filesystems (
amlFilesystemName,
resourceGroupName,
subscriptionId,
tags,
location,
identity,
sku,
zones,
properties
)
SELECT 
'{{ amlFilesystemName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ tags }}',
'{{ location }}',
'{{ identity }}',
'{{ sku }}',
'{{ zones }}',
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
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: string
        - name: userAssignedIdentities
          value: []
    - name: sku
      value:
        - name: name
          value: string
    - name: zones
      value:
        - string
    - name: properties
      value:
        - name: storageCapacityTiB
          value: number
        - name: health
          value:
            - name: state
              value: string
            - name: statusCode
              value: string
            - name: statusDescription
              value: string
        - name: provisioningState
          value: string
        - name: filesystemSubnet
          value: []
        - name: clientInfo
          value:
            - name: mgsAddress
              value: string
            - name: mountCommand
              value: string
            - name: lustreVersion
              value: string
            - name: containerStorageInterface
              value:
                - name: persistentVolumeClaim
                  value: string
                - name: persistentVolume
                  value: string
                - name: storageClass
                  value: string
        - name: throughputProvisionedMBps
          value: integer
        - name: encryptionSettings
          value:
            - name: keyEncryptionKey
              value:
                - name: keyUrl
                  value: string
                - name: sourceVault
                  value:
                    - name: id
                      value: string
        - name: maintenanceWindow
          value:
            - name: dayOfWeek
              value: string
            - name: timeOfDayUTC
              value: string
        - name: hsm
          value:
            - name: settings
              value:
                - name: importPrefix
                  value: string
                - name: importPrefixesInitial
                  value:
                    - string
            - name: archiveStatus
              value:
                - - name: filesystemPath
                    value: string
                  - name: status
                    value:
                      - name: state
                        value: string
                      - name: lastCompletionTime
                        value: string
                      - name: lastStartedTime
                        value: string
                      - name: percentComplete
                        value: integer
                      - name: errorCode
                        value: string
                      - name: errorMessage
                        value: string
        - name: rootSquashSettings
          value:
            - name: mode
              value: string
            - name: noSquashNidLists
              value: string
            - name: squashUID
              value: integer
            - name: squashGID
              value: integer
            - name: status
              value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>aml_filesystems</code> resource.

```sql
/*+ update */
UPDATE azure.storage_cache.aml_filesystems
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
amlFilesystemName = '{{ amlFilesystemName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>aml_filesystems</code> resource.

```sql
/*+ delete */
DELETE FROM azure.storage_cache.aml_filesystems
WHERE amlFilesystemName = '{{ amlFilesystemName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
