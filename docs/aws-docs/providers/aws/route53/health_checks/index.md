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


Used to retrieve a list of <code>health_checks</code> in a region or to create or delete a <code>health_checks</code> resource, use <code>health_check</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>health_checks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Route53::HealthCheck.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53.health_checks" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="health_check_id" /></td><td><code>string</code></td><td></td></tr>
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
health_check_id
FROM aws.route53.health_checks
;
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },

    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "HealthCheckConfig": {
  "AlarmIdentifier": {
   "Name": "{{ Name }}",
   "Region": "{{ Region }}"
  },
  "ChildHealthChecks": [
   "{{ ChildHealthChecks[0] }}"
  ],
  "EnableSNI": "{{ EnableSNI }}",
  "FailureThreshold": "{{ FailureThreshold }}",
  "FullyQualifiedDomainName": "{{ FullyQualifiedDomainName }}",
  "HealthThreshold": "{{ HealthThreshold }}",
  "InsufficientDataHealthStatus": "{{ InsufficientDataHealthStatus }}",
  "Inverted": "{{ Inverted }}",
  "IPAddress": "{{ IPAddress }}",
  "MeasureLatency": "{{ MeasureLatency }}",
  "Port": "{{ Port }}",
  "Regions": [
   "{{ Regions[0] }}"
  ],
  "RequestInterval": "{{ RequestInterval }}",
  "ResourcePath": "{{ ResourcePath }}",
  "SearchString": "{{ SearchString }}",
  "RoutingControlArn": "{{ RoutingControlArn }}",
  "Type": "{{ Type }}"
 }
}
>>>
--required properties only
INSERT INTO aws.route53.health_checks (
 HealthCheckConfig,
 region
)
SELECT 
{{ HealthCheckConfig }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "HealthCheckConfig": {
  "AlarmIdentifier": {
   "Name": "{{ Name }}",
   "Region": "{{ Region }}"
  },
  "ChildHealthChecks": [
   "{{ ChildHealthChecks[0] }}"
  ],
  "EnableSNI": "{{ EnableSNI }}",
  "FailureThreshold": "{{ FailureThreshold }}",
  "FullyQualifiedDomainName": "{{ FullyQualifiedDomainName }}",
  "HealthThreshold": "{{ HealthThreshold }}",
  "InsufficientDataHealthStatus": "{{ InsufficientDataHealthStatus }}",
  "Inverted": "{{ Inverted }}",
  "IPAddress": "{{ IPAddress }}",
  "MeasureLatency": "{{ MeasureLatency }}",
  "Port": "{{ Port }}",
  "Regions": [
   "{{ Regions[0] }}"
  ],
  "RequestInterval": "{{ RequestInterval }}",
  "ResourcePath": "{{ ResourcePath }}",
  "SearchString": "{{ SearchString }}",
  "RoutingControlArn": "{{ RoutingControlArn }}",
  "Type": "{{ Type }}"
 },
 "HealthCheckTags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.route53.health_checks (
 HealthCheckConfig,
 HealthCheckTags,
 region
)
SELECT 
 {{ HealthCheckConfig }},
 {{ HealthCheckTags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

### Delete
```json
route53:DeleteHealthCheck
```

### List
```json
route53:ListHealthChecks,
route53:ListTagsForResource
```

