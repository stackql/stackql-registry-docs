---
title: instance_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_templates
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

Creates, updates, deletes, gets or lists a <code>instance_templates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instance_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.instance_templates" /></td></tr>
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="instanceTemplate, project" /> | Returns the specified instance template. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project" /> | Retrieves a list of instance templates that are contained within the specified project. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="project" /> | Creates an instance template in the specified project using the data that is included in the request. If you are creating a new template to update an existing instance group, your new instance template must use the same network or, if applicable, the same subnetwork as the original template. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="instanceTemplate, project" /> | Deletes the specified instance template. Deleting an instance template is permanent and cannot be undone. It is not possible to delete templates that are already in use by a managed instance group. |

## `SELECT` examples

Retrieves a list of instance templates that are contained within the specified project.

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
FROM google.compute.instance_templates
WHERE project = '{{ project }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>instance_templates</code> resource.

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
INSERT INTO google.compute.instance_templates (
project,
name,
description,
properties,
sourceInstance,
sourceInstanceParams,
region
)
SELECT 
'{{ project }}',
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
kind: string
id: string
creationTimestamp: string
name: string
description: string
properties:
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
selfLink: string
sourceInstance: string
sourceInstanceParams:
  diskConfigs:
    - deviceName: string
      instantiateFrom: string
      autoDelete: boolean
      customImage: string
region: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>instance_templates</code> resource.

```sql
/*+ delete */
DELETE FROM google.compute.instance_templates
WHERE instanceTemplate = '{{ instanceTemplate }}'
AND project = '{{ project }}';
```
