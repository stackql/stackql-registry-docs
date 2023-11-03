---
title: stack
hide_title: false
hide_table_of_contents: false
keywords:
  - stack
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
Gets an individual <code>stack</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stack</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.opsworks.stack</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>AgentVersion</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Attributes</code></td><td><code>object</code></td><td></td></tr><tr><td><code>ChefConfiguration</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>CloneAppIds</code></td><td><code>array</code></td><td></td></tr><tr><td><code>ClonePermissions</code></td><td><code>boolean</code></td><td></td></tr><tr><td><code>ConfigurationManager</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>CustomCookbooksSource</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>CustomJson</code></td><td><code>object</code></td><td></td></tr><tr><td><code>DefaultAvailabilityZone</code></td><td><code>string</code></td><td></td></tr><tr><td><code>DefaultInstanceProfileArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>DefaultOs</code></td><td><code>string</code></td><td></td></tr><tr><td><code>DefaultRootDeviceType</code></td><td><code>string</code></td><td></td></tr><tr><td><code>DefaultSshKeyName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>DefaultSubnetId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>EcsClusterArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ElasticIps</code></td><td><code>array</code></td><td></td></tr><tr><td><code>HostnameTheme</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr><tr><td><code>RdsDbInstances</code></td><td><code>array</code></td><td></td></tr><tr><td><code>ServiceRoleArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>SourceStackId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr><tr><td><code>UseCustomCookbooks</code></td><td><code>boolean</code></td><td></td></tr><tr><td><code>UseOpsworksSecurityGroups</code></td><td><code>boolean</code></td><td></td></tr><tr><td><code>VpcId</code></td><td><code>string</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.opsworks.stack
WHERE region = 'us-east-1' AND data__Identifier = '{Id}'
</pre>
