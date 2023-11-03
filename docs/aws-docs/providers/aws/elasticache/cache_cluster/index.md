---
title: cache_cluster
hide_title: false
hide_table_of_contents: false
keywords:
  - cache_cluster
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
Gets an individual <code>cache_cluster</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cache_cluster</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.elasticache.cache_cluster</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>CacheSecurityGroupNames</code></td><td><code>array</code></td><td></td></tr><tr><td><code>SnapshotArns</code></td><td><code>array</code></td><td></td></tr><tr><td><code>Port</code></td><td><code>integer</code></td><td></td></tr><tr><td><code>ConfigurationEndpointAddress</code></td><td><code>string</code></td><td></td></tr><tr><td><code>NotificationTopicArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>NumCacheNodes</code></td><td><code>integer</code></td><td></td></tr><tr><td><code>SnapshotName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>TransitEncryptionEnabled</code></td><td><code>boolean</code></td><td></td></tr><tr><td><code>NetworkType</code></td><td><code>string</code></td><td></td></tr><tr><td><code>PreferredAvailabilityZones</code></td><td><code>array</code></td><td></td></tr><tr><td><code>VpcSecurityGroupIds</code></td><td><code>array</code></td><td></td></tr><tr><td><code>ClusterName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>RedisEndpointAddress</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Engine</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr><tr><td><code>EngineVersion</code></td><td><code>string</code></td><td></td></tr><tr><td><code>RedisEndpointPort</code></td><td><code>string</code></td><td></td></tr><tr><td><code>CacheSubnetGroupName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>CacheParameterGroupName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>PreferredMaintenanceWindow</code></td><td><code>string</code></td><td></td></tr><tr><td><code>AutoMinorVersionUpgrade</code></td><td><code>boolean</code></td><td></td></tr><tr><td><code>PreferredAvailabilityZone</code></td><td><code>string</code></td><td></td></tr><tr><td><code>SnapshotWindow</code></td><td><code>string</code></td><td></td></tr><tr><td><code>CacheNodeType</code></td><td><code>string</code></td><td></td></tr><tr><td><code>SnapshotRetentionLimit</code></td><td><code>integer</code></td><td></td></tr><tr><td><code>ConfigurationEndpointPort</code></td><td><code>string</code></td><td></td></tr><tr><td><code>IpDiscovery</code></td><td><code>string</code></td><td></td></tr><tr><td><code>LogDeliveryConfigurations</code></td><td><code>array</code></td><td></td></tr><tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>AZMode</code></td><td><code>string</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.elasticache.cache_cluster
WHERE region = 'us-east-1' AND data__Identifier = '<Id>'
</pre>
