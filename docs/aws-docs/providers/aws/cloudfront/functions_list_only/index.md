---
title: functions_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - functions_list_only
  - cloudfront
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

Lists <code>functions</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/functions/"><code>functions</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>functions_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates a CF function.<br />To create a function, you provide the function code and some configuration information about the function. The response contains an Amazon Resource Name (ARN) that uniquely identifies the function, and the function’s stage.<br />By default, when you create a function, it’s in the <code>DEVELOPMENT</code> stage. In this stage, you can &#91;test the function&#93;(https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/test-function.html) in the CF console (or with <code>TestFunction</code> in the CF API).<br />When you’re ready to use your function with a CF distribution, publish the function to the <code>LIVE</code> stage. You can do this in the CF console, with <code>PublishFunction</code> in the CF API, or by updating the <code>AWS::CloudFront::Function</code> resource with the <code>AutoPublish</code> property set to <code>true</code>. When the function is published to the <code>LIVE</code> stage, you can attach it to a distribution’s cache behavior, using the function’s ARN.<br />To automatically publish the function to the <code>LIVE</code> stage when it’s created, set the <code>AutoPublish</code> property to <code>true</code>.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudfront.functions_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="function_arn" /></td><td><code>string</code></td><td></td></tr>
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
Lists all <code>functions</code> in a region.
```sql
SELECT
region,
function_arn
FROM aws.cloudfront.functions_list_only
;
```


## Permissions

For permissions required to operate on the <code>functions_list_only</code> resource, see <a href="/providers/aws/cloudfront/functions/#permissions"><code>functions</code></a>

