---
title: buckets
hide_title: false
hide_table_of_contents: false
keywords:
  - buckets
  - storage
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

Creates, updates, deletes, gets or lists a <code>buckets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>buckets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.storage.buckets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the bucket. For buckets, the id and name properties are the same. |
| <CopyableCode code="name" /> | `string` | The name of the bucket. |
| <CopyableCode code="acl" /> | `array` | Access controls on the bucket. |
| <CopyableCode code="autoclass" /> | `object` | The bucket's Autoclass configuration. |
| <CopyableCode code="billing" /> | `object` | The bucket's billing configuration. |
| <CopyableCode code="cors" /> | `array` | The bucket's Cross-Origin Resource Sharing (CORS) configuration. |
| <CopyableCode code="customPlacementConfig" /> | `object` | The bucket's custom placement configuration for Custom Dual Regions. |
| <CopyableCode code="defaultEventBasedHold" /> | `boolean` | The default value for event-based hold on newly created objects in this bucket. Event-based hold is a way to retain objects indefinitely until an event occurs, signified by the hold's release. After being released, such objects will be subject to bucket-level retention (if any). One sample use case of this flag is for banks to hold loan documents for at least 3 years after loan is paid in full. Here, bucket-level retention is 3 years and the event is loan being paid in full. In this example, these objects will be held intact for any number of years until the event has occurred (event-based hold on the object is released) and then 3 more years after that. That means retention duration of the objects begins from the moment event-based hold transitioned from true to false. Objects under event-based hold cannot be deleted, overwritten or archived until the hold is removed. |
| <CopyableCode code="defaultObjectAcl" /> | `array` | Default access controls to apply to new objects when no ACL is provided. |
| <CopyableCode code="encryption" /> | `object` | Encryption configuration for a bucket. |
| <CopyableCode code="etag" /> | `string` | HTTP 1.1 Entity tag for the bucket. |
| <CopyableCode code="generation" /> | `string` | The generation of this bucket. |
| <CopyableCode code="hardDeleteTime" /> | `string` | The hard delete time of the bucket in RFC 3339 format. |
| <CopyableCode code="hierarchicalNamespace" /> | `object` | The bucket's hierarchical namespace configuration. |
| <CopyableCode code="iamConfiguration" /> | `object` | The bucket's IAM configuration. |
| <CopyableCode code="ipFilter" /> | `object` | The bucket's IP filter configuration. Specifies the network sources that are allowed to access the operations on the bucket, as well as its underlying objects. Only enforced when the mode is set to 'Enabled'. |
| <CopyableCode code="kind" /> | `string` | The kind of item this is. For buckets, this is always storage#bucket. |
| <CopyableCode code="labels" /> | `object` | User-provided labels, in key/value pairs. |
| <CopyableCode code="lifecycle" /> | `object` | The bucket's lifecycle configuration. See [Lifecycle Management](https://cloud.google.com/storage/docs/lifecycle) for more information. |
| <CopyableCode code="location" /> | `string` | The location of the bucket. Object data for objects in the bucket resides in physical storage within this region. Defaults to US. See the [Developer's Guide](https://cloud.google.com/storage/docs/locations) for the authoritative list. |
| <CopyableCode code="locationType" /> | `string` | The type of the bucket location. |
| <CopyableCode code="logging" /> | `object` | The bucket's logging configuration, which defines the destination bucket and optional name prefix for the current bucket's logs. |
| <CopyableCode code="metageneration" /> | `string` | The metadata generation of this bucket. |
| <CopyableCode code="objectRetention" /> | `object` | The bucket's object retention config. |
| <CopyableCode code="owner" /> | `object` | The owner of the bucket. This is always the project team's owner group. |
| <CopyableCode code="projectNumber" /> | `string` | The project number of the project the bucket belongs to. |
| <CopyableCode code="retentionPolicy" /> | `object` | The bucket's retention policy. The retention policy enforces a minimum retention time for all objects contained in the bucket, based on their creation time. Any attempt to overwrite or delete objects younger than the retention period will result in a PERMISSION_DENIED error. An unlocked retention policy can be modified or removed from the bucket via a storage.buckets.update operation. A locked retention policy cannot be removed or shortened in duration for the lifetime of the bucket. Attempting to remove or decrease period of a locked retention policy will result in a PERMISSION_DENIED error. |
| <CopyableCode code="rpo" /> | `string` | The Recovery Point Objective (RPO) of this bucket. Set to ASYNC_TURBO to turn on Turbo Replication on a bucket. |
| <CopyableCode code="satisfiesPZI" /> | `boolean` | Reserved for future use. |
| <CopyableCode code="satisfiesPZS" /> | `boolean` | Reserved for future use. |
| <CopyableCode code="selfLink" /> | `string` | The URI of this bucket. |
| <CopyableCode code="softDeletePolicy" /> | `object` | The bucket's soft delete policy, which defines the period of time that soft-deleted objects will be retained, and cannot be permanently deleted. |
| <CopyableCode code="softDeleteTime" /> | `string` | The soft delete time of the bucket in RFC 3339 format. |
| <CopyableCode code="storageClass" /> | `string` | The bucket's default storage class, used whenever no storageClass is specified for a newly-created object. This defines how objects in the bucket are stored and determines the SLA and the cost of storage. Values include MULTI_REGIONAL, REGIONAL, STANDARD, NEARLINE, COLDLINE, ARCHIVE, and DURABLE_REDUCED_AVAILABILITY. If this value is not specified when the bucket is created, it will default to STANDARD. For more information, see [Storage Classes](https://cloud.google.com/storage/docs/storage-classes). |
| <CopyableCode code="timeCreated" /> | `string` | The creation time of the bucket in RFC 3339 format. |
| <CopyableCode code="updated" /> | `string` | The modification time of the bucket in RFC 3339 format. |
| <CopyableCode code="versioning" /> | `object` | The bucket's versioning configuration. |
| <CopyableCode code="website" /> | `object` | The bucket's website configuration, controlling how the service behaves when accessing bucket contents as a web site. See the [Static Website Examples](https://cloud.google.com/storage/docs/static-website) for more information. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="bucket" /> | Returns metadata for the specified bucket. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project" /> | Retrieves a list of buckets for a given project. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="project" /> | Creates a new bucket. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="bucket" /> | Deletes an empty bucket. Deletions are permanent unless soft delete is enabled on the bucket. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="bucket" /> | Patches a bucket. Changes to the bucket will be readable immediately after writing, but configuration changes may take time to propagate. |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="bucket" /> | Updates a bucket. Changes to the bucket will be readable immediately after writing, but configuration changes may take time to propagate. |
| <CopyableCode code="lock_retention_policy" /> | `EXEC` | <CopyableCode code="bucket, ifMetagenerationMatch" /> | Locks retention policy on a bucket. |
| <CopyableCode code="restore" /> | `EXEC` | <CopyableCode code="bucket, generation" /> | Restores a soft-deleted bucket. |

## `SELECT` examples

Returns metadata for the specified bucket.

```sql
SELECT
id,
name,
acl,
autoclass,
billing,
cors,
customPlacementConfig,
defaultEventBasedHold,
defaultObjectAcl,
encryption,
etag,
generation,
hardDeleteTime,
hierarchicalNamespace,
iamConfiguration,
ipFilter,
kind,
labels,
lifecycle,
location,
locationType,
logging,
metageneration,
objectRetention,
owner,
projectNumber,
retentionPolicy,
rpo,
satisfiesPZI,
satisfiesPZS,
selfLink,
softDeletePolicy,
softDeleteTime,
storageClass,
timeCreated,
updated,
versioning,
website
FROM google.storage.buckets
WHERE bucket = '{{ bucket }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>buckets</code> resource.

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
INSERT INTO google.storage.buckets (
project,
acl,
billing,
cors,
customPlacementConfig,
defaultEventBasedHold,
defaultObjectAcl,
encryption,
etag,
hierarchicalNamespace,
iamConfiguration,
ipFilter,
labels,
lifecycle,
autoclass,
location,
locationType,
logging,
generation,
metageneration,
name,
owner,
projectNumber,
retentionPolicy,
objectRetention,
rpo,
softDeletePolicy,
storageClass,
timeCreated,
updated,
softDeleteTime,
hardDeleteTime,
versioning,
website,
satisfiesPZS,
satisfiesPZI
)
SELECT 
'{{ project }}',
'{{ acl }}',
'{{ billing }}',
'{{ cors }}',
'{{ customPlacementConfig }}',
true|false,
'{{ defaultObjectAcl }}',
'{{ encryption }}',
'{{ etag }}',
'{{ hierarchicalNamespace }}',
'{{ iamConfiguration }}',
'{{ ipFilter }}',
'{{ labels }}',
'{{ lifecycle }}',
'{{ autoclass }}',
'{{ location }}',
'{{ locationType }}',
'{{ logging }}',
'{{ generation }}',
'{{ metageneration }}',
'{{ name }}',
'{{ owner }}',
'{{ projectNumber }}',
'{{ retentionPolicy }}',
'{{ objectRetention }}',
'{{ rpo }}',
'{{ softDeletePolicy }}',
'{{ storageClass }}',
'{{ timeCreated }}',
'{{ updated }}',
'{{ softDeleteTime }}',
'{{ hardDeleteTime }}',
'{{ versioning }}',
'{{ website }}',
true|false,
true|false
;
```
</TabItem>
<TabItem value="manifest">

```yaml
acl:
  - bucket: string
    domain: string
    email: string
    entity: string
    entityId: string
    etag: string
    id: string
    kind: string
    projectTeam:
      projectNumber: string
      team: string
    role: string
    selfLink: string
billing:
  requesterPays: boolean
cors:
  - maxAgeSeconds: integer
    method:
      - type: string
    origin:
      - type: string
    responseHeader:
      - type: string
customPlacementConfig:
  dataLocations:
    - type: string
defaultEventBasedHold: boolean
defaultObjectAcl:
  - bucket: string
    domain: string
    email: string
    entity: string
    entityId: string
    etag: string
    generation: string
    id: string
    kind: string
    object: string
    projectTeam:
      projectNumber: string
      team: string
    role: string
    selfLink: string
encryption:
  defaultKmsKeyName: string
etag: string
hierarchicalNamespace:
  enabled: boolean
iamConfiguration:
  bucketPolicyOnly:
    enabled: boolean
    lockedTime: string
  uniformBucketLevelAccess:
    enabled: boolean
    lockedTime: string
  publicAccessPrevention: string
id: string
ipFilter:
  mode: string
  publicNetworkSource:
    allowedIpCidrRanges:
      - type: string
  vpcNetworkSources:
    - network: string
      allowedIpCidrRanges:
        - type: string
kind: string
labels: object
lifecycle:
  rule:
    - action:
        storageClass: string
        type: string
      condition:
        age: integer
        createdBefore: string
        customTimeBefore: string
        daysSinceCustomTime: integer
        daysSinceNoncurrentTime: integer
        isLive: boolean
        matchesPattern: string
        matchesPrefix:
          - type: string
        matchesSuffix:
          - type: string
        matchesStorageClass:
          - type: string
        noncurrentTimeBefore: string
        numNewerVersions: integer
autoclass:
  enabled: boolean
  toggleTime: string
  terminalStorageClass: string
  terminalStorageClassUpdateTime: string
location: string
locationType: string
logging:
  logBucket: string
  logObjectPrefix: string
generation: string
metageneration: string
name: string
owner:
  entity: string
  entityId: string
projectNumber: string
retentionPolicy:
  effectiveTime: string
  isLocked: boolean
  retentionPeriod: string
objectRetention:
  mode: string
rpo: string
selfLink: string
softDeletePolicy:
  retentionDurationSeconds: string
  effectiveTime: string
storageClass: string
timeCreated: string
updated: string
softDeleteTime: string
hardDeleteTime: string
versioning:
  enabled: boolean
website:
  mainPageSuffix: string
  notFoundPage: string
satisfiesPZS: boolean
satisfiesPZI: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>buckets</code> resource.

```sql
/*+ update */
UPDATE google.storage.buckets
SET 
acl = '{{ acl }}',
billing = '{{ billing }}',
cors = '{{ cors }}',
customPlacementConfig = '{{ customPlacementConfig }}',
defaultEventBasedHold = true|false,
defaultObjectAcl = '{{ defaultObjectAcl }}',
encryption = '{{ encryption }}',
etag = '{{ etag }}',
hierarchicalNamespace = '{{ hierarchicalNamespace }}',
iamConfiguration = '{{ iamConfiguration }}',
ipFilter = '{{ ipFilter }}',
labels = '{{ labels }}',
lifecycle = '{{ lifecycle }}',
autoclass = '{{ autoclass }}',
location = '{{ location }}',
locationType = '{{ locationType }}',
logging = '{{ logging }}',
generation = '{{ generation }}',
metageneration = '{{ metageneration }}',
name = '{{ name }}',
owner = '{{ owner }}',
projectNumber = '{{ projectNumber }}',
retentionPolicy = '{{ retentionPolicy }}',
objectRetention = '{{ objectRetention }}',
rpo = '{{ rpo }}',
softDeletePolicy = '{{ softDeletePolicy }}',
storageClass = '{{ storageClass }}',
timeCreated = '{{ timeCreated }}',
updated = '{{ updated }}',
softDeleteTime = '{{ softDeleteTime }}',
hardDeleteTime = '{{ hardDeleteTime }}',
versioning = '{{ versioning }}',
website = '{{ website }}',
satisfiesPZS = true|false,
satisfiesPZI = true|false
WHERE 
bucket = '{{ bucket }}';
```

## `REPLACE` example

Replaces all fields in the specified <code>buckets</code> resource.

```sql
/*+ update */
REPLACE google.storage.buckets
SET 
acl = '{{ acl }}',
billing = '{{ billing }}',
cors = '{{ cors }}',
customPlacementConfig = '{{ customPlacementConfig }}',
defaultEventBasedHold = true|false,
defaultObjectAcl = '{{ defaultObjectAcl }}',
encryption = '{{ encryption }}',
etag = '{{ etag }}',
hierarchicalNamespace = '{{ hierarchicalNamespace }}',
iamConfiguration = '{{ iamConfiguration }}',
ipFilter = '{{ ipFilter }}',
labels = '{{ labels }}',
lifecycle = '{{ lifecycle }}',
autoclass = '{{ autoclass }}',
location = '{{ location }}',
locationType = '{{ locationType }}',
logging = '{{ logging }}',
generation = '{{ generation }}',
metageneration = '{{ metageneration }}',
name = '{{ name }}',
owner = '{{ owner }}',
projectNumber = '{{ projectNumber }}',
retentionPolicy = '{{ retentionPolicy }}',
objectRetention = '{{ objectRetention }}',
rpo = '{{ rpo }}',
softDeletePolicy = '{{ softDeletePolicy }}',
storageClass = '{{ storageClass }}',
timeCreated = '{{ timeCreated }}',
updated = '{{ updated }}',
softDeleteTime = '{{ softDeleteTime }}',
hardDeleteTime = '{{ hardDeleteTime }}',
versioning = '{{ versioning }}',
website = '{{ website }}',
satisfiesPZS = true|false,
satisfiesPZI = true|false
WHERE 
bucket = '{{ bucket }}';
```

## `DELETE` example

Deletes the specified <code>buckets</code> resource.

```sql
/*+ delete */
DELETE FROM google.storage.buckets
WHERE bucket = '{{ bucket }}';
```
