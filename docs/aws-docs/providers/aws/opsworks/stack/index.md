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
<tr><td><b>Description</b></td><td>stack</td></tr>
<tr><td><b>Id</b></td><td><code>aws.opsworks.stack</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>agent_version</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>attributes</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>chef_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>clone_app_ids</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>clone_permissions</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>configuration_manager</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>custom_cookbooks_source</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>custom_json</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>default_availability_zone</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>default_instance_profile_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>default_os</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>default_root_device_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>default_ssh_key_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>default_subnet_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ecs_cluster_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>elastic_ips</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>hostname_theme</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>rds_db_instances</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>service_role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>source_stack_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>use_custom_cookbooks</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>use_opsworks_security_groups</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>vpc_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
agent_version,
attributes,
chef_configuration,
clone_app_ids,
clone_permissions,
configuration_manager,
custom_cookbooks_source,
custom_json,
default_availability_zone,
default_instance_profile_arn,
default_os,
default_root_device_type,
default_ssh_key_name,
default_subnet_id,
ecs_cluster_arn,
elastic_ips,
hostname_theme,
name,
rds_db_instances,
service_role_arn,
source_stack_id,
tags,
use_custom_cookbooks,
use_opsworks_security_groups,
vpc_id
FROM aws.opsworks.stack
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
