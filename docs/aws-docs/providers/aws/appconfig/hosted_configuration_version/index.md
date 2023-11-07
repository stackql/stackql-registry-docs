---
title: hosted_configuration_version
hide_title: false
hide_table_of_contents: false
keywords:
  - hosted_configuration_version
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
Gets an individual <code>hosted_configuration_version</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hosted_configuration_version</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>hosted_configuration_version</td></tr>
<tr><td><b>Id</b></td><td><code>aws.appconfig.hosted_configuration_version</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ConfigurationProfileId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ContentType</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>LatestVersionNumber</code></td><td><code>number</code></td><td></td></tr>
<tr><td><code>Content</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>VersionLabel</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ApplicationId</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.appconfig.hosted_configuration_version<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;Id&gt;'
</pre>
