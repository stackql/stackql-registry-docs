---
title: vpc_connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_connectors
  - apprunner
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>vpc_connectors</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.apprunner.vpc_connectors</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>VpcConnectorName</code></td><td><code>string</code></td><td>A name for the VPC connector. If you don't specify a name, AWS CloudFormation generates a name for your VPC connector.</td></tr><tr><td><code>VpcConnectorArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of this VPC connector.</td></tr><tr><td><code>VpcConnectorRevision</code></td><td><code>integer</code></td><td>The revision of this VPC connector. It's unique among all the active connectors ("Status": "ACTIVE") that share the same Name.</td></tr><tr><td><code>Subnets</code></td><td><code>array</code></td><td>A list of IDs of subnets that App Runner should use when it associates your service with a custom Amazon VPC. Specify IDs of subnets of a single Amazon VPC. App Runner determines the Amazon VPC from the subnets you specify.</td></tr><tr><td><code>SecurityGroups</code></td><td><code>array</code></td><td>A list of IDs of security groups that App Runner should use for access to AWS resources under the specified subnets. If not specified, App Runner uses the default security group of the Amazon VPC. The default security group allows all outbound traffic.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>A list of metadata items that you can associate with your VPC connector resource. A tag is a key-value pair.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.apprunner.vpc_connectors
WHERE region = 'us-east-1'
</pre>
