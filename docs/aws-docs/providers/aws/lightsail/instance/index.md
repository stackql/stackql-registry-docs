---
title: instance
hide_title: false
hide_table_of_contents: false
keywords:
  - instance
  - lightsail
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
<tr><td><b>Id</b></td><td><code>aws.lightsail.instance</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>SupportCode</code></td><td><code>string</code></td><td>Support code to help identify any issues</td></tr><tr><td><code>ResourceType</code></td><td><code>string</code></td><td>Resource type of Lightsail instance.</td></tr><tr><td><code>IsStaticIp</code></td><td><code>boolean</code></td><td>Is the IP Address of the Instance is the static IP</td></tr><tr><td><code>PrivateIpAddress</code></td><td><code>string</code></td><td>Private IP Address of the Instance</td></tr><tr><td><code>PublicIpAddress</code></td><td><code>string</code></td><td>Public IP Address of the Instance</td></tr><tr><td><code>Location</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Hardware</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>State</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Networking</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>UserName</code></td><td><code>string</code></td><td>Username of the  Lightsail instance.</td></tr><tr><td><code>SshKeyName</code></td><td><code>string</code></td><td>SSH Key Name of the  Lightsail instance.</td></tr><tr><td><code>InstanceName</code></td><td><code>string</code></td><td>The names to use for your new Lightsail instance.</td></tr><tr><td><code>AvailabilityZone</code></td><td><code>string</code></td><td>The Availability Zone in which to create your instance. Use the following format: us-east-2a (case sensitive). Be sure to add the include Availability Zones parameter to your request.</td></tr><tr><td><code>BundleId</code></td><td><code>string</code></td><td>The bundle of specification information for your virtual private server (or instance ), including the pricing plan (e.g., micro_1_0 ).</td></tr><tr><td><code>BlueprintId</code></td><td><code>string</code></td><td>The ID for a virtual private server image (e.g., app_wordpress_4_4 or app_lamp_7_0 ). Use the get blueprints operation to return a list of available images (or blueprints ).</td></tr><tr><td><code>AddOns</code></td><td><code>array</code></td><td>An array of objects representing the add-ons to enable for the new instance.</td></tr><tr><td><code>UserData</code></td><td><code>string</code></td><td>A launch script you can create that configures a server with additional user data. For example, you might want to run apt-get -y update.</td></tr><tr><td><code>KeyPairName</code></td><td><code>string</code></td><td>The name of your key pair.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr><tr><td><code>InstanceArn</code></td><td><code>string</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.lightsail.instance
WHERE region = 'us-east-1' AND data__Identifier = '{InstanceName}'
```
