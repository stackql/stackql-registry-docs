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
Gets or operates on an individual <code>endpoint_access</code> resource, use <code>endpoint_accesses</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoint_access</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for a Redshift-managed VPC endpoint.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.redshift.endpoint_access</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>address</code></td><td><code>string</code></td><td>The DNS address of the endpoint.</td></tr>
<tr><td><code>cluster_identifier</code></td><td><code>string</code></td><td>A unique identifier for the cluster. You use this identifier to refer to the cluster for any subsequent cluster operations such as deleting or modifying. All alphabetical characters must be lower case, no hypens at the end, no two consecutive hyphens. Cluster name should be unique for all clusters within an AWS account</td></tr>
<tr><td><code>vpc_security_groups</code></td><td><code>array</code></td><td>A list of Virtual Private Cloud (VPC) security groups to be associated with the endpoint.</td></tr>
<tr><td><code>resource_owner</code></td><td><code>string</code></td><td>The AWS account ID of the owner of the cluster.</td></tr>
<tr><td><code>endpoint_status</code></td><td><code>string</code></td><td>The status of the endpoint.</td></tr>
<tr><td><code>endpoint_name</code></td><td><code>string</code></td><td>The name of the endpoint.</td></tr>
<tr><td><code>endpoint_create_time</code></td><td><code>string</code></td><td>The time (UTC) that the endpoint was created.</td></tr>
<tr><td><code>subnet_group_name</code></td><td><code>string</code></td><td>The subnet group name where Amazon Redshift chooses to deploy the endpoint.</td></tr>
<tr><td><code>port</code></td><td><code>integer</code></td><td>The port number on which the cluster accepts incoming connections.</td></tr>
<tr><td><code>vpc_security_group_ids</code></td><td><code>array</code></td><td>A list of vpc security group ids to apply to the created endpoint access.</td></tr>
<tr><td><code>vpc_endpoint</code></td><td><code>object</code></td><td>The connection endpoint for connecting to an Amazon Redshift cluster through the proxy.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
address,
cluster_identifier,
vpc_security_groups,
resource_owner,
endpoint_status,
endpoint_name,
endpoint_create_time,
subnet_group_name,
port,
vpc_security_group_ids,
vpc_endpoint
FROM aws.redshift.endpoint_access
WHERE data__Identifier = '<EndpointName>';
```

## Permissions

To operate on the <code>endpoint_access</code> resource, the following permissions are required:

### Read
```json
redshift:DescribeEndpointAccess,
ec2:DescribeClientVpnEndpoints,
ec2:DescribeVpcEndpoint,
ec2:DescribeVpcAttribute,
ec2:DescribeSecurityGroups,
ec2:DescribeAddresses,
ec2:DescribeInternetGateways,
ec2:DescribeSubnets
```

### Update
```json
redshift:DescribeEndpointAccess,
redshift:ModifyEndpointAccess,
ec2:ModifyClientVpnEndpoint,
ec2:ModifyVpcEndpoint,
ec2:DescribeVpcAttribute,
ec2:DescribeSecurityGroups,
ec2:DescribeAddresses,
ec2:DescribeInternetGateways,
ec2:DescribeSubnets
```

### Delete
```json
redshift:DeleteEndpointAccess,
redshift:DescribeEndpointAccess,
ec2:DeleteClientVpnEndpoint,
ec2:DeleteVpcEndpoint,
ec2:DescribeVpcAttribute,
ec2:DescribeSecurityGroups,
ec2:DescribeAddresses,
ec2:DescribeInternetGateways,
ec2:DescribeSubnets,
ec2:DescribeVpcEndpoint
```

