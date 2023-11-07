---
title: vpc_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_endpoints
  - opensearchserverless
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>vpc_endpoints</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.opensearchserverless.vpc_endpoints</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td>The identifier of the VPC Endpoint</td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>The name of the VPC Endpoint</td></tr>
<tr><td><code>SecurityGroupIds</code></td><td><code>array</code></td><td>The ID of one or more security groups to associate with the endpoint network interface</td></tr>
<tr><td><code>SubnetIds</code></td><td><code>array</code></td><td>The ID of one or more subnets in which to create an endpoint network interface</td></tr>
<tr><td><code>VpcId</code></td><td><code>string</code></td><td>The ID of the VPC in which the endpoint will be used.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.opensearchserverless.vpc_endpoints
WHERE region = 'us-east-1'
</pre>
