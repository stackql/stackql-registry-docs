---
title: instance
hide_title: false
hide_table_of_contents: false
keywords:
  - instance
  - opsworks
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>instance</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instance</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>instance</td></tr>
<tr><td><b>Id</b></td><td><code>aws.opsworks.instance</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>AvailabilityZone</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>PrivateDnsName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>PrivateIp</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>PublicDnsName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>PublicIp</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>AgentVersion</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>AmiId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Architecture</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>AutoScalingType</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>BlockDeviceMappings</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>EbsOptimized</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>ElasticIps</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Hostname</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>InstallUpdatesOnBoot</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>InstanceType</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>LayerIds</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Os</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>RootDeviceType</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>SshKeyName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>StackId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>SubnetId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Tenancy</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>TimeBasedAutoScaling</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>VirtualizationType</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Volumes</code></td><td><code>array</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.opsworks.instance
WHERE region = 'us-east-1' AND data__Identifier = '&lt;Id&gt;'
</pre>
