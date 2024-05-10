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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>environment</code> resource, use <code>environments</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AppConfig::Environment</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appconfig.environment" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="environment_id" /></td><td><code>string</code></td><td>The environment ID.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description of the environment.</td></tr>
<tr><td><CopyableCode code="monitors" /></td><td><code>array</code></td><td>Amazon CloudWatch alarms to monitor during the deployment process.</td></tr>
<tr><td><CopyableCode code="application_id" /></td><td><code>string</code></td><td>The application ID.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Metadata to assign to the environment. Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A name for the environment.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
environment_id,
description,
monitors,
application_id,
tags,
name
FROM aws.appconfig.environment
WHERE region = 'us-east-1' AND data__Identifier = '<ApplicationId>|<EnvironmentId>';
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

