---
title: region_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - region_instances
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

Creates, updates, deletes, gets or lists a <code>region_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>region_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.region_instances" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="bulk_insert" /> | `INSERT` | <CopyableCode code="project, region" /> | Creates multiple instances in a given region. Count specifies the number of instances to create. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>region_instances</code> resource.

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
INSERT INTO google.compute.region_instances (
project,
region,
count,
minCount,
namePattern,
perInstanceProperties,
sourceInstanceTemplate,
instanceProperties,
locationPolicy
)
SELECT 
'{{ project }}',
'{{ region }}',
'{{ count }}',
'{{ minCount }}',
'{{ namePattern }}',
'{{ perInstanceProperties }}',
'{{ sourceInstanceTemplate }}',
'{{ instanceProperties }}',
'{{ locationPolicy }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: count
      value: '{{ count }}'
    - name: minCount
      value: '{{ minCount }}'
    - name: namePattern
      value: '{{ namePattern }}'
    - name: perInstanceProperties
      value: '{{ perInstanceProperties }}'
    - name: sourceInstanceTemplate
      value: '{{ sourceInstanceTemplate }}'
    - name: instanceProperties
      value:
        - name: description
          value: '{{ description }}'
        - name: tags
          value:
            - name: items
              value:
                - name: type
                  value: '{{ type }}'
            - name: fingerprint
              value: '{{ fingerprint }}'
        - name: resourceManagerTags
          value: '{{ resourceManagerTags }}'
        - name: machineType
          value: '{{ machineType }}'
        - name: canIpForward
          value: '{{ canIpForward }}'
        - name: networkInterfaces
          value:
            - name: $ref
              value: '{{ $ref }}'
        - name: disks
          value:
            - name: $ref
              value: '{{ $ref }}'
        - name: metadata
          value:
            - name: fingerprint
              value: '{{ fingerprint }}'
            - name: items
              value:
                - name: key
                  value: '{{ key }}'
                - name: value
                  value: '{{ value }}'
        - name: serviceAccounts
          value:
            - name: $ref
              value: '{{ $ref }}'
        - name: scheduling
          value:
            - name: onHostMaintenance
              value: '{{ onHostMaintenance }}'
            - name: automaticRestart
              value: '{{ automaticRestart }}'
            - name: preemptible
              value: '{{ preemptible }}'
            - name: nodeAffinities
              value:
                - name: $ref
                  value: '{{ $ref }}'
            - name: minNodeCpus
              value: '{{ minNodeCpus }}'
            - name: locationHint
              value: '{{ locationHint }}'
            - name: availabilityDomain
              value: '{{ availabilityDomain }}'
            - name: provisioningModel
              value: '{{ provisioningModel }}'
            - name: instanceTerminationAction
              value: '{{ instanceTerminationAction }}'
            - name: maxRunDuration
              value:
                - name: seconds
                  value: '{{ seconds }}'
                - name: nanos
                  value: '{{ nanos }}'
            - name: terminationTime
              value: '{{ terminationTime }}'
            - name: onInstanceStopAction
              value:
                - name: discardLocalSsd
                  value: '{{ discardLocalSsd }}'
        - name: labels
          value: '{{ labels }}'
        - name: guestAccelerators
          value:
            - name: $ref
              value: '{{ $ref }}'
        - name: minCpuPlatform
          value: '{{ minCpuPlatform }}'
        - name: reservationAffinity
          value:
            - name: consumeReservationType
              value: '{{ consumeReservationType }}'
            - name: key
              value: '{{ key }}'
            - name: values
              value:
                - name: type
                  value: '{{ type }}'
        - name: shieldedInstanceConfig
          value:
            - name: enableSecureBoot
              value: '{{ enableSecureBoot }}'
            - name: enableVtpm
              value: '{{ enableVtpm }}'
            - name: enableIntegrityMonitoring
              value: '{{ enableIntegrityMonitoring }}'
        - name: resourcePolicies
          value:
            - name: type
              value: '{{ type }}'
        - name: confidentialInstanceConfig
          value:
            - name: enableConfidentialCompute
              value: '{{ enableConfidentialCompute }}'
            - name: confidentialInstanceType
              value: '{{ confidentialInstanceType }}'
        - name: privateIpv6GoogleAccess
          value: '{{ privateIpv6GoogleAccess }}'
        - name: advancedMachineFeatures
          value:
            - name: enableNestedVirtualization
              value: '{{ enableNestedVirtualization }}'
            - name: threadsPerCore
              value: '{{ threadsPerCore }}'
            - name: visibleCoreCount
              value: '{{ visibleCoreCount }}'
            - name: enableUefiNetworking
              value: '{{ enableUefiNetworking }}'
            - name: performanceMonitoringUnit
              value: '{{ performanceMonitoringUnit }}'
            - name: turboMode
              value: '{{ turboMode }}'
        - name: networkPerformanceConfig
          value:
            - name: totalEgressBandwidthTier
              value: '{{ totalEgressBandwidthTier }}'
        - name: keyRevocationActionType
          value: '{{ keyRevocationActionType }}'
    - name: locationPolicy
      value:
        - name: locations
          value: '{{ locations }}'
        - name: targetShape
          value: '{{ targetShape }}'

```
</TabItem>
</Tabs>
