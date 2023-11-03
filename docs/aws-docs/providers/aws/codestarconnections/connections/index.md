---
title: connections
hide_title: false
hide_table_of_contents: false
keywords:
  - connections
  - codestarconnections
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>connections</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.codestarconnections.connections</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ConnectionArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the  connection. The ARN is used as the connection reference when the connection is shared between AWS services.</td></tr><tr><td><code>ConnectionName</code></td><td><code>string</code></td><td>The name of the connection. Connection names must be unique in an AWS user account.</td></tr><tr><td><code>ConnectionStatus</code></td><td><code>string</code></td><td>The current status of the connection.</td></tr><tr><td><code>OwnerAccountId</code></td><td><code>string</code></td><td>The name of the external provider where your third-party code repository is configured. For Bitbucket, this is the account ID of the owner of the Bitbucket repository.</td></tr><tr><td><code>ProviderType</code></td><td><code>string</code></td><td>The name of the external provider where your third-party code repository is configured. You must specify either a ProviderType or a HostArn.</td></tr><tr><td><code>HostArn</code></td><td><code>string</code></td><td>The host arn configured to represent the infrastructure where your third-party provider is installed. You must specify either a ProviderType or a HostArn.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>Specifies the tags applied to a connection.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.codestarconnections.connections
WHERE region = 'us-east-1'
</pre>
