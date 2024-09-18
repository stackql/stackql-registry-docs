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
count: string
minCount: string
namePattern: string
perInstanceProperties: object
sourceInstanceTemplate: string
instanceProperties:
  description: string
  tags:
    items:
      - type: string
    fingerprint: string
  resourceManagerTags: object
  machineType: string
  canIpForward: boolean
  networkInterfaces:
    - kind: string
      network: string
      subnetwork: string
      networkIP: string
      ipv6Address: string
      internalIpv6PrefixLength: integer
      name: string
      accessConfigs:
        - kind: string
          type: string
          name: string
          natIP: string
          externalIpv6: string
          externalIpv6PrefixLength: integer
          setPublicPtr: boolean
          publicPtrDomainName: string
          networkTier: string
          securityPolicy: string
      ipv6AccessConfigs:
        - kind: string
          type: string
          name: string
          natIP: string
          externalIpv6: string
          externalIpv6PrefixLength: integer
          setPublicPtr: boolean
          publicPtrDomainName: string
          networkTier: string
          securityPolicy: string
      aliasIpRanges:
        - ipCidrRange: string
          subnetworkRangeName: string
      fingerprint: string
      stackType: string
      ipv6AccessType: string
      queueCount: integer
      nicType: string
      networkAttachment: string
  disks:
    - kind: string
      type: string
      mode: string
      savedState: string
      source: string
      deviceName: string
      index: integer
      boot: boolean
      initializeParams:
        diskName: string
        sourceImage: string
        diskSizeGb: string
        diskType: string
        sourceImageEncryptionKey:
          rawKey: string
          rsaEncryptedKey: string
          kmsKeyName: string
          sha256: string
          kmsKeyServiceAccount: string
        labels: object
        sourceSnapshot: string
        description: string
        replicaZones:
          - type: string
        resourcePolicies:
          - type: string
        onUpdateAction: string
        provisionedIops: string
        licenses:
          - type: string
        architecture: string
        resourceManagerTags: object
        provisionedThroughput: string
        enableConfidentialCompute: boolean
        storagePool: string
      autoDelete: boolean
      licenses:
        - type: string
      interface: string
      guestOsFeatures:
        - type: string
      diskSizeGb: string
      shieldedInstanceInitialState:
        pk:
          content: string
          fileType: string
        keks:
          - content: string
            fileType: string
        dbs:
          - content: string
            fileType: string
        dbxs:
          - content: string
            fileType: string
      forceAttach: boolean
      architecture: string
  metadata:
    kind: string
    fingerprint: string
    items:
      - key: string
        value: string
  serviceAccounts:
    - email: string
      scopes:
        - type: string
  scheduling:
    onHostMaintenance: string
    automaticRestart: boolean
    preemptible: boolean
    nodeAffinities:
      - key: string
        operator: string
        values:
          - type: string
    minNodeCpus: integer
    locationHint: string
    availabilityDomain: integer
    provisioningModel: string
    instanceTerminationAction: string
    maxRunDuration:
      seconds: string
      nanos: integer
    terminationTime: string
    onInstanceStopAction:
      discardLocalSsd: boolean
  labels: object
  guestAccelerators:
    - acceleratorType: string
      acceleratorCount: integer
  minCpuPlatform: string
  reservationAffinity:
    consumeReservationType: string
    key: string
    values:
      - type: string
  shieldedInstanceConfig:
    enableSecureBoot: boolean
    enableVtpm: boolean
    enableIntegrityMonitoring: boolean
  resourcePolicies:
    - type: string
  confidentialInstanceConfig:
    enableConfidentialCompute: boolean
    confidentialInstanceType: string
  privateIpv6GoogleAccess: string
  advancedMachineFeatures:
    enableNestedVirtualization: boolean
    threadsPerCore: integer
    visibleCoreCount: integer
    enableUefiNetworking: boolean
    performanceMonitoringUnit: string
    turboMode: string
  networkPerformanceConfig:
    totalEgressBandwidthTier: string
  keyRevocationActionType: string
locationPolicy:
  locations: object
  targetShape: string

```
</TabItem>
</Tabs>
