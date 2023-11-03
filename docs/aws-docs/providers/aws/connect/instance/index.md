---
title: instance
hide_title: false
hide_table_of_contents: false
keywords:
  - instance
  - connect
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>instance</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instance</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.connect.instance</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td>An instanceId is automatically generated on creation and assigned as the unique identifier.</td></tr><tr><td><code>Arn</code></td><td><code>string</code></td><td>An instanceArn is automatically generated on creation based on instanceId.</td></tr><tr><td><code>IdentityManagementType</code></td><td><code>string</code></td><td>Specifies the type of directory integration for new instance.</td></tr><tr><td><code>InstanceAlias</code></td><td><code>string</code></td><td>Alias of the new directory created as part of new instance creation.</td></tr><tr><td><code>CreatedTime</code></td><td><code>string</code></td><td>Timestamp of instance creation logged as part of instance creation.</td></tr><tr><td><code>ServiceRole</code></td><td><code>string</code></td><td>Service linked role created as part of instance creation.</td></tr><tr><td><code>InstanceStatus</code></td><td><code>string</code></td><td>Specifies the creation status of new instance.</td></tr><tr><td><code>DirectoryId</code></td><td><code>string</code></td><td>Existing directoryId user wants to map to the new Connect instance.</td></tr><tr><td><code>Attributes</code></td><td><code>undefined</code></td><td>The attributes for the instance.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.connect.instance
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>'
</pre>
