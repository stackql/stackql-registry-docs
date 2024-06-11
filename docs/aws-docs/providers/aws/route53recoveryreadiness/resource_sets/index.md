---
title: resource_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_sets
  - route53recoveryreadiness
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

Creates, updates, deletes or gets a <code>resource_set</code> resource or lists <code>resource_sets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Schema for the AWS Route53 Recovery Readiness ResourceSet Resource and API.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53recoveryreadiness.resource_sets" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="resource_set_name" /></td><td><code>string</code></td><td>The name of the resource set to create.</td></tr>
<tr><td><CopyableCode code="resources" /></td><td><code>array</code></td><td>A list of resource objects in the resource set.</td></tr>
<tr><td><CopyableCode code="resource_set_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the resource set.</td></tr>
<tr><td><CopyableCode code="resource_set_type" /></td><td><code>string</code></td><td>The resource type of the resources in the resource set. Enter one of the following values for resource type: AWS: :AutoScaling: :AutoScalingGroup, AWS: :CloudWatch: :Alarm, AWS: :EC2: :CustomerGateway, AWS: :DynamoDB: :Table, AWS: :EC2: :Volume, AWS: :ElasticLoadBalancing: :LoadBalancer, AWS: :ElasticLoadBalancingV2: :LoadBalancer, AWS: :MSK: :Cluster, AWS: :RDS: :DBCluster, AWS: :Route53: :HealthCheck, AWS: :SQS: :Queue, AWS: :SNS: :Topic, AWS: :SNS: :Subscription, AWS: :EC2: :VPC, AWS: :EC2: :VPNConnection, AWS: :EC2: :VPNGateway, AWS::Route53RecoveryReadiness::DNSTargetResource</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A tag to associate with the parameters for a resource set.</td></tr>
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
    <td><CopyableCode code="ResourceSetType, Resources, region" /></td>
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
List all <code>resource_sets</code> in a region.
```sql
SELECT
region,
resource_set_name
FROM aws.route53recoveryreadiness.resource_sets
WHERE region = 'us-east-1';
```
Gets all properties from a <code>resource_set</code>.
```sql
SELECT
region,
resource_set_name,
resources,
resource_set_arn,
resource_set_type,
tags
FROM aws.route53recoveryreadiness.resource_sets
WHERE region = 'us-east-1' AND data__Identifier = '<ResourceSetName>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>resource_set</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.route53recoveryreadiness.resource_sets (
 Resources,
 ResourceSetType,
 region
)
SELECT 
'{{ Resources }}',
 '{{ ResourceSetType }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.route53recoveryreadiness.resource_sets (
 ResourceSetName,
 Resources,
 ResourceSetType,
 Tags,
 region
)
SELECT 
 '{{ ResourceSetName }}',
 '{{ Resources }}',
 '{{ ResourceSetType }}',
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
  - name: resource_set
    props:
      - name: ResourceSetName
        value: '{{ ResourceSetName }}'
      - name: Resources
        value:
          - ResourceArn: '{{ ResourceArn }}'
            ComponentId: '{{ ComponentId }}'
            DnsTargetResource:
              DomainName: '{{ DomainName }}'
              RecordSetId: '{{ RecordSetId }}'
              HostedZoneArn: '{{ HostedZoneArn }}'
              RecordType: '{{ RecordType }}'
              TargetResource:
                NLBResource:
                  Arn: '{{ Arn }}'
                R53Resource:
                  DomainName: '{{ DomainName }}'
                  RecordSetId: '{{ RecordSetId }}'
            ReadinessScopes:
              - '{{ ReadinessScopes[0] }}'
      - name: ResourceSetType
        value: '{{ ResourceSetType }}'
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
DELETE FROM aws.route53recoveryreadiness.resource_sets
WHERE data__Identifier = '<ResourceSetName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>resource_sets</code> resource, the following permissions are required:

### Create
```json
route53-recovery-readiness:CreateResourceSet,
route53-recovery-readiness:GetResourceSet,
route53-recovery-readiness:GetRecoveryGroup,
route53-recovery-readiness:GetCell,
route53-recovery-readiness:ListTagsForResources,
route53-recovery-readiness:TagResource
```

### Read
```json
route53-recovery-readiness:GetResourceSet,
route53-recovery-readiness:ListTagsForResources
```

### Update
```json
route53-recovery-readiness:UpdateResourceSet,
route53-recovery-readiness:GetResourceSet,
route53-recovery-readiness:GetRecoveryGroup,
route53-recovery-readiness:GetCell,
route53-recovery-readiness:ListTagsForResources,
route53-recovery-readiness:TagResource,
route53-recovery-readiness:UntagResource
```

### Delete
```json
route53-recovery-readiness:DeleteResourceSet,
route53-recovery-readiness:GetResourceSet
```

### List
```json
route53-recovery-readiness:ListResourceSets
```

