---
title: notebook_instance
hide_title: false
hide_table_of_contents: false
keywords:
  - notebook_instance
  - sagemaker
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>notebook_instance</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notebook_instance</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>notebook_instance</td></tr>
<tr><td><b>Id</b></td><td><code>aws.sagemaker.notebook_instance</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>kms_key_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>volume_size_in_gb</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>additional_code_repositories</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>default_code_repository</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>direct_internet_access</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>platform_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>accelerator_types</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>subnet_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>security_group_ids</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>instance_metadata_service_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>root_access</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>notebook_instance_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>instance_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>lifecycle_config_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
kms_key_id,
volume_size_in_gb,
additional_code_repositories,
default_code_repository,
direct_internet_access,
platform_identifier,
accelerator_types,
subnet_id,
security_group_ids,
role_arn,
instance_metadata_service_configuration,
root_access,
id,
notebook_instance_name,
instance_type,
lifecycle_config_name,
tags
FROM aws.sagemaker.notebook_instance
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
