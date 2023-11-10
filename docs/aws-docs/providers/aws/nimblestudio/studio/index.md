---
title: studio
hide_title: false
hide_table_of_contents: false
keywords:
  - studio
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
Gets an individual <code>studio</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>studio</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>studio</td></tr>
<tr><td><b>Id</b></td><td><code>aws.nimblestudio.studio</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>admin_role_arn</code></td><td><code>string</code></td><td>&lt;p&gt;The IAM role that Studio Admins will assume when logging in to the Nimble Studio portal.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>display_name</code></td><td><code>string</code></td><td>&lt;p&gt;A friendly name for the studio.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>home_region</code></td><td><code>string</code></td><td>&lt;p&gt;The Amazon Web Services Region where the studio resource is located.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>sso_client_id</code></td><td><code>string</code></td><td>&lt;p&gt;The Amazon Web Services SSO application client ID used to integrate with Amazon Web Services SSO to enable Amazon Web Services SSO users to log in to Nimble Studio portal.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>studio_encryption_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>studio_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>studio_name</code></td><td><code>string</code></td><td>&lt;p&gt;The studio name that is used in the URL of the Nimble Studio portal when accessed by Nimble Studio users.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>studio_url</code></td><td><code>string</code></td><td>&lt;p&gt;The address of the web page for the studio.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>user_role_arn</code></td><td><code>string</code></td><td>&lt;p&gt;The IAM role that Studio Users will assume when logging in to the Nimble Studio portal.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
admin_role_arn,
display_name,
home_region,
sso_client_id,
studio_encryption_configuration,
studio_id,
studio_name,
studio_url,
tags,
user_role_arn
FROM aws.nimblestudio.studio
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;StudioId&gt;'
```
