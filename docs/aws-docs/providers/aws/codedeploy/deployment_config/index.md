---
title: deployment_config
hide_title: false
hide_table_of_contents: false
keywords:
  - deployment_config
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
Gets an individual <code>deployment_config</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployment_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>deployment_config</td></tr>
<tr><td><b>Id</b></td><td><code>aws.codedeploy.deployment_config</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ComputePlatform</code></td><td><code>string</code></td><td>The destination platform type for the deployment (Lambda, Server, or ECS).</td></tr>
<tr><td><code>DeploymentConfigName</code></td><td><code>string</code></td><td>A name for the deployment configuration. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the deployment configuration name. For more information, see Name Type.</td></tr>
<tr><td><code>MinimumHealthyHosts</code></td><td><code>undefined</code></td><td>The minimum number of healthy instances that should be available at any time during the deployment. There are two parameters expected in the input: type and value.</td></tr>
<tr><td><code>TrafficRoutingConfig</code></td><td><code>undefined</code></td><td>The configuration that specifies how the deployment traffic is routed.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.codedeploy.deployment_config<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;DeploymentConfigName&gt;'
</pre>
