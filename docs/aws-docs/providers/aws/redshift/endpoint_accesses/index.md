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


Used to retrieve a list of <code>endpoint_accesses</code> in a region or to create or delete a <code>endpoint_accesses</code> resource, use <code>endpoint_access</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoint_accesses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for a Redshift-managed VPC endpoint.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.redshift.endpoint_accesses" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="endpoint_name" /></td><td><code>string</code></td><td>The name of the endpoint.</td></tr>
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
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
endpoint_name
FROM aws.redshift.endpoint_accesses
WHERE region = 'us-east-1';
```

## `INSERT` Example

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
-- endpoint_access.iql (required properties only)
INSERT INTO aws.redshift.endpoint_accesses (
 ClusterIdentifier,
 EndpointName,
 SubnetGroupName,
 VpcSecurityGroupIds,
 region
)
SELECT 
'{{ ClusterIdentifier }}',
 '{{ EndpointName }}',
 '{{ SubnetGroupName }}',
 '{{ VpcSecurityGroupIds }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- endpoint_access.iql (all properties)
INSERT INTO aws.redshift.endpoint_accesses (
 ClusterIdentifier,
 ResourceOwner,
 EndpointName,
 SubnetGroupName,
 VpcSecurityGroupIds,
 region
)
SELECT 
 '{{ ClusterIdentifier }}',
 '{{ ResourceOwner }}',
 '{{ EndpointName }}',
 '{{ SubnetGroupName }}',
 '{{ VpcSecurityGroupIds }}',
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
      - name: ClusterIdentifier
        value: '{{ ClusterIdentifier }}'
      - name: ResourceOwner
        value: '{{ ResourceOwner }}'
      - name: EndpointName
        value: '{{ EndpointName }}'
      - name: SubnetGroupName
        value: '{{ SubnetGroupName }}'
      - name: VpcSecurityGroupIds
        value:
          - '{{ VpcSecurityGroupIds[0] }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.redshift.endpoint_accesses
WHERE data__Identifier = '<EndpointName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>endpoint_accesses</code> resource, the following permissions are required:

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

