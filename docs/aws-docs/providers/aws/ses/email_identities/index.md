---
title: email_identities
hide_title: false
hide_table_of_contents: false
keywords:
  - email_identities
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Used to retrieve a list of <code>email_identities</code> in a region or to create or delete a <code>email_identities</code> resource, use <code>email_identity</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>email_identities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SES::EmailIdentity</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ses.email_identities" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="email_identity" /></td><td><code>string</code></td><td>The email address or domain to verify.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
email_identity
FROM aws.ses.email_identities
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },

    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "EmailIdentity": "{{ EmailIdentity }}"
}
>>>
--required properties only
INSERT INTO aws.ses.email_identities (
 EmailIdentity,
 region
)
SELECT 
{{ EmailIdentity }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "EmailIdentity": "{{ EmailIdentity }}",
 "ConfigurationSetAttributes": {
  "ConfigurationSetName": "{{ ConfigurationSetName }}"
 },
 "DkimSigningAttributes": {
  "DomainSigningSelector": "{{ DomainSigningSelector }}",
  "DomainSigningPrivateKey": "{{ DomainSigningPrivateKey }}",
  "NextSigningKeyLength": "{{ NextSigningKeyLength }}"
 },
 "DkimAttributes": {
  "SigningEnabled": "{{ SigningEnabled }}"
 },
 "MailFromAttributes": {
  "MailFromDomain": "{{ MailFromDomain }}",
  "BehaviorOnMxFailure": "{{ BehaviorOnMxFailure }}"
 },
 "FeedbackAttributes": {
  "EmailForwardingEnabled": "{{ EmailForwardingEnabled }}"
 }
}
>>>
--all properties
INSERT INTO aws.ses.email_identities (
 EmailIdentity,
 ConfigurationSetAttributes,
 DkimSigningAttributes,
 DkimAttributes,
 MailFromAttributes,
 FeedbackAttributes,
 region
)
SELECT 
 {{ EmailIdentity }},
 {{ ConfigurationSetAttributes }},
 {{ DkimSigningAttributes }},
 {{ DkimAttributes }},
 {{ MailFromAttributes }},
 {{ FeedbackAttributes }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.ses.email_identities
WHERE data__Identifier = '<EmailIdentity>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>email_identities</code> resource, the following permissions are required:

### Create
```json
ses:CreateEmailIdentity,
ses:PutEmailIdentityMailFromAttributes,
ses:PutEmailIdentityFeedbackAttributes,
ses:PutEmailIdentityDkimAttributes,
ses:GetEmailIdentity
```

### Delete
```json
ses:DeleteEmailIdentity
```

### List
```json
ses:ListEmailIdentities
```

