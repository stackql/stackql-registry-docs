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


Used to retrieve a list of <code>domains</code> in a region or to create or delete a <code>domains</code> resource, use <code>domain</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A domain defined for 3rd party data source in Profile Service</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.customerprofiles.domains" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td>The unique name of the domain.</td></tr>
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
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
domain_name
FROM aws.customerprofiles.domains
WHERE region = 'us-east-1';
```

## `INSERT` Example

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

## `DELETE` Example

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

### Delete
```json
profile:DeleteDomain
```

### List
```json
profile:ListDomains
```

