---
title: endpoint_authorization
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoint_authorization
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
Gets an individual <code>endpoint_authorization</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoint_authorization</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>endpoint_authorization</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.redshift.endpoint_authorization</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>grantor</code></td><td><code>string</code></td><td>The AWS account ID of the cluster owner.</td></tr>
<tr><td><code>grantee</code></td><td><code>string</code></td><td>The AWS account ID of the grantee of the cluster.</td></tr>
<tr><td><code>cluster_identifier</code></td><td><code>string</code></td><td>The cluster identifier.</td></tr>
<tr><td><code>authorize_time</code></td><td><code>string</code></td><td>The time (UTC) when the authorization was created.</td></tr>
<tr><td><code>cluster_status</code></td><td><code>string</code></td><td>The status of the cluster.</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>The status of the authorization action.</td></tr>
<tr><td><code>allowed_all_vpcs</code></td><td><code>boolean</code></td><td>Indicates whether all VPCs in the grantee account are allowed access to the cluster.</td></tr>
<tr><td><code>allowed_vpcs</code></td><td><code>array</code></td><td>The VPCs allowed access to the cluster.</td></tr>
<tr><td><code>endpoint_count</code></td><td><code>integer</code></td><td>The number of Redshift-managed VPC endpoints created for the authorization.</td></tr>
<tr><td><code>account</code></td><td><code>string</code></td><td>The target AWS account ID to grant or revoke access for.</td></tr>
<tr><td><code>vpc_ids</code></td><td><code>array</code></td><td>The virtual private cloud (VPC) identifiers to grant or revoke access to.</td></tr>
<tr><td><code>force</code></td><td><code>boolean</code></td><td> Indicates whether to force the revoke action. If true, the Redshift-managed VPC endpoints associated with the endpoint authorization are also deleted.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
grantor,
grantee,
cluster_identifier,
authorize_time,
cluster_status,
status,
allowed_all_vpcs,
allowed_vpcs,
endpoint_count,
account,
vpc_ids,
force
FROM awscc.redshift.endpoint_authorization
WHERE region = 'us-east-1'
AND data__Identifier = '{ClusterIdentifier}';
AND data__Identifier = '{Account}';
```

## Permissions

To operate on the <code>endpoint_authorization</code> resource, the following permissions are required:

### Read
```json
redshift:DescribeEndpointAuthorization
```

### Update
```json
redshift:AuthorizeEndpointAccess,
redshift:DescribeEndpointAuthorization,
redshift:RevokeEndpointAccess
```

### Delete
```json
redshift:RevokeEndpointAccess,
redshift:DeleteEndpointAccess,
redshift:DescribeEndpointAuthorization,
ec2:DeleteClientVpnEndpoint,
ec2:DescribeVpcAttribute,
ec2:DescribeSecurityGroups,
ec2:DescribeAddresses,
ec2:DescribeInternetGateways,
ec2:DescribeSubnets
```

