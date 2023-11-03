---
title: simple_ads
hide_title: false
hide_table_of_contents: false
keywords:
  - simple_ads
  - directoryservice
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>simple_ads</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>simple_ads</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.directoryservice.simple_ads</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>DirectoryId</code></td><td><code>string</code></td><td>The unique identifier for a directory.</td></tr><tr><td><code>Alias</code></td><td><code>string</code></td><td>The alias for a directory.</td></tr><tr><td><code>DnsIpAddresses</code></td><td><code>array</code></td><td>The IP addresses of the DNS servers for the directory, such as [ "172.31.3.154", "172.31.63.203" ].</td></tr><tr><td><code>CreateAlias</code></td><td><code>boolean</code></td><td>The name of the configuration set.</td></tr><tr><td><code>Description</code></td><td><code>string</code></td><td>Description for the directory.</td></tr><tr><td><code>EnableSso</code></td><td><code>boolean</code></td><td>Whether to enable single sign-on for a Simple Active Directory in AWS.</td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td>The fully qualified domain name for the AWS Managed Simple AD directory.</td></tr><tr><td><code>Password</code></td><td><code>string</code></td><td>The password for the default administrative user named Admin.</td></tr><tr><td><code>ShortName</code></td><td><code>string</code></td><td>The NetBIOS name for your domain.</td></tr><tr><td><code>Size</code></td><td><code>string</code></td><td>The size of the directory.</td></tr><tr><td><code>VpcSettings</code></td><td><code>undefined</code></td><td>VPC settings of the Simple AD directory server in AWS.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.directoryservice.simple_ads
WHERE region = 'us-east-1'
```
