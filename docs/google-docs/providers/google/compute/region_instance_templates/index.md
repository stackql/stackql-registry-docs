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
    - name: properties
      value:
        - name: description
          value: string
        - name: tags
          value:
            - name: items
              value:
                - string
            - name: fingerprint
              value: string
        - name: resourceManagerTags
          value: object
        - name: machineType
          value: string
        - name: canIpForward
          value: boolean
        - name: networkInterfaces
          value:
            - - name: kind
                value: string
              - name: network
                value: string
              - name: subnetwork
                value: string
              - name: networkIP
                value: string
              - name: ipv6Address
                value: string
              - name: internalIpv6PrefixLength
                value: integer
              - name: name
                value: string
              - name: accessConfigs
                value:
                  - - name: kind
                      value: string
                    - name: type
                      value: string
                    - name: name
                      value: string
                    - name: natIP
                      value: string
                    - name: externalIpv6
                      value: string
                    - name: externalIpv6PrefixLength
                      value: integer
                    - name: setPublicPtr
                      value: boolean
                    - name: publicPtrDomainName
                      value: string
                    - name: networkTier
                      value: string
                    - name: securityPolicy
                      value: string
              - name: ipv6AccessConfigs
                value:
                  - - name: kind
                      value: string
                    - name: type
                      value: string
                    - name: name
                      value: string
                    - name: natIP
                      value: string
                    - name: externalIpv6
                      value: string
                    - name: externalIpv6PrefixLength
                      value: integer
                    - name: setPublicPtr
                      value: boolean
                    - name: publicPtrDomainName
                      value: string
                    - name: networkTier
                      value: string
                    - name: securityPolicy
                      value: string
              - name: aliasIpRanges
                value:
                  - - name: ipCidrRange
                      value: string
                    - name: subnetworkRangeName
                      value: string
              - name: fingerprint
                value: string
              - name: stackType
                value: string
              - name: ipv6AccessType
                value: string
              - name: queueCount
                value: integer
              - name: nicType
                value: string
              - name: networkAttachment
                value: string
        - name: disks
          value:
            - - name: kind
                value: string
              - name: type
                value: string
              - name: mode
                value: string
              - name: savedState
                value: string
              - name: source
                value: string
              - name: deviceName
                value: string
              - name: index
                value: integer
              - name: boot
                value: boolean
              - name: initializeParams
                value:
                  - name: diskName
                    value: string
                  - name: sourceImage
                    value: string
                  - name: diskSizeGb
                    value: string
                  - name: diskType
                    value: string
                  - name: sourceImageEncryptionKey
                    value:
                      - name: rawKey
                        value: string
                      - name: rsaEncryptedKey
                        value: string
                      - name: kmsKeyName
                        value: string
                      - name: sha256
                        value: string
                      - name: kmsKeyServiceAccount
                        value: string
                  - name: labels
                    value: object
                  - name: sourceSnapshot
                    value: string
                  - name: description
                    value: string
                  - name: replicaZones
                    value:
                      - string
                  - name: resourcePolicies
                    value:
                      - string
                  - name: onUpdateAction
                    value: string
                  - name: provisionedIops
                    value: string
                  - name: licenses
                    value:
                      - string
                  - name: architecture
                    value: string
                  - name: resourceManagerTags
                    value: object
                  - name: provisionedThroughput
                    value: string
                  - name: enableConfidentialCompute
                    value: boolean
                  - name: storagePool
                    value: string
              - name: autoDelete
                value: boolean
              - name: licenses
                value:
                  - string
              - name: interface
                value: string
              - name: guestOsFeatures
                value:
                  - - name: type
                      value: string
              - name: diskSizeGb
                value: string
              - name: shieldedInstanceInitialState
                value:
                  - name: pk
                    value:
                      - name: content
                        value: string
                      - name: fileType
                        value: string
                  - name: keks
                    value:
                      - - name: content
                          value: string
                        - name: fileType
                          value: string
                  - name: dbs
                    value:
                      - - name: content
                          value: string
                        - name: fileType
                          value: string
                  - name: dbxs
                    value:
                      - - name: content
                          value: string
                        - name: fileType
                          value: string
              - name: forceAttach
                value: boolean
              - name: architecture
                value: string
        - name: metadata
          value:
            - name: kind
              value: string
            - name: fingerprint
              value: string
            - name: items
              value:
                - - name: key
                    value: string
                  - name: value
                    value: string
        - name: serviceAccounts
          value:
            - - name: email
                value: string
              - name: scopes
                value:
                  - string
        - name: scheduling
          value:
            - name: onHostMaintenance
              value: string
            - name: automaticRestart
              value: boolean
            - name: preemptible
              value: boolean
            - name: nodeAffinities
              value:
                - - name: key
                    value: string
                  - name: operator
                    value: string
                  - name: values
                    value:
                      - string
            - name: minNodeCpus
              value: integer
            - name: locationHint
              value: string
            - name: availabilityDomain
              value: integer
            - name: provisioningModel
              value: string
            - name: instanceTerminationAction
              value: string
            - name: maxRunDuration
              value:
                - name: seconds
                  value: string
                - name: nanos
                  value: integer
            - name: terminationTime
              value: string
            - name: onInstanceStopAction
              value:
                - name: discardLocalSsd
                  value: boolean
        - name: labels
          value: object
        - name: guestAccelerators
          value:
            - - name: acceleratorType
                value: string
              - name: acceleratorCount
                value: integer
        - name: minCpuPlatform
          value: string
        - name: reservationAffinity
          value:
            - name: consumeReservationType
              value: string
            - name: key
              value: string
            - name: values
              value:
                - string
        - name: shieldedInstanceConfig
          value:
            - name: enableSecureBoot
              value: boolean
            - name: enableVtpm
              value: boolean
            - name: enableIntegrityMonitoring
              value: boolean
        - name: resourcePolicies
          value:
            - string
        - name: confidentialInstanceConfig
          value:
            - name: enableConfidentialCompute
              value: boolean
            - name: confidentialInstanceType
              value: string
        - name: privateIpv6GoogleAccess
          value: string
        - name: advancedMachineFeatures
          value:
            - name: enableNestedVirtualization
              value: boolean
            - name: threadsPerCore
              value: integer
            - name: visibleCoreCount
              value: integer
            - name: enableUefiNetworking
              value: boolean
            - name: performanceMonitoringUnit
              value: string
            - name: turboMode
              value: string
        - name: networkPerformanceConfig
          value:
            - name: totalEgressBandwidthTier
              value: string
        - name: keyRevocationActionType
          value: string
    - name: selfLink
      value: string
    - name: sourceInstance
      value: string
    - name: sourceInstanceParams
      value:
        - name: diskConfigs
          value:
            - - name: deviceName
                value: string
              - name: instantiateFrom
                value: string
              - name: autoDelete
                value: boolean
              - name: customImage
                value: string
    - name: region
      value: string

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
