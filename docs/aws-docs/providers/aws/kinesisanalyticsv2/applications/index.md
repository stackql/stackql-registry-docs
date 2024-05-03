---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - kinesisanalyticsv2
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

Used to retrieve a list of <code>applications</code> in a region or create a <code>applications</code> resource, use <code>application</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates an Amazon Kinesis Data Analytics application. For information about creating a Kinesis Data Analytics application, see &#91;Creating an Application&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kinesisanalytics&#x2F;latest&#x2F;java&#x2F;getting-started.html).</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.kinesisanalyticsv2.applications" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="application_name" /></td><td><code>string</code></td><td>The name of the application.</td></tr>
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
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
application_name
FROM aws.kinesisanalyticsv2.applications
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>applications</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
kinesisanalytics:CreateApplication,
kinesisanalytics:DescribeApplication,
kinesisanalytics:ListTagsForResource,
kinesisanalytics:UpdateApplicationMaintenanceConfiguration
```

### List
```json
kinesisanalytics:ListApplications
```

