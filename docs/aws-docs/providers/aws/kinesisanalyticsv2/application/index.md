---
title: application
hide_title: false
hide_table_of_contents: false
keywords:
  - application
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

Gets or operates on an individual <code>application</code> resource, use <code>applications</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates an Amazon Kinesis Data Analytics application. For information about creating a Kinesis Data Analytics application, see &#91;Creating an Application&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kinesisanalytics&#x2F;latest&#x2F;java&#x2F;getting-started.html).</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.kinesisanalyticsv2.application" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="application_configuration" /></td><td><code>object</code></td><td>Use this parameter to configure the application.</td></tr>
<tr><td><CopyableCode code="application_description" /></td><td><code>string</code></td><td>The description of the application.</td></tr>
<tr><td><CopyableCode code="application_mode" /></td><td><code>string</code></td><td>To create a Kinesis Data Analytics Studio notebook, you must set the mode to `INTERACTIVE`. However, for a Kinesis Data Analytics for Apache Flink application, the mode is optional.</td></tr>
<tr><td><CopyableCode code="application_name" /></td><td><code>string</code></td><td>The name of the application.</td></tr>
<tr><td><CopyableCode code="runtime_environment" /></td><td><code>string</code></td><td>The runtime environment for the application.</td></tr>
<tr><td><CopyableCode code="service_execution_role" /></td><td><code>string</code></td><td>Specifies the IAM role that the application uses to access external resources.</td></tr>
<tr><td><CopyableCode code="run_configuration" /></td><td><code>object</code></td><td>Specifies run configuration (start parameters) of a Kinesis Data Analytics application. Evaluated on update for RUNNING applications an only.</td></tr>
<tr><td><CopyableCode code="application_maintenance_configuration" /></td><td><code>object</code></td><td>Used to configure start of maintenance window.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of one or more tags to assign to the application. A tag is a key-value pair that identifies an application. Note that the maximum number of application tags includes system tags. The maximum number of user-defined application tags is 50.</td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
application_configuration,
application_description,
application_mode,
application_name,
runtime_environment,
service_execution_role,
run_configuration,
application_maintenance_configuration,
tags
FROM aws.kinesisanalyticsv2.application
WHERE data__Identifier = '<ApplicationName>';
```

## Permissions

To operate on the <code>application</code> resource, the following permissions are required:

### Read
```json
kinesisanalytics:DescribeApplication,
kinesisanalytics:ListTagsForResource
```

### Update
```json
kinesisanalytics:UpdateApplication,
kinesisanalytics:DescribeApplication,
kinesisanalytics:TagResource,
kinesisanalytics:UntagResource,
kinesisanalytics:AddApplicationVpcConfiguration,
kinesisanalytics:DeleteApplicationVpcConfiguration,
kinesisanalytics:UpdateApplicationMaintenanceConfiguration,
kinesisanalytics:ListTagsForResource
```

### Delete
```json
kinesisanalytics:DescribeApplication,
kinesisanalytics:DeleteApplication
```

