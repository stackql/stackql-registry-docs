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
null
<tr><td><b>Id</b></td><td><code>aws.iotfleethub.application</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ApplicationId</code></td><td><code>string</code></td><td>The ID of the application.</td></tr><tr><td><code>ApplicationArn</code></td><td><code>string</code></td><td>The ARN of the application.</td></tr><tr><td><code>ApplicationName</code></td><td><code>string</code></td><td>Application Name, should be between 1 and 256 characters.</td></tr><tr><td><code>ApplicationDescription</code></td><td><code>string</code></td><td>Application Description, should be between 1 and 2048 characters.</td></tr><tr><td><code>ApplicationUrl</code></td><td><code>string</code></td><td>The URL of the application.</td></tr><tr><td><code>ApplicationState</code></td><td><code>string</code></td><td>The current state of the application.</td></tr><tr><td><code>ApplicationCreationDate</code></td><td><code>integer</code></td><td>When the Application was created</td></tr><tr><td><code>ApplicationLastUpdateDate</code></td><td><code>integer</code></td><td>When the Application was last updated</td></tr><tr><td><code>RoleArn</code></td><td><code>string</code></td><td>The ARN of the role that the web application assumes when it interacts with AWS IoT Core. For more info on configuring this attribute, see https://docs.aws.amazon.com/iot/latest/apireference/API_iotfleethub_CreateApplication.html#API_iotfleethub_CreateApplication_RequestSyntax</td></tr><tr><td><code>SsoClientId</code></td><td><code>string</code></td><td>The AWS SSO application generated client ID (used with AWS SSO APIs).</td></tr><tr><td><code>ErrorMessage</code></td><td><code>string</code></td><td>A message indicating why Create or Delete Application failed.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the application.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.iotfleethub.application
WHERE region = 'us-east-1' AND data__Identifier = '<ApplicationId>'
</pre>
