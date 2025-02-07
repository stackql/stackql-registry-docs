---
title: region_commitments
hide_title: false
hide_table_of_contents: false
keywords:
  - region_commitments
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

Creates, updates, deletes, gets or lists a <code>region_commitments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>region_commitments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.region_commitments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| <CopyableCode code="name" /> | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| <CopyableCode code="description" /> | `string` | An optional description of this resource. Provide this property when you create the resource. |
| <CopyableCode code="autoRenew" /> | `boolean` | Specifies whether to enable automatic renewal for the commitment. The default value is false if not specified. The field can be updated until the day of the commitment expiration at 12:00am PST. If the field is set to true, the commitment will be automatically renewed for either one or three years according to the terms of the existing commitment. |
| <CopyableCode code="category" /> | `string` | The category of the commitment. Category MACHINE specifies commitments composed of machine resources such as VCPU or MEMORY, listed in resources. Category LICENSE specifies commitments composed of software licenses, listed in licenseResources. Note that only MACHINE commitments should have a Type specified. |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| <CopyableCode code="endTimestamp" /> | `string` | [Output Only] Commitment end time in RFC3339 text format. |
| <CopyableCode code="existingReservations" /> | `array` | Specifies the already existing reservations to attach to the Commitment. This field is optional, and it can be a full or partial URL. For example, the following are valid URLs to an reservation: - https://www.googleapis.com/compute/v1/projects/project/zones/zone /reservations/reservation - projects/project/zones/zone/reservations/reservation  |
| <CopyableCode code="kind" /> | `string` | [Output Only] Type of the resource. Always compute#commitment for commitments. |
| <CopyableCode code="licenseResource" /> | `object` | Commitment for a particular license resource. |
| <CopyableCode code="mergeSourceCommitments" /> | `array` | List of source commitments to be merged into a new commitment. |
| <CopyableCode code="plan" /> | `string` | The plan for this commitment, which determines duration and discount rate. The currently supported plans are TWELVE_MONTH (1 year), and THIRTY_SIX_MONTH (3 years). |
| <CopyableCode code="region" /> | `string` | [Output Only] URL of the region where this commitment may be used. |
| <CopyableCode code="reservations" /> | `array` | List of create-on-create reservations for this commitment. |
| <CopyableCode code="resources" /> | `array` | A list of commitment amounts for particular resources. Note that VCPU and MEMORY resource commitments must occur together. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined URL for the resource. |
| <CopyableCode code="splitSourceCommitment" /> | `string` | Source commitment to be split into a new commitment. |
| <CopyableCode code="startTimestamp" /> | `string` | [Output Only] Commitment start time in RFC3339 text format. |
| <CopyableCode code="status" /> | `string` | [Output Only] Status of the commitment with regards to eventual expiration (each commitment has an end date defined). One of the following values: NOT_YET_ACTIVE, ACTIVE, EXPIRED. |
| <CopyableCode code="statusMessage" /> | `string` | [Output Only] An optional, human-readable explanation of the status. |
| <CopyableCode code="type" /> | `string` | The type of commitment, which affects the discount rate and the eligible resources. Type MEMORY_OPTIMIZED specifies a commitment that will only apply to memory optimized machines. Type ACCELERATOR_OPTIMIZED specifies a commitment that will only apply to accelerator optimized machines. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="aggregated_list" /> | `SELECT` | <CopyableCode code="project" /> | Retrieves an aggregated list of commitments by region. To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`. |
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="commitment, project, region" /> | Returns the specified commitment resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project, region" /> | Retrieves a list of commitments contained within the specified region. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="project, region" /> | Creates a commitment in the specified project using the data included in the request. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="commitment, project, region" /> | Updates the specified commitment with the data included in the request. Update is performed only on selected fields included as part of update-mask. Only the following fields can be modified: auto_renew. |

## `SELECT` examples

Retrieves an aggregated list of commitments by region. To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

```sql
SELECT
id,
name,
description,
autoRenew,
category,
creationTimestamp,
endTimestamp,
existingReservations,
kind,
licenseResource,
mergeSourceCommitments,
plan,
region,
reservations,
resources,
selfLink,
splitSourceCommitment,
startTimestamp,
status,
statusMessage,
type
FROM google.compute.region_commitments
WHERE project = '{{ project }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>region_commitments</code> resource.

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
INSERT INTO google.compute.region_commitments (
project,
region,
name,
description,
region,
status,
statusMessage,
plan,
startTimestamp,
endTimestamp,
resources,
type,
reservations,
category,
licenseResource,
autoRenew,
mergeSourceCommitments,
splitSourceCommitment,
existingReservations
)
SELECT 
'{{ project }}',
'{{ region }}',
'{{ name }}',
'{{ description }}',
'{{ region }}',
'{{ status }}',
'{{ statusMessage }}',
'{{ plan }}',
'{{ startTimestamp }}',
'{{ endTimestamp }}',
'{{ resources }}',
'{{ type }}',
'{{ reservations }}',
'{{ category }}',
'{{ licenseResource }}',
{{ autoRenew }},
'{{ mergeSourceCommitments }}',
'{{ splitSourceCommitment }}',
'{{ existingReservations }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: kind
      value: string
    - name: id
      value: string
    - name: creationTimestamp
      value: string
    - name: name
      value: string
    - name: description
      value: string
    - name: region
      value: string
    - name: selfLink
      value: string
    - name: status
      value: string
    - name: statusMessage
      value: string
    - name: plan
      value: string
    - name: startTimestamp
      value: string
    - name: endTimestamp
      value: string
    - name: resources
      value:
        - - name: type
            value: string
          - name: amount
            value: string
          - name: acceleratorType
            value: string
    - name: type
      value: string
    - name: reservations
      value:
        - - name: kind
            value: string
          - name: id
            value: string
          - name: creationTimestamp
            value: string
          - name: selfLink
            value: string
          - name: zone
            value: string
          - name: description
            value: string
          - name: name
            value: string
          - name: specificReservation
            value:
              - name: instanceProperties
                value:
                  - name: machineType
                    value: string
                  - name: guestAccelerators
                    value:
                      - - name: acceleratorType
                          value: string
                        - name: acceleratorCount
                          value: integer
                  - name: minCpuPlatform
                    value: string
                  - name: localSsds
                    value:
                      - - name: diskSizeGb
                          value: string
                        - name: interface
                          value: string
                  - name: locationHint
                    value: string
              - name: count
                value: string
              - name: inUseCount
                value: string
              - name: assuredCount
                value: string
              - name: sourceInstanceTemplate
                value: string
          - name: aggregateReservation
            value:
              - name: vmFamily
                value: string
              - name: reservedResources
                value:
                  - - name: accelerator
                      value:
                        - name: acceleratorCount
                          value: integer
                        - name: acceleratorType
                          value: string
              - name: inUseResources
                value:
                  - []
              - name: workloadType
                value: string
          - name: commitment
            value: string
          - name: specificReservationRequired
            value: boolean
          - name: status
            value: string
          - name: shareSettings
            value:
              - name: shareType
                value: string
              - name: projectMap
                value: object
          - name: satisfiesPzs
            value: boolean
          - name: resourcePolicies
            value: object
          - name: resourceStatus
            value:
              - name: specificSkuAllocation
                value:
                  - name: sourceInstanceTemplateId
                    value: string
    - name: category
      value: string
    - name: licenseResource
      value:
        - name: license
          value: string
        - name: amount
          value: string
        - name: coresPerLicense
          value: string
    - name: autoRenew
      value: boolean
    - name: mergeSourceCommitments
      value:
        - string
    - name: splitSourceCommitment
      value: string
    - name: existingReservations
      value:
        - string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>region_commitments</code> resource.

```sql
/*+ update */
UPDATE google.compute.region_commitments
SET 
name = '{{ name }}',
description = '{{ description }}',
region = '{{ region }}',
status = '{{ status }}',
statusMessage = '{{ statusMessage }}',
plan = '{{ plan }}',
startTimestamp = '{{ startTimestamp }}',
endTimestamp = '{{ endTimestamp }}',
resources = '{{ resources }}',
type = '{{ type }}',
reservations = '{{ reservations }}',
category = '{{ category }}',
licenseResource = '{{ licenseResource }}',
autoRenew = true|false,
mergeSourceCommitments = '{{ mergeSourceCommitments }}',
splitSourceCommitment = '{{ splitSourceCommitment }}',
existingReservations = '{{ existingReservations }}'
WHERE 
commitment = '{{ commitment }}'
AND project = '{{ project }}'
AND region = '{{ region }}';
```
