---
title: resource_set
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_set
  - route53recoveryreadiness
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>resource_set</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_set</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>resource_set</td></tr>
<tr><td><b>Id</b></td><td><code>aws.route53recoveryreadiness.resource_set</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ResourceSetName</code></td><td><code>string</code></td><td>The name of the resource set to create.</td></tr>
<tr><td><code>Resources</code></td><td><code>array</code></td><td>A list of resource objects in the resource set.</td></tr>
<tr><td><code>ResourceSetArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the resource set.</td></tr>
<tr><td><code>ResourceSetType</code></td><td><code>string</code></td><td>The resource type of the resources in the resource set. Enter one of the following values for resource type: &lt;br&#x2F;&gt;&lt;br&#x2F;&gt;AWS: :AutoScaling: :AutoScalingGroup, AWS: :CloudWatch: :Alarm, AWS: :EC2: :CustomerGateway, AWS: :DynamoDB: :Table, AWS: :EC2: :Volume, AWS: :ElasticLoadBalancing: :LoadBalancer, AWS: :ElasticLoadBalancingV2: :LoadBalancer, AWS: :MSK: :Cluster, AWS: :RDS: :DBCluster, AWS: :Route53: :HealthCheck, AWS: :SQS: :Queue, AWS: :SNS: :Topic, AWS: :SNS: :Subscription, AWS: :EC2: :VPC, AWS: :EC2: :VPNConnection, AWS: :EC2: :VPNGateway, AWS::Route53RecoveryReadiness::DNSTargetResource</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>A tag to associate with the parameters for a resource set.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.route53recoveryreadiness.resource_set<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;ResourceSetName&gt;'
</pre>
