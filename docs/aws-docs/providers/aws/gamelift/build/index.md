---
title: build
hide_title: false
hide_table_of_contents: false
keywords:
  - build
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
Gets an individual <code>build</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>build</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.gamelift.build</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>BuildId</code></td><td><code>string</code></td><td>A unique identifier for a build to be deployed on the new fleet. If you are deploying the fleet with a custom game build, you must specify this property. The build must have been successfully uploaded to Amazon GameLift and be in a READY status. This fleet setting cannot be changed once the fleet is created.</td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>A descriptive label that is associated with a build. Build names do not need to be unique.</td></tr>
<tr><td><code>OperatingSystem</code></td><td><code>string</code></td><td>The operating system that the game server binaries are built to run on. This value determines the type of fleet resources that you can use for this build. If your game build contains multiple executables, they all must run on the same operating system. If an operating system is not specified when creating a build, Amazon GameLift uses the default value (WINDOWS_2012). This value cannot be changed later.</td></tr>
<tr><td><code>StorageLocation</code></td><td><code>undefined</code></td><td>Information indicating where your game build files are stored. Use this parameter only when creating a build with files stored in an Amazon S3 bucket that you own. The storage location must specify an Amazon S3 bucket name and key. The location must also specify a role ARN that you set up to allow Amazon GameLift to access your Amazon S3 bucket. The S3 bucket and your new build must be in the same Region.</td></tr>
<tr><td><code>Version</code></td><td><code>string</code></td><td>Version information that is associated with this build. Version strings do not need to be unique.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.gamelift.build
WHERE region = 'us-east-1' AND data__Identifier = '&lt;BuildId&gt;'
</pre>
