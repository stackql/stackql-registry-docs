---
title: observability_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - observability_configurations
  - apprunner
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>observability_configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>observability_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::AppRunner::ObservabilityConfiguration resource  is an AWS App Runner resource type that specifies an App Runner observability configuration</td></tr>
<tr><td><b>Id</b></td><td><code>aws.apprunner.observability_configurations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>observability_configuration_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of this ObservabilityConfiguration</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
observability_configuration_arn
FROM aws.apprunner.observability_configurations
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>observability_configurations</code> resource, the following permissions are required:

### Create
```json
apprunner:CreateObservabilityConfiguration,
apprunner:DescribeObservabilityConfiguration,
apprunner:TagResource
```

### List
```json
apprunner:ListObservabilityConfigurations
```

