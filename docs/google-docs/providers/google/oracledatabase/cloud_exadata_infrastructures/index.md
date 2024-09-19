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
name: string
displayName: string
gcpOracleZone: string
entitlementId: string
properties:
  ocid: string
  computeCount: integer
  storageCount: integer
  totalStorageSizeGb: integer
  availableStorageSizeGb: integer
  maintenanceWindow:
    preference: string
    months:
      - type: string
        enumDescriptions: string
        enum: string
    weeksOfMonth:
      - type: string
        format: string
    daysOfWeek:
      - type: string
        enumDescriptions: string
        enum: string
    hoursOfDay:
      - type: string
        format: string
    leadTimeWeek: integer
    patchingMode: string
    customActionTimeoutMins: integer
    isCustomActionTimeoutEnabled: boolean
  state: string
  shape: string
  ociUrl: string
  cpuCount: integer
  maxCpuCount: integer
  memorySizeGb: integer
  maxMemoryGb: integer
  dbNodeStorageSizeGb: integer
  maxDbNodeStorageSizeGb: integer
  dataStorageSizeTb: number
  maxDataStorageTb: number
  activatedStorageCount: integer
  additionalStorageCount: integer
  dbServerVersion: string
  storageServerVersion: string
  nextMaintenanceRunId: string
  nextMaintenanceRunTime: string
  nextSecurityMaintenanceRunTime: string
  customerContacts:
    - email: string
  monthlyStorageServerVersion: string
  monthlyDbServerVersion: string
labels: object
createTime: string

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
