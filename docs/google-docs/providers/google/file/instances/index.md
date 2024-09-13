
---
title: instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instances
  - file
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

Creates, updates, deletes or gets an <code>instance</code> resource or lists <code>instances</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.file.instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the instance, in the format `projects/{project}/locations/{location}/instances/{instance}`. |
| <CopyableCode code="description" /> | `string` | The description of the instance (2048 characters or less). |
| <CopyableCode code="configurablePerformanceEnabled" /> | `boolean` | Output only. Indicates whether this instance's performance is configurable. If enabled, adjust it using the 'performance_config' field. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the instance was created. |
| <CopyableCode code="deletionProtectionEnabled" /> | `boolean` | Optional. Indicates whether the instance is protected against deletion. |
| <CopyableCode code="deletionProtectionReason" /> | `string` | Optional. The reason for enabling deletion protection. |
| <CopyableCode code="etag" /> | `string` | Server-specified ETag for the instance resource to prevent simultaneous updates from overwriting each other. |
| <CopyableCode code="fileShares" /> | `array` | File system shares on the instance. For this version, only a single file share is supported. |
| <CopyableCode code="kmsKeyName" /> | `string` | KMS key name used for data encryption. |
| <CopyableCode code="labels" /> | `object` | Resource labels to represent user provided metadata. |
| <CopyableCode code="networks" /> | `array` | VPC networks to which the instance is connected. For this version, only a single network is supported. |
| <CopyableCode code="performanceConfig" /> | `object` | Used for setting the performance configuration. If the user doesn't specify PerformanceConfig, automatically provision the default performance settings as described in https://cloud.google.com/filestore/docs/performance. Larger instances will be linearly set to more IOPS. If the instance's capacity is increased or decreased, its performance will be automatically adjusted upwards or downwards accordingly (respectively). |
| <CopyableCode code="performanceLimits" /> | `object` | The enforced performance limits, calculated from the instance's performance configuration. |
| <CopyableCode code="protocol" /> | `string` | Immutable. The protocol indicates the access protocol for all shares in the instance. This field is immutable and it cannot be changed after the instance has been created. Default value: `NFS_V3`. |
| <CopyableCode code="replication" /> | `object` | Replication specifications. |
| <CopyableCode code="satisfiesPzi" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="state" /> | `string` | Output only. The instance state. |
| <CopyableCode code="statusMessage" /> | `string` | Output only. Additional information about the instance state, if available. |
| <CopyableCode code="suspensionReasons" /> | `array` | Output only. Field indicates all the reasons the instance is in "SUSPENDED" state. |
| <CopyableCode code="tags" /> | `object` | Optional. Input only. Immutable. Tag key-value pairs are bound to this resource. For example: "123/environment": "production", "123/costCenter": "marketing" |
| <CopyableCode code="tier" /> | `string` | The service tier of the instance. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Gets the details of a specific instance. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists all instances in a project for either a specified location or for all locations. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates an instance. When creating from a backup, the capacity of the new instance needs to be equal to or larger than the capacity of the backup (and also equal to or larger than the minimum capacity of the tier). |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Deletes an instance. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Updates the settings of a specific instance. |
| <CopyableCode code="promote_replica" /> | `EXEC` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Promote the standby instance (replica). |
| <CopyableCode code="restore" /> | `EXEC` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Restores an existing instance's file share from a backup. The capacity of the instance needs to be equal to or larger than the capacity of the backup (and also equal to or larger than the minimum capacity of the tier). |
| <CopyableCode code="revert" /> | `EXEC` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Revert an existing instance's file system to a specified snapshot. |

## `SELECT` examples

Lists all instances in a project for either a specified location or for all locations.

```sql
SELECT
name,
description,
configurablePerformanceEnabled,
createTime,
deletionProtectionEnabled,
deletionProtectionReason,
etag,
fileShares,
kmsKeyName,
labels,
networks,
performanceConfig,
performanceLimits,
protocol,
replication,
satisfiesPzi,
satisfiesPzs,
state,
statusMessage,
suspensionReasons,
tags,
tier
FROM google.file.instances
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>instances</code> resource.

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
INSERT INTO google.file.instances (
locationsId,
projectsId,
name,
description,
state,
statusMessage,
createTime,
tier,
labels,
fileShares,
networks,
etag,
satisfiesPzs,
satisfiesPzi,
kmsKeyName,
suspensionReasons,
replication,
tags,
protocol,
configurablePerformanceEnabled,
performanceConfig,
performanceLimits,
deletionProtectionEnabled,
deletionProtectionReason
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ description }}',
'{{ state }}',
'{{ statusMessage }}',
'{{ createTime }}',
'{{ tier }}',
'{{ labels }}',
'{{ fileShares }}',
'{{ networks }}',
'{{ etag }}',
true|false,
true|false,
'{{ kmsKeyName }}',
'{{ suspensionReasons }}',
'{{ replication }}',
'{{ tags }}',
'{{ protocol }}',
true|false,
'{{ performanceConfig }}',
'{{ performanceLimits }}',
true|false,
'{{ deletionProtectionReason }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: description
        value: '{{ description }}'
      - name: state
        value: '{{ state }}'
      - name: statusMessage
        value: '{{ statusMessage }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: tier
        value: '{{ tier }}'
      - name: labels
        value: '{{ labels }}'
      - name: fileShares
        value: '{{ fileShares }}'
      - name: networks
        value: '{{ networks }}'
      - name: etag
        value: '{{ etag }}'
      - name: satisfiesPzs
        value: '{{ satisfiesPzs }}'
      - name: satisfiesPzi
        value: '{{ satisfiesPzi }}'
      - name: kmsKeyName
        value: '{{ kmsKeyName }}'
      - name: suspensionReasons
        value: '{{ suspensionReasons }}'
      - name: replication
        value: '{{ replication }}'
      - name: tags
        value: '{{ tags }}'
      - name: protocol
        value: '{{ protocol }}'
      - name: configurablePerformanceEnabled
        value: '{{ configurablePerformanceEnabled }}'
      - name: performanceConfig
        value: '{{ performanceConfig }}'
      - name: performanceLimits
        value: '{{ performanceLimits }}'
      - name: deletionProtectionEnabled
        value: '{{ deletionProtectionEnabled }}'
      - name: deletionProtectionReason
        value: '{{ deletionProtectionReason }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a instance only if the necessary resources are available.

```sql
UPDATE google.file.instances
SET 
name = '{{ name }}',
description = '{{ description }}',
state = '{{ state }}',
statusMessage = '{{ statusMessage }}',
createTime = '{{ createTime }}',
tier = '{{ tier }}',
labels = '{{ labels }}',
fileShares = '{{ fileShares }}',
networks = '{{ networks }}',
etag = '{{ etag }}',
satisfiesPzs = true|false,
satisfiesPzi = true|false,
kmsKeyName = '{{ kmsKeyName }}',
suspensionReasons = '{{ suspensionReasons }}',
replication = '{{ replication }}',
tags = '{{ tags }}',
protocol = '{{ protocol }}',
configurablePerformanceEnabled = true|false,
performanceConfig = '{{ performanceConfig }}',
performanceLimits = '{{ performanceLimits }}',
deletionProtectionEnabled = true|false,
deletionProtectionReason = '{{ deletionProtectionReason }}'
WHERE 
instancesId = '{{ instancesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified instance resource.

```sql
DELETE FROM google.file.instances
WHERE instancesId = '{{ instancesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
