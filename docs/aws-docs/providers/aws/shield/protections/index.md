---
title: protections
hide_title: false
hide_table_of_contents: false
keywords:
  - protections
  - shield
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

Creates, updates, deletes or gets a <code>protection</code> resource or lists <code>protections</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>protections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Enables AWS Shield Advanced for a specific AWS resource. The resource can be an Amazon CloudFront distribution, Amazon Route 53 hosted zone, AWS Global Accelerator standard accelerator, Elastic IP Address, Application Load Balancer, or a Classic Load Balancer. You can protect Amazon EC2 instances and Network Load Balancers by association with protected Amazon EC2 Elastic IP addresses.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.shield.protections" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="protection_id" /></td><td><code>string</code></td><td>The unique identifier (ID) of the protection.</td></tr>
<tr><td><CopyableCode code="protection_arn" /></td><td><code>string</code></td><td>The ARN (Amazon Resource Name) of the protection.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Friendly name for the Protection.</td></tr>
<tr><td><CopyableCode code="resource_arn" /></td><td><code>string</code></td><td>The ARN (Amazon Resource Name) of the resource to be protected.</td></tr>
<tr><td><CopyableCode code="health_check_arns" /></td><td><code>array</code></td><td>The Amazon Resource Names (ARNs) of the health check to associate with the protection.</td></tr>
<tr><td><CopyableCode code="application_layer_automatic_response_configuration" /></td><td><code>object</code></td><td>The automatic application layer DDoS mitigation settings for a Protection. This configuration determines whether Shield Advanced automatically manages rules in the web ACL in order to respond to application layer events that Shield Advanced determines to be DDoS attacks.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>One or more tag key-value pairs for the Protection object.</td></tr>
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
    <td><CopyableCode code="Name, ResourceArn, region" /></td>
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
    <td><CopyableCode code="list_resource" /></td>
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
List all <code>protections</code> in a region.
```sql
SELECT
region,
protection_arn
FROM aws.shield.protections
;
```
Gets all properties from a <code>protection</code>.
```sql
SELECT
region,
protection_id,
protection_arn,
name,
resource_arn,
health_check_arns,
application_layer_automatic_response_configuration,
tags
FROM aws.shield.protections
WHERE data__Identifier = '<ProtectionArn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>protection</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.shield.protections (
 Name,
 ResourceArn,
 region
)
SELECT 
'{{ Name }}',
 '{{ ResourceArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.shield.protections (
 Name,
 ResourceArn,
 HealthCheckArns,
 ApplicationLayerAutomaticResponseConfiguration,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ ResourceArn }}',
 '{{ HealthCheckArns }}',
 '{{ ApplicationLayerAutomaticResponseConfiguration }}',
 '{{ Tags }}',
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
  - name: protection
    props:
      - name: Name
        value: '{{ Name }}'
      - name: ResourceArn
        value: '{{ ResourceArn }}'
      - name: HealthCheckArns
        value:
          - '{{ HealthCheckArns[0] }}'
      - name: ApplicationLayerAutomaticResponseConfiguration
        value:
          Action: {}
          Status: '{{ Status }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.shield.protections
WHERE data__Identifier = '<ProtectionArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>protections</code> resource, the following permissions are required:

### Create
```json
shield:CreateProtection,
shield:DeleteProtection,
shield:DescribeProtection,
shield:ListProtections,
shield:EnableApplicationLayerAutomaticResponse,
shield:AssociateHealthCheck,
shield:TagResource,
ec2:DescribeAddresses,
elasticloadbalancing:DescribeLoadBalancers,
route53:GetHealthCheck,
iam:GetRole,
iam:CreateServiceLinkedRole,
wafv2:GetWebACLForResource,
wafv2:GetWebACL
```

### Delete
```json
shield:DeleteProtection,
shield:UntagResource
```

### Read
```json
shield:DescribeProtection,
shield:ListTagsForResource
```

### Update
```json
shield:DescribeProtection,
shield:AssociateHealthCheck,
shield:DisassociateHealthCheck,
shield:EnableApplicationLayerAutomaticResponse,
shield:UpdateApplicationLayerAutomaticResponse,
shield:DisableApplicationLayerAutomaticResponse,
shield:ListTagsForResource,
shield:TagResource,
shield:UntagResource,
route53:GetHealthCheck,
iam:GetRole,
iam:CreateServiceLinkedRole,
wafv2:GetWebACLForResource,
wafv2:GetWebACL
```

### List
```json
shield:ListProtections
```

