---
title: auto_scaling_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - auto_scaling_groups
  - autoscaling
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>auto_scaling_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>auto_scaling_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.autoscaling.auto_scaling_groups</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>LifecycleHookSpecificationList</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>LoadBalancerNames</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>LaunchConfigurationName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ServiceLinkedRoleARN</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>TargetGroupARNs</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Cooldown</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>NotificationConfigurations</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>DesiredCapacity</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>HealthCheckGracePeriod</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>DefaultInstanceWarmup</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>NewInstancesProtectedFromScaleIn</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>LaunchTemplate</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>MixedInstancesPolicy</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>VPCZoneIdentifier</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Context</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>LaunchTemplateSpecification</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>CapacityRebalance</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>InstanceId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>AvailabilityZones</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>MetricsCollection</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>MaxSize</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>MinSize</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>TerminationPolicies</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>AutoScalingGroupName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DesiredCapacityType</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>PlacementGroup</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>HealthCheckType</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>MaxInstanceLifetime</code></td><td><code>integer</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.autoscaling.auto_scaling_groups
WHERE region = 'us-east-1'
</pre>
