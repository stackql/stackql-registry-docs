---
title: region_instance_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - region_instance_templates
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

Creates, updates, deletes, gets or lists a <code>region_instance_templates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>region_instance_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.region_instance_templates" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] A unique identifier for this instance template. The server defines this identifier. |
| <CopyableCode code="name" /> | `string` | Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| <CopyableCode code="description" /> | `string` | An optional description of this resource. Provide this property when you create the resource. |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] The creation timestamp for this instance template in RFC3339 text format. |
| <CopyableCode code="kind" /> | `string` | [Output Only] The resource type, which is always compute#instanceTemplate for instance templates. |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="region" /> | `string` | [Output Only] URL of the region where the instance template resides. Only applicable for regional resources. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] The URL for this instance template. The server defines this URL. |
| <CopyableCode code="sourceInstance" /> | `string` | The source instance used to create the template. You can provide this as a partial or full URL to the resource. For example, the following are valid values: - https://www.googleapis.com/compute/v1/projects/project/zones/zone /instances/instance - projects/project/zones/zone/instances/instance  |
| <CopyableCode code="sourceInstanceParams" /> | `object` | A specification of the parameters to use when creating the instance template from a source instance. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="instanceTemplate, project, region" /> | Returns the specified instance template. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project, region" /> | Retrieves a list of instance templates that are contained within the specified project and region. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="project, region" /> | Creates an instance template in the specified project and region using the global instance template whose URL is included in the request. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="instanceTemplate, project, region" /> | Deletes the specified instance template. Deleting an instance template is permanent and cannot be undone. |

## `SELECT` examples

Retrieves a list of instance templates that are contained within the specified project and region.

```sql
SELECT
id,
name,
description,
creationTimestamp,
kind,
properties,
region,
selfLink,
sourceInstance,
sourceInstanceParams
FROM google.compute.region_instance_templates
WHERE project = '{{ project }}'
AND region = '{{ region }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>region_instance_templates</code> resource.

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
INSERT INTO google.compute.region_instance_templates (
project,
region,
name,
description,
properties,
sourceInstance,
sourceInstanceParams,
region
)
SELECT 
'{{ project }}',
'{{ region }}',
'{{ name }}',
'{{ description }}',
'{{ properties }}',
'{{ sourceInstance }}',
'{{ sourceInstanceParams }}',
'{{ region }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: description
      value: '{{ description }}'
    - name: properties
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
    - name: sourceInstance
      value: '{{ sourceInstance }}'
    - name: sourceInstanceParams
      value:
        - name: diskConfigs
          value:
            - name: $ref
              value: '{{ $ref }}'
    - name: region
      value: '{{ region }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>region_instance_templates</code> resource.

```sql
/*+ delete */
DELETE FROM google.compute.region_instance_templates
WHERE instanceTemplate = '{{ instanceTemplate }}'
AND project = '{{ project }}'
AND region = '{{ region }}';
```
