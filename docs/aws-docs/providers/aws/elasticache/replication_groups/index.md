---
title: replication_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_groups
  - elasticache
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>replication_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.elasticache.replication_groups</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>PreferredCacheClusterAZs</code></td><td><code>array</code></td><td></td></tr><tr><td><code>PrimaryEndPointPort</code></td><td><code>string</code></td><td></td></tr><tr><td><code>CacheSecurityGroupNames</code></td><td><code>array</code></td><td></td></tr><tr><td><code>ReaderEndPointPort</code></td><td><code>string</code></td><td></td></tr><tr><td><code>NodeGroupConfiguration</code></td><td><code>array</code></td><td></td></tr><tr><td><code>SnapshotArns</code></td><td><code>array</code></td><td></td></tr><tr><td><code>ConfigurationEndPointPort</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Port</code></td><td><code>integer</code></td><td></td></tr><tr><td><code>ReadEndPointPortsList</code></td><td><code>array</code></td><td></td></tr><tr><td><code>NumNodeGroups</code></td><td><code>integer</code></td><td></td></tr><tr><td><code>NotificationTopicArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>SnapshotName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>AutomaticFailoverEnabled</code></td><td><code>boolean</code></td><td></td></tr><tr><td><code>ReplicasPerNodeGroup</code></td><td><code>integer</code></td><td></td></tr><tr><td><code>ReplicationGroupDescription</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ReaderEndPointAddress</code></td><td><code>string</code></td><td></td></tr><tr><td><code>MultiAZEnabled</code></td><td><code>boolean</code></td><td></td></tr><tr><td><code>TransitEncryptionEnabled</code></td><td><code>boolean</code></td><td></td></tr><tr><td><code>NetworkType</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ReplicationGroupId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Engine</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr><tr><td><code>NumCacheClusters</code></td><td><code>integer</code></td><td></td></tr><tr><td><code>PrimaryEndPointAddress</code></td><td><code>string</code></td><td></td></tr><tr><td><code>GlobalReplicationGroupId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ConfigurationEndPointAddress</code></td><td><code>string</code></td><td></td></tr><tr><td><code>EngineVersion</code></td><td><code>string</code></td><td></td></tr><tr><td><code>KmsKeyId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>CacheSubnetGroupName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>CacheParameterGroupName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>PreferredMaintenanceWindow</code></td><td><code>string</code></td><td></td></tr><tr><td><code>PrimaryClusterId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ReadEndPointPorts</code></td><td><code>string</code></td><td></td></tr><tr><td><code>AtRestEncryptionEnabled</code></td><td><code>boolean</code></td><td></td></tr><tr><td><code>AutoMinorVersionUpgrade</code></td><td><code>boolean</code></td><td></td></tr><tr><td><code>SecurityGroupIds</code></td><td><code>array</code></td><td></td></tr><tr><td><code>SnapshotWindow</code></td><td><code>string</code></td><td></td></tr><tr><td><code>TransitEncryptionMode</code></td><td><code>string</code></td><td></td></tr><tr><td><code>CacheNodeType</code></td><td><code>string</code></td><td></td></tr><tr><td><code>SnapshotRetentionLimit</code></td><td><code>integer</code></td><td></td></tr><tr><td><code>ReadEndPointAddressesList</code></td><td><code>array</code></td><td></td></tr><tr><td><code>SnapshottingClusterId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>UserGroupIds</code></td><td><code>array</code></td><td></td></tr><tr><td><code>IpDiscovery</code></td><td><code>string</code></td><td></td></tr><tr><td><code>AuthToken</code></td><td><code>string</code></td><td></td></tr><tr><td><code>DataTieringEnabled</code></td><td><code>boolean</code></td><td></td></tr><tr><td><code>LogDeliveryConfigurations</code></td><td><code>array</code></td><td></td></tr><tr><td><code>ReadEndPointAddresses</code></td><td><code>string</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.elasticache.replication_groups
WHERE region = 'us-east-1'
```
