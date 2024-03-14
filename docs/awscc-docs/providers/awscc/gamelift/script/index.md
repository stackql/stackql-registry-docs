---
title: script
hide_title: false
hide_table_of_contents: false
keywords:
  - script
  - gamelift
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>script</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>script</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>script</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.gamelift.script</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>A descriptive label that is associated with a script. Script names do not need to be unique.</td></tr>
<tr><td><code>storage_location</code></td><td><code>object</code></td><td>The location of the Amazon S3 bucket where a zipped file containing your Realtime scripts is stored. The storage location must specify the Amazon S3 bucket name, the zip file name (the "key"), and a role ARN that allows Amazon GameLift to access the Amazon S3 storage location. The S3 bucket must be in the same Region where you want to create a new script. By default, Amazon GameLift uploads the latest version of the zip file; if you have S3 object versioning turned on, you can use the ObjectVersion parameter to specify an earlier version.</td></tr>
<tr><td><code>version</code></td><td><code>string</code></td><td>The version that is associated with a script. Version strings do not need to be unique.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>creation_time</code></td><td><code>string</code></td><td>A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) that is assigned to a Amazon GameLift script resource and uniquely identifies it. ARNs are unique across all Regions. In a GameLift script ARN, the resource ID matches the Id value.</td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>A unique identifier for the Realtime script</td></tr>
<tr><td><code>size_on_disk</code></td><td><code>integer</code></td><td>The file size of the uploaded Realtime script, expressed in bytes. When files are uploaded from an S3 location, this value remains at "0".</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
name,
storage_location,
version,
tags,
creation_time,
arn,
id,
size_on_disk
FROM awscc.gamelift.script
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>script</code> resource, the following permissions are required:

### Read
```json
gamelift:DescribeScript,
gamelift:ListScripts,
gamelift:ListTagsForResource
```

### Delete
```json
gamelift:DeleteScript
```

### Update
```json
gamelift:DescribeScript,
gamelift:UpdateScript,
gamelift:ListTagsForResource,
gamelift:TagResource,
gamelift:UntagResource,
iam:PassRole
```

