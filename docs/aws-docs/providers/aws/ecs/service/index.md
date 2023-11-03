---
title: service
hide_title: false
hide_table_of_contents: false
keywords:
  - service
  - ecs
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>service</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.ecs.service</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ServiceArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>CapacityProviderStrategy</code></td><td><code>array</code></td><td></td></tr><tr><td><code>Cluster</code></td><td><code>string</code></td><td></td></tr><tr><td><code>DeploymentConfiguration</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>DeploymentController</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>DesiredCount</code></td><td><code>integer</code></td><td></td></tr><tr><td><code>EnableECSManagedTags</code></td><td><code>boolean</code></td><td></td></tr><tr><td><code>EnableExecuteCommand</code></td><td><code>boolean</code></td><td></td></tr><tr><td><code>HealthCheckGracePeriodSeconds</code></td><td><code>integer</code></td><td></td></tr><tr><td><code>LaunchType</code></td><td><code>string</code></td><td></td></tr><tr><td><code>LoadBalancers</code></td><td><code>array</code></td><td></td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr><tr><td><code>NetworkConfiguration</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>PlacementConstraints</code></td><td><code>array</code></td><td></td></tr><tr><td><code>PlacementStrategies</code></td><td><code>array</code></td><td></td></tr><tr><td><code>PlatformVersion</code></td><td><code>string</code></td><td></td></tr><tr><td><code>PropagateTags</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Role</code></td><td><code>string</code></td><td></td></tr><tr><td><code>SchedulingStrategy</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ServiceConnectConfiguration</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>ServiceName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ServiceRegistries</code></td><td><code>array</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr><tr><td><code>TaskDefinition</code></td><td><code>string</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.ecs.service
WHERE region = 'us-east-1' AND data__Identifier = '<ServiceArn>' AND data__Identifier = '<Cluster>'
</pre>
