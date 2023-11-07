---
title: environments
hide_title: false
hide_table_of_contents: false
keywords:
  - environments
  - m2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>environments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>environments</td></tr>
<tr><td><b>Id</b></td><td><code>aws.m2.environments</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>The description of the environment.</td></tr>
<tr><td><code>EngineType</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>EngineVersion</code></td><td><code>string</code></td><td>The version of the runtime engine for the environment.</td></tr>
<tr><td><code>EnvironmentArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the runtime environment.</td></tr>
<tr><td><code>EnvironmentId</code></td><td><code>string</code></td><td>The unique identifier of the environment.</td></tr>
<tr><td><code>HighAvailabilityConfig</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>InstanceType</code></td><td><code>string</code></td><td>The type of instance underlying the environment.</td></tr>
<tr><td><code>KmsKeyId</code></td><td><code>string</code></td><td>The ID or the Amazon Resource Name (ARN) of the customer managed KMS Key used for encrypting environment-related resources.</td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>The name of the environment.</td></tr>
<tr><td><code>PreferredMaintenanceWindow</code></td><td><code>string</code></td><td>Configures a desired maintenance window for the environment. If you do not provide a value, a random system-generated value will be assigned.</td></tr>
<tr><td><code>PubliclyAccessible</code></td><td><code>boolean</code></td><td>Specifies whether the environment is publicly accessible.</td></tr>
<tr><td><code>SecurityGroupIds</code></td><td><code>array</code></td><td>The list of security groups for the VPC associated with this environment.</td></tr>
<tr><td><code>StorageConfigurations</code></td><td><code>array</code></td><td>The storage configurations defined for the runtime environment.</td></tr>
<tr><td><code>SubnetIds</code></td><td><code>array</code></td><td>The unique identifiers of the subnets assigned to this runtime environment.</td></tr>
<tr><td><code>Tags</code></td><td><code>object</code></td><td>Tags associated to this environment.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.m2.environments<br/>WHERE region = 'us-east-1'
</pre>
