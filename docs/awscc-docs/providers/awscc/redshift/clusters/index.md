---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
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
Retrieves a list of <code>clusters</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>clusters</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.redshift.clusters</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>cluster_identifier</code></td><td><code>string</code></td><td>A unique identifier for the cluster. You use this identifier to refer to the cluster for any subsequent cluster operations such as deleting or modifying. All alphabetical characters must be lower case, no hypens at the end, no two consecutive hyphens. Cluster name should be unique for all clusters within an AWS account</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>clusters</code> resource, the following permissions are required:

### Create
<pre>
iam:PassRole,
iam:CreateServiceLinkedRole,
redshift:DescribeClusters,
redshift:CreateCluster,
redshift:RestoreFromClusterSnapshot,
redshift:EnableLogging,
redshift:DescribeLoggingStatus,
redshift:CreateTags,
redshift:DescribeTags,
redshift:GetResourcePolicy,
redshift:PutResourcePolicy,
redshift:ModifyClusterMaintenance,
ec2:DescribeVpcs,
ec2:DescribeSubnets,
ec2:DescribeNetworkInterfaces,
ec2:DescribeAddresses,
ec2:AssociateAddress,
ec2:CreateNetworkInterface,
ec2:ModifyNetworkInterfaceAttribute,
ec2:CreateVpcEndpoint,
ec2:DescribeVpcEndpoints,
ec2:ModifyVpcEndpoint,
ec2:AllocateAddress,
ec2:CreateSecurityGroup,
ec2:DescribeVpcAttribute,
ec2:DescribeSecurityGroups,
ec2:DescribeInternetGateways,
ec2:DescribeSecurityGroupRules,
ec2:DescribeAvailabilityZones,
ec2:DescribeNetworkAcls,
ec2:DescribeRouteTables,
cloudwatch:PutMetricData</pre>

### List
<pre>
redshift:DescribeTags,
redshift:DescribeClusters</pre>


## Example
```sql
SELECT
region,
cluster_identifier
FROM awscc.redshift.clusters
WHERE region = 'us-east-1'
```
