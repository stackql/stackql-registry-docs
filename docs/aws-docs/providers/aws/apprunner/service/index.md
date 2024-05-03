---
title: service
hide_title: false
hide_table_of_contents: false
keywords:
  - service
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>service</code> resource, use <code>services</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::AppRunner::Service resource specifies an AppRunner Service.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apprunner.service" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="service_name" /></td><td><code>string</code></td><td>The AppRunner Service Name.</td></tr>
<tr><td><CopyableCode code="service_id" /></td><td><code>string</code></td><td>The AppRunner Service Id</td></tr>
<tr><td><CopyableCode code="service_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the AppRunner Service.</td></tr>
<tr><td><CopyableCode code="service_url" /></td><td><code>string</code></td><td>The Service Url of the AppRunner Service.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>AppRunner Service status.</td></tr>
<tr><td><CopyableCode code="source_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="instance_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="encryption_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="health_check_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="observability_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="auto_scaling_configuration_arn" /></td><td><code>string</code></td><td>Autoscaling configuration ARN</td></tr>
<tr><td><CopyableCode code="network_configuration" /></td><td><code>object</code></td><td></td></tr>
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
service_name,
service_id,
service_arn,
service_url,
status,
source_configuration,
instance_configuration,
tags,
encryption_configuration,
health_check_configuration,
observability_configuration,
auto_scaling_configuration_arn,
network_configuration
FROM aws.apprunner.service
WHERE data__Identifier = '<ServiceArn>';
```

## Permissions

To operate on the <code>service</code> resource, the following permissions are required:

### Read
```json
apprunner:DescribeService
```

### Update
```json
apprunner:UpdateService,
iam:PassRole
```

### Delete
```json
apprunner:DeleteService
```

