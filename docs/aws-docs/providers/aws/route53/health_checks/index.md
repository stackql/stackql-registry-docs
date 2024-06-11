---
title: health_checks
hide_title: false
hide_table_of_contents: false
keywords:
  - health_checks
  - route53
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

Creates, updates, deletes or gets a <code>health_check</code> resource or lists <code>health_checks</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>health_checks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Route53::HealthCheck.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53.health_checks" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="health_check_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="health_check_config" /></td><td><code>object</code></td><td>A complex type that contains information about the health check.</td></tr>
<tr><td><CopyableCode code="health_check_tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
    <td><CopyableCode code="HealthCheckConfig, region" /></td>
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
List all <code>health_checks</code> in a region.
```sql
SELECT
region,
health_check_id
FROM aws.route53.health_checks
;
```
Gets all properties from a <code>health_check</code>.
```sql
SELECT
region,
health_check_id,
health_check_config,
health_check_tags
FROM aws.route53.health_checks
WHERE data__Identifier = '<HealthCheckId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>health_check</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.route53.health_checks (
 HealthCheckConfig,
 region
)
SELECT 
'{{ HealthCheckConfig }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.route53.health_checks (
 HealthCheckConfig,
 HealthCheckTags,
 region
)
SELECT 
 '{{ HealthCheckConfig }}',
 '{{ HealthCheckTags }}',
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
  - name: health_check
    props:
      - name: HealthCheckConfig
        value:
          AlarmIdentifier:
            Name: '{{ Name }}'
            Region: '{{ Region }}'
          ChildHealthChecks:
            - '{{ ChildHealthChecks[0] }}'
          EnableSNI: '{{ EnableSNI }}'
          FailureThreshold: '{{ FailureThreshold }}'
          FullyQualifiedDomainName: '{{ FullyQualifiedDomainName }}'
          HealthThreshold: '{{ HealthThreshold }}'
          InsufficientDataHealthStatus: '{{ InsufficientDataHealthStatus }}'
          Inverted: '{{ Inverted }}'
          IPAddress: '{{ IPAddress }}'
          MeasureLatency: '{{ MeasureLatency }}'
          Port: '{{ Port }}'
          Regions:
            - '{{ Regions[0] }}'
          RequestInterval: '{{ RequestInterval }}'
          ResourcePath: '{{ ResourcePath }}'
          SearchString: '{{ SearchString }}'
          RoutingControlArn: '{{ RoutingControlArn }}'
          Type: '{{ Type }}'
      - name: HealthCheckTags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.route53.health_checks
WHERE data__Identifier = '<HealthCheckId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>health_checks</code> resource, the following permissions are required:

### Create
```json
route53:CreateHealthCheck,
route53:ChangeTagsForResource,
cloudwatch:DescribeAlarms,
route53-recovery-control-config:DescribeRoutingControl
```

### Read
```json
route53:GetHealthCheck,
route53:ListTagsForResource
```

### Update
```json
route53:UpdateHealthCheck,
route53:ChangeTagsForResource,
route53:ListTagsForResource,
cloudwatch:DescribeAlarms
```

### Delete
```json
route53:DeleteHealthCheck
```

### List
```json
route53:ListHealthChecks,
route53:ListTagsForResource
```

