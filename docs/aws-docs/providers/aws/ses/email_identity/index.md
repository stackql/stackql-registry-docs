---
title: email_identity
hide_title: false
hide_table_of_contents: false
keywords:
  - email_identity
  - ses
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>email_identity</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>email_identity</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SES::EmailIdentity</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ses.email_identity</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>email_identity</code></td><td><code>string</code></td><td>The email address or domain to verify.</td></tr>
<tr><td><code>configuration_set_attributes</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>dkim_signing_attributes</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>dkim_attributes</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>mail_from_attributes</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>feedback_attributes</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>dkim_dns_token_name1</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>dkim_dns_token_name2</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>dkim_dns_token_name3</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>dkim_dns_token_value1</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>dkim_dns_token_value2</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>dkim_dns_token_value3</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
email_identity,
configuration_set_attributes,
dkim_signing_attributes,
dkim_attributes,
mail_from_attributes,
feedback_attributes,
dkim_dns_token_name1,
dkim_dns_token_name2,
dkim_dns_token_name3,
dkim_dns_token_value1,
dkim_dns_token_value2,
dkim_dns_token_value3
FROM aws.ses.email_identity
WHERE data__Identifier = '<EmailIdentity>';
```

## Permissions

To operate on the <code>email_identity</code> resource, the following permissions are required:

### Read
```json
ses:GetEmailIdentity
```

### Update
```json
ses:PutEmailIdentityMailFromAttributes,
ses:PutEmailIdentityFeedbackAttributes,
ses:PutEmailIdentityConfigurationSetAttributes,
ses:PutEmailIdentityDkimSigningAttributes,
ses:PutEmailIdentityDkimAttributes,
ses:GetEmailIdentity
```

### Delete
```json
ses:DeleteEmailIdentity
```

