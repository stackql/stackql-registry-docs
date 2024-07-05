---
title: instances_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - instances_list_only
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Lists <code>instances</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/instances/"><code>instances</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instances_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Lightsail::Instance</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lightsail.instances_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="support_code" /></td><td><code>string</code></td><td>Support code to help identify any issues</td></tr>
<tr><td><CopyableCode code="resource_type" /></td><td><code>string</code></td><td>Resource type of Lightsail instance.</td></tr>
<tr><td><CopyableCode code="is_static_ip" /></td><td><code>boolean</code></td><td>Is the IP Address of the Instance is the static IP</td></tr>
<tr><td><CopyableCode code="private_ip_address" /></td><td><code>string</code></td><td>Private IP Address of the Instance</td></tr>
<tr><td><CopyableCode code="public_ip_address" /></td><td><code>string</code></td><td>Public IP Address of the Instance</td></tr>
<tr><td><CopyableCode code="ipv6_addresses" /></td><td><code>array</code></td><td>IPv6 addresses of the instance</td></tr>
<tr><td><CopyableCode code="location" /></td><td><code>object</code></td><td>Location of a resource.</td></tr>
<tr><td><CopyableCode code="hardware" /></td><td><code>object</code></td><td>Hardware of the Instance.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>object</code></td><td>Current State of the Instance.</td></tr>
<tr><td><CopyableCode code="networking" /></td><td><code>object</code></td><td>Networking of the Instance.</td></tr>
<tr><td><CopyableCode code="user_name" /></td><td><code>string</code></td><td>Username of the Lightsail instance.</td></tr>
<tr><td><CopyableCode code="ssh_key_name" /></td><td><code>string</code></td><td>SSH Key Name of the Lightsail instance.</td></tr>
<tr><td><CopyableCode code="instance_name" /></td><td><code>string</code></td><td>The names to use for your new Lightsail instance.</td></tr>
<tr><td><CopyableCode code="availability_zone" /></td><td><code>string</code></td><td>The Availability Zone in which to create your instance. Use the following format: us-east-2a (case sensitive). Be sure to add the include Availability Zones parameter to your request.</td></tr>
<tr><td><CopyableCode code="bundle_id" /></td><td><code>string</code></td><td>The bundle of specification information for your virtual private server (or instance ), including the pricing plan (e.g., micro_1_0 ).</td></tr>
<tr><td><CopyableCode code="blueprint_id" /></td><td><code>string</code></td><td>The ID for a virtual private server image (e.g., app_wordpress_4_4 or app_lamp_7_0 ). Use the get blueprints operation to return a list of available images (or blueprints ).</td></tr>
<tr><td><CopyableCode code="add_ons" /></td><td><code>array</code></td><td>An array of objects representing the add-ons to enable for the new instance.</td></tr>
<tr><td><CopyableCode code="user_data" /></td><td><code>string</code></td><td>A launch script you can create that configures a server with additional user data. For example, you might want to run apt-get -y update.</td></tr>
<tr><td><CopyableCode code="key_pair_name" /></td><td><code>string</code></td><td>The name of your key pair.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>instances</code> in a region.
```sql
SELECT
region,
instance_name
FROM aws.lightsail.instances_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>instances_list_only</code> resource, see <a href="/providers/aws/lightsail/instances/#permissions"><code>instances</code></a>


