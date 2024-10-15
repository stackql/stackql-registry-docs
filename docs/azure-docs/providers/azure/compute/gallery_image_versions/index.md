---
title: gallery_image_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - gallery_image_versions
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

Creates, updates, deletes, gets or lists a <code>gallery_image_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gallery_image_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.gallery_image_versions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_gallery_image_versions', value: 'view', },
        { label: 'gallery_image_versions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="galleryImageName" /> | `text` | field from the `properties` object |
| <CopyableCode code="galleryImageVersionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="galleryName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="publishing_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="replication_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="safety_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="security_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_profile" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="galleryImageName, galleryImageVersionName, galleryName, resourceGroupName, subscriptionId" /> | Retrieves information about a gallery image version. |
| <CopyableCode code="list_by_gallery_image" /> | `SELECT` | <CopyableCode code="galleryImageName, galleryName, resourceGroupName, subscriptionId" /> | List gallery image versions in a gallery image definition. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="galleryImageName, galleryImageVersionName, galleryName, resourceGroupName, subscriptionId" /> | Create or update a gallery image version. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="galleryImageName, galleryImageVersionName, galleryName, resourceGroupName, subscriptionId" /> | Delete a gallery image version. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="galleryImageName, galleryImageVersionName, galleryName, resourceGroupName, subscriptionId" /> | Update a gallery image version. |

## `SELECT` examples

List gallery image versions in a gallery image definition.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_gallery_image_versions', value: 'view', },
        { label: 'gallery_image_versions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
galleryImageName,
galleryImageVersionName,
galleryName,
location,
provisioning_state,
publishing_profile,
replication_status,
resourceGroupName,
safety_profile,
security_profile,
storage_profile,
subscriptionId,
tags,
type
FROM azure.compute.vw_gallery_image_versions
WHERE galleryImageName = '{{ galleryImageName }}'
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
FROM azure.compute.gallery_image_versions
WHERE galleryImageName = '{{ galleryImageName }}'
AND galleryName = '{{ galleryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>gallery_image_versions</code> resource.

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
INSERT INTO azure.compute.gallery_image_versions (
galleryImageName,
galleryImageVersionName,
galleryName,
resourceGroupName,
subscriptionId,
properties,
location,
tags
)
SELECT 
'{{ galleryImageName }}',
'{{ galleryImageVersionName }}',
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
        - name: provisioningState
          value: []
        - name: storageProfile
          value:
            - name: source
              value:
                - name: communityGalleryImageId
                  value: string
                - name: virtualMachineId
                  value: string
                - name: id
                  value: string
            - name: osDiskImage
              value:
                - name: sizeInGB
                  value: integer
                - name: hostCaching
                  value: string
                - name: source
                  value:
                    - name: uri
                      value: string
                    - name: storageAccountId
                      value: string
                    - name: id
                      value: string
            - name: dataDiskImages
              value:
                - - name: lun
                    value: integer
                  - name: sizeInGB
                    value: integer
                  - name: hostCaching
                    value: string
        - name: safetyProfile
          value:
            - name: reportedForPolicyViolation
              value: boolean
            - name: policyViolations
              value:
                - - name: category
                    value: string
                  - name: details
                    value: string
            - name: allowDeletionOfReplicatedLocations
              value: boolean
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
        - name: securityProfile
          value:
            - name: uefiSettings
              value:
                - name: signatureTemplateNames
                  value:
                    - []
                - name: additionalSignatures
                  value:
                    - name: pk
                      value:
                        - name: type
                          value: string
                        - name: value
                          value:
                            - string
                    - name: kek
                      value:
                        - - name: type
                            value: string
                          - name: value
                            value:
                              - string
                    - name: db
                      value:
                        - - name: type
                            value: string
                          - name: value
                            value:
                              - string
                    - name: dbx
                      value:
                        - - name: type
                            value: string
                          - name: value
                            value:
                              - string
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

Updates a <code>gallery_image_versions</code> resource.

```sql
/*+ update */
UPDATE azure.compute.gallery_image_versions
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
galleryImageName = '{{ galleryImageName }}'
AND galleryImageVersionName = '{{ galleryImageVersionName }}'
AND galleryName = '{{ galleryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>gallery_image_versions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.compute.gallery_image_versions
WHERE galleryImageName = '{{ galleryImageName }}'
AND galleryImageVersionName = '{{ galleryImageVersionName }}'
AND galleryName = '{{ galleryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
