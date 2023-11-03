---
title: cluster
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster
  - dax
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>cluster</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cluster</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.dax.cluster</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>SSESpecification</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>ClusterDiscoveryEndpointURL</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ReplicationFactor</code></td><td><code>integer</code></td><td></td></tr><tr><td><code>ParameterGroupName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>AvailabilityZones</code></td><td><code>array</code></td><td></td></tr><tr><td><code>IAMRoleARN</code></td><td><code>string</code></td><td></td></tr><tr><td><code>SubnetGroupName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>PreferredMaintenanceWindow</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ClusterEndpointEncryptionType</code></td><td><code>string</code></td><td></td></tr><tr><td><code>NotificationTopicARN</code></td><td><code>string</code></td><td></td></tr><tr><td><code>SecurityGroupIds</code></td><td><code>array</code></td><td></td></tr><tr><td><code>NodeType</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ClusterName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ClusterDiscoveryEndpoint</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>object</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.dax.cluster
WHERE region = 'us-east-1' AND data__Identifier = '{Id}'
</pre>
