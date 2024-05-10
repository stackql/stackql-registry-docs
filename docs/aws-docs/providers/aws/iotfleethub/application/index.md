---
title: application
hide_title: false
hide_table_of_contents: false
keywords:
  - application
  - iotfleethub
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


Gets or updates an individual <code>application</code> resource, use <code>applications</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::IoTFleetHub::Application</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotfleethub.application" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="application_id" /></td><td><code>string</code></td><td>The ID of the application.</td></tr>
<tr><td><CopyableCode code="application_arn" /></td><td><code>string</code></td><td>The ARN of the application.</td></tr>
<tr><td><CopyableCode code="application_name" /></td><td><code>string</code></td><td>Application Name, should be between 1 and 256 characters.</td></tr>
<tr><td><CopyableCode code="application_description" /></td><td><code>string</code></td><td>Application Description, should be between 1 and 2048 characters.</td></tr>
<tr><td><CopyableCode code="application_url" /></td><td><code>string</code></td><td>The URL of the application.</td></tr>
<tr><td><CopyableCode code="application_state" /></td><td><code>string</code></td><td>The current state of the application.</td></tr>
<tr><td><CopyableCode code="application_creation_date" /></td><td><code>integer</code></td><td>When the Application was created</td></tr>
<tr><td><CopyableCode code="application_last_update_date" /></td><td><code>integer</code></td><td>When the Application was last updated</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The ARN of the role that the web application assumes when it interacts with AWS IoT Core. For more info on configuring this attribute, see https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;iot&#x2F;latest&#x2F;apireference&#x2F;API_iotfleethub_CreateApplication.html#API_iotfleethub_CreateApplication_RequestSyntax</td></tr>
<tr><td><CopyableCode code="sso_client_id" /></td><td><code>string</code></td><td>The AWS SSO application generated client ID (used with AWS SSO APIs).</td></tr>
<tr><td><CopyableCode code="error_message" /></td><td><code>string</code></td><td>A message indicating why Create or Delete Application failed.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the application.</td></tr>
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
application_id,
application_arn,
application_name,
application_description,
application_url,
application_state,
application_creation_date,
application_last_update_date,
role_arn,
sso_client_id,
error_message,
tags
FROM aws.iotfleethub.application
WHERE region = 'us-east-1' AND data__Identifier = '<ApplicationId>';
```


## Permissions

To operate on the <code>application</code> resource, the following permissions are required:

### Read
```json
iotfleethub:DescribeApplication
```

### Update
```json
iotfleethub:UpdateApplication,
iotfleethub:DescribeApplication,
iotfleethub:TagResource,
iotfleethub:UntagResource
```

