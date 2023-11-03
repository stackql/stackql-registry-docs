---
title: deployment_group
hide_title: false
hide_table_of_contents: false
keywords:
  - deployment_group
  - codedeploy
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>deployment_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployment_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.codedeploy.deployment_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>OnPremisesTagSet</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>ApplicationName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>DeploymentStyle</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>ServiceRoleArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>BlueGreenDeploymentConfiguration</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>AutoScalingGroups</code></td><td><code>array</code></td><td></td></tr><tr><td><code>Ec2TagSet</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>OutdatedInstancesStrategy</code></td><td><code>string</code></td><td></td></tr><tr><td><code>TriggerConfigurations</code></td><td><code>array</code></td><td></td></tr><tr><td><code>Deployment</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>DeploymentConfigName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>AlarmConfiguration</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Ec2TagFilters</code></td><td><code>array</code></td><td></td></tr><tr><td><code>ECSServices</code></td><td><code>array</code></td><td></td></tr><tr><td><code>AutoRollbackConfiguration</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>LoadBalancerInfo</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>DeploymentGroupName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr><tr><td><code>OnPremisesInstanceTagFilters</code></td><td><code>array</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.codedeploy.deployment_group
WHERE region = 'us-east-1' AND data__Identifier = '{Id}'
</pre>
