---
title: replication_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_instances
  - dms
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>replication_instances</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>replication_instances</td></tr>
<tr><td><b>Id</b></td><td><code>aws.dms.replication_instances</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ReplicationInstanceIdentifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>EngineVersion</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>KmsKeyId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>AvailabilityZone</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>PreferredMaintenanceWindow</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>AutoMinorVersionUpgrade</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>ReplicationSubnetGroupIdentifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ReplicationInstancePrivateIpAddresses</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>AllocatedStorage</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>ResourceIdentifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>VpcSecurityGroupIds</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>AllowMajorVersionUpgrade</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>ReplicationInstanceClass</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>PubliclyAccessible</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>MultiAZ</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>ReplicationInstancePublicIpAddresses</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.dms.replication_instances<br/>WHERE region = 'us-east-1'
</pre>
