---
title: cluster
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster
  - emr
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>cluster</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cluster</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>cluster</td></tr>
<tr><td><b>Id</b></td><td><code>aws.emr.cluster</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>steps</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>step_concurrency_level</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>ebs_root_volume_size</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>o_srelease_label</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>service_role</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>log_uri</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>bootstrap_actions</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>master_public_dn_s</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>configurations</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>release_label</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>managed_scaling_policy</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>log_encryption_kms_key_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>additional_info</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>auto_termination_policy</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>kerberos_attributes</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>applications</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>auto_scaling_role</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>custom_ami_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>instances</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>scale_down_behavior</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>job_flow_role</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>visible_to_all_users</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>security_configuration</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
steps,
step_concurrency_level,
ebs_root_volume_size,
o_srelease_label,
name,
service_role,
log_uri,
bootstrap_actions,
master_public_dn_s,
configurations,
release_label,
tags,
managed_scaling_policy,
log_encryption_kms_key_id,
additional_info,
auto_termination_policy,
kerberos_attributes,
applications,
auto_scaling_role,
custom_ami_id,
instances,
scale_down_behavior,
job_flow_role,
visible_to_all_users,
security_configuration,
id
FROM aws.emr.cluster
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
