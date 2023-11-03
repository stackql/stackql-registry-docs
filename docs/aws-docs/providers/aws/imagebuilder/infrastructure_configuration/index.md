---
title: infrastructure_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - infrastructure_configuration
  - imagebuilder
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>infrastructure_configuration</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>infrastructure_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.imagebuilder.infrastructure_configuration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the infrastructure configuration.</td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td>The name of the infrastructure configuration.</td></tr><tr><td><code>Description</code></td><td><code>string</code></td><td>The description of the infrastructure configuration.</td></tr><tr><td><code>InstanceTypes</code></td><td><code>array</code></td><td>The instance types of the infrastructure configuration.</td></tr><tr><td><code>SecurityGroupIds</code></td><td><code>array</code></td><td>The security group IDs of the infrastructure configuration.</td></tr><tr><td><code>Logging</code></td><td><code>undefined</code></td><td>The logging configuration of the infrastructure configuration.</td></tr><tr><td><code>SubnetId</code></td><td><code>string</code></td><td>The subnet ID of the infrastructure configuration.</td></tr><tr><td><code>KeyPair</code></td><td><code>string</code></td><td>The EC2 key pair of the infrastructure configuration..</td></tr><tr><td><code>TerminateInstanceOnFailure</code></td><td><code>boolean</code></td><td>The terminate instance on failure configuration of the infrastructure configuration.</td></tr><tr><td><code>InstanceProfileName</code></td><td><code>string</code></td><td>The instance profile of the infrastructure configuration.</td></tr><tr><td><code>InstanceMetadataOptions</code></td><td><code>undefined</code></td><td>The instance metadata option settings for the infrastructure configuration.</td></tr><tr><td><code>SnsTopicArn</code></td><td><code>string</code></td><td>The SNS Topic Amazon Resource Name (ARN) of the infrastructure configuration.</td></tr><tr><td><code>ResourceTags</code></td><td><code>object</code></td><td>The tags attached to the resource created by Image Builder.</td></tr><tr><td><code>Tags</code></td><td><code>object</code></td><td>The tags associated with the component.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.imagebuilder.infrastructure_configuration
WHERE region = 'us-east-1' AND data__Identifier = '{Arn}'
</pre>
