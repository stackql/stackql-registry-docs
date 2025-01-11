---
title: application_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - application_tags
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

Expands all tag keys and values for <code>applications</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::IoTFleetHub::Application</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotfleethub.application_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="application_id" /></td><td><code>string</code></td><td>The ID of the application.</td></tr>
<tr><td><CopyableCode code="application_arn" /></td><td><code>string</code></td><td>The ARN of the application.</td></tr>
<tr><td><CopyableCode code="application_name" /></td><td><code>string</code></td><td>Application Name, should be between 1 and 256 characters.</td></tr>
<tr><td><CopyableCode code="application_description" /></td><td><code>string</code></td><td>Application Description, should be between 1 and 2048 characters.</td></tr>
<tr><td><CopyableCode code="application_url" /></td><td><code>string</code></td><td>The URL of the application.</td></tr>
<tr><td><CopyableCode code="application_state" /></td><td><code>string</code></td><td>The current state of the application.</td></tr>
<tr><td><CopyableCode code="application_creation_date" /></td><td><code>integer</code></td><td>When the Application was created</td></tr>
<tr><td><CopyableCode code="application_last_update_date" /></td><td><code>integer</code></td><td>When the Application was last updated</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The ARN of the role that the web application assumes when it interacts with AWS IoT Core. For more info on configuring this attribute, see https://docs.aws.amazon.com/iot/latest/apireference/API_iotfleethub_CreateApplication.html#API_iotfleethub_CreateApplication_RequestSyntax</td></tr>
<tr><td><CopyableCode code="sso_client_id" /></td><td><code>string</code></td><td>The AWS SSO application generated client ID (used with AWS SSO APIs).</td></tr>
<tr><td><CopyableCode code="error_message" /></td><td><code>string</code></td><td>A message indicating why Create or Delete Application failed.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>applications</code> in a region.
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
tag_key,
tag_value
FROM aws.iotfleethub.application_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>application_tags</code> resource, see <a href="/providers/aws/iotfleethub/applications/#permissions"><code>applications</code></a>

