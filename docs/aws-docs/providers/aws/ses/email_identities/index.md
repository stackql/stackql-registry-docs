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
    <td><CopyableCode code="EmailIdentity, region" /></td>
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

Use the following StackQL query and manifest file to create a new <code>email_identity</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.ses.email_identities (
 EmailIdentity,
 region
)
SELECT 
'{{ EmailIdentity }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
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
 '{{ EmailIdentity }}',
 '{{ ConfigurationSetAttributes }}',
 '{{ DkimSigningAttributes }}',
 '{{ DkimAttributes }}',
 '{{ MailFromAttributes }}',
 '{{ FeedbackAttributes }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: email_identity
    props:
      - name: EmailIdentity
        value: '{{ EmailIdentity }}'
      - name: ConfigurationSetAttributes
        value:
          ConfigurationSetName: '{{ ConfigurationSetName }}'
      - name: DkimSigningAttributes
        value:
          DomainSigningSelector: '{{ DomainSigningSelector }}'
          DomainSigningPrivateKey: '{{ DomainSigningPrivateKey }}'
          NextSigningKeyLength: '{{ NextSigningKeyLength }}'
      - name: DkimAttributes
        value:
          SigningEnabled: '{{ SigningEnabled }}'
      - name: MailFromAttributes
        value:
          MailFromDomain: '{{ MailFromDomain }}'
          BehaviorOnMxFailure: '{{ BehaviorOnMxFailure }}'
      - name: FeedbackAttributes
        value:
          EmailForwardingEnabled: '{{ EmailForwardingEnabled }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
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

