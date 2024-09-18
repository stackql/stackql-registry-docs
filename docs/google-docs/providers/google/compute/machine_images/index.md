---
title: machine_images
hide_title: false
hide_table_of_contents: false
keywords:
  - machine_images
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

Creates, updates, deletes, gets or lists a <code>machine_images</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>machine_images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.machine_images" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] A unique identifier for this machine image. The server defines this identifier. |
| <CopyableCode code="name" /> | `string` | Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| <CopyableCode code="description" /> | `string` | An optional description of this resource. Provide this property when you create the resource. |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] The creation timestamp for this machine image in RFC3339 text format. |
| <CopyableCode code="guestFlush" /> | `boolean` | [Input Only] Whether to attempt an application consistent machine image by informing the OS to prepare for the snapshot process. |
| <CopyableCode code="instanceProperties" /> | `object` |  |
| <CopyableCode code="kind" /> | `string` | [Output Only] The resource type, which is always compute#machineImage for machine image. |
| <CopyableCode code="machineImageEncryptionKey" /> | `object` |  |
| <CopyableCode code="satisfiesPzi" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | [Output Only] Reserved for future use. |
| <CopyableCode code="savedDisks" /> | `array` | An array of Machine Image specific properties for disks attached to the source instance |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] The URL for this machine image. The server defines this URL. |
| <CopyableCode code="sourceDiskEncryptionKeys" /> | `array` | [Input Only] The customer-supplied encryption key of the disks attached to the source instance. Required if the source disk is protected by a customer-supplied encryption key. |
| <CopyableCode code="sourceInstance" /> | `string` | The source instance used to create the machine image. You can provide this as a partial or full URL to the resource. For example, the following are valid values: - https://www.googleapis.com/compute/v1/projects/project/zones/zone /instances/instance - projects/project/zones/zone/instances/instance  |
| <CopyableCode code="sourceInstanceProperties" /> | `object` | DEPRECATED: Please use compute#instanceProperties instead. New properties will not be added to this field. |
| <CopyableCode code="status" /> | `string` | [Output Only] The status of the machine image. One of the following values: INVALID, CREATING, READY, DELETING, and UPLOADING. |
| <CopyableCode code="storageLocations" /> | `array` | The regional or multi-regional Cloud Storage bucket location where the machine image is stored. |
| <CopyableCode code="totalStorageBytes" /> | `string` | [Output Only] Total size of the storage used by the machine image. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="machineImage, project" /> | Returns the specified machine image. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project" /> | Retrieves a list of machine images that are contained within the specified project. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="project" /> | Creates a machine image in the specified project using the data that is included in the request. If you are creating a new machine image to update an existing instance, your new machine image should use the same network or, if applicable, the same subnetwork as the original instance. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="machineImage, project" /> | Deletes the specified machine image. Deleting a machine image is permanent and cannot be undone. |

## `SELECT` examples

Retrieves a list of machine images that are contained within the specified project.

```sql
SELECT
id,
name,
description,
creationTimestamp,
guestFlush,
instanceProperties,
kind,
machineImageEncryptionKey,
satisfiesPzi,
satisfiesPzs,
savedDisks,
selfLink,
sourceDiskEncryptionKeys,
sourceInstance,
sourceInstanceProperties,
status,
storageLocations,
totalStorageBytes
FROM google.compute.machine_images
WHERE project = '{{ project }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>machine_images</code> resource.

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
INSERT INTO google.compute.machine_images (
project,
name,
description,
sourceInstance,
status,
sourceInstanceProperties,
instanceProperties,
savedDisks,
storageLocations,
machineImageEncryptionKey,
guestFlush,
sourceDiskEncryptionKeys,
totalStorageBytes,
satisfiesPzs
)
SELECT 
'{{ project }}',
'{{ name }}',
'{{ description }}',
'{{ sourceInstance }}',
'{{ status }}',
'{{ sourceInstanceProperties }}',
'{{ instanceProperties }}',
'{{ savedDisks }}',
'{{ storageLocations }}',
'{{ machineImageEncryptionKey }}',
true|false,
'{{ sourceDiskEncryptionKeys }}',
'{{ totalStorageBytes }}',
true|false
;
```
</TabItem>
<TabItem value="manifest">

```yaml
kind: string
id: string
creationTimestamp: string
name: string
description: string
selfLink: string
sourceInstance: string
status: string
sourceInstanceProperties:
  description: string
  tags:
    items:
      - type: string
    fingerprint: string
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
      source: string
      deviceName: string
      index: integer
      boot: boolean
      autoDelete: boolean
      licenses:
        - type: string
      interface: string
      guestOsFeatures:
        - type: string
      diskEncryptionKey:
        rawKey: string
        rsaEncryptedKey: string
        kmsKeyName: string
        sha256: string
        kmsKeyServiceAccount: string
      diskSizeGb: string
      storageBytes: string
      storageBytesStatus: string
      diskType: string
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
  deletionProtection: boolean
  keyRevocationActionType: string
instanceProperties:
  description: string
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
  serviceAccounts:
    - email: string
      scopes:
        - type: string
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
savedDisks:
  - kind: string
    sourceDisk: string
    storageBytes: string
    storageBytesStatus: string
    architecture: string
storageLocations:
  - type: string
guestFlush: boolean
sourceDiskEncryptionKeys:
  - sourceDisk: string
totalStorageBytes: string
satisfiesPzs: boolean
satisfiesPzi: boolean

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>machine_images</code> resource.

```sql
/*+ delete */
DELETE FROM google.compute.machine_images
WHERE machineImage = '{{ machineImage }}'
AND project = '{{ project }}';
```
