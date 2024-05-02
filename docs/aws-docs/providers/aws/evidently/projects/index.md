---
title: projects
hide_title: false
hide_table_of_contents: false
keywords:
  - projects
  - evidently
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>projects</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Evidently::Project</td></tr>
<tr><td><b>Id</b></td><td><code>aws.evidently.projects</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
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
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
arn
FROM aws.evidently.projects
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>projects</code> resource, the following permissions are required:

### Create
```json
evidently:CreateProject,
evidently:GetProject,
logs:CreateLogDelivery,
logs:GetLogDelivery,
logs:ListLogDeliveries,
s3:PutBucketPolicy,
s3:GetBucketPolicy,
evidently:TagResource,
evidently:ExportProjectAsConfiguration,
appconfig:GetEnvironment,
appconfig:CreateConfigurationProfile,
appconfig:CreateHostedConfigurationVersion,
appconfig:CreateExtensionAssociation,
appconfig:TagResource,
iam:GetRole,
iam:CreateServiceLinkedRole
```

