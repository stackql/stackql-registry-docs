---
title: location_smbs
hide_title: false
hide_table_of_contents: false
keywords:
  - location_smbs
  - datasync
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>location_smbs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>location_smbs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.datasync.location_smbs</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>AgentArns</code></td><td><code>array</code></td><td>The Amazon Resource Names (ARNs) of agents to use for a Simple Message Block (SMB) location.</td></tr><tr><td><code>Domain</code></td><td><code>string</code></td><td>The name of the Windows domain that the SMB server belongs to.</td></tr><tr><td><code>MountOptions</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Password</code></td><td><code>string</code></td><td>The password of the user who can mount the share and has the permissions to access files and folders in the SMB share.</td></tr><tr><td><code>ServerHostname</code></td><td><code>string</code></td><td>The name of the SMB server. This value is the IP address or Domain Name Service (DNS) name of the SMB server.</td></tr><tr><td><code>Subdirectory</code></td><td><code>string</code></td><td>The subdirectory in the SMB file system that is used to read data from the SMB source location or write data to the SMB destination</td></tr><tr><td><code>User</code></td><td><code>string</code></td><td>The user who can mount the share, has the permissions to access files and folders in the SMB share.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr><tr><td><code>LocationArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the SMB location that is created.</td></tr><tr><td><code>LocationUri</code></td><td><code>string</code></td><td>The URL of the SMB location that was described.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.datasync.location_smbs
WHERE region = 'us-east-1'
</pre>
