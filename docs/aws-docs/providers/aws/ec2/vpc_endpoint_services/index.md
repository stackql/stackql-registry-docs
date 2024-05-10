---
title: vpc_endpoint_services
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_endpoint_services
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


Used to retrieve a list of <code>vpc_endpoint_services</code> in a region or to create or delete a <code>vpc_endpoint_services</code> resource, use <code>vpc_endpoint_service</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_endpoint_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::VPCEndpointService</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.vpc_endpoint_services" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="service_id" /></td><td><code>string</code></td><td></td></tr>
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
service_id
FROM aws.ec2.vpc_endpoint_services
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>vpc_endpoint_service</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- vpc_endpoint_service.iql (required properties only)
INSERT INTO aws.ec2.vpc_endpoint_services (
 NetworkLoadBalancerArns,
 ContributorInsightsEnabled,
 PayerResponsibility,
 AcceptanceRequired,
 GatewayLoadBalancerArns,
 region
)
SELECT 
'{{ NetworkLoadBalancerArns }}',
 '{{ ContributorInsightsEnabled }}',
 '{{ PayerResponsibility }}',
 '{{ AcceptanceRequired }}',
 '{{ GatewayLoadBalancerArns }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- vpc_endpoint_service.iql (all properties)
INSERT INTO aws.ec2.vpc_endpoint_services (
 NetworkLoadBalancerArns,
 ContributorInsightsEnabled,
 PayerResponsibility,
 AcceptanceRequired,
 GatewayLoadBalancerArns,
 region
)
SELECT 
 '{{ NetworkLoadBalancerArns }}',
 '{{ ContributorInsightsEnabled }}',
 '{{ PayerResponsibility }}',
 '{{ AcceptanceRequired }}',
 '{{ GatewayLoadBalancerArns }}',
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
  - name: vpc_endpoint_service
    props:
      - name: NetworkLoadBalancerArns
        value:
          - '{{ NetworkLoadBalancerArns[0] }}'
      - name: ContributorInsightsEnabled
        value: '{{ ContributorInsightsEnabled }}'
      - name: PayerResponsibility
        value: '{{ PayerResponsibility }}'
      - name: AcceptanceRequired
        value: '{{ AcceptanceRequired }}'
      - name: GatewayLoadBalancerArns
        value:
          - '{{ GatewayLoadBalancerArns[0] }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.ec2.vpc_endpoint_services
WHERE data__Identifier = '<ServiceId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>vpc_endpoint_services</code> resource, the following permissions are required:

### Create
```json
ec2:CreateVpcEndpointServiceConfiguration,
ec2:ModifyVpcEndpointServiceConfiguration,
ec2:ModifyVpcEndpointServicePayerResponsibility,
cloudwatch:ListManagedInsightRules,
cloudwatch:DeleteInsightRules,
cloudwatch:PutManagedInsightRules,
ec2:DescribeVpcEndpointServiceConfigurations
```

### Delete
```json
ec2:DeleteVpcEndpointServiceConfigurations,
ec2:DescribeVpcEndpointServiceConfigurations,
cloudwatch:ListManagedInsightRules,
cloudwatch:DeleteInsightRules
```

### List
```json
ec2:DescribeVpcEndpointServiceConfigurations,
cloudwatch:ListManagedInsightRules
```

