---
title: stack
hide_title: false
hide_table_of_contents: false
keywords:
  - stack
  - appstream
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>stack</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stack</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>stack</td></tr>
<tr><td><b>Id</b></td><td><code>aws.appstream.stack</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>StorageConnectors</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>DeleteStorageConnectors</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>EmbedHostDomains</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>UserSettings</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>AttributesToDelete</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>RedirectURL</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>StreamingExperienceSettings</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>FeedbackURL</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ApplicationSettings</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>DisplayName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>AccessEndpoints</code></td><td><code>array</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.appstream.stack<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;Id&gt;'
</pre>
