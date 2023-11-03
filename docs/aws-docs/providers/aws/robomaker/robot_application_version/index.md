---
title: robot_application_version
hide_title: false
hide_table_of_contents: false
keywords:
  - robot_application_version
  - robomaker
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>robot_application_version</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>robot_application_version</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.robomaker.robot_application_version</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Application</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>CurrentRevisionId</code></td><td><code>string</code></td><td>The revision ID of robot application.</td></tr><tr><td><code>ApplicationVersion</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Arn</code></td><td><code>undefined</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.robomaker.robot_application_version
WHERE region = 'us-east-1' AND data__Identifier = '{Arn}'
```
