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
Gets an individual <code>application</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>application</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iotfleethub.application</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>application_id</code></td><td><code>string</code></td><td>The ID of the application.</td></tr>
<tr><td><code>application_arn</code></td><td><code>string</code></td><td>The ARN of the application.</td></tr>
<tr><td><code>application_name</code></td><td><code>string</code></td><td>Application Name, should be between 1 and 256 characters.</td></tr>
<tr><td><code>application_description</code></td><td><code>string</code></td><td>Application Description, should be between 1 and 2048 characters.</td></tr>
<tr><td><code>application_url</code></td><td><code>string</code></td><td>The URL of the application.</td></tr>
<tr><td><code>application_state</code></td><td><code>string</code></td><td>The current state of the application.</td></tr>
<tr><td><code>application_creation_date</code></td><td><code>integer</code></td><td>When the Application was created</td></tr>
<tr><td><code>application_last_update_date</code></td><td><code>integer</code></td><td>When the Application was last updated</td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td>The ARN of the role that the web application assumes when it interacts with AWS IoT Core. For more info on configuring this attribute, see https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;iot&#x2F;latest&#x2F;apireference&#x2F;API_iotfleethub_CreateApplication.html#API_iotfleethub_CreateApplication_RequestSyntax</td></tr>
<tr><td><code>sso_client_id</code></td><td><code>string</code></td><td>The AWS SSO application generated client ID (used with AWS SSO APIs).</td></tr>
<tr><td><code>error_message</code></td><td><code>string</code></td><td>A message indicating why Create or Delete Application failed.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the application.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
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
FROM awscc.iotfleethub.application
WHERE data__Identifier = '<ApplicationId>';
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

### Delete
```json
iotfleethub:DeleteApplication,
iotfleethub:DescribeApplication,
sso:DeleteManagedApplicationInstance
```

