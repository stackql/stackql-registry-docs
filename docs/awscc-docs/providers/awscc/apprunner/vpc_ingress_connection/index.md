---
title: vpc_ingress_connection
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_ingress_connection
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
Gets an individual <code>vpc_ingress_connection</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_ingress_connection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>vpc_ingress_connection</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.apprunner.vpc_ingress_connection</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>vpc_ingress_connection_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the VpcIngressConnection.</td></tr>
<tr><td><code>vpc_ingress_connection_name</code></td><td><code>string</code></td><td>The customer-provided Vpc Ingress Connection name.</td></tr>
<tr><td><code>service_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the service.</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>The current status of the VpcIngressConnection.</td></tr>
<tr><td><code>domain_name</code></td><td><code>string</code></td><td>The Domain name associated with the VPC Ingress Connection.</td></tr>
<tr><td><code>ingress_vpc_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>vpc_ingress_connection</code> resource, the following permissions are required:

### Read
<pre>
apprunner:DescribeVpcIngressConnection</pre>

### Update
<pre>
apprunner:UpdateVpcIngressConnection</pre>

### Delete
<pre>
apprunner:DeleteVpcIngressConnection</pre>


## Example
```sql
SELECT
region,
vpc_ingress_connection_arn,
vpc_ingress_connection_name,
service_arn,
status,
domain_name,
ingress_vpc_configuration,
tags
FROM awscc.apprunner.vpc_ingress_connection
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;VpcIngressConnectionArn&gt;'
```
