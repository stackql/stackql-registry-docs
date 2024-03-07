---
title: environment
hide_title: false
hide_table_of_contents: false
keywords:
  - environment
  - appconfig
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>environment</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>environment</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.appconfig.environment</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>environment_id</code></td><td><code>string</code></td><td>The environment ID.</td></tr>
<tr><td><code>application_id</code></td><td><code>string</code></td><td>The application ID.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>A name for the environment.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>A description of the environment.</td></tr>
<tr><td><code>monitors</code></td><td><code>array</code></td><td>Amazon CloudWatch alarms to monitor during the deployment process.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>Metadata to assign to the environment. Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
environment_id,
application_id,
name,
description,
monitors,
tags
FROM awscc.appconfig.environment
WHERE region = 'us-east-1'
AND data__Identifier = '{ApplicationId}';
AND data__Identifier = '{EnvironmentId}';
```

## Permissions

To operate on the <code>environment</code> resource, the following permissions are required:

### Read
```json
appconfig:GetEnvironment,
appconfig:ListTagsForResource
```

### Update
```json
appconfig:UpdateEnvironment,
appconfig:TagResource,
appconfig:UntagResource,
iam:PassRole
```

### Delete
```json
appconfig:GetEnvironment,
appconfig:DeleteEnvironment
```

