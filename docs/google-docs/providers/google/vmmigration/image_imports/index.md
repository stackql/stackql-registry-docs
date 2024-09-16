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
      value: '{{ cloudStorageUri }}'
    - name: diskImageTargetDefaults
      value:
        - name: osAdaptationParameters
          value:
            - name: generalize
              value: '{{ generalize }}'
            - name: licenseType
              value: '{{ licenseType }}'
        - name: dataDiskImageImport
          value: []
        - name: imageName
          value: '{{ imageName }}'
        - name: targetProject
          value: '{{ targetProject }}'
        - name: description
          value: '{{ description }}'
        - name: familyName
          value: '{{ familyName }}'
        - name: labels
          value: '{{ labels }}'
        - name: additionalLicenses
          value:
            - name: type
              value: '{{ type }}'
        - name: singleRegionStorage
          value: '{{ singleRegionStorage }}'
        - name: encryption
          value:
            - name: kmsKey
              value: '{{ kmsKey }}'
    - name: machineImageTargetDefaults
      value:
        - name: skipOsAdaptation
          value: []
        - name: machineImageName
          value: '{{ machineImageName }}'
        - name: targetProject
          value: '{{ targetProject }}'
        - name: description
          value: '{{ description }}'
        - name: singleRegionStorage
          value: '{{ singleRegionStorage }}'
        - name: machineImageParametersOverrides
          value:
            - name: machineType
              value: '{{ machineType }}'
        - name: serviceAccount
          value:
            - name: email
              value: '{{ email }}'
            - name: scopes
              value:
                - name: type
                  value: '{{ type }}'
        - name: additionalLicenses
          value:
            - name: type
              value: '{{ type }}'
        - name: labels
          value: '{{ labels }}'
        - name: tags
          value:
            - name: type
              value: '{{ type }}'
        - name: shieldedInstanceConfig
          value:
            - name: secureBoot
              value: '{{ secureBoot }}'
            - name: enableVtpm
              value: '{{ enableVtpm }}'
            - name: enableIntegrityMonitoring
              value: '{{ enableIntegrityMonitoring }}'
        - name: networkInterfaces
          value:
            - name: $ref
              value: '{{ $ref }}'

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
