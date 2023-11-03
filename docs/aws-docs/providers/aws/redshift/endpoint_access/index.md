---
title: endpoint_access
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoint_access
  - redshift
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>endpoint_access</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoint_access</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.redshift.endpoint_access</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Address</code></td><td><code>string</code></td><td>The DNS address of the endpoint.</td></tr><tr><td><code>ClusterIdentifier</code></td><td><code>string</code></td><td>A unique identifier for the cluster. You use this identifier to refer to the cluster for any subsequent cluster operations such as deleting or modifying. All alphabetical characters must be lower case, no hypens at the end, no two consecutive hyphens. Cluster name should be unique for all clusters within an AWS account</td></tr><tr><td><code>VpcSecurityGroups</code></td><td><code>array</code></td><td>A list of Virtual Private Cloud (VPC) security groups to be associated with the endpoint.</td></tr><tr><td><code>ResourceOwner</code></td><td><code>string</code></td><td>The AWS account ID of the owner of the cluster.</td></tr><tr><td><code>EndpointStatus</code></td><td><code>string</code></td><td>The status of the endpoint.</td></tr><tr><td><code>EndpointName</code></td><td><code>string</code></td><td>The name of the endpoint.</td></tr><tr><td><code>EndpointCreateTime</code></td><td><code>string</code></td><td>The time (UTC) that the endpoint was created.</td></tr><tr><td><code>SubnetGroupName</code></td><td><code>string</code></td><td>The subnet group name where Amazon Redshift chooses to deploy the endpoint.</td></tr><tr><td><code>Port</code></td><td><code>integer</code></td><td>The port number on which the cluster accepts incoming connections.</td></tr><tr><td><code>VpcSecurityGroupIds</code></td><td><code>array</code></td><td>A list of vpc security group ids to apply to the created endpoint access.</td></tr><tr><td><code>VpcEndpoint</code></td><td><code>object</code></td><td>The connection endpoint for connecting to an Amazon Redshift cluster through the proxy.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.redshift.endpoint_access
WHERE region = 'us-east-1' AND data__Identifier = '<EndpointName>'
</pre>
