---
title: instance
hide_title: false
hide_table_of_contents: false
keywords:
  - instance
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
Gets an individual <code>instance</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instance</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>instance</td></tr>
<tr><td><b>Id</b></td><td><code>aws.opsworks.instance</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>availability_zone</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>private_dns_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>private_ip</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>public_dns_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>public_ip</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>agent_version</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ami_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>architecture</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>auto_scaling_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>block_device_mappings</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>ebs_optimized</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>elastic_ips</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>hostname</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>install_updates_on_boot</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>instance_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>layer_ids</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>os</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>root_device_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ssh_key_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>stack_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>subnet_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tenancy</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>time_based_auto_scaling</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>virtualization_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>volumes</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
availability_zone,
private_dns_name,
private_ip,
public_dns_name,
public_ip,
agent_version,
ami_id,
architecture,
auto_scaling_type,
block_device_mappings,
ebs_optimized,
elastic_ips,
hostname,
install_updates_on_boot,
instance_type,
layer_ids,
os,
root_device_type,
ssh_key_name,
stack_id,
subnet_id,
tenancy,
time_based_auto_scaling,
virtualization_type,
volumes
FROM aws.opsworks.instance
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
