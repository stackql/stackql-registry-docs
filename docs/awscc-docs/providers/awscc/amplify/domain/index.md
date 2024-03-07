---
title: domain
hide_title: false
hide_table_of_contents: false
keywords:
  - domain
  - amplify
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>domain</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domain</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>domain</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.amplify.domain</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>app_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>auto_sub_domain_creation_patterns</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>auto_sub_domain_ia_mrole</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>certificate_record</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>certificate</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>certificate_settings</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>domain_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>domain_status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>update_status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>enable_auto_sub_domain</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>status_reason</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>sub_domain_settings</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>domain</code> resource, the following permissions are required:

### Delete
<pre>
amplify:DeleteDomainAssociation,
iam:PassRole,
amplify:DeleteDomainAssociation</pre>

### Read
<pre>
amplify:GetDomainAssociation,
route53:ListHostedZones,
iam:PassRole,
amplify:ListTagsForResource</pre>

### Update
<pre>
amplify:UpdateDomainAssociation,
route53:ListHostedZones,
route53:ChangeResourceRecordSets,
iam:PassRole,
amplify:ListTagsForResource,
amplify:TagResource,
amplify:UntagResource</pre>


## Example
```sql
SELECT
region,
app_id,
arn,
auto_sub_domain_creation_patterns,
auto_sub_domain_ia_mrole,
certificate_record,
certificate,
certificate_settings,
domain_name,
domain_status,
update_status,
enable_auto_sub_domain,
status_reason,
sub_domain_settings
FROM awscc.amplify.domain
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Arn&gt;'
```
