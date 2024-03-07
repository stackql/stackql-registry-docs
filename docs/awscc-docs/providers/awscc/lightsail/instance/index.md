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
<tr><td><b>Description</b></td><td>instance</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.lightsail.instance</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>support_code</code></td><td><code>string</code></td><td>Support code to help identify any issues</td></tr>
<tr><td><code>resource_type</code></td><td><code>string</code></td><td>Resource type of Lightsail instance.</td></tr>
<tr><td><code>is_static_ip</code></td><td><code>boolean</code></td><td>Is the IP Address of the Instance is the static IP</td></tr>
<tr><td><code>private_ip_address</code></td><td><code>string</code></td><td>Private IP Address of the Instance</td></tr>
<tr><td><code>public_ip_address</code></td><td><code>string</code></td><td>Public IP Address of the Instance</td></tr>
<tr><td><code>location</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>hardware</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>state</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>networking</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>user_name</code></td><td><code>string</code></td><td>Username of the  Lightsail instance.</td></tr>
<tr><td><code>ssh_key_name</code></td><td><code>string</code></td><td>SSH Key Name of the  Lightsail instance.</td></tr>
<tr><td><code>instance_name</code></td><td><code>string</code></td><td>The names to use for your new Lightsail instance.</td></tr>
<tr><td><code>availability_zone</code></td><td><code>string</code></td><td>The Availability Zone in which to create your instance. Use the following format: us-east-2a (case sensitive). Be sure to add the include Availability Zones parameter to your request.</td></tr>
<tr><td><code>bundle_id</code></td><td><code>string</code></td><td>The bundle of specification information for your virtual private server (or instance ), including the pricing plan (e.g., micro_1_0 ).</td></tr>
<tr><td><code>blueprint_id</code></td><td><code>string</code></td><td>The ID for a virtual private server image (e.g., app_wordpress_4_4 or app_lamp_7_0 ). Use the get blueprints operation to return a list of available images (or blueprints ).</td></tr>
<tr><td><code>add_ons</code></td><td><code>array</code></td><td>An array of objects representing the add-ons to enable for the new instance.</td></tr>
<tr><td><code>user_data</code></td><td><code>string</code></td><td>A launch script you can create that configures a server with additional user data. For example, you might want to run apt-get -y update.</td></tr>
<tr><td><code>key_pair_name</code></td><td><code>string</code></td><td>The name of your key pair.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>instance_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>instance</code> resource, the following permissions are required:

### Read
```json
lightsail:GetInstances,
lightsail:GetInstance
```

### Delete
```json
lightsail:GetInstances,
lightsail:GetInstance,
lightsail:DeleteInstance
```

### Update
```json
lightsail:GetInstances,
lightsail:GetInstance,
lightsail:DeleteInstance,
lightsail:EnableAddOn,
lightsail:DisableAddOn,
lightsail:PutInstancePublicPorts,
lightsail:AttachDisk,
lightsail:DetachDisk,
lightsail:StartInstance,
lightsail:StopInstance,
lightsail:GetDisk,
lightsail:TagResource,
lightsail:UntagResource
```


## Example
```sql
SELECT
region,
support_code,
resource_type,
is_static_ip,
private_ip_address,
public_ip_address,
location,
hardware,
state,
networking,
user_name,
ssh_key_name,
instance_name,
availability_zone,
bundle_id,
blueprint_id,
add_ons,
user_data,
key_pair_name,
tags,
instance_arn
FROM awscc.lightsail.instance
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;InstanceName&gt;'
```
