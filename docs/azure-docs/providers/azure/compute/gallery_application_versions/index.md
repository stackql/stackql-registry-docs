---
title: gallery_application_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - gallery_application_versions
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

Creates, updates, deletes, gets or lists a <code>gallery_application_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gallery_application_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.gallery_application_versions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_gallery_application_versions', value: 'view', },
        { label: 'gallery_application_versions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="galleryApplicationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="galleryApplicationVersionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="galleryName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="publishing_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="replication_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="safety_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags |
| <CopyableCode code="type" /> | `text` | Resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a gallery image version. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="galleryApplicationName, galleryApplicationVersionName, galleryName, resourceGroupName, subscriptionId" /> | Retrieves information about a gallery Application Version. |
| <CopyableCode code="list_by_gallery_application" /> | `SELECT` | <CopyableCode code="galleryApplicationName, galleryName, resourceGroupName, subscriptionId" /> | List gallery Application Versions in a gallery Application Definition. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="galleryApplicationName, galleryApplicationVersionName, galleryName, resourceGroupName, subscriptionId" /> | Create or update a gallery Application Version. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="galleryApplicationName, galleryApplicationVersionName, galleryName, resourceGroupName, subscriptionId" /> | Delete a gallery Application Version. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="galleryApplicationName, galleryApplicationVersionName, galleryName, resourceGroupName, subscriptionId" /> | Update a gallery Application Version. |

## `SELECT` examples

List gallery Application Versions in a gallery Application Definition.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_gallery_application_versions', value: 'view', },
        { label: 'gallery_application_versions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
galleryApplicationName,
galleryApplicationVersionName,
galleryName,
location,
provisioning_state,
publishing_profile,
replication_status,
resourceGroupName,
safety_profile,
subscriptionId,
tags,
type
FROM azure.compute.vw_gallery_application_versions
WHERE galleryApplicationName = '{{ galleryApplicationName }}'
AND galleryName = '{{ galleryName }}'
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
FROM azure.compute.gallery_application_versions
WHERE galleryApplicationName = '{{ galleryApplicationName }}'
AND galleryName = '{{ galleryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>gallery_application_versions</code> resource.

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
INSERT INTO azure.compute.gallery_application_versions (
galleryApplicationName,
galleryApplicationVersionName,
galleryName,
resourceGroupName,
subscriptionId,
properties,
location,
tags
)
SELECT 
'{{ galleryApplicationName }}',
'{{ galleryApplicationVersionName }}',
'{{ galleryName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
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
        - name: publishingProfile
          value:
            - name: source
              value:
                - name: mediaLink
                  value: string
                - name: defaultConfigurationLink
                  value: string
            - name: manageActions
              value:
                - name: install
                  value: string
                - name: remove
                  value: string
                - name: update
                  value: string
            - name: settings
              value:
                - name: packageFileName
                  value: string
                - name: configFileName
                  value: string
            - name: advancedSettings
              value: object
            - name: enableHealthCheck
              value: boolean
            - name: customActions
              value:
                - - name: name
                    value: string
                  - name: script
                    value: string
                  - name: description
                    value: string
                  - name: parameters
                    value:
                      - - name: name
                          value: string
                        - name: required
                          value: boolean
                        - name: type
                          value: string
                        - name: defaultValue
                          value: string
                        - name: description
                          value: string
            - name: targetRegions
              value:
                - - name: name
                    value: string
                  - name: regionalReplicaCount
                    value: integer
                  - name: storageAccountType
                    value: string
                  - name: encryption
                    value:
                      - name: osDiskImage
                        value:
                          - name: securityProfile
                            value:
                              - name: confidentialVMEncryptionType
                                value: string
                              - name: secureVMDiskEncryptionSetId
                                value: string
                          - name: diskEncryptionSetId
                            value: string
                      - name: dataDiskImages
                        value:
                          - - name: lun
                              value: integer
                            - name: diskEncryptionSetId
                              value: string
                  - name: excludeFromLatest
                    value: boolean
            - name: replicaCount
              value: integer
            - name: excludeFromLatest
              value: boolean
            - name: publishedDate
              value: string
            - name: endOfLifeDate
              value: string
            - name: storageAccountType
              value: string
            - name: replicationMode
              value: string
            - name: targetExtendedLocations
              value:
                - - name: name
                    value: string
                  - name: extendedLocation
                    value:
                      - name: name
                        value: string
                      - name: type
                        value: []
                  - name: extendedLocationReplicaCount
                    value: integer
                  - name: storageAccountType
                    value: string
        - name: safetyProfile
          value:
            - name: allowDeletionOfReplicatedLocations
              value: boolean
        - name: provisioningState
          value: []
        - name: replicationStatus
          value:
            - name: aggregatedState
              value: string
            - name: summary
              value:
                - - name: region
                    value: string
                  - name: state
                    value: string
                  - name: details
                    value: string
                  - name: progress
                    value: integer
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

## `UPDATE` example

Updates a <code>gallery_application_versions</code> resource.

```sql
/*+ update */
UPDATE azure.compute.gallery_application_versions
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
galleryApplicationName = '{{ galleryApplicationName }}'
AND galleryApplicationVersionName = '{{ galleryApplicationVersionName }}'
AND galleryName = '{{ galleryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>gallery_application_versions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.compute.gallery_application_versions
WHERE galleryApplicationName = '{{ galleryApplicationName }}'
AND galleryApplicationVersionName = '{{ galleryApplicationVersionName }}'
AND galleryName = '{{ galleryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
