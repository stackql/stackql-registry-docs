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

Creates, updates, deletes or gets a <code>vpc_endpoint_service</code> resource or lists <code>vpc_endpoint_services</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_endpoint_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::VPCEndpointService</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.vpc_endpoint_services" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="network_load_balancer_arns" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="contributor_insights_enabled" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="payer_responsibility" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="service_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="acceptance_required" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="gateway_load_balancer_arns" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="region" /></td>
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
Gets all <code>vpc_endpoint_services</code> in a region.
```sql
SELECT
region,
network_load_balancer_arns,
contributor_insights_enabled,
payer_responsibility,
service_id,
acceptance_required,
gateway_load_balancer_arns
FROM aws.ec2.vpc_endpoint_services
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>vpc_endpoint_service</code>.
```sql
SELECT
region,
network_load_balancer_arns,
contributor_insights_enabled,
payer_responsibility,
service_id,
acceptance_required,
gateway_load_balancer_arns
FROM aws.ec2.vpc_endpoint_services
WHERE region = 'us-east-1' AND data__Identifier = '<ServiceId>';
```

## `INSERT` example

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
/*+ create */
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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### Update
```json
ec2:ModifyVpcEndpointServiceConfiguration,
ec2:DeleteVpcEndpointServiceConfigurations,
ec2:DescribeVpcEndpointServiceConfigurations,
ec2:ModifyVpcEndpointServicePayerResponsibility,
cloudwatch:ListManagedInsightRules,
cloudwatch:DeleteInsightRules,
cloudwatch:PutManagedInsightRules
```

### Read
```json
ec2:DescribeVpcEndpointServiceConfigurations,
cloudwatch:ListManagedInsightRules
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

