---
title: image_imports
hide_title: false
hide_table_of_contents: false
keywords:
  - image_imports
  - vmmigration
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

Creates, updates, deletes, gets or lists a <code>image_imports</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>image_imports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.vmmigration.image_imports" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource path of the ImageImport. |
| <CopyableCode code="cloudStorageUri" /> | `string` | Immutable. The path to the Cloud Storage file from which the image should be imported. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time the image import was created. |
| <CopyableCode code="diskImageTargetDefaults" /> | `object` | The target details of the image resource that will be created by the import job. |
| <CopyableCode code="encryption" /> | `object` | Encryption message describes the details of the applied encryption. |
| <CopyableCode code="machineImageTargetDefaults" /> | `object` | The target details of the machine image resource that will be created by the image import job. |
| <CopyableCode code="recentImageImportJobs" /> | `array` | Output only. The result of the most recent runs for this ImageImport. All jobs for this ImageImport can be listed via ListImageImportJobs. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="imageImportsId, locationsId, projectsId" /> | Gets details of a single ImageImport. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists ImageImports in a given project. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new ImageImport in a given project. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="imageImportsId, locationsId, projectsId" /> | Deletes a single ImageImport. |

## `SELECT` examples

Lists ImageImports in a given project.

```sql
SELECT
name,
cloudStorageUri,
createTime,
diskImageTargetDefaults,
encryption,
machineImageTargetDefaults,
recentImageImportJobs
FROM google.vmmigration.image_imports
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>image_imports</code> resource.

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
INSERT INTO google.vmmigration.image_imports (
locationsId,
projectsId,
cloudStorageUri,
diskImageTargetDefaults,
machineImageTargetDefaults,
encryption
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ cloudStorageUri }}',
'{{ diskImageTargetDefaults }}',
'{{ machineImageTargetDefaults }}',
'{{ encryption }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: cloudStorageUri
      value: string
    - name: diskImageTargetDefaults
      value:
        - name: osAdaptationParameters
          value:
            - name: generalize
              value: boolean
            - name: licenseType
              value: string
        - name: dataDiskImageImport
          value: []
        - name: imageName
          value: string
        - name: targetProject
          value: string
        - name: description
          value: string
        - name: familyName
          value: string
        - name: labels
          value: object
        - name: additionalLicenses
          value:
            - string
        - name: singleRegionStorage
          value: boolean
        - name: encryption
          value:
            - name: kmsKey
              value: string
    - name: machineImageTargetDefaults
      value:
        - name: skipOsAdaptation
          value: []
        - name: machineImageName
          value: string
        - name: targetProject
          value: string
        - name: description
          value: string
        - name: singleRegionStorage
          value: boolean
        - name: machineImageParametersOverrides
          value:
            - name: machineType
              value: string
        - name: serviceAccount
          value:
            - name: email
              value: string
            - name: scopes
              value:
                - string
        - name: additionalLicenses
          value:
            - string
        - name: labels
          value: object
        - name: tags
          value:
            - string
        - name: shieldedInstanceConfig
          value:
            - name: secureBoot
              value: string
            - name: enableVtpm
              value: boolean
            - name: enableIntegrityMonitoring
              value: boolean
        - name: networkInterfaces
          value:
            - - name: network
                value: string
              - name: subnetwork
                value: string
              - name: internalIp
                value: string
              - name: externalIp
                value: string
              - name: networkTier
                value: string
    - name: name
      value: string
    - name: createTime
      value: string
    - name: recentImageImportJobs
      value:
        - - name: cloudStorageUri
            value: string
          - name: name
            value: string
          - name: createdResources
            value:
              - string
          - name: state
            value: string
          - name: createTime
            value: string
          - name: endTime
            value: string
          - name: errors
            value:
              - - name: code
                  value: integer
                - name: message
                  value: string
                - name: details
                  value:
                    - object
          - name: warnings
            value:
              - - name: code
                  value: string
                - name: warningMessage
                  value:
                    - name: locale
                      value: string
                    - name: message
                      value: string
                - name: helpLinks
                  value:
                    - - name: description
                        value: string
                      - name: url
                        value: string
                - name: warningTime
                  value: string
          - name: steps
            value:
              - - name: initializing
                  value: []
                - name: loadingSourceFiles
                  value: []
                - name: adaptingOs
                  value: []
                - name: creatingImage
                  value: []
                - name: startTime
                  value: string
                - name: endTime
                  value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>image_imports</code> resource.

```sql
/*+ delete */
DELETE FROM google.vmmigration.image_imports
WHERE imageImportsId = '{{ imageImportsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
