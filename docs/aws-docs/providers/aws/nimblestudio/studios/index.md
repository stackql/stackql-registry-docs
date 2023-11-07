---
title: studios
hide_title: false
hide_table_of_contents: false
keywords:
  - studios
  - nimblestudio
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>studios</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>studios</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>studios</td></tr>
<tr><td><b>Id</b></td><td><code>aws.nimblestudio.studios</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>AdminRoleArn</code></td><td><code>string</code></td><td>&lt;p&gt;The IAM role that Studio Admins will assume when logging in to the Nimble Studio portal.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>DisplayName</code></td><td><code>string</code></td><td>&lt;p&gt;A friendly name for the studio.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>HomeRegion</code></td><td><code>string</code></td><td>&lt;p&gt;The Amazon Web Services Region where the studio resource is located.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>SsoClientId</code></td><td><code>string</code></td><td>&lt;p&gt;The Amazon Web Services SSO application client ID used to integrate with Amazon Web Services SSO to enable Amazon Web Services SSO users to log in to Nimble Studio portal.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>StudioEncryptionConfiguration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>StudioId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>StudioName</code></td><td><code>string</code></td><td>&lt;p&gt;The studio name that is used in the URL of the Nimble Studio portal when accessed by Nimble Studio users.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>StudioUrl</code></td><td><code>string</code></td><td>&lt;p&gt;The address of the web page for the studio.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>Tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>UserRoleArn</code></td><td><code>string</code></td><td>&lt;p&gt;The IAM role that Studio Users will assume when logging in to the Nimble Studio portal.&lt;&#x2F;p&gt;</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.nimblestudio.studios<br/>WHERE region = 'us-east-1'
</pre>
