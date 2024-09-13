
---
title: instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instances
  - alloydb
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
<tr><td><b>Id</b></td><td><CopyableCode code="google.alloydb.instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The name of the instance resource with the format: * projects/{project}/locations/{region}/clusters/{cluster_id}/instances/{instance_id} where the cluster and instance ID segments should satisfy the regex expression `[a-z]([a-z0-9-]{0,61}[a-z0-9])?`, e.g. 1-63 characters of lowercase letters, numbers, and dashes, starting with a letter, and ending with a letter or number. For more details see https://google.aip.dev/122. The prefix of the instance resource name is the name of the parent resource: * projects/{project}/locations/{region}/clusters/{cluster_id} |
| <CopyableCode code="annotations" /> | `object` | Annotations to allow client tools to store small amount of arbitrary data. This is distinct from labels. https://google.aip.dev/128 |
| <CopyableCode code="availabilityType" /> | `string` | Availability type of an Instance. If empty, defaults to REGIONAL for primary instances. For read pools, availability_type is always UNSPECIFIED. Instances in the read pools are evenly distributed across available zones within the region (i.e. read pools with more than one node will have a node in at least two zones). |
| <CopyableCode code="clientConnectionConfig" /> | `object` | Client connection configuration |
| <CopyableCode code="createTime" /> | `string` | Output only. Create time stamp |
| <CopyableCode code="databaseFlags" /> | `object` | Database flags. Set at instance level. * They are copied from primary instance on read instance creation. * Read instances can set new or override existing flags that are relevant for reads, e.g. for enabling columnar cache on a read instance. Flags set on read instance may or may not be present on primary. This is a list of "key": "value" pairs. "key": The name of the flag. These flags are passed at instance setup time, so include both server options and system variables for Postgres. Flags are specified with underscores, not hyphens. "value": The value of the flag. Booleans are set to **on** for true and **off** for false. This field must be omitted if the flag doesn't take a value. |
| <CopyableCode code="deleteTime" /> | `string` | Output only. Delete time stamp |
| <CopyableCode code="displayName" /> | `string` | User-settable and human-readable display name for the Instance. |
| <CopyableCode code="etag" /> | `string` | For Resource freshness validation (https://google.aip.dev/154) |
| <CopyableCode code="gceZone" /> | `string` | The Compute Engine zone that the instance should serve from, per https://cloud.google.com/compute/docs/regions-zones This can ONLY be specified for ZONAL instances. If present for a REGIONAL instance, an error will be thrown. If this is absent for a ZONAL instance, instance is created in a random zone with available capacity. |
| <CopyableCode code="instanceType" /> | `string` | Required. The type of the instance. Specified at creation time. |
| <CopyableCode code="ipAddress" /> | `string` | Output only. The IP address for the Instance. This is the connection endpoint for an end-user application. |
| <CopyableCode code="labels" /> | `object` | Labels as key value pairs |
| <CopyableCode code="machineConfig" /> | `object` | MachineConfig describes the configuration of a machine. |
| <CopyableCode code="networkConfig" /> | `object` | Metadata related to instance level network configuration. |
| <CopyableCode code="nodes" /> | `array` | Output only. List of available read-only VMs in this instance, including the standby for a PRIMARY instance. |
| <CopyableCode code="outboundPublicIpAddresses" /> | `array` | Output only. All outbound public IP addresses configured for the instance. |
| <CopyableCode code="pscInstanceConfig" /> | `object` | PscInstanceConfig contains PSC related configuration at an instance level. |
| <CopyableCode code="publicIpAddress" /> | `string` | Output only. The public IP addresses for the Instance. This is available ONLY when enable_public_ip is set. This is the connection endpoint for an end-user application. |
| <CopyableCode code="queryInsightsConfig" /> | `object` | QueryInsights Instance specific configuration. |
| <CopyableCode code="readPoolConfig" /> | `object` | Configuration for a read pool instance. |
| <CopyableCode code="reconciling" /> | `boolean` | Output only. Reconciling (https://google.aip.dev/128#reconciliation). Set to true if the current state of Instance does not match the user's intended state, and the service is actively updating the resource to reconcile them. This can happen due to user-triggered updates or system actions like failover or maintenance. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="state" /> | `string` | Output only. The current serving state of the instance. |
| <CopyableCode code="uid" /> | `string` | Output only. The system-generated UID of the resource. The UID is assigned when the resource is created, and it is retained until it is deleted. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Update time stamp |
| <CopyableCode code="writableNode" /> | `object` | Details of a single node in the instance. Nodes in an AlloyDB instance are ephemereal, they can change during update, failover, autohealing and resize operations. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clustersId, instancesId, locationsId, projectsId" /> | Gets details of a single Instance. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="clustersId, locationsId, projectsId" /> | Lists Instances in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="clustersId, locationsId, projectsId" /> | Creates a new Instance in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clustersId, instancesId, locationsId, projectsId" /> | Deletes a single Instance. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="clustersId, instancesId, locationsId, projectsId" /> | Updates the parameters of a single Instance. |
| <CopyableCode code="failover" /> | `EXEC` | <CopyableCode code="clustersId, instancesId, locationsId, projectsId" /> | Forces a Failover for a highly available instance. Failover promotes the HA standby instance as the new primary. Imperative only. |
| <CopyableCode code="inject_fault" /> | `EXEC` | <CopyableCode code="clustersId, instancesId, locationsId, projectsId" /> | Injects fault in an instance. Imperative only. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="clustersId, instancesId, locationsId, projectsId" /> | Restart an Instance in a cluster. Imperative only. |

## `SELECT` examples

Lists Instances in a given project and location.

```sql
SELECT
name,
annotations,
availabilityType,
clientConnectionConfig,
createTime,
databaseFlags,
deleteTime,
displayName,
etag,
gceZone,
instanceType,
ipAddress,
labels,
machineConfig,
networkConfig,
nodes,
outboundPublicIpAddresses,
pscInstanceConfig,
publicIpAddress,
queryInsightsConfig,
readPoolConfig,
reconciling,
satisfiesPzs,
state,
uid,
updateTime,
writableNode
FROM google.alloydb.instances
WHERE clustersId = '{{ clustersId }}'
AND locationsId = '{{ locationsId }}'
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
INSERT INTO google.alloydb.instances (
clustersId,
locationsId,
projectsId,
name,
displayName,
uid,
createTime,
updateTime,
deleteTime,
labels,
state,
instanceType,
machineConfig,
availabilityType,
gceZone,
databaseFlags,
writableNode,
nodes,
queryInsightsConfig,
readPoolConfig,
ipAddress,
publicIpAddress,
reconciling,
etag,
annotations,
clientConnectionConfig,
satisfiesPzs,
pscInstanceConfig,
networkConfig,
outboundPublicIpAddresses
)
SELECT 
'{{ clustersId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ displayName }}',
'{{ uid }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ deleteTime }}',
'{{ labels }}',
'{{ state }}',
'{{ instanceType }}',
'{{ machineConfig }}',
'{{ availabilityType }}',
'{{ gceZone }}',
'{{ databaseFlags }}',
'{{ writableNode }}',
'{{ nodes }}',
'{{ queryInsightsConfig }}',
'{{ readPoolConfig }}',
'{{ ipAddress }}',
'{{ publicIpAddress }}',
true|false,
'{{ etag }}',
'{{ annotations }}',
'{{ clientConnectionConfig }}',
true|false,
'{{ pscInstanceConfig }}',
'{{ networkConfig }}',
'{{ outboundPublicIpAddresses }}'
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
      - name: displayName
        value: '{{ displayName }}'
      - name: uid
        value: '{{ uid }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: deleteTime
        value: '{{ deleteTime }}'
      - name: labels
        value: '{{ labels }}'
      - name: state
        value: '{{ state }}'
      - name: instanceType
        value: '{{ instanceType }}'
      - name: machineConfig
        value: '{{ machineConfig }}'
      - name: availabilityType
        value: '{{ availabilityType }}'
      - name: gceZone
        value: '{{ gceZone }}'
      - name: databaseFlags
        value: '{{ databaseFlags }}'
      - name: writableNode
        value: '{{ writableNode }}'
      - name: nodes
        value: '{{ nodes }}'
      - name: queryInsightsConfig
        value: '{{ queryInsightsConfig }}'
      - name: readPoolConfig
        value: '{{ readPoolConfig }}'
      - name: ipAddress
        value: '{{ ipAddress }}'
      - name: publicIpAddress
        value: '{{ publicIpAddress }}'
      - name: reconciling
        value: '{{ reconciling }}'
      - name: etag
        value: '{{ etag }}'
      - name: annotations
        value: '{{ annotations }}'
      - name: clientConnectionConfig
        value: '{{ clientConnectionConfig }}'
      - name: satisfiesPzs
        value: '{{ satisfiesPzs }}'
      - name: pscInstanceConfig
        value: '{{ pscInstanceConfig }}'
      - name: networkConfig
        value: '{{ networkConfig }}'
      - name: outboundPublicIpAddresses
        value: '{{ outboundPublicIpAddresses }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a instance only if the necessary resources are available.

```sql
UPDATE google.alloydb.instances
SET 
name = '{{ name }}',
displayName = '{{ displayName }}',
uid = '{{ uid }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
deleteTime = '{{ deleteTime }}',
labels = '{{ labels }}',
state = '{{ state }}',
instanceType = '{{ instanceType }}',
machineConfig = '{{ machineConfig }}',
availabilityType = '{{ availabilityType }}',
gceZone = '{{ gceZone }}',
databaseFlags = '{{ databaseFlags }}',
writableNode = '{{ writableNode }}',
nodes = '{{ nodes }}',
queryInsightsConfig = '{{ queryInsightsConfig }}',
readPoolConfig = '{{ readPoolConfig }}',
ipAddress = '{{ ipAddress }}',
publicIpAddress = '{{ publicIpAddress }}',
reconciling = true|false,
etag = '{{ etag }}',
annotations = '{{ annotations }}',
clientConnectionConfig = '{{ clientConnectionConfig }}',
satisfiesPzs = true|false,
pscInstanceConfig = '{{ pscInstanceConfig }}',
networkConfig = '{{ networkConfig }}',
outboundPublicIpAddresses = '{{ outboundPublicIpAddresses }}'
WHERE 
clustersId = '{{ clustersId }}'
AND instancesId = '{{ instancesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified instance resource.

```sql
DELETE FROM google.alloydb.instances
WHERE clustersId = '{{ clustersId }}'
AND instancesId = '{{ instancesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
