---
title: cloud_exadata_infrastructures
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_exadata_infrastructures
  - oracledatabase
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

Creates, updates, deletes, gets or lists a <code>cloud_exadata_infrastructures</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cloud_exadata_infrastructures</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.oracledatabase.cloud_exadata_infrastructures" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The name of the Exadata Infrastructure resource with the format: projects/{project}/locations/{region}/cloudExadataInfrastructures/{cloud_exadata_infrastructure} |
| <CopyableCode code="createTime" /> | `string` | Output only. The date and time that the Exadata Infrastructure was created. |
| <CopyableCode code="displayName" /> | `string` | Optional. User friendly name for this resource. |
| <CopyableCode code="entitlementId" /> | `string` | Output only. Entitlement ID of the private offer against which this infrastructure resource is provisioned. |
| <CopyableCode code="gcpOracleZone" /> | `string` | Optional. GCP location where Oracle Exadata is hosted. |
| <CopyableCode code="labels" /> | `object` | Optional. Labels or tags associated with the resource. |
| <CopyableCode code="properties" /> | `object` | Various properties of Exadata Infrastructure. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cloudExadataInfrastructuresId, locationsId, projectsId" /> | Gets details of a single Exadata Infrastructure. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists Exadata Infrastructures in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new Exadata Infrastructure in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="cloudExadataInfrastructuresId, locationsId, projectsId" /> | Deletes a single Exadata Infrastructure. |

## `SELECT` examples

Lists Exadata Infrastructures in a given project and location.

```sql
SELECT
name,
createTime,
displayName,
entitlementId,
gcpOracleZone,
labels,
properties
FROM google.oracledatabase.cloud_exadata_infrastructures
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>cloud_exadata_infrastructures</code> resource.

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
INSERT INTO google.oracledatabase.cloud_exadata_infrastructures (
locationsId,
projectsId,
name,
displayName,
gcpOracleZone,
properties,
labels
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ displayName }}',
'{{ gcpOracleZone }}',
'{{ properties }}',
'{{ labels }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: displayName
      value: string
    - name: gcpOracleZone
      value: string
    - name: entitlementId
      value: string
    - name: properties
      value:
        - name: ocid
          value: string
        - name: computeCount
          value: integer
        - name: storageCount
          value: integer
        - name: totalStorageSizeGb
          value: integer
        - name: availableStorageSizeGb
          value: integer
        - name: maintenanceWindow
          value:
            - name: preference
              value: string
            - name: months
              value:
                - string
            - name: weeksOfMonth
              value:
                - integer
            - name: daysOfWeek
              value:
                - string
            - name: hoursOfDay
              value:
                - integer
            - name: leadTimeWeek
              value: integer
            - name: patchingMode
              value: string
            - name: customActionTimeoutMins
              value: integer
            - name: isCustomActionTimeoutEnabled
              value: boolean
        - name: state
          value: string
        - name: shape
          value: string
        - name: ociUrl
          value: string
        - name: cpuCount
          value: integer
        - name: maxCpuCount
          value: integer
        - name: memorySizeGb
          value: integer
        - name: maxMemoryGb
          value: integer
        - name: dbNodeStorageSizeGb
          value: integer
        - name: maxDbNodeStorageSizeGb
          value: integer
        - name: dataStorageSizeTb
          value: number
        - name: maxDataStorageTb
          value: number
        - name: activatedStorageCount
          value: integer
        - name: additionalStorageCount
          value: integer
        - name: dbServerVersion
          value: string
        - name: storageServerVersion
          value: string
        - name: nextMaintenanceRunId
          value: string
        - name: nextMaintenanceRunTime
          value: string
        - name: nextSecurityMaintenanceRunTime
          value: string
        - name: customerContacts
          value:
            - - name: email
                value: string
        - name: monthlyStorageServerVersion
          value: string
        - name: monthlyDbServerVersion
          value: string
    - name: labels
      value: object
    - name: createTime
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>cloud_exadata_infrastructures</code> resource.

```sql
/*+ delete */
DELETE FROM google.oracledatabase.cloud_exadata_infrastructures
WHERE cloudExadataInfrastructuresId = '{{ cloudExadataInfrastructuresId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
