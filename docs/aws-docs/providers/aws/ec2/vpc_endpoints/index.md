---
title: vpc_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_endpoints
  - ec2
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

Creates, updates, deletes or gets a <code>vpc_endpoint</code> resource or lists <code>vpc_endpoints</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies a VPC endpoint. A VPC endpoint provides a private connection between your VPC and an endpoint service. You can use an endpoint service provided by AWS, an MKT Partner, or another AWS accounts in your organization. For more information, see the &#91;User Guide&#93;(https://docs.aws.amazon.com/vpc/latest/privatelink/).<br />An endpoint of type <code>Interface</code> establishes connections between the subnets in your VPC and an AWS-service, your own service, or a service hosted by another AWS-account. With an interface VPC endpoint, you specify the subnets in which to create the endpoint and the security groups to associate with the endpoint network interfaces.<br />An endpoint of type <code>gateway</code> serves as a target for a route in your route table for traffic destined for S3 or DDB. You can specify an endpoint policy for the endpoint, which controls access to the service from your VPC. You can also specify the VPC route tables that use the endpoint. For more information about connectivity to S3, see &#91;W</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.vpc_endpoints" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="creation_timestamp" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="dns_entries" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="network_interface_ids" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="policy_document" /></td><td><code>object</code></td><td>An endpoint policy, which controls access to the service from the VPC. The default endpoint policy allows full access to the service. Endpoint policies are supported only for gateway and interface endpoints.<br />For CloudFormation templates in YAML, you can provide the policy in JSON or YAML format. CFNlong converts YAML policies to JSON format before calling the API to create or modify the VPC endpoint.</td></tr>
<tr><td><CopyableCode code="private_dns_enabled" /></td><td><code>boolean</code></td><td>Indicate whether to associate a private hosted zone with the specified VPC. The private hosted zone contains a record set for the default public DNS name for the service for the Region (for example, <code>kinesis.us-east-1.amazonaws.com</code>), which resolves to the private IP addresses of the endpoint network interfaces in the VPC. This enables you to make requests to the default public DNS name for the service instead of the public DNS names that are automatically generated by the VPC endpoint service.<br />To use a private hosted zone, you must set the following VPC attributes to <code>true</code>: <code>enableDnsHostnames</code> and <code>enableDnsSupport</code>.<br />This property is supported only for interface endpoints.<br />Default: <code>false</code></td></tr>
<tr><td><CopyableCode code="route_table_ids" /></td><td><code>array</code></td><td>The IDs of the route tables. Routing is supported only for gateway endpoints.</td></tr>
<tr><td><CopyableCode code="security_group_ids" /></td><td><code>array</code></td><td>The IDs of the security groups to associate with the endpoint network interfaces. If this parameter is not specified, we use the default security group for the VPC. Security groups are supported only for interface endpoints.</td></tr>
<tr><td><CopyableCode code="service_name" /></td><td><code>string</code></td><td>The name of the endpoint service.</td></tr>
<tr><td><CopyableCode code="subnet_ids" /></td><td><code>array</code></td><td>The IDs of the subnets in which to create endpoint network interfaces. You must specify this property for an interface endpoint or a Gateway Load Balancer endpoint. You can't specify this property for a gateway endpoint. For a Gateway Load Balancer endpoint, you can specify only one subnet.</td></tr>
<tr><td><CopyableCode code="vpc_endpoint_type" /></td><td><code>string</code></td><td>The type of endpoint.<br />Default: Gateway</td></tr>
<tr><td><CopyableCode code="vpc_id" /></td><td><code>string</code></td><td>The ID of the VPC.</td></tr>
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
    <td><CopyableCode code="VpcId, ServiceName, region" /></td>
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
Gets all <code>vpc_endpoints</code> in a region.
```sql
SELECT
region,
id,
creation_timestamp,
dns_entries,
network_interface_ids,
policy_document,
private_dns_enabled,
route_table_ids,
security_group_ids,
service_name,
subnet_ids,
vpc_endpoint_type,
vpc_id
FROM aws.ec2.vpc_endpoints
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>vpc_endpoint</code>.
```sql
SELECT
region,
id,
creation_timestamp,
dns_entries,
network_interface_ids,
policy_document,
private_dns_enabled,
route_table_ids,
security_group_ids,
service_name,
subnet_ids,
vpc_endpoint_type,
vpc_id
FROM aws.ec2.vpc_endpoints
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>vpc_endpoint</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.vpc_endpoints (
 ServiceName,
 VpcId,
 region
)
SELECT 
'{{ ServiceName }}',
 '{{ VpcId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.vpc_endpoints (
 PolicyDocument,
 PrivateDnsEnabled,
 RouteTableIds,
 SecurityGroupIds,
 ServiceName,
 SubnetIds,
 VpcEndpointType,
 VpcId,
 region
)
SELECT 
 '{{ PolicyDocument }}',
 '{{ PrivateDnsEnabled }}',
 '{{ RouteTableIds }}',
 '{{ SecurityGroupIds }}',
 '{{ ServiceName }}',
 '{{ SubnetIds }}',
 '{{ VpcEndpointType }}',
 '{{ VpcId }}',
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
  - name: vpc_endpoint
    props:
      - name: PolicyDocument
        value: {}
      - name: PrivateDnsEnabled
        value: '{{ PrivateDnsEnabled }}'
      - name: RouteTableIds
        value:
          - '{{ RouteTableIds[0] }}'
      - name: SecurityGroupIds
        value:
          - '{{ SecurityGroupIds[0] }}'
      - name: ServiceName
        value: '{{ ServiceName }}'
      - name: SubnetIds
        value:
          - '{{ SubnetIds[0] }}'
      - name: VpcEndpointType
        value: '{{ VpcEndpointType }}'
      - name: VpcId
        value: '{{ VpcId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ec2.vpc_endpoints
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>vpc_endpoints</code> resource, the following permissions are required:

### Create
```json
ec2:CreateVpcEndpoint,
ec2:DescribeVpcEndpoints
```

### Read
```json
ec2:DescribeVpcEndpoints
```

### Update
```json
ec2:ModifyVpcEndpoint,
ec2:DescribeVpcEndpoints
```

### Delete
```json
ec2:DeleteVpcEndpoints,
ec2:DescribeVpcEndpoints
```

### List
```json
ec2:DescribeVpcEndpoints
```

