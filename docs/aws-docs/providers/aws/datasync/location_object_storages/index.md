---
title: location_object_storages
hide_title: false
hide_table_of_contents: false
keywords:
  - location_object_storages
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
Retrieves a list of <code>location_object_storages</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>location_object_storages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.datasync.location_object_storages</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>AccessKey</code></td><td><code>string</code></td><td>Optional. The access key is used if credentials are required to access the self-managed object storage server.</td></tr><tr><td><code>AgentArns</code></td><td><code>array</code></td><td>The Amazon Resource Name (ARN) of the agents associated with the self-managed object storage server location.</td></tr><tr><td><code>BucketName</code></td><td><code>string</code></td><td>The name of the bucket on the self-managed object storage server.</td></tr><tr><td><code>SecretKey</code></td><td><code>string</code></td><td>Optional. The secret key is used if credentials are required to access the self-managed object storage server.</td></tr><tr><td><code>ServerCertificate</code></td><td><code>string</code></td><td>X.509 PEM content containing a certificate authority or chain to trust.</td></tr><tr><td><code>ServerHostname</code></td><td><code>string</code></td><td>The name of the self-managed object storage server. This value is the IP address or Domain Name Service (DNS) name of the object storage server.</td></tr><tr><td><code>ServerPort</code></td><td><code>integer</code></td><td>The port that your self-managed server accepts inbound network traffic on.</td></tr><tr><td><code>ServerProtocol</code></td><td><code>string</code></td><td>The protocol that the object storage server uses to communicate.</td></tr><tr><td><code>Subdirectory</code></td><td><code>string</code></td><td>The subdirectory in the self-managed object storage server that is used to read data from.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr><tr><td><code>LocationArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the location that is created.</td></tr><tr><td><code>LocationUri</code></td><td><code>string</code></td><td>The URL of the object storage location that was described.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.datasync.location_object_storages
WHERE region = 'us-east-1'
</pre>
