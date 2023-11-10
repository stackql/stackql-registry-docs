---
title: project
hide_title: false
hide_table_of_contents: false
keywords:
  - project
  - iotsitewise
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>project</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>project</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>project</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iotsitewise.project</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>portal_id</code></td><td><code>string</code></td><td>The ID of the portal in which to create the project.</td></tr>
<tr><td><code>project_id</code></td><td><code>string</code></td><td>The ID of the project.</td></tr>
<tr><td><code>project_name</code></td><td><code>string</code></td><td>A friendly name for the project.</td></tr>
<tr><td><code>project_description</code></td><td><code>string</code></td><td>A description for the project.</td></tr>
<tr><td><code>project_arn</code></td><td><code>string</code></td><td>The ARN of the project.</td></tr>
<tr><td><code>asset_ids</code></td><td><code>array</code></td><td>The IDs of the assets to be associated to the project.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the project.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
portal_id,
project_id,
project_name,
project_description,
project_arn,
asset_ids,
tags
FROM aws.iotsitewise.project
WHERE region = 'us-east-1'
AND data__Identifier = '<ProjectId>'
```
