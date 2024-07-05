---
title: endpoint_accesses
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoint_accesses
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets an <code>endpoint_access</code> resource or lists <code>endpoint_accesses</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoint_accesses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for a Redshift-managed VPC endpoint.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.redshift.endpoint_accesses" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="endpoint_status" /></td><td><code>string</code></td><td>The status of the endpoint.</td></tr>
<tr><td><CopyableCode code="vpc_endpoint" /></td><td><code>object</code></td><td>The connection endpoint for connecting to an Amazon Redshift cluster through the proxy.</td></tr>
<tr><td><CopyableCode code="address" /></td><td><code>string</code></td><td>The DNS address of the endpoint.</td></tr>
<tr><td><CopyableCode code="endpoint_name" /></td><td><code>string</code></td><td>The name of the endpoint.</td></tr>
<tr><td><CopyableCode code="vpc_security_group_ids" /></td><td><code>array</code></td><td>A list of vpc security group ids to apply to the created endpoint access.</td></tr>
<tr><td><CopyableCode code="resource_owner" /></td><td><code>string</code></td><td>The AWS account ID of the owner of the cluster.</td></tr>
<tr><td><CopyableCode code="subnet_group_name" /></td><td><code>string</code></td><td>The subnet group name where Amazon Redshift chooses to deploy the endpoint.</td></tr>
<tr><td><CopyableCode code="port" /></td><td><code>integer</code></td><td>The port number on which the cluster accepts incoming connections.</td></tr>
<tr><td><CopyableCode code="endpoint_create_time" /></td><td><code>string</code></td><td>The time (UTC) that the endpoint was created.</td></tr>
<tr><td><CopyableCode code="cluster_identifier" /></td><td><code>string</code></td><td>A unique identifier for the cluster. You use this identifier to refer to the cluster for any subsequent cluster operations such as deleting or modifying. All alphabetical characters must be lower case, no hypens at the end, no two consecutive hyphens. Cluster name should be unique for all clusters within an AWS account</td></tr>
<tr><td><CopyableCode code="vpc_security_groups" /></td><td><code>array</code></td><td>A list of Virtual Private Cloud (VPC) security groups to be associated with the endpoint.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="ClusterIdentifier, SubnetGroupName, EndpointName, VpcSecurityGroupIds, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>endpoint_accesses</code> in a region.
```sql
SELECT
region,
endpoint_status,
vpc_endpoint,
address,
endpoint_name,
vpc_security_group_ids,
resource_owner,
subnet_group_name,
port,
endpoint_create_time,
cluster_identifier,
vpc_security_groups
FROM aws.redshift.endpoint_accesses
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>endpoint_access</code>.
```sql
SELECT
region,
endpoint_status,
vpc_endpoint,
address,
endpoint_name,
vpc_security_group_ids,
resource_owner,
subnet_group_name,
port,
endpoint_create_time,
cluster_identifier,
vpc_security_groups
FROM aws.redshift.endpoint_accesses
WHERE region = 'us-east-1' AND data__Identifier = '<EndpointName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>endpoint_access</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.redshift.endpoint_accesses (
 EndpointName,
 VpcSecurityGroupIds,
 SubnetGroupName,
 ClusterIdentifier,
 region
)
SELECT 
'{{ EndpointName }}',
 '{{ VpcSecurityGroupIds }}',
 '{{ SubnetGroupName }}',
 '{{ ClusterIdentifier }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.redshift.endpoint_accesses (
 EndpointName,
 VpcSecurityGroupIds,
 ResourceOwner,
 SubnetGroupName,
 ClusterIdentifier,
 region
)
SELECT 
 '{{ EndpointName }}',
 '{{ VpcSecurityGroupIds }}',
 '{{ ResourceOwner }}',
 '{{ SubnetGroupName }}',
 '{{ ClusterIdentifier }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: endpoint_access
    props:
      - name: EndpointName
        value: '{{ EndpointName }}'
      - name: VpcSecurityGroupIds
        value:
          - '{{ VpcSecurityGroupIds[0] }}'
      - name: ResourceOwner
        value: '{{ ResourceOwner }}'
      - name: SubnetGroupName
        value: '{{ SubnetGroupName }}'
      - name: ClusterIdentifier
        value: '{{ ClusterIdentifier }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.redshift.endpoint_accesses
WHERE data__Identifier = '<EndpointName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>endpoint_accesses</code> resource, the following permissions are required:

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

### Create
```json
redshift:CreateEndpointAccess,
redshift:DescribeEndpointAccess,
ec2:CreateClientVpnEndpoint,
ec2:CreateVpcEndpoint,
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

### List
```json
redshift:DescribeEndpointAccess,
ec2:DescribeClientVpnEndpoints,
ec2:DescribeVpcEndpoints,
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

