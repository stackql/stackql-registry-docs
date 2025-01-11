---
title: message_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - message_templates
  - wisdom
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

Creates, updates, deletes or gets a <code>message_template</code> resource or lists <code>message_templates</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>message_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Wisdom::MessageTemplate Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.wisdom.message_templates" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="knowledge_base_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the knowledge base to which the message template belongs.</td></tr>
<tr><td><CopyableCode code="message_template_id" /></td><td><code>string</code></td><td>The unique identifier of the message template.</td></tr>
<tr><td><CopyableCode code="message_template_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the message template.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the message template.</td></tr>
<tr><td><CopyableCode code="channel_subtype" /></td><td><code>string</code></td><td>The channel subtype this message template applies to.</td></tr>
<tr><td><CopyableCode code="content" /></td><td><code>object</code></td><td>The content of the message template.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the message template.</td></tr>
<tr><td><CopyableCode code="language" /></td><td><code>string</code></td><td>The language code value for the language in which the message template is written. The supported language codes include de_DE, en_US, es_ES, fr_FR, id_ID, it_IT, ja_JP, ko_KR, pt_BR, zh_CN, zh_TW</td></tr>
<tr><td><CopyableCode code="grouping_configuration" /></td><td><code>object</code></td><td>The configuration information of the user groups that the message template is accessible to.</td></tr>
<tr><td><CopyableCode code="default_attributes" /></td><td><code>object</code></td><td>An object that specifies the default values to use for variables in the message template. This object contains different categories of key-value pairs. Each key defines a variable or placeholder in the message template. The corresponding value defines the default value for that variable.</td></tr>
<tr><td><CopyableCode code="message_template_content_sha256" /></td><td><code>string</code></td><td>The content SHA256 of the message template.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags used to organize, track, or control access for this resource. For example, &#123; "tags": &#123;"key1":"value1", "key2":"value2"&#125; &#125;.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-messagetemplate.html"><code>AWS::Wisdom::MessageTemplate</code></a>.

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
    <td><CopyableCode code="KnowledgeBaseArn, ChannelSubtype, Name, Content, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>message_templates</code> in a region.
```sql
SELECT
region,
knowledge_base_arn,
message_template_id,
message_template_arn,
name,
channel_subtype,
content,
description,
language,
grouping_configuration,
default_attributes,
message_template_content_sha256,
tags
FROM aws.wisdom.message_templates
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>message_template</code>.
```sql
SELECT
region,
knowledge_base_arn,
message_template_id,
message_template_arn,
name,
channel_subtype,
content,
description,
language,
grouping_configuration,
default_attributes,
message_template_content_sha256,
tags
FROM aws.wisdom.message_templates
WHERE region = 'us-east-1' AND data__Identifier = '<MessageTemplateArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>message_template</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.wisdom.message_templates (
 KnowledgeBaseArn,
 Name,
 ChannelSubtype,
 Content,
 region
)
SELECT 
'{{ KnowledgeBaseArn }}',
 '{{ Name }}',
 '{{ ChannelSubtype }}',
 '{{ Content }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.wisdom.message_templates (
 KnowledgeBaseArn,
 Name,
 ChannelSubtype,
 Content,
 Description,
 Language,
 GroupingConfiguration,
 DefaultAttributes,
 Tags,
 region
)
SELECT 
 '{{ KnowledgeBaseArn }}',
 '{{ Name }}',
 '{{ ChannelSubtype }}',
 '{{ Content }}',
 '{{ Description }}',
 '{{ Language }}',
 '{{ GroupingConfiguration }}',
 '{{ DefaultAttributes }}',
 '{{ Tags }}',
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
  - name: message_template
    props:
      - name: KnowledgeBaseArn
        value: '{{ KnowledgeBaseArn }}'
      - name: Name
        value: '{{ Name }}'
      - name: ChannelSubtype
        value: '{{ ChannelSubtype }}'
      - name: Content
        value:
          EmailMessageTemplateContent:
            Subject: '{{ Subject }}'
            Body:
              PlainText:
                Content: '{{ Content }}'
              Html: null
            Headers:
              - Name: '{{ Name }}'
                Value: '{{ Value }}'
          SmsMessageTemplateContent:
            Body:
              PlainText: null
      - name: Description
        value: '{{ Description }}'
      - name: Language
        value: '{{ Language }}'
      - name: GroupingConfiguration
        value:
          Criteria: '{{ Criteria }}'
          Values:
            - '{{ Values[0] }}'
      - name: DefaultAttributes
        value:
          SystemAttributes:
            Name: '{{ Name }}'
            CustomerEndpoint:
              Address: '{{ Address }}'
            SystemEndpoint: null
          AgentAttributes:
            FirstName: '{{ FirstName }}'
            LastName: '{{ LastName }}'
          CustomerProfileAttributes:
            ProfileId: '{{ ProfileId }}'
            ProfileARN: '{{ ProfileARN }}'
            FirstName: '{{ FirstName }}'
            MiddleName: '{{ MiddleName }}'
            LastName: '{{ LastName }}'
            AccountNumber: '{{ AccountNumber }}'
            EmailAddress: '{{ EmailAddress }}'
            PhoneNumber: '{{ PhoneNumber }}'
            AdditionalInformation: '{{ AdditionalInformation }}'
            PartyType: '{{ PartyType }}'
            BusinessName: '{{ BusinessName }}'
            BirthDate: '{{ BirthDate }}'
            Gender: '{{ Gender }}'
            MobilePhoneNumber: '{{ MobilePhoneNumber }}'
            HomePhoneNumber: '{{ HomePhoneNumber }}'
            BusinessPhoneNumber: '{{ BusinessPhoneNumber }}'
            BusinessEmailAddress: '{{ BusinessEmailAddress }}'
            Address1: '{{ Address1 }}'
            Address2: '{{ Address2 }}'
            Address3: '{{ Address3 }}'
            Address4: '{{ Address4 }}'
            City: '{{ City }}'
            County: '{{ County }}'
            Country: '{{ Country }}'
            PostalCode: '{{ PostalCode }}'
            Province: '{{ Province }}'
            State: '{{ State }}'
            ShippingAddress1: '{{ ShippingAddress1 }}'
            ShippingAddress2: '{{ ShippingAddress2 }}'
            ShippingAddress3: '{{ ShippingAddress3 }}'
            ShippingAddress4: '{{ ShippingAddress4 }}'
            ShippingCity: '{{ ShippingCity }}'
            ShippingCounty: '{{ ShippingCounty }}'
            ShippingCountry: '{{ ShippingCountry }}'
            ShippingPostalCode: '{{ ShippingPostalCode }}'
            ShippingProvince: '{{ ShippingProvince }}'
            ShippingState: '{{ ShippingState }}'
            MailingAddress1: '{{ MailingAddress1 }}'
            MailingAddress2: '{{ MailingAddress2 }}'
            MailingAddress3: '{{ MailingAddress3 }}'
            MailingAddress4: '{{ MailingAddress4 }}'
            MailingCity: '{{ MailingCity }}'
            MailingCounty: '{{ MailingCounty }}'
            MailingCountry: '{{ MailingCountry }}'
            MailingPostalCode: '{{ MailingPostalCode }}'
            MailingProvince: '{{ MailingProvince }}'
            MailingState: '{{ MailingState }}'
            BillingAddress1: '{{ BillingAddress1 }}'
            BillingAddress2: '{{ BillingAddress2 }}'
            BillingAddress3: '{{ BillingAddress3 }}'
            BillingAddress4: '{{ BillingAddress4 }}'
            BillingCity: '{{ BillingCity }}'
            BillingCounty: '{{ BillingCounty }}'
            BillingCountry: '{{ BillingCountry }}'
            BillingPostalCode: '{{ BillingPostalCode }}'
            BillingProvince: '{{ BillingProvince }}'
            BillingState: '{{ BillingState }}'
            Custom: {}
          CustomAttributes: null
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.wisdom.message_templates
WHERE data__Identifier = '<MessageTemplateArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>message_templates</code> resource, the following permissions are required:

### Create
```json
wisdom:CreateMessageTemplate,
wisdom:GetMessageTemplate,
wisdom:TagResource,
connect:SearchRoutingProfiles,
connect:DescribeRoutingProfile
```

### Update
```json
wisdom:UpdateMessageTemplate,
wisdom:UpdateMessageTemplateMetadata,
wisdom:GetMessageTemplate,
wisdom:TagResource,
wisdom:UntagResource,
connect:SearchRoutingProfiles,
connect:DescribeRoutingProfile
```

### Delete
```json
wisdom:DeleteMessageTemplate,
wisdom:UntagResource
```

### List
```json
wisdom:ListMessageTemplates
```

### Read
```json
wisdom:GetMessageTemplate
```
