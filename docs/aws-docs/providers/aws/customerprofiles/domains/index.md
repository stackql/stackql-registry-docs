---
title: domains
hide_title: false
hide_table_of_contents: false
keywords:
  - domains
  - customerprofiles
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

Creates, updates, deletes or gets a <code>domain</code> resource or lists <code>domains</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A domain defined for 3rd party data source in Profile Service</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.customerprofiles.domains" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td>The unique name of the domain.</td></tr>
<tr><td><CopyableCode code="dead_letter_queue_url" /></td><td><code>string</code></td><td>The URL of the SQS dead letter queue</td></tr>
<tr><td><CopyableCode code="default_encryption_key" /></td><td><code>string</code></td><td>The default encryption key</td></tr>
<tr><td><CopyableCode code="default_expiration_days" /></td><td><code>integer</code></td><td>The default number of days until the data within the domain expires.</td></tr>
<tr><td><CopyableCode code="matching" /></td><td><code>The process of matching duplicate profiles. If Matching = true, Amazon Connect Customer Profiles starts a weekly batch process called Identity Resolution Job. If you do not specify a date and time for Identity Resolution Job to run, by default it runs every Saturday at 12AM UTC to detect duplicate profiles in your domains. After the Identity Resolution Job completes, use the GetMatches API to return and review the results. Or, if you have configured ExportingConfig in the MatchingRequest, you can download the results from S3.</code></td><td></td></tr>
<tr><td><CopyableCode code="rule_based_matching" /></td><td><code>The process of matching duplicate profiles using the Rule-Based matching. If RuleBasedMatching = true, Amazon Connect Customer Profiles will start to match and merge your profiles according to your configuration in the RuleBasedMatchingRequest. You can use the ListRuleBasedMatches and GetSimilarProfiles API to return and review the results. Also, if you have configured ExportingConfig in the RuleBasedMatchingRequest, you can download the results from S3.</code></td><td></td></tr>
<tr><td><CopyableCode code="stats" /></td><td><code>Usage-specific statistics about the domain.</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags (keys and values) associated with the domain</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The time of this integration got created</td></tr>
<tr><td><CopyableCode code="last_updated_at" /></td><td><code>string</code></td><td>The time of this integration got last updated at</td></tr>
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
    <td><CopyableCode code="DomainName, DefaultExpirationDays, region" /></td>
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
    <td><CopyableCode code="list_resource" /></td>
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
List all <code>domains</code> in a region.
```sql
SELECT
region,
domain_name
FROM aws.customerprofiles.domains
WHERE region = 'us-east-1';
```
Gets all properties from a <code>domain</code>.
```sql
SELECT
region,
domain_name,
dead_letter_queue_url,
default_encryption_key,
default_expiration_days,
matching,
rule_based_matching,
stats,
tags,
created_at,
last_updated_at
FROM aws.customerprofiles.domains
WHERE region = 'us-east-1' AND data__Identifier = '<DomainName>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>domain</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.customerprofiles.domains (
 DomainName,
 DefaultExpirationDays,
 region
)
SELECT 
'{{ DomainName }}',
 '{{ DefaultExpirationDays }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.customerprofiles.domains (
 DomainName,
 DeadLetterQueueUrl,
 DefaultEncryptionKey,
 DefaultExpirationDays,
 Matching,
 RuleBasedMatching,
 Tags,
 region
)
SELECT 
 '{{ DomainName }}',
 '{{ DeadLetterQueueUrl }}',
 '{{ DefaultEncryptionKey }}',
 '{{ DefaultExpirationDays }}',
 '{{ Matching }}',
 '{{ RuleBasedMatching }}',
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
  - name: domain
    props:
      - name: DomainName
        value: '{{ DomainName }}'
      - name: DeadLetterQueueUrl
        value: '{{ DeadLetterQueueUrl }}'
      - name: DefaultEncryptionKey
        value: '{{ DefaultEncryptionKey }}'
      - name: DefaultExpirationDays
        value: '{{ DefaultExpirationDays }}'
      - name: Matching
        value:
          Enabled: '{{ Enabled }}'
          AutoMerging:
            Enabled: '{{ Enabled }}'
            ConflictResolution:
              ConflictResolvingModel: '{{ ConflictResolvingModel }}'
              SourceName: '{{ SourceName }}'
            Consolidation:
              MatchingAttributesList:
                - - '{{ 0[0] }}'
            MinAllowedConfidenceScoreForMerging: null
          ExportingConfig:
            S3Exporting:
              S3BucketName: '{{ S3BucketName }}'
              S3KeyName: '{{ S3KeyName }}'
          JobSchedule:
            DayOfTheWeek: '{{ DayOfTheWeek }}'
            Time: '{{ Time }}'
      - name: RuleBasedMatching
        value:
          Enabled: '{{ Enabled }}'
          AttributeTypesSelector:
            AttributeMatchingModel: '{{ AttributeMatchingModel }}'
            Address:
              - '{{ Address[0] }}'
            EmailAddress:
              - '{{ EmailAddress[0] }}'
            PhoneNumber:
              - '{{ PhoneNumber[0] }}'
          ConflictResolution: null
          ExportingConfig: null
          MatchingRules:
            - Rule:
                - '{{ Rule[0] }}'
          MaxAllowedRuleLevelForMatching: '{{ MaxAllowedRuleLevelForMatching }}'
          MaxAllowedRuleLevelForMerging: '{{ MaxAllowedRuleLevelForMerging }}'
          Status: '{{ Status }}'
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
DELETE FROM aws.customerprofiles.domains
WHERE data__Identifier = '<DomainName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>domains</code> resource, the following permissions are required:

### Create
```json
profile:CreateDomain,
profile:TagResource
```

### Read
```json
profile:GetDomain
```

### Update
```json
profile:GetDomain,
profile:UpdateDomain,
profile:UntagResource,
profile:TagResource
```

### Delete
```json
profile:DeleteDomain
```

### List
```json
profile:ListDomains
```

